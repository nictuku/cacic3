import logging

import cherrypy

import turbogears
from turbogears import controllers, expose, validate, redirect
from turbogears.validators import Int

from turbogears import identity
from turbogears.database import session

from turbogears.widgets import TableForm, CheckBoxList, DataGrid

from cacic3 import json
from cacic3 import model 
from cacic3.model import Computer, Hardware, Network, NetworkActions, OpSys
from cacic3.model import computers_table, descricao_hardware, select, func

from cacic3.widgets import AjaxMultiSelect

from IPy import IP

# doesn't work
# from turbogears.toolbox.catwalk import CatWalk

log = logging.getLogger("cacic3.controllers")

class Reports(object):
    report_categories = ['hardware']

    @expose()
    def index(self):
        return '<a href="/reports/hardware">Hardware</a>'

    @expose()
    def default(self, category):
        return self.build_report(category)

    @expose(template='cacic3.templates.display_report')
    def display(self, category, **kw):
        report_tables = []

        # get selected networks
        networks = kw.get('Networks', None)
        os_ids = kw.get('Operating Systems', None)

        # if none was selected, get all; there's probably a better way of handling
        # this, by conditionally adding where clauses to the reports selects
        if not networks:
            action = self._get_action_from_category(category)
            networks = [x[0] for x in self._get_network_items(action)]

        if not os_ids:
            os_ids = [x[0] for x in self._get_os_items()]

        fields = self._get_mandatory_fields () + kw['Report Items']
        if category == 'hardware':
            items = Computer.select (apply(Computer.c.netaddr.in_, networks))
            items = [item for item in items if str(item.os_id) in os_ids]
            count = 1
            for item in items:
                item.index = count
                item.os_name = item.opsys.name
                count += 1
            del count
            # force conversion to str, since there is a check with isinstance,
            # and we don't want to have field names be something other than
            # ASCII anyway
            fields = [(field.title(), str(field.strip())) for field in fields]
            grid = DataGrid (fields = fields)
            report_tables.append ((grid, items))

        if kw.has_key ('Statistics Items'):
            report_tables += self._get_statistics_tables (kw['Statistics Items'],
                                                          networks, os_ids)

        return dict(report_tables = report_tables)

    def _get_statistics_tables(self, fields, networks, os_ids):
        statistics_tables = []

        def _get_item_name (item):
            return item[1]

        def _get_item_percentage (item):
            log.debug ('ITEM: ' + str(item[0]))
            log.debug('TOTAL: ' + str(total))
            return item[0] * float(100) / total

        for field in fields:
            computer_field = eval ('computers_table.c.%s' % (field))
            # get total number of rows
            result = select ([func.count (computer_field)],
                             (descricao_hardware.c.nm_campo_tab_hardware == field)).execute ()
            total = result.fetchone ()[0]
            log.debug ('TOTAL_ANTES: ' + str(total))

            result = select ([func.count (computer_field),
                              computer_field, descricao_hardware],
                             (descricao_hardware.c.nm_campo_tab_hardware == field),
                             group_by = [computer_field]).execute ()
            grid = DataGrid (fields = 
                             [ ('Item', _get_item_name),
                               ('Percentagem', _get_item_percentage) ])
            items = result.fetchall ()
            statistics_tables.append ((grid, items))
        return statistics_tables

    def _get_mandatory_fields(self):
        return ['index', 'name', 'ipaddr', 'os_name']

    def _get_hardware_items(self):
        items = Hardware.select(order_by=Hardware.c.description)
        return [(x.field_name, x.description) for x in items]

    # FIXME: need to figure out what this is all about
    def _get_network_situation(self):
        return 'T'

    def _get_network_items(self, action):
        if self._get_network_situation () == 'T':
            items = [(x.netaddr, x.name) for x in Network.select ()]
        else:
            items = NetworkActions.select (NetworkActions.c.action == action)
            items = [(x.network.netaddr, x.network.name) for x in items]
        return items

    def _get_os_items(self):
        items = OpSys.select (OpSys.c.id > 0)
        return [(str(x.id), str(x.full_name)) for x in items]

    def _get_action_from_category(self, category):
        if category == 'hardware':
            return 'cs_coleta_hardware'

    def _report_needs_statistics(self, category):
        if category == 'hardware':
            return True

    def build_report (self, category):
        widgets = []
        items = None
        action = self._get_action_from_category(category)
        provides_statistics = self._report_needs_statistics(category)
        if not category in self.report_categories:
            turbogears.redirect ('/reports')

        get_func = eval('self._get_%s_items' % (category))
        items = get_func ()

        # Will probably find a better UI for this; something like
        # a combobox which displays the available items and allows
        # you to add them to a list; each item on that list will have
        # a checkbox that allows you to select which ones you want on
        # the statistics
        widgets.append(CheckBoxList('Report Items',
                                    options=items,
                                    validator=Int()))
        if provides_statistics:
            widgets.append(CheckBoxList('Statistics Items',
                                        options=[],
                                        validator=Int()))

        # stuff that has to be selected on all forms
        items = self._get_network_items(action)
        widgets.append(CheckBoxList('Networks',
                                    options=items,
                                    validator=Int()))

        items = self._get_os_items()
        widgets.append(CheckBoxList('Operating Systems',
                                    options=items,
                                    validator=Int()))

        tform = TableForm ("report_form", fields = widgets,
                           action = '/reports/display/%s' % (category),
                           submit_text = "Build report!")
        return dict(tform=tform, provides_statistics = provides_statistics,
                    tg_template='cacic3.templates.buildreport')

