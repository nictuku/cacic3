from datetime import datetime

from sqlalchemy import *
from sqlalchemy.ext.activemapper import ActiveMapper, column, \
                                    one_to_many, one_to_one, many_to_many, assign_mapper

from turbogears import identity 
from turbogears.database import metadata, session

from sqlalchemy.ext.sqlsoup import SqlSoup

# hack to fix http://trac.turbogears.org/turbogears/ticket/1146
from turbogears import config
db_cfg = config.get('sqlalchemy.dburi','sqlite:///:memory:') 
local_metadata = BoundMetaData(db_cfg)
new_metadata = SqlSoup(db_cfg)

# tables properly set
# FIXME: create a primary key in this table
computers_table = Table('computadores', local_metadata, autoload=True)
configs_table = Table('configuracoes', local_metadata, autoload=True)

class Configs(object):
    pass

# assign_mapper(session.context, Configs, configs_table)

# must be adapted
acoes = Table('acoes', local_metadata, autoload=True)
acoes_excecoes = Table('acoes_excecoes', local_metadata, autoload=True)
acoes_redes = Table('acoes_redes', local_metadata, autoload=True)
acoes_so = Table('acoes_so', local_metadata, autoload=True)
aplicativos_monitorados = Table('aplicativos_monitorados', local_metadata, autoload=True)
compartilhamentos = Table('compartilhamentos', local_metadata, autoload=True)
descricao_hardware = Table('descricao_hardware', local_metadata, autoload=True)
gerentes = Table('gerentes', local_metadata, autoload=True)
gerentes_versoes_modulos = Table('gerentes_versoes_modulos', local_metadata, autoload=True)
grupo_usuarios = Table('grupo_usuarios', local_metadata, autoload=True)
historico_hardware = Table('historico_hardware', local_metadata, autoload=True)
historico_tcp_ip = Table('historico_tcp_ip', local_metadata, autoload=True)
officescan = Table('officescan', local_metadata, autoload=True)
patrimonio = Table('patrimonio', local_metadata, autoload=True)
patrimonio_config_interface = Table('patrimonio_config_interface', local_metadata, autoload=True)
perfis_aplicativos_monitorados = Table('perfis_aplicativos_monitorados', local_metadata, autoload=True)
redes = Table('redes', local_metadata, autoload=True)
redes_versoes_modulos = Table('redes_versoes_modulos', local_metadata, autoload=True)
so = Table('so', local_metadata, autoload=True)
softwares_inventariados = Table('softwares_inventariados', local_metadata, autoload=True)
softwares_inventariados_estacoes = Table('softwares_inventariados_estacoes', local_metadata, autoload=True)
tipos_unidades_disco = Table('tipos_unidades_disco', local_metadata, autoload=True)
unid_organizacional_nivel1 = Table('unid_organizacional_nivel1', local_metadata, autoload=True)
unid_organizacional_nivel2 = Table('unid_organizacional_nivel2', local_metadata, autoload=True)
unidades_disco = Table('unidades_disco', local_metadata, autoload=True)
usuarios = Table('usuarios', local_metadata, autoload=True)
variaveis_ambiente = Table('variaveis_ambiente', local_metadata, autoload=True)
variaveis_ambiente_estacoes = Table('variaveis_ambiente_estacoes', local_metadata, autoload=True)
versoes_softwares = Table('versoes_softwares', local_metadata, autoload=True)

class Network(object):
    pass
assign_mapper(session.context, Network, redes,
              properties = {
        'ipaddr': redes.c.id_ip_rede,
        'name': redes.c.nm_rede,
        }
              )

class NetworkActions(object):
    pass
assign_mapper(session.context, NetworkActions, acoes_redes,
              properties = {
        'action': acoes_redes.c.id_acao,
        'network': relation(Network, foreignkey = acoes_redes.c.id_ip_rede,
                            primaryjoin=redes.c.id_ip_rede == acoes_redes.c.id_ip_rede)
        }
              )

class Computer(object):
    pass
assign_mapper(session.context, Computer, computers_table,
              properties = { 
        'ipaddr': computers_table.c.id_ip_rede,
        'network': relation(Network, foreignkey = computers_table.c.id_ip_rede,
                            primaryjoin=redes.c.id_ip_rede == computers_table.c.id_ip_rede)
        }
              )

class Hardware(object):
    pass
assign_mapper(session.context, Hardware, descricao_hardware,
              properties = {
        'field_name': descricao_hardware.c.nm_campo_tab_hardware,
        'description': descricao_hardware.c.te_desc_hardware
        }
              )

class Visit(ActiveMapper):
    class mapping:
        __table__ = "visit"
        visit_key = column(String(40), primary_key=True)
        created = column(DateTime, nullable=False, default=datetime.now)
        expiry = column(DateTime)

    def lookup_visit(cls, visit_key):
        return Visit.get(visit_key)
    lookup_visit = classmethod(lookup_visit)

class VisitIdentity(ActiveMapper):
    class mapping:
        __table__ = "visit_identity"
        visit_key = column(String, # foreign_key="visit.visit_key",
                          primary_key=True)
        user_id = column(Integer, foreign_key="usuarios.id_usuario", index=True)

class Group(ActiveMapper):
    pass

mapper (Group, grupo_usuarios, properties = {
        'group_id': grupo_usuarios.c.id_grupo_usuarios,
        'group_name': grupo_usuarios.c.nm_grupo_usuarios,
        'display_name': grupo_usuarios.c.te_grupo_usuarios,
        'description': grupo_usuarios.c.te_descricao_grupo
        }
        )
metadata.tables['grupo_usuarios'] = grupo_usuarios

class User(ActiveMapper):
    pass

mapper (User, usuarios, properties = {
        'user_id': usuarios.c.id_usuario,
        'user_name': usuarios.c.nm_usuario_acesso,
        'display_name': usuarios.c.nm_usuario_completo,
        'password': usuarios.c.te_senha
        }
       )
metadata.tables['usuarios'] = usuarios

class Permission(object):
    pass


