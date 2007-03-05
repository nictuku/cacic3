from datetime import datetime

from turbogears.database import metadata, session
from elixir import Unicode, DateTime, String, Integer, Field
from elixir import Entity, has_field, using_options
from elixir import has_many, belongs_to, has_and_belongs_to_many,with_fields
from sqlalchemy import ForeignKey
from datetime import datetime

class So(Entity):
    with_fields(
        id_so = Field(Integer(11)),
        te_desc_so = Field(String(50)),
        sg_so = Field(String(10)),
    )
    has_many('computadores', of_kind='Computadores')
    has_many('acoes_excecao', of_kind='AcoesExcecoes')

    
class Computadores(Entity):
    with_fields(
        te_node_address = Field(String(17), primary_key=True),
        te_nome_computador = Field(String(25)),
        id_ip_rede = Field(String(15), nullable=False),
        te_dominio_windows = Field(String(30)),
        te_dominio_dns = Field(String(30)),
        te_placa_video_desc = Field(String(70)),
        dt_hr_inclusao = Field(DateTime),
        te_gateway = Field(String(15)),
        te_wins_primario = Field(String(15)),
        te_cpu_desc = Field(String(70))    ,
        te_wins_secundario = Field(String(15)),
        te_dns_primario = Field(String(15)),
        qt_placa_video_mem = Field(Integer(11)),
        te_dns_secundario = Field(String(15)),
        te_placa_mae_desc = Field(String(70)),
        te_serv_dhcp = Field(String(15)),
        qt_mem_ram = Field(Integer(11)),
        te_cpu_serial = Field(String(40)),
        te_cpu_fabricante = Field(String(70)),
        te_cpu_freq = Field(String(6)),
        te_mem_ram_desc = Field(String(70)),
        te_bios_desc = Field(String(70)) ,
        dt_hr_ult_acesso = Field(DateTime),
        te_versao_cacic = Field(String(10), primary_key=True),
        te_bios_fabricante = Field(String(50)),
        te_placa_mae_fabricante = Field(String(70)) ,
        qt_placa_video_cores = Field(Integer(11)),
        te_placa_video_resolucao = Field(String(10)),
        te_placa_som_desc = Field(String(50)),
        te_cdrom_desc = Field(String(50)),
        te_teclado_desc = Field(String(50)),
        te_mouse_desc = Field(String(50)),
        te_modem_desc = Field(String(70)),
        te_workgroup = Field(String(20)),
        dt_hr_coleta_forcada_estacao = Field(DateTime),
        te_nomes_curtos_modulos = Field(String(255)),
        te_origem_mac = Field(String),
    )
    belongs_to('so', of_kind='So', colname='id_so')
    has_many('acoes_excecoes', of_kind='AcoesExcecoes')
    using_options(tablename='computadores')
    
class Acoes(Entity):
    with_fields(
        id_acao = Field(String(20)),
        te_descricao_breve = Field(String(100)),
        te_descricao = Field(String),
        dt_hr_alteracao = Field(DateTime),
        cs_situacao = Field(String(1)),
        te_nome_curto_modulo = Field(String(20)),
    )
    has_many('acoes_excecoes', of_kind='AcoesExcecoes')
    using_options(tablename='acoes')


class AcoesExcecoes(Entity):
    belongs_to('acoes', of_kind='Acoes', colname='id_acao')
    belongs_to('computadores', of_kind='Computadores', colname=[ 'te_node_address', 'te_versao_cacic'])
    belongs_to('so', of_kind='So', colname='id_so')
    using_options(tablename='acoes_excecoes')
    

#class AcoesRedes(Entity):
#    id_acao = Field(String(20))
#    id_ip_rede = Field(String(15))
#    dt_hr_coleta_forcada = Field(DateTime)
#
#class AcoesSo(Entity):
#    id_acao = Field(String(20))
#    id_so = Field(Integer(11))
#     
#    

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