class Root(controllers.RootController):
    reports = Reports ()

    @expose(template="cacic3.templates.index")
    def index(self):
        computers = model.db.computers.select()
        return dict(computers=computers)

    @expose (template="cacic3.templates.test_widgets")
    def test_widgets(self):
        w = AjaxMultiSelect ('caraio')
        return dict(w = w)

    @expose(template="cacic3.templates.buildreport")
    def buildreport(self, category=None):
        items = Hardware.select (order_by=Hardware.c.description)
        items = [(x.field_name, x.description) for x in items]
        tform = TableForm ("Build a Hardware report", fields =
                           [CheckBoxList("hardware",
                                         options=items,
                                         validator=Int())],
                           action = '/showreport',
                           submit_text = "Build report!")
        return dict(tform=tform)

    @expose(template="cacic3.templates.showreport")
    def showreport(self, **kw):
        fields = kw['hardware']
        items = Computer.select ()
        # force conversion to str, since there is a check with isinstance,
        # and we don't want to have field names be something other than
        # ASCII anyway
        fields = [(field.title(), str(field.strip())) for field in fields]
        grid = DataGrid (fields = fields)
        return dict(grid = grid, items = items)

    @expose(template="cacic3.templates.login")
    def login(self, forward_url=None, previous_url=None, *args, **kw):

        if not identity.current.anonymous \
            and identity.was_login_attempted() \
            and not identity.get_identity_errors():
            raise redirect(forward_url)

        forward_url=None
        previous_url= cherrypy.request.path

        if identity.was_login_attempted():
            msg=_("The credentials you supplied were not correct or "
                   "did not grant access to this resource.")
        elif identity.get_identity_errors():
            msg=_("You must provide your credentials before accessing "
                   "this resource.")
        else:
            msg=_("Please log in.")
            forward_url= cherrypy.request.headers.get("Referer", "/")
        cherrypy.response.status=403
        return dict(message=msg, previous_url=previous_url, logging_in=True,
                    original_parameters=cherrypy.request.params,
                    forward_url=forward_url)

    @expose()
    def logout(self):
        identity.current.logout()
        raise redirect("/")

# class Cacic2:
    @expose()
    def cacic2(self, ws, operation, **kw):
        """Access interface to legacy agents. 
        This method is used by v2 agents and is supposed to do exactly
        what the original server does.
        """
        if not ws == 'ws':
            cherrypy.response.status = 403
            msg = "Error: expecting ws, got %s." % ws
        msg = self.old_ws(operation, kw)
        return dict(message=msg)

    def old_ws(self, operation, kw):
        """Implements http://cetico.org/cacic/comunicacao_agente-gerente
        """
        # should we check auth? I think it's useless since it's hard
        # coded in the agent. Anywait, the legacy tests are:
        # HTTP_USER_AGENT=='AGENTE_CACIC'
        # AUTH_USER=='USER_CACIC'
        # AUTH_PW=='PW_CACIC'

        db = model.new_metadata
        if operation == 'get_config.php':
            if kw.get('in_chkcacic', '') == 'chkcacic':
                # STEP 1: get_config.php
                log.debug("STEP 1 running")
                remote_ip = cherrypy.request.remote_addr
                nets = db.redes.select()
                # pick a config for this client
                try:
                    r_config = self._get_subnet_config(remote_ip, nets)
                except:
                    log.info("No subnet config found for this client")
                    # FIXME: else, get standard config if set
                    # nets = db.redes.select(model.and_(
                    # db.configuracoes.c.te_serv_updates_padrao==\
                    # db.redes.c.te_serv_updates)).select()
                    return
                else:
                    ret = '<?xml version="1.0" encoding="iso-8859-1" ?>\
<STATUS>OK</STATUS><CONFIGS>'
                    for c in model.new_metadata.redes.columns:
                        k = c.key
                        ret += '<' + str(k).upper() + '>' + getattr(r_config, k, '') + \
                            '</' + k.upper() + '>' 
                    log.debug("ret: %s" % ret)
                    return ret
                # CACIC2 would also include a partial computer account in the
                # database. For the sake of simplicity, I'll wait until step2.
            else:
                msg = "Error: get_config requires a parameters"
        elif operation == 'set_tcp_ip.php':
            # STEP 2: set_tcp_ip.php
            log.debug("STEP 2 running")
            # Get POST arguments from the request and accept only those 
            # values used in the 'computadores' table.
            set_list = [c.key for c in db.computadores.columns]
            set_machine = {}
            for s in set_list:
                set_machine[s] = kw.get(s, '')
            # FIXME: this is doing nothing
            self._update_computer(set_machine)
            # TODO: instead of returning this, we should add/update the computer in the database
            return repr(set_machine)
        else:
            msg = "Error: invalid operation found"
        return msg

    def _get_subnet_config(self,remote_ip, nets):
        """Get the config to be used for the remote client
        """
        for net in nets:
            # is the remote IP in the subnet for this config entry?
            subnet = net.id_ip_rede + '/' + net.te_mascara_rede
            log.debug("Testing subnet match: %s - %s" % (remote_ip, subnet))
            if remote_ip in IP(subnet):
                log.debug("Remote client matches %s subnet." % subnet)
                return net
        raise Exception, "No matching subnet found"

    def _update_computer(self, set_machine):
        """Updates the computer info in the database.
        Creates a new computer entry if needed.
        """
        pass

# FIXME: cherrypy.tree.mount(Cacic2(),"/cacic2")
