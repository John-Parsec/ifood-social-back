# Generated by Django 5.0.3 on 2024-06-17 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cidade",
            fields=[
                (
                    "cod_cidade",
                    models.IntegerField(
                        db_column="COD_CIDADE", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_cidade",
                    models.CharField(
                        blank=True, db_column="DCR_CIDADE", max_length=45, null=True
                    ),
                ),
            ],
            options={
                "db_table": "CIDADE",
            },
        ),
        migrations.CreateModel(
            name="Evento",
            fields=[
                (
                    "cod_evento",
                    models.IntegerField(
                        db_column="COD_EVENTO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_evento",
                    models.CharField(
                        blank=True, db_column="DCR_EVENTO", max_length=45, null=True
                    ),
                ),
                (
                    "num_ordem_evento",
                    models.IntegerField(
                        blank=True, db_column="NUM_ORDEM_EVENTO", null=True
                    ),
                ),
            ],
            options={
                "db_table": "EVENTO",
            },
        ),
        migrations.CreateModel(
            name="FormaPagto",
            fields=[
                (
                    "cod_forma_pagto",
                    models.IntegerField(
                        db_column="COD_FORMA_PAGTO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_forma_pagto",
                    models.CharField(
                        blank=True,
                        db_column="DCR_FORMA_PAGTO",
                        max_length=45,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "FORMA_PAGTO",
            },
        ),
        migrations.CreateModel(
            name="Funcionario",
            fields=[
                (
                    "cod_funcionario",
                    models.IntegerField(
                        db_column="COD_FUNCIONARIO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "nome_funcionario",
                    models.CharField(
                        blank=True,
                        db_column="NOME_FUNCIONARIO",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "num_telefone",
                    models.CharField(
                        blank=True, db_column="NUM_TELEFONE", max_length=15, null=True
                    ),
                ),
                (
                    "dcr_email",
                    models.CharField(
                        blank=True, db_column="DCR_EMAIL", max_length=45, null=True
                    ),
                ),
            ],
            options={
                "db_table": "FUNCIONARIO",
            },
        ),
        migrations.CreateModel(
            name="Bairro",
            fields=[
                (
                    "cod_bairro",
                    models.IntegerField(
                        db_column="COD_BAIRRO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_bairro",
                    models.CharField(
                        blank=True, db_column="DCR_BAIRRO", max_length=45, null=True
                    ),
                ),
                (
                    "cod_cidade",
                    models.ForeignKey(
                        db_column="COD_CIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.cidade",
                    ),
                ),
            ],
            options={
                "db_table": "BAIRRO",
            },
        ),
        migrations.CreateModel(
            name="Empreendimento",
            fields=[
                (
                    "cod_empreedimento",
                    models.IntegerField(
                        db_column="COD_EMPREEDIMENTO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_empreendimento",
                    models.CharField(
                        blank=True,
                        db_column="DCR_EMPREENDIMENTO",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "dcr_nome_fantasia",
                    models.CharField(
                        blank=True,
                        db_column="DCR_NOME_FANTASIA",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "dcr_endereco",
                    models.CharField(
                        blank=True, db_column="DCR_ENDERECO", max_length=45, null=True
                    ),
                ),
                (
                    "dcr_complemento",
                    models.CharField(
                        blank=True,
                        db_column="DCR_COMPLEMENTO",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "num_cep",
                    models.CharField(
                        blank=True, db_column="NUM_CEP", max_length=10, null=True
                    ),
                ),
                (
                    "img_empreendimento",
                    models.TextField(
                        blank=True, db_column="IMG_EMPREENDIMENTO", null=True
                    ),
                ),
                (
                    "bairro_cod_bairro",
                    models.ForeignKey(
                        db_column="BAIRRO_COD_BAIRRO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.bairro",
                    ),
                ),
                (
                    "cod_cidade",
                    models.ForeignKey(
                        db_column="COD_CIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.cidade",
                    ),
                ),
            ],
            options={
                "db_table": "EMPREENDIMENTO",
            },
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "cod_categoria",
                    models.IntegerField(
                        db_column="COD_CATEGORIA", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_categoria",
                    models.CharField(
                        blank=True, db_column="DCR_CATEGORIA", max_length=45, null=True
                    ),
                ),
                (
                    "img_categoria",
                    models.TextField(blank=True, db_column="IMG_CATEGORIA", null=True),
                ),
                (
                    "cod_empreedimento",
                    models.ForeignKey(
                        db_column="COD_EMPREEDIMENTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.empreendimento",
                    ),
                ),
            ],
            options={
                "db_table": "CATEGORIA",
            },
        ),
        migrations.CreateModel(
            name="Cardapio",
            fields=[
                (
                    "cod_cardapio",
                    models.IntegerField(
                        db_column="COD_CARDAPIO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_cardapio",
                    models.CharField(
                        blank=True, db_column="DCR_CARDAPIO", max_length=45, null=True
                    ),
                ),
                (
                    "dcr_titulo_apres",
                    models.CharField(
                        blank=True,
                        db_column="DCR_TITULO_APRES",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "cod_empreedimento",
                    models.ForeignKey(
                        db_column="COD_EMPREEDIMENTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.empreendimento",
                    ),
                ),
            ],
            options={
                "db_table": "CARDAPIO",
            },
        ),
        migrations.CreateModel(
            name="EmprendFuncionario",
            fields=[
                (
                    "cod_empreend_funcionario",
                    models.IntegerField(
                        db_column="COD_EMPREEND_FUNCIONARIO",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "tip_funcionario",
                    models.CharField(
                        blank=True, db_column="TIP_FUNCIONARIO", max_length=1, null=True
                    ),
                ),
                (
                    "img_empreend_funcionario",
                    models.TextField(
                        blank=True, db_column="IMG_EMPREEND_FUNCIONARIO", null=True
                    ),
                ),
                (
                    "cod_empreedimento",
                    models.ForeignKey(
                        db_column="COD_EMPREEDIMENTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.empreendimento",
                    ),
                ),
                (
                    "cod_funcionario",
                    models.ForeignKey(
                        db_column="COD_FUNCIONARIO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.funcionario",
                    ),
                ),
            ],
            options={
                "db_table": "EMPREND_FUNCIONARIO",
            },
        ),
        migrations.CreateModel(
            name="Localidade",
            fields=[
                (
                    "cod_localidade",
                    models.IntegerField(
                        db_column="COD_LOCALIDADE", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_localidade",
                    models.CharField(
                        blank=True, db_column="DCR_LOCALIDADE", max_length=45, null=True
                    ),
                ),
                (
                    "cod_bairro",
                    models.ForeignKey(
                        db_column="COD_BAIRRO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.bairro",
                    ),
                ),
                (
                    "localidade_cod_localidade",
                    models.ForeignKey(
                        db_column="LOCALIDADE_COD_LOCALIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.localidade",
                    ),
                ),
            ],
            options={
                "db_table": "LOCALIDADE",
            },
        ),
        migrations.AddField(
            model_name="empreendimento",
            name="cod_localidade",
            field=models.ForeignKey(
                db_column="COD_LOCALIDADE",
                on_delete=django.db.models.deletion.CASCADE,
                to="api_cliente.localidade",
            ),
        ),
        migrations.CreateModel(
            name="Disponibilidade",
            fields=[
                (
                    "cod_disponibilidade",
                    models.IntegerField(
                        db_column="COD_DISPONIBILIDADE",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "num_dia_semana",
                    models.IntegerField(
                        blank=True, db_column="NUM_DIA_SEMANA", null=True
                    ),
                ),
                (
                    "hora_fim",
                    models.DateTimeField(blank=True, db_column="HORA_FIM", null=True),
                ),
                (
                    "hora_inicio",
                    models.DateTimeField(
                        blank=True, db_column="HORA_INICIO", null=True
                    ),
                ),
                (
                    "cod_empreedimento",
                    models.ForeignKey(
                        db_column="COD_EMPREEDIMENTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.empreendimento",
                    ),
                ),
                (
                    "cod_localidade",
                    models.ForeignKey(
                        db_column="COD_LOCALIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.localidade",
                    ),
                ),
            ],
            options={
                "db_table": "DISPONIBILIDADE",
            },
        ),
        migrations.CreateModel(
            name="DisponExcecao",
            fields=[
                (
                    "cod_dispon_excecao",
                    models.IntegerField(
                        db_column="COD_DISPON_EXCECAO",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "data_excecao",
                    models.DateTimeField(
                        blank=True, db_column="DATA_EXCECAO", null=True
                    ),
                ),
                (
                    "tip_excecao",
                    models.CharField(
                        blank=True, db_column="TIP_EXCECAO", max_length=1, null=True
                    ),
                ),
                (
                    "hora_inicio",
                    models.DateTimeField(
                        blank=True, db_column="HORA_INICIO", null=True
                    ),
                ),
                (
                    "hora_fim",
                    models.DateTimeField(blank=True, db_column="HORA_FIM", null=True),
                ),
                (
                    "cod_empreedimento",
                    models.ForeignKey(
                        db_column="COD_EMPREEDIMENTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.empreendimento",
                    ),
                ),
                (
                    "cod_localidade",
                    models.ForeignKey(
                        db_column="COD_LOCALIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.localidade",
                    ),
                ),
            ],
            options={
                "db_table": "DISPON_EXCECAO",
            },
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "cod_cliente",
                    models.IntegerField(
                        db_column="COD_CLIENTE", primary_key=True, serialize=False
                    ),
                ),
                (
                    "nome_cliente",
                    models.CharField(
                        blank=True, db_column="NOME_CLIENTE", max_length=45, null=True
                    ),
                ),
                (
                    "dcr_endereco",
                    models.CharField(
                        blank=True, db_column="DCR_ENDERECO", max_length=45, null=True
                    ),
                ),
                (
                    "dcr_complemento",
                    models.CharField(
                        blank=True,
                        db_column="DCR_COMPLEMENTO",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "num_cep",
                    models.CharField(
                        blank=True, db_column="NUM_CEP", max_length=10, null=True
                    ),
                ),
                (
                    "cod_bairro",
                    models.ForeignKey(
                        db_column="COD_BAIRRO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.bairro",
                    ),
                ),
                (
                    "cod_cidade",
                    models.ForeignKey(
                        db_column="COD_CIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.cidade",
                    ),
                ),
                (
                    "cod_localidade",
                    models.ForeignKey(
                        db_column="COD_LOCALIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.localidade",
                    ),
                ),
            ],
            options={
                "db_table": "CLIENTE",
            },
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "cod_pedido",
                    models.IntegerField(
                        db_column="COD_PEDIDO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "tip_pedido",
                    models.CharField(
                        blank=True, db_column="TIP_PEDIDO", max_length=1, null=True
                    ),
                ),
                (
                    "data_pedido",
                    models.DateTimeField(
                        blank=True, db_column="DATA_PEDIDO", null=True
                    ),
                ),
                (
                    "vlr_pedido",
                    models.DecimalField(
                        blank=True,
                        db_column="VLR_PEDIDO",
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "dcr_dados_pagto",
                    models.CharField(
                        blank=True,
                        db_column="DCR_DADOS_PAGTO",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "cod_cliente",
                    models.ForeignKey(
                        db_column="COD_CLIENTE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.cliente",
                    ),
                ),
                (
                    "cod_forma_pagto",
                    models.ForeignKey(
                        blank=True,
                        db_column="COD_FORMA_PAGTO",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.formapagto",
                    ),
                ),
            ],
            options={
                "db_table": "PEDIDO",
            },
        ),
        migrations.CreateModel(
            name="Entrega",
            fields=[
                (
                    "cod_entrega",
                    models.IntegerField(
                        db_column="COD_ENTREGA", primary_key=True, serialize=False
                    ),
                ),
                (
                    "data_saida",
                    models.DateTimeField(blank=True, db_column="DATA_SAIDA", null=True),
                ),
                (
                    "data_entrega",
                    models.DateTimeField(
                        blank=True, db_column="DATA_ENTREGA", null=True
                    ),
                ),
                (
                    "vlr_entrega",
                    models.DecimalField(
                        blank=True,
                        db_column="VLR_ENTREGA",
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "dcr_endereco",
                    models.CharField(
                        blank=True, db_column="DCR_ENDERECO", max_length=45, null=True
                    ),
                ),
                (
                    "dcr_complem",
                    models.CharField(
                        blank=True, db_column="DCR_COMPLEM", max_length=45, null=True
                    ),
                ),
                (
                    "num_cep",
                    models.CharField(
                        blank=True, db_column="NUM_CEP", max_length=10, null=True
                    ),
                ),
                (
                    "txt_referencia",
                    models.CharField(
                        blank=True, db_column="TXT_REFERENCIA", max_length=45, null=True
                    ),
                ),
                (
                    "flag_encomenda",
                    models.CharField(
                        blank=True, db_column="FLAG_ENCOMENDA", max_length=1, null=True
                    ),
                ),
                (
                    "flag_entregador",
                    models.CharField(
                        blank=True, db_column="FLAG_ENTREGADOR", max_length=1, null=True
                    ),
                ),
                (
                    "cod_bairro",
                    models.ForeignKey(
                        db_column="COD_BAIRRO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.bairro",
                    ),
                ),
                (
                    "cod_cidade",
                    models.ForeignKey(
                        db_column="COD_CIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.cidade",
                    ),
                ),
                (
                    "cod_funcionario",
                    models.ForeignKey(
                        db_column="COD_FUNCIONARIO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.funcionario",
                    ),
                ),
                (
                    "cod_localidade",
                    models.ForeignKey(
                        db_column="COD_LOCALIDADE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.localidade",
                    ),
                ),
                (
                    "cod_pedido",
                    models.ForeignKey(
                        db_column="COD_PEDIDO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.pedido",
                    ),
                ),
            ],
            options={
                "db_table": "ENTREGA",
            },
        ),
        migrations.CreateModel(
            name="AvaliacaoPedido",
            fields=[
                (
                    "cod_avaliacao_pedido",
                    models.IntegerField(
                        db_column="COD_AVALIACAO_PEDIDO",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "num_nota_avaliacao",
                    models.IntegerField(
                        blank=True, db_column="NUM_NOTA_AVALIACAO", null=True
                    ),
                ),
                (
                    "txt_avaliacao",
                    models.CharField(
                        blank=True, db_column="TXT_AVALIACAO", max_length=100, null=True
                    ),
                ),
                (
                    "cod_cliente",
                    models.ForeignKey(
                        db_column="COD_CLIENTE",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.cliente",
                    ),
                ),
                (
                    "cod_pedido",
                    models.ForeignKey(
                        db_column="COD_PEDIDO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.pedido",
                    ),
                ),
            ],
            options={
                "db_table": "AVALIACAO_PEDIDO",
            },
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "cod_produto",
                    models.IntegerField(
                        db_column="COD_PRODUTO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "dcr_produto",
                    models.CharField(
                        blank=True, db_column="DCR_PRODUTO", max_length=45, null=True
                    ),
                ),
                (
                    "img_produto",
                    models.TextField(blank=True, db_column="IMG_PRODUTO", null=True),
                ),
                (
                    "vlr_produto",
                    models.DecimalField(
                        blank=True,
                        db_column="VLR_PRODUTO",
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "flag_disponivel",
                    models.CharField(
                        blank=True, db_column="FLAG_DISPONIVEL", max_length=1, null=True
                    ),
                ),
                (
                    "cod_categoria",
                    models.ForeignKey(
                        db_column="COD_CATEGORIA",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.categoria",
                    ),
                ),
                (
                    "cod_empreedimento",
                    models.ForeignKey(
                        db_column="COD_EMPREEDIMENTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.empreendimento",
                    ),
                ),
            ],
            options={
                "db_table": "PRODUTO",
            },
        ),
        migrations.CreateModel(
            name="ItemPedido",
            fields=[
                (
                    "cod_item_pedido",
                    models.IntegerField(
                        db_column="COD_ITEM_PEDIDO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "vlr_produto",
                    models.DecimalField(
                        blank=True,
                        db_column="VLR_PRODUTO",
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "qtd_produto",
                    models.DecimalField(
                        blank=True,
                        db_column="QTD_PRODUTO",
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "vlr_total",
                    models.DecimalField(
                        blank=True,
                        db_column="VLR_TOTAL",
                        decimal_places=2,
                        max_digits=9,
                        null=True,
                    ),
                ),
                (
                    "cod_pedido",
                    models.ForeignKey(
                        db_column="COD_PEDIDO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.pedido",
                    ),
                ),
                (
                    "cod_produto",
                    models.ForeignKey(
                        db_column="COD_PRODUTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.produto",
                    ),
                ),
            ],
            options={
                "db_table": "ITEM_PEDIDO",
            },
        ),
        migrations.CreateModel(
            name="RastreamentoPedido",
            fields=[
                (
                    "cod_rastreamento_pedido",
                    models.IntegerField(
                        db_column="COD_RASTREAMENTO_PEDIDO",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "data_hora_evento",
                    models.DateTimeField(
                        blank=True, db_column="DATA_HORA_EVENTO", null=True
                    ),
                ),
                (
                    "cod_evento_pedido",
                    models.ForeignKey(
                        db_column="COD_EVENTO_PEDIDO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.evento",
                    ),
                ),
                (
                    "cod_pedido",
                    models.ForeignKey(
                        db_column="COD_PEDIDO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.pedido",
                    ),
                ),
            ],
            options={
                "db_table": "RASTREAMENTO_PEDIDO",
            },
        ),
        migrations.CreateModel(
            name="SecaoCardapio",
            fields=[
                (
                    "cod_secao_cardapio",
                    models.IntegerField(
                        db_column="COD_SECAO_CARDAPIO",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "dcr_secao_cardapio",
                    models.CharField(
                        blank=True,
                        db_column="DCR_SECAO_CARDAPIO",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "dcr_titulo_apres",
                    models.CharField(
                        blank=True,
                        db_column="DCR_TITULO_APRES",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "num_ordem",
                    models.IntegerField(blank=True, db_column="NUM_ORDEM", null=True),
                ),
                (
                    "cod_cardapio",
                    models.ForeignKey(
                        db_column="COD_CARDAPIO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.cardapio",
                    ),
                ),
            ],
            options={
                "db_table": "SECAO_CARDAPIO",
            },
        ),
        migrations.CreateModel(
            name="SecaoProduto",
            fields=[
                (
                    "cod_secao_produto",
                    models.CharField(
                        db_column="COD_SECAO_PRODUTO",
                        max_length=45,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "num_ordem",
                    models.CharField(
                        blank=True, db_column="NUM_ORDEM", max_length=45, null=True
                    ),
                ),
                (
                    "produto_cod_produto",
                    models.ForeignKey(
                        db_column="PRODUTO_COD_PRODUTO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.produto",
                    ),
                ),
                (
                    "secao_cardapio_cod_secao_cardapio",
                    models.ForeignKey(
                        db_column="SECAO_CARDAPIO_COD_SECAO_CARDAPIO",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api_cliente.secaocardapio",
                    ),
                ),
            ],
            options={
                "db_table": "SECAO_PRODUTO",
            },
        ),
    ]
