from rest_framework import serializers
from .models import *

def get_model_serializer(model_):
    class ModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_
            fields = '__all__'
    return ModelSerializer




class AvaliacaoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoPedido
        fields = '__all__'


class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairro
        fields = '__all__'


class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class DisponibilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidade
        fields = '__all__'


class DisponExcecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisponExcecao
        fields = '__all__'


class EmpreendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empreendimento
        fields = '__all__'


class EmprendFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmprendFuncionario
        fields = '__all__'


class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class FormaPagtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagto
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__'


class LocalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidade
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class RastreamentoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RastreamentoPedido
        fields = '__all__'


class SecaoCardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecaoCardapio
        fields = '__all__'


class SecaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecaoProduto
        fields = '__all__'