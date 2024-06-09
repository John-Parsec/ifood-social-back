from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class AvaliacaoPedido(models.Model):
    cod_avaliacao_pedido = models.IntegerField(db_column='COD_AVALIACAO_PEDIDO', primary_key=True)  # Field name made lowercase.
    num_nota_avaliacao = models.IntegerField(db_column='NUM_NOTA_AVALIACAO', blank=True, null=True)  # Field name made lowercase.
    txt_avaliacao = models.CharField(db_column='TXT_AVALIACAO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='COD_PEDIDO')  # Field name made lowercase.
    cod_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='COD_CLIENTE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AVALIACAO_PEDIDO'


class Bairro(models.Model):
    cod_bairro = models.IntegerField(db_column='COD_BAIRRO', primary_key=True)  # Field name made lowercase.
    dcr_bairro = models.CharField(db_column='DCR_BAIRRO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cod_cidade = models.ForeignKey('Cidade', models.DO_NOTHING, db_column='COD_CIDADE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BAIRRO'


class Cardapio(models.Model):
    cod_cardapio = models.IntegerField(db_column='COD_CARDAPIO', primary_key=True)  # Field name made lowercase.
    dcr_cardapio = models.CharField(db_column='DCR_CARDAPIO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_titulo_apres = models.CharField(db_column='DCR_TITULO_APRES', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cod_empreedimento = models.ForeignKey('Empreendimento', models.DO_NOTHING, db_column='COD_EMPREEDIMENTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARDAPIO'


class Categoria(models.Model):
    cod_categoria = models.IntegerField(db_column='COD_CATEGORIA', primary_key=True)  # Field name made lowercase.
    dcr_categoria = models.CharField(db_column='DCR_CATEGORIA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    img_categoria = models.TextField(db_column='IMG_CATEGORIA', blank=True, null=True)  # Field name made lowercase.
    cod_empreedimento = models.ForeignKey('Empreendimento', models.DO_NOTHING, db_column='COD_EMPREEDIMENTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORIA'


class Cidade(models.Model):
    cod_cidade = models.IntegerField(db_column='COD_CIDADE', primary_key=True)  # Field name made lowercase.
    dcr_cidade = models.CharField(db_column='DCR_CIDADE', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CIDADE'


class Cliente(models.Model):
    cod_cliente = models.IntegerField(db_column='COD_CLIENTE', primary_key=True)  # Field name made lowercase.
    nome_cliente = models.CharField(db_column='NOME_CLIENTE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_endereco = models.CharField(db_column='DCR_ENDERECO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_complemento = models.CharField(db_column='DCR_COMPLEMENTO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    num_cep = models.CharField(db_column='NUM_CEP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cod_cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='COD_CIDADE')  # Field name made lowercase.
    cod_bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='COD_BAIRRO')  # Field name made lowercase.
    cod_localidade = models.ForeignKey('Localidade', models.DO_NOTHING, db_column='COD_LOCALIDADE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTE'


class Disponibilidade(models.Model):
    cod_disponibilidade = models.IntegerField(db_column='COD_DISPONIBILIDADE', primary_key=True)  # Field name made lowercase.
    num_dia_semana = models.IntegerField(db_column='NUM_DIA_SEMANA', blank=True, null=True)  # Field name made lowercase.
    hora_fim = models.DateTimeField(db_column='HORA_FIM', blank=True, null=True)  # Field name made lowercase.
    hora_inicio = models.DateTimeField(db_column='HORA_INICIO', blank=True, null=True)  # Field name made lowercase.
    cod_localidade = models.ForeignKey('Localidade', models.DO_NOTHING, db_column='COD_LOCALIDADE')  # Field name made lowercase.
    cod_empreedimento = models.ForeignKey('Empreendimento', models.DO_NOTHING, db_column='COD_EMPREEDIMENTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DISPONIBILIDADE'


class DisponExcecao(models.Model):
    cod_dispon_excecao = models.IntegerField(db_column='COD_DISPON_EXCECAO', primary_key=True)  # Field name made lowercase.
    data_excecao = models.DateTimeField(db_column='DATA_EXCECAO', blank=True, null=True)  # Field name made lowercase.
    tip_excecao = models.CharField(db_column='TIP_EXCECAO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hora_inicio = models.DateTimeField(db_column='HORA_INICIO', blank=True, null=True)  # Field name made lowercase.
    hora_fim = models.DateTimeField(db_column='HORA_FIM', blank=True, null=True)  # Field name made lowercase.
    cod_empreedimento = models.ForeignKey('Empreendimento', models.DO_NOTHING, db_column='COD_EMPREEDIMENTO')  # Field name made lowercase.
    cod_localidade = models.ForeignKey('Localidade', models.DO_NOTHING, db_column='COD_LOCALIDADE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DISPON_EXCECAO'


class Empreendimento(models.Model):
    cod_empreedimento = models.IntegerField(db_column='COD_EMPREEDIMENTO', primary_key=True)  # Field name made lowercase.
    dcr_empreendimento = models.CharField(db_column='DCR_EMPREENDIMENTO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_nome_fantasia = models.CharField(db_column='DCR_NOME_FANTASIA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_endereco = models.CharField(db_column='DCR_ENDERECO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_complemento = models.CharField(db_column='DCR_COMPLEMENTO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    num_cep = models.CharField(db_column='NUM_CEP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cod_cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='COD_CIDADE')  # Field name made lowercase.
    bairro_cod_bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='BAIRRO_COD_BAIRRO')  # Field name made lowercase.
    cod_localidade = models.ForeignKey('Localidade', models.DO_NOTHING, db_column='COD_LOCALIDADE')  # Field name made lowercase.
    img_empreendimento = models.TextField(db_column='IMG_EMPREENDIMENTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPREENDIMENTO'


class EmprendFuncionario(models.Model):
    cod_empreend_funcionario = models.IntegerField(db_column='COD_EMPREEND_FUNCIONARIO', primary_key=True)  # Field name made lowercase.
    tip_funcionario = models.CharField(db_column='TIP_FUNCIONARIO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_empreedimento = models.ForeignKey(Empreendimento, models.DO_NOTHING, db_column='COD_EMPREEDIMENTO')  # Field name made lowercase.
    cod_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='COD_FUNCIONARIO')  # Field name made lowercase.
    img_empreend_funcionario = models.TextField(db_column='IMG_EMPREEND_FUNCIONARIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPREND_FUNCIONARIO'


class Entrega(models.Model):
    cod_entrega = models.IntegerField(db_column='COD_ENTREGA', primary_key=True)  # Field name made lowercase.
    cod_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='COD_PEDIDO')  # Field name made lowercase.
    cod_funcionario = models.ForeignKey('Funcionario', models.DO_NOTHING, db_column='COD_FUNCIONARIO')  # Field name made lowercase.
    data_saida = models.DateTimeField(db_column='DATA_SAIDA', blank=True, null=True)  # Field name made lowercase.
    data_entrega = models.DateTimeField(db_column='DATA_ENTREGA', blank=True, null=True)  # Field name made lowercase.
    vlr_entrega = models.DecimalField(db_column='VLR_ENTREGA', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    dcr_endereco = models.CharField(db_column='DCR_ENDERECO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_complem = models.CharField(db_column='DCR_COMPLEM', max_length=45, blank=True, null=True)  # Field name made lowercase.
    num_cep = models.CharField(db_column='NUM_CEP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    txt_referencia = models.CharField(db_column='TXT_REFERENCIA', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cod_cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='COD_CIDADE')  # Field name made lowercase.
    cod_bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='COD_BAIRRO')  # Field name made lowercase.
    cod_localidade = models.ForeignKey('Localidade', models.DO_NOTHING, db_column='COD_LOCALIDADE')  # Field name made lowercase.
    flag_encomenda = models.CharField(db_column='FLAG_ENCOMENDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    flag_entregador = models.CharField(db_column='FLAG_ENTREGADOR', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENTREGA'


class Evento(models.Model):
    cod_evento = models.IntegerField(db_column='COD_EVENTO', primary_key=True)  # Field name made lowercase.
    dcr_evento = models.CharField(db_column='DCR_EVENTO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    num_ordem_evento = models.IntegerField(db_column='NUM_ORDEM_EVENTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EVENTO'


class FormaPagto(models.Model):
    cod_forma_pagto = models.IntegerField(db_column='COD_FORMA_PAGTO', primary_key=True)  # Field name made lowercase.
    dcr_forma_pagto = models.CharField(db_column='DCR_FORMA_PAGTO', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORMA_PAGTO'


class Funcionario(models.Model):
    cod_funcionario = models.IntegerField(db_column='COD_FUNCIONARIO', primary_key=True)  # Field name made lowercase.
    nome_funcionario = models.CharField(db_column='NOME_FUNCIONARIO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    num_telefone = models.CharField(db_column='NUM_TELEFONE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dcr_email = models.CharField(db_column='DCR_EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUNCIONARIO'


class ItemPedido(models.Model):
    cod_item_pedido = models.IntegerField(db_column='COD_ITEM_PEDIDO', primary_key=True)  # Field name made lowercase.
    vlr_produto = models.DecimalField(db_column='VLR_PRODUTO', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qtd_produto = models.DecimalField(db_column='QTD_PRODUTO', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    vlr_total = models.DecimalField(db_column='VLR_TOTAL', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='COD_PEDIDO')  # Field name made lowercase.
    cod_produto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='COD_PRODUTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITEM_PEDIDO'


class Localidade(models.Model):
    cod_localidade = models.IntegerField(db_column='COD_LOCALIDADE', primary_key=True)  # Field name made lowercase.
    dcr_localidade = models.CharField(db_column='DCR_LOCALIDADE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cod_bairro = models.ForeignKey(Bairro, models.DO_NOTHING, db_column='COD_BAIRRO')  # Field name made lowercase.
    localidade_cod_localidade = models.ForeignKey('self', models.DO_NOTHING, db_column='LOCALIDADE_COD_LOCALIDADE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCALIDADE'


class Pedido(models.Model):
    cod_pedido = models.IntegerField(db_column='COD_PEDIDO', primary_key=True)  # Field name made lowercase.
    tip_pedido = models.CharField(db_column='TIP_PEDIDO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_pedido = models.DateTimeField(db_column='DATA_PEDIDO', blank=True, null=True)  # Field name made lowercase.
    vlr_pedido = models.DecimalField(db_column='VLR_PEDIDO', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cod_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='COD_CLIENTE')  # Field name made lowercase.
    cod_forma_pagto = models.ForeignKey(FormaPagto, models.DO_NOTHING, db_column='COD_FORMA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dcr_dados_pagto = models.CharField(db_column='DCR_DADOS_PAGTO', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PEDIDO'


class Produto(models.Model):
    cod_produto = models.IntegerField(db_column='COD_PRODUTO', primary_key=True)  # Field name made lowercase.
    dcr_produto = models.CharField(db_column='DCR_PRODUTO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    img_produto = models.TextField(db_column='IMG_PRODUTO', blank=True, null=True)  # Field name made lowercase.
    vlr_produto = models.DecimalField(db_column='VLR_PRODUTO', max_digits=9, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    flag_disponivel = models.CharField(db_column='FLAG_DISPONIVEL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='COD_CATEGORIA')  # Field name made lowercase.
    cod_empreedimento = models.ForeignKey(Empreendimento, models.DO_NOTHING, db_column='COD_EMPREEDIMENTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTO'


class RastreamentoPedido(models.Model):
    cod_rastreamento_pedido = models.IntegerField(db_column='COD_RASTREAMENTO_PEDIDO', primary_key=True)  # Field name made lowercase.
    cod_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='COD_PEDIDO')  # Field name made lowercase.
    cod_evento_pedido = models.ForeignKey(Evento, models.DO_NOTHING, db_column='COD_EVENTO_PEDIDO')  # Field name made lowercase.
    data_hora_evento = models.DateTimeField(db_column='DATA_HORA_EVENTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RASTREAMENTO_PEDIDO'


class SecaoCardapio(models.Model):
    cod_secao_cardapio = models.IntegerField(db_column='COD_SECAO_CARDAPIO', primary_key=True)  # Field name made lowercase.
    dcr_secao_cardapio = models.CharField(db_column='DCR_SECAO_CARDAPIO', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dcr_titulo_apres = models.CharField(db_column='DCR_TITULO_APRES', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cod_cardapio = models.ForeignKey(Cardapio, models.DO_NOTHING, db_column='COD_CARDAPIO')  # Field name made lowercase.
    num_ordem = models.IntegerField(db_column='NUM_ORDEM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SECAO_CARDAPIO'


class SecaoProduto(models.Model):
    cod_secao_produto = models.CharField(db_column='COD_SECAO_PRODUTO', primary_key=True, max_length=45)  # Field name made lowercase.
    produto_cod_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='PRODUTO_COD_PRODUTO')  # Field name made lowercase.
    secao_cardapio_cod_secao_cardapio = models.ForeignKey(SecaoCardapio, models.DO_NOTHING, db_column='SECAO_CARDAPIO_COD_SECAO_CARDAPIO')  # Field name made lowercase.
    num_ordem = models.CharField(db_column='NUM_ORDEM', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SECAO_PRODUTO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
