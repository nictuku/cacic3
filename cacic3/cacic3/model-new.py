from datetime import datetime

#from sqlalchemy import *
#from sqlalchemy.ext.activemapper import ActiveMapper, column, \
#                                    one_to_many, one_to_one, many_to_many, assign_mapper

from turbogears import identity 
from turbogears.database import metadata, session
from turboentity import *

# hack to fix http://trac.turbogears.org/turbogears/ticket/1146
#ifrom turbogears import config
#db_cfg = config.get('sqlalchemy.dburi','sqlite:///:memory:') 
#local_metadata = BoundMetaData(db_cfg)
#local_metadata = metadata

# tables properly set
# FIXME: create a primary key in this table
#computers_table = Table('computadores', local_metadata, autoload=True)
#configs_table = Table('configuracoes', local_metadata, autoload=True)

class So(Entity):
    id_so = Column(Integer(11))
    te_desc_so = Column(String(50))
    sg_so = Column(String(10))
    
class Computadores(Entity):
    te_node_address = Column(String(17), primary_key=True)
    te_nome_computador = Column(String(25), primary_key=True)
    id_ip_rede = Column(String(15), nullable=False)
    te_dominio_windows = Column(String(30))
    te_dominio_dns = Column(String(30))
    te_placa_video_desc = Column(String(70))
    dt_hr_inclusao = Column(Date)
    te_gateway = Column(String(15))
    te_wins_primario = Column(String(15))
    te_cpu_desc = Column(String(70))    
    te_wins_secundario = Column(String(15))
    te_dns_primario = Column(String(15))
    qt_placa_video_mem = Column(Integer(11))
    te_dns_secundario = Column(String(15))
    te_placa_mae_desc = Column(String(70))
    te_serv_dhcp = Column(String(15))
    qt_mem_ram = Column(Integer(11))
    te_cpu_serial = Column(String(40))
    te_cpu_fabricante = Column(String(70))
    te_cpu_freq = Column(String(6))
    te_mem_ram_desc = Column(String(70))
    te_bios_desc = Column(String(70)) 
    dt_hr_ult_acesso = Column(Date)
    te_versao_cacic = Column(String(10))
    te_bios_fabricante = Column(String(50))
    te_placa_mae_fabricante = Column(String(70)) 
    qt_placa_video_cores = Column(Integer(11))
    te_placa_video_resolucao = Column(String(10))
    te_placa_som_desc = Column(String(50))
    te_cdrom_desc = Column(String(50))
    te_teclado_desc = Column(String(50))
    te_mouse_desc = Column(String(50))
    te_modem_desc = Column(String(70))
    te_workgroup = Column(String(20))
    dt_hr_coleta_forcada_estacao = Column(Date)
    te_nomes_curtos_modulos = Column(String(255))
    te_origem_mac = Column(String)

    id_so = OneToMany("So")
    
    
class Acoes(Entity):
    id_acao = Column(String(20))
    te_descricao_breve = Column(String(100))
    te_descricao = Column(String)
    dt_hr_alteracao = Column(Date)
    cs_situacao = Column(String(1))
    te_nome_curto_modulo = Column(String(20))


class AcoesExcecoes(Entity):
    id_acao = OneToMany("Acoes") # confirmar
    te_node_address = OneToMany("Computadores")
    id_so = ManyToMany("So") 
    

class AcoesRedes(Entity):
    id_acao = Column(String(20))
    id_ip_rede = Column(String(15))
    dt_hr_coleta_forcada = Column(Date)

class AcoesSo(Entity):
    id_acao = Column(String(20))
    id_so = Column(Integer(11))
     
    
#acoes_excecoes = Table('acoes_excecoes', local_metadata, autoload=True)
#acoes_redes = Table('acoes_redes', local_metadata, autoload=True)
#acoes_so = Table('acoes_so', local_metadata, autoload=True)
#aplicativos_monitorados = Table('aplicativos_monitorados', local_metadata, autoload=True)
#compartilhamentos = Table('compartilhamentos', local_metadata, autoload=True)
#descricao_hardware = Table('descricao_hardware', local_metadata, autoload=True)
#gerentes = Table('gerentes', local_metadata, autoload=True)
#gerentes_versoes_modulos = Table('gerentes_versoes_modulos', local_metadata, autoload=True)
#grupo_usuarios = Table('grupo_usuarios', local_metadata, autoload=True)
#historico_hardware = Table('historico_hardware', local_metadata, autoload=True)
#historico_tcp_ip = Table('historico_tcp_ip', local_metadata, autoload=True)
#officescan = Table('officescan', local_metadata, autoload=True)
#patrimonio = Table('patrimonio', local_metadata, autoload=True)
#patrimonio_config_interface = Table('patrimonio_config_interface', local_metadata, autoload=True)
#perfis_aplicativos_monitorados = Table('perfis_aplicativos_monitorados', local_metadata, autoload=True)
#redes = Table('redes', local_metadata, autoload=True)
#redes_versoes_modulos = Table('redes_versoes_modulos', local_metadata, autoload=True)
#opsys_table = Table('so', local_metadata, autoload=True)
#softwares_inventariados = Table('softwares_inventariados', local_metadata, autoload=True)
#softwares_inventariados_estacoes = Table('softwares_inventariados_estacoes', local_metadata, autoload=True)
#tipos_unidades_disco = Table('tipos_unidades_disco', local_metadata, autoload=True)
#unid_organizacional_nivel1 = Table('unid_organizacional_nivel1', local_metadata, autoload=True)
#unid_organizacional_nivel2 = Table('unid_organizacional_nivel2', local_metadata, autoload=True)
#unidades_disco = Table('unidades_disco', local_metadata, autoload=True)
#usuarios = Table('usuarios', local_metadata, autoload=True)
#variaveis_ambiente = Table('variaveis_ambiente', local_metadata, autoload=True)
#variaveis_ambiente_estacoes = Table('variaveis_ambiente_estacoes', local_metadata, autoload=True)
#versoes_softwares = Table('versoes_softwares', local_metadata, autoload=True)


#class Visit(ActiveMapper):
#    class mapping:
#        __table__ = "visit"
#        visit_key = column(String(40), primary_key=True)
#        created = column(DateTime, nullable=False, default=datetime.now)
#        expiry = column(DateTime)
#
#    def lookup_visit(cls, visit_key):
#        return Visit.get(visit_key)
#    lookup_visit = classmethod(lookup_visit)
#
#class VisitIdentity(ActiveMapper):
#    class mapping:
#        __table__ = "visit_identity"
#        visit_key = column(String, # foreign_key="visit.visit_key",
#                          primary_key=True)
#        user_id = column(Integer, foreign_key="usuarios.id_usuario", index=True)
#
#class Group(ActiveMapper):
#    pass
#
#mapper (Group, grupo_usuarios, properties = {
#        'group_id': grupo_usuarios.c.id_grupo_usuarios,
#        'group_name': grupo_usuarios.c.nm_grupo_usuarios,
#        'display_name': grupo_usuarios.c.te_grupo_usuarios,
#        'description': grupo_usuarios.c.te_descricao_grupo
#        }
#        )
#metadata.tables['grupo_usuarios'] = grupo_usuarios
#
#class User(ActiveMapper):
#    pass
#
#mapper (User, usuarios, properties = {
#        'user_id': usuarios.c.id_usuario,
#        'user_name': usuarios.c.nm_usuario_acesso,
#        'display_name': usuarios.c.nm_usuario_completo,
#        'password': usuarios.c.te_senha
#        }
#       )
#metadata.tables['usuarios'] = usuarios
#
#class Permission(object):
#    pass
#
#
