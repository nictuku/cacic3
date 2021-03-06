from datetime import datetime

from turbogears.database import metadata, session
from elixir import Unicode, DateTime, String, Integer, TEXT, CHAR, Field
from elixir import Entity, has_field, using_options
from elixir import has_many, belongs_to, has_and_belongs_to_many,with_fields,has_one
from sqlalchemy import ForeignKey
from datetime import datetime

class acoes(Entity):

    has_field('id_acao',String,primary_key=True,nullable=False,default=None),
    has_field('te_descricao_breve',String,nullable=True,default=None),
    has_field('te_descricao',TEXT,nullable=True,default=None),
    has_field('dt_hr_alteracao',DateTime,nullable=True,default=datetime.now),
    has_field('cs_situacao',CHAR,nullable=True,default=None),
    has_field('te_nome_curto_modulo',String,nullable=True,default=None),

    has_many('acoes_excecoes', of_kind='acoes_excecoes')
    using_options(tablename='acoes')

class acoes_excecoes(Entity):

    belongs_to('acoes', of_kind='acoes', colname='id_acao')
    belongs_to('computadores', of_kind='computadores', colname=[ 'te_node_address'])
    belongs_to('so', of_kind='so', colname='id_so')
    using_options(tablename='acoes_excecoes')

class acoes_redes(Entity):

    has_field('id_acao',String,primary_key=True,nullable=False,default=None,
        key='action'),
    has_field('id_ip_rede',String,primary_key=True,nullable=False,default=None),
    has_field('dt_hr_coleta_forcada',DateTime,nullable=True,default=None),

    
   #     'network': relation(Network, foreignkey = acoes_redes.c.id_ip_rede,
   #                                 primaryjoin=redes.c.id_ip_rede == acoes_redes.c.id_ip_rede)

    using_options(tablename='acoes_redes')

class acoes_so(Entity):

    has_field('id_acao',String,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),

    using_options(tablename='acoes_so')

class aplicativos_monitorados(Entity):

    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('id_aplicativo',Integer,primary_key=True,nullable=False,default=0),
    has_field('te_versao',String,nullable=True,default=None),
    has_field('te_licenca',String,nullable=True,default=None),
    has_field('te_ver_engine',String,nullable=True,default=None),
    has_field('te_ver_pattern',String,nullable=True,default=None),
    has_field('cs_instalado',CHAR,nullable=True,default=None),

    using_options(tablename='aplicativos_monitorados')

class compartilhamentos(Entity):

    has_field('nm_compartilhamento',String,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('nm_dir_compart',String,nullable=True,default=None),
    has_field('in_senha_escrita',CHAR,nullable=True,default=None),
    has_field('in_senha_leitura',CHAR,nullable=True,default=None),
    has_field('cs_tipo_permissao',CHAR,nullable=True,default=None),
    has_field('cs_tipo_compart',CHAR,nullable=True,default=None),
    has_field('te_comentario',String,nullable=True,default=None),

    using_options(tablename='compartilhamentos')

class computadores(Entity):

    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('te_nome_computador',String,nullable=True,default=None),
    has_field('id_ip_rede',String,nullable=False,default=None),
    has_field('te_dominio_windows',String,nullable=True,default=None),
    has_field('te_dominio_dns',String,nullable=True,default=None),
    has_field('te_placa_video_desc',String,nullable=True,default=None),
    has_field('te_ip',String,nullable=True,default=None),
    has_field('te_mascara',String,nullable=True,default=None),
    has_field('te_nome_host',String,nullable=True,default=None),
    has_field('te_placa_rede_desc',String,nullable=True,default=None),
    has_field('dt_hr_inclusao',DateTime,nullable=True,default=None),
    has_field('te_gateway',String,nullable=True,default=None),
    has_field('te_wins_primario',String,nullable=True,default=None),
    has_field('te_cpu_desc',String,nullable=True,default=None),
    has_field('te_wins_secundario',String,nullable=True,default=None),
    has_field('te_dns_primario',String,nullable=True,default=None),
    has_field('qt_placa_video_mem',Integer,nullable=True,default=None),
    has_field('te_dns_secundario',String,nullable=True,default=None),
    has_field('te_placa_mae_desc',String,nullable=True,default=None),
    has_field('te_serv_dhcp',String,nullable=True,default=None),
    has_field('qt_mem_ram',Integer,nullable=True,default=None),
    has_field('te_cpu_serial',String,nullable=True,default=None),
    has_field('te_cpu_fabricante',String,nullable=True,default=None),
    has_field('te_cpu_freq',String,nullable=True,default=None),
    has_field('te_mem_ram_desc',String,nullable=True,default=None),
    has_field('te_bios_desc',String,nullable=True,default=None),
    has_field('te_bios_data',String,nullable=True,default=None),
    has_field('dt_hr_ult_acesso',DateTime,nullable=True,default=None),
    has_field('te_versao_cacic',String,nullable=True,default=None),
    has_field('te_bios_fabricante',String,nullable=True,default=None),
    has_field('te_placa_mae_fabricante',String,nullable=True,default=None),
    has_field('qt_placa_video_cores',Integer,nullable=True,default=None),
    has_field('te_placa_video_resolucao',String,nullable=True,default=None),
    has_field('te_placa_som_desc',String,nullable=True,default=None),
    has_field('te_cdrom_desc',String,nullable=True,default=None),
    has_field('te_teclado_desc',String,nullable=False,default=None),
    has_field('te_mouse_desc',String,nullable=True,default=None),
    has_field('te_modem_desc',String,nullable=True,default=None),
    has_field('te_workgroup',String,nullable=True,default=None),
    has_field('dt_hr_coleta_forcada_estacao',DateTime,nullable=True,default=None),
    has_field('te_nomes_curtos_modulos',String,nullable=True,default=None),
    has_field('te_origem_mac',TEXT,nullable=True,default=None),

    belongs_to('so', of_kind='So', colname='id_so', primary_key=True)
    has_many('acoes_excecoes', of_kind='acoes_excecoes', inverse='computadores')
    using_options(tablename='computadores')

class configuracoes(Entity):

    has_field('te_notificar_mudanca_hardware',TEXT,nullable=True,default=None),
    has_field('in_exibe_erros_criticos',CHAR,nullable=True,default=None),
    has_field('in_exibe_bandeja',CHAR,nullable=True,default=None),
    has_field('nu_exec_apos',Integer,nullable=True,default=None),
    has_field('dt_hr_alteracao_patrim_interface',DateTime,nullable=True,default=None),
    has_field('dt_hr_alteracao_patrim_uon1',DateTime,nullable=True,default=datetime.now),
    has_field('dt_hr_alteracao_patrim_uon2',DateTime,nullable=True,default=None),
    has_field('dt_hr_coleta_forcada',DateTime,nullable=True,default=None),
    has_field('te_notificar_mudanca_patrim',TEXT,nullable=True,default=None),
    has_field('nm_organizacao',String,nullable=True,default=None),
    has_field('nu_intervalo_exec',Integer,nullable=True,default=None),
    has_field('nu_intervalo_renovacao_patrim',Integer,nullable=True,default=None),
    has_field('te_senha_adm_agente',String,nullable=True,default=None),
    has_field('te_super_gerentes',TEXT,nullable=True,default=None),
    has_field('te_serv_updates_padrao',String,nullable=True,default=None),
    has_field('te_serv_banco_padrao',String,nullable=True,default=None),
    has_field('te_enderecos_mac_invalidos',TEXT,nullable=True,default=None),
    has_field('te_janelas_excecao',TEXT,nullable=True,default=None),

    using_options(tablename='configuracoes')

class descricao_hardware(Entity):

    has_field('nm_campo_tab_hardware',String,primary_key=True,nullable=False,default=None,key='field_name'),
    has_field('te_desc_hardware',String,nullable=False,default=None,key='description')
    has_field('cs_notificacao_ativada',CHAR,nullable=True,default=None),

    using_options(tablename='descricao_hardware')

class gerentes(Entity):

    has_field('id_ip_gerente',String,primary_key=True,nullable=False,default=None),
    has_field('nm_gerente',String,nullable=True,default=None),
    has_field('te_observacao',String,nullable=True,default=None),
    has_field('nm_pessoa_contato',String,nullable=True,default=None),
    has_field('nu_telefone',String,nullable=True,default=None),
    has_field('te_email_contato',String,nullable=True,default=None),
    has_field('nm_usuario_login_repositorio',String,nullable=True,default=None),
    has_field('te_senha_login_repositorio',String,nullable=True,default=None),
    has_field('te_path_repositorio',String,nullable=False,default=None),
    has_field('nu_porta_repositorio',String,nullable=True,default=None),

    using_options(tablename='gerentes')

class gerentes_versoes_modulos(Entity):

    has_field('id_ip_gerente',String,primary_key=True,nullable=False,default=None),
    has_field('nm_modulo',String,nullable=True,default=None),
    has_field('te_versao_modulo',String,nullable=True,default=None),

    using_options(tablename='gerentes_versoes_modulos')

class group_permission(Entity):

    has_field('group_id',Integer,primary_key=True,nullable=False,default=None),
    has_field('permission_id',Integer,primary_key=True,nullable=False,default=None),

    using_options(tablename='group_permission')

class grupo_usuarios(Entity):

    has_field('id_grupo_usuarios',Integer,primary_key=True,nullable=False,default=None),
    has_field('te_grupo_usuarios',String,nullable=True,default=None),
    has_field('te_menu_grupo',String,nullable=True,default=None),
    has_field('nm_grupo_usuarios',String,nullable=False,default=None),
    has_field('te_descricao_grupo',TEXT,nullable=False,default=None),

    using_options(tablename='grupo_usuarios')
    belongs_to('group', of_kind='Group', 
        #colname=[ 'id_grupo_usuarios',
        #'nm_grupo_usuarios','te_grupo_usuarios','te_descricao_grupo' ]
        )

class historico_hardware(Entity):

    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('dt_hr_alteracao',DateTime,primary_key=True,nullable=False,default=datetime.now),
    has_field('te_placa_video_desc',String,nullable=True,default=None),
    has_field('te_placa_rede_desc',String,nullable=True,default=None),
    has_field('te_cpu_desc',String,nullable=True,default=None),
    has_field('qt_placa_video_mem',Integer,nullable=True,default=None),
    has_field('te_placa_mae_desc',String,nullable=True,default=None),
    has_field('qt_mem_ram',Integer,nullable=True,default=None),
    has_field('te_cpu_serial',String,nullable=True,default=None),
    has_field('te_cpu_fabricante',String,nullable=True,default=None),
    has_field('te_cpu_freq',String,nullable=True,default=None),
    has_field('te_mem_ram_desc',String,nullable=True,default=None),
    has_field('te_bios_desc',String,nullable=True,default=None),
    has_field('te_bios_data',String,nullable=True,default=None),
    has_field('te_bios_fabricante',String,nullable=True,default=None),
    has_field('te_placa_mae_fabricante',String,nullable=True,default=None),
    has_field('qt_placa_video_cores',Integer,nullable=True,default=None),
    has_field('te_placa_video_resolucao',String,nullable=True,default=None),
    has_field('te_placa_som_desc',String,nullable=True,default=None),
    has_field('te_cdrom_desc',String,nullable=True,default=None),
    has_field('te_teclado_desc',String,nullable=True,default=None),
    has_field('te_mouse_desc',String,nullable=True,default=None),
    has_field('te_modem_desc',String,nullable=True,default=None),
    has_field('te_lic_win',String,nullable=True,default=None),
    has_field('te_key_win',String,nullable=True,default=None),

    using_options(tablename='historico_hardware')

class historico_tcp_ip(Entity):

    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('dt_hr_alteracao',DateTime,primary_key=True,nullable=False,default=datetime.now),
    has_field('te_nome_computador',String,nullable=True,default=None),
    has_field('te_dominio_windows',String,nullable=True,default=None),
    has_field('te_dominio_dns',String,nullable=True,default=None),
    has_field('te_ip',String,nullable=True,default=None),
    has_field('te_mascara',String,nullable=True,default=None),
    has_field('id_ip_rede',String,nullable=True,default=None),
    has_field('te_nome_host',String,nullable=True,default=None),
    has_field('te_gateway',String,nullable=True,default=None),
    has_field('te_wins_primario',String,nullable=True,default=None),
    has_field('te_wins_secundario',String,nullable=True,default=None),
    has_field('te_dns_primario',String,nullable=True,default=None),
    has_field('te_dns_secundario',String,nullable=True,default=None),
    has_field('te_serv_dhcp',String,nullable=True,default=None),
    has_field('te_workgroup',String,nullable=True,default=None),

    using_options(tablename='historico_tcp_ip')

class officescan(Entity):

    has_field('nu_versao_engine',String,nullable=True,default=None),
    has_field('nu_versao_pattern',String,nullable=True,default=None),
    has_field('dt_hr_instalacao',DateTime,nullable=True,default=None),
    has_field('dt_hr_coleta',DateTime,nullable=True,default=None),
    has_field('te_servidor',String,nullable=True,default=None),
    has_field('in_ativo',CHAR,nullable=True,default=None),
    has_field('te_node_address',String,nullable=False,default=None),
    has_field('id_so',Integer,nullable=False,default=0),

    using_options(tablename='officescan')

class patrimonio(Entity):

    has_field('id_unid_organizacional_nivel1',Integer,nullable=True,default=None),
    has_field('id_so',Integer,nullable=False,default=0),
    has_field('dt_hr_alteracao',DateTime,primary_key=True,nullable=False,default=datetime.now),
    has_field('te_node_address',String,nullable=True,default=None),
    has_field('id_unid_organizacional_nivel2',Integer,nullable=True,default=None),
    has_field('te_localizacao_complementar',String,nullable=True,default=None),
    has_field('te_info_patrimonio1',String,nullable=True,default=None),
    has_field('te_info_patrimonio2',String,nullable=True,default=None),
    has_field('te_info_patrimonio3',String,nullable=True,default=None),
    has_field('te_info_patrimonio4',String,nullable=True,default=None),
    has_field('te_info_patrimonio5',String,nullable=True,default=None),
    has_field('te_info_patrimonio6',String,nullable=True,default=None),

    using_options(tablename='patrimonio')

class patrimonio_config_interface(Entity):

    has_field('id_etiqueta',String,primary_key=True,nullable=False,default=None),
    has_field('nm_etiqueta',String,nullable=True,default=None),
    has_field('te_etiqueta',String,nullable=False,default=None),
    has_field('in_exibir_etiqueta',CHAR,nullable=True,default=None),
    has_field('te_help_etiqueta',String,nullable=True,default=None),
    has_field('te_plural_etiqueta',String,nullable=True,default=None),
    has_field('nm_campo_tab_patrimonio',String,nullable=True,default=None),
    has_field('in_destacar_duplicidade',CHAR,nullable=True,default='N'),

    using_options(tablename='patrimonio_config_interface')

class perfis_aplicativos_monitorados(Entity):

    has_field('id_aplicativo',Integer,primary_key=True,nullable=False,default=None),
    has_field('nm_aplicativo',String,nullable=False,default=None),
    has_field('cs_car_inst_w9x',CHAR,nullable=True,default=None),
    has_field('te_car_inst_w9x',String,nullable=True,default=None),
    has_field('cs_car_ver_w9x',CHAR,nullable=True,default=None),
    has_field('te_car_ver_w9x',String,nullable=True,default=None),
    has_field('cs_car_inst_wnt',CHAR,nullable=True,default=None),
    has_field('te_car_inst_wnt',String,nullable=True,default=None),
    has_field('cs_car_ver_wnt',CHAR,nullable=True,default=None),
    has_field('te_car_ver_wnt',String,nullable=True,default=None),
    has_field('cs_ide_licenca',CHAR,nullable=True,default=None),
    has_field('te_ide_licenca',String,nullable=True,default=None),
    has_field('dt_atualizacao',DateTime,nullable=False,default=datetime.now),
    has_field('te_arq_ver_eng_w9x',String,nullable=True,default=None),
    has_field('te_arq_ver_pat_w9x',String,nullable=True,default=None),
    has_field('te_arq_ver_eng_wnt',String,nullable=True,default=None),
    has_field('te_arq_ver_pat_wnt',String,nullable=True,default=None),
    has_field('te_dir_padrao_w9x',String,nullable=True,default=None),
    has_field('te_dir_padrao_wnt',String,nullable=True,default=None),
    has_field('id_so',Integer,nullable=True,default=0),
    has_field('te_descritivo',TEXT,nullable=True,default=None),
    has_field('in_disponibiliza_info',CHAR,nullable=True,default='N'),

    using_options(tablename='perfis_aplicativos_monitorados')

class permission(Entity):

    has_field('description',String,nullable=True,default=None),
    has_field('permission_id',Integer,primary_key=True,nullable=False,default=None),
    has_field('permission_name',String,nullable=True,default=None),

    using_options(tablename='permission')

class redes(Entity):

    has_field('id_ip_rede',String,primary_key=True,nullable=False,default=None,
        key='netaddr'),
    has_field('nm_rede',String,nullable=True,default=None,
        key='name'),
    has_field('te_observacao',String,nullable=True,default=None),
    has_field('nm_pessoa_contato1',String,nullable=True,default=None),
    has_field('nm_pessoa_contato2',String,nullable=True,default=None),
    has_field('nu_telefone1',String,nullable=True,default=None),
    has_field('te_email_contato2',String,nullable=True,default=None),
    has_field('nu_telefone2',String,nullable=True,default=None),
    has_field('te_email_contato1',String,nullable=True,default=None),
    has_field('te_serv_cacic',String,nullable=True,default=None),
    has_field('te_serv_updates',String,nullable=True,default=None),
    has_field('te_path_serv_updates',String,nullable=True,default=None),
    has_field('nm_usuario_login_serv_updates',String,nullable=True,default=None),
    has_field('te_senha_login_serv_updates',String,nullable=True,default=None),
    has_field('nu_porta_serv_updates',String,nullable=True,default=None),
    has_field('te_mascara_rede',String,nullable=True,default=None),
    has_field('dt_verifica_updates',DateTime,nullable=True,default=None),

    using_options(tablename='redes')

class redes_versoes_modulos(Entity):

    has_field('id_ip_rede',String,primary_key=True,nullable=False,default=None),
    has_field('nm_modulo',String,primary_key=True,nullable=False,default=None),
    has_field('te_versao_modulo',String,nullable=True,default=None),

    using_options(tablename='redes_versoes_modulos')

class so(Entity):

    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('te_desc_so',String,nullable=True,default=None,
        key='full_name'),
    has_field('sg_so',String,nullable=True,default=None,
        key='name'),
    has_many('computadores', of_kind='Computadores')
    has_many('acoes_excecao', of_kind='AcoesExcecoes')

    using_options(tablename='so')

class softwares_inventariados(Entity):

    has_field('id_software_inventariado',Integer,primary_key=True,nullable=False,default=None),
    has_field('nm_software_inventariado',String,nullable=False,default=None),

    using_options(tablename='softwares_inventariados')

class softwares_inventariados_estacoes(Entity):

    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('id_software_inventariado',Integer,primary_key=True,nullable=False,default=0),

    using_options(tablename='softwares_inventariados_estacoes')

class tipos_unidades_disco(Entity):

    has_field('id_tipo_unid_disco',CHAR,primary_key=True,nullable=False,default=None),
    has_field('te_tipo_unid_disco',String,nullable=True,default=None),

    using_options(tablename='tipos_unidades_disco')

class unid_organizacional_nivel1(Entity):

    has_field('id_unid_organizacional_nivel1',Integer,primary_key=True,nullable=False,default=None),
    has_field('nm_unid_organizacional_nivel1',String,nullable=True,default=None),
    has_field('te_endereco_uon1',String,nullable=True,default=None),
    has_field('te_bairro_uon1',String,nullable=True,default=None),
    has_field('te_cidade_uon1',String,nullable=True,default=None),
    has_field('te_uf_uon1',CHAR,nullable=True,default=None),
    has_field('nm_responsavel_uon1',String,nullable=True,default=None),
    has_field('te_email_responsavel_uon1',String,nullable=True,default=None),
    has_field('nu_tel1_responsavel_uon1',String,nullable=True,default=None),
    has_field('nu_tel2_responsavel_uon1',String,nullable=True,default=None),

    using_options(tablename='unid_organizacional_nivel1')

class unid_organizacional_nivel2(Entity):

    has_field('id_unid_organizacional_nivel2',Integer,primary_key=True,nullable=False,default=None),
    has_field('id_unid_organizacional_nivel1',Integer,primary_key=True,nullable=False,default=0),
    has_field('nm_unid_organizacional_nivel2',String,nullable=False,default=None),
    has_field('te_endereco_uon2',String,nullable=True,default=None),
    has_field('te_bairro_uon2',String,nullable=True,default=None),
    has_field('te_cidade_uon2',String,nullable=True,default=None),
    has_field('te_uf_uon2',CHAR,nullable=True,default=None),
    has_field('nm_responsavel_uon2',String,nullable=True,default=None),
    has_field('te_email_responsavel_uon2',String,nullable=True,default=None),
    has_field('nu_tel1_responsavel_uon2',String,nullable=True,default=None),
    has_field('nu_tel2_responsavel_uon2',String,nullable=True,default=None),

    using_options(tablename='unid_organizacional_nivel2')

class unidades_disco(Entity):

    has_field('te_letra',CHAR,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('id_tipo_unid_disco',CHAR,nullable=True,default=None),
    has_field('nu_serial',String,nullable=True,default=None),
    has_field('nu_capacidade',Integer,nullable=True,default=None),
    has_field('nu_espaco_livre',Integer,nullable=True,default=None),
    has_field('te_unc',String,nullable=True,default=None),
    has_field('cs_sist_arq',String,nullable=True,default=None),

    using_options(tablename='unidades_disco')

class user_group(Entity):
    """This came from TG, I think
    """

    has_field('user_id',Integer,primary_key=True,nullable=False,default=None),
    has_field('group_id',Integer,primary_key=True,nullable=False,default=None),

    belongs_to('group', of_kind='Group')
    using_options(tablename='user_group')

class usuarios(Entity):

    has_field('id_usuario',Integer,primary_key=True,nullable=False,default=None),
    has_field('nm_usuario_acesso',String,nullable=False,default=None),
    has_field('nm_usuario_completo',String,nullable=False,default=None),
    has_field('te_senha',String,nullable=False,default=None),
    has_field('dt_log_in',DateTime,nullable=False,default=datetime.now),
    has_field('id_grupo_usuarios',Integer,nullable=True,default=None),

    belongs_to('user_id', of_kind='VisitIdentity', colname='id_usuario' )
    belongs_to('user_name', of_kind='VisitIdentity', colname='nm_usuario_acesso' )
    belongs_to('display_name',  of_kind='VisitIdentity', colname='nm_usuario_completo')
    belongs_to('password', of_kind='VisitIdentity', colname='te_senha')
    using_options(tablename='usuarios')

class variaveis_ambiente(Entity):

    has_field('id_variavel_ambiente',Integer,primary_key=True,nullable=False,default=None),
    has_field('nm_variavel_ambiente',String,nullable=False,default=None),

    using_options(tablename='variaveis_ambiente')

class variaveis_ambiente_estacoes(Entity):

    has_field('te_node_address',String,primary_key=True,nullable=False,default=None),
    has_field('id_so',Integer,primary_key=True,nullable=False,default=0),
    has_field('id_variavel_ambiente',Integer,primary_key=True,nullable=False,default=0),
    has_field('vl_variavel_ambiente',String,nullable=False,default=None),

    using_options(tablename='variaveis_ambiente_estacoes')

class versoes_softwares(Entity):

    has_field('id_so',Integer,nullable=False,default=0),
    has_field('te_node_address',String,nullable=False,default=None),
    has_field('te_versao_bde',String,nullable=True,default=None),
    has_field('te_versao_dao',String,nullable=True,default=None),
    has_field('te_versao_ado',String,nullable=True,default=None),
    has_field('te_versao_odbc',String,nullable=True,default=None),
    has_field('te_versao_directx',Integer,nullable=True,default=None),
    has_field('te_versao_acrobat_reader',String,nullable=True,default=None),
    has_field('te_versao_ie',String,nullable=True,default=None),
    has_field('te_versao_mozilla',String,nullable=True,default=None),
    has_field('te_versao_jre',String,nullable=True,default=None),

    using_options(tablename='versoes_softwares')

class Visit(Entity):

    has_field('created',DateTime,nullable=False,default=None),
    has_field('expiry',DateTime,nullable=True,default=None),
    has_field('visit_key',String,primary_key=True,nullable=False,default=None),

    using_options(tablename='visit')

    def lookup_visit(cls, visit_key):
        return Visit.get(visit_key)
    lookup_visit = classmethod(lookup_visit)

class VisitIdentity(Entity):

    has_field('visit_key',String,primary_key=True,nullable=False,default=None),
    has_one('user_id', of_kind="usuarios", inverse='user_id'),

    using_options(tablename='visit_identity')


class Group(Entity):
    has_one('group_id', of_kind='grupo_usuarios', inverse='group')
    has_one('group_name', of_kind='grupo_usuarios', inverse='group'),
    has_one('display_name', of_kind='grupo_usuarios', inverse='group'),
    has_one('description', of_kind='grupo_usuarios', inverse='group')

# still useful?
# metadata.tables['grupo_usuarios'] = grupo_usuarios.table

class User(Entity):
    has_one('user_id', of_kind='usuarios', inverse='user_id')
    has_one('user_name', of_kind='usuarios', inverse='user_name')
    has_one('display_name', of_kind='usuarios', inverse='display_name')
    has_one('password', of_kind='usuarios', inverse='password')    

# still useful?
# metadata.tables['usuarios'] = usuarios.table

class Permission(object):
    pass

# transitional classes. we will only use these in the future
class Computer(computadores):
    pass

class Hardware(descricao_hardware):
    pass
    
class Network(redes):
    pass

class NetworkActions(acoes_redes):
    pass

class OpSys(so):
    pass

