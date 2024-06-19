from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def avaliacoes_pedido(request):
    if request.method == 'GET':
        avaliacao = AvaliacaoPedido.objects.all()
        serializer = AvaliacaoPedidoSerializer(avaliacao, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AvaliacaoPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def avaliacao_pedido(request, id):
    if request.method == 'DELETE':
        avaliacao = AvaliacaoPedido.objects.get(id=id)
        avaliacao.delete()
        return Response({'message': 'Avaliação deletada com sucesso!'})
    elif request.method == 'PUT':
        avaliacao = AvaliacaoPedido.objects.get(id=id)
        serializer = AvaliacaoPedidoSerializer(avaliacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        avaliacao = AvaliacaoPedido.objects.get(id=id)
        serializer = AvaliacaoPedidoSerializer(avaliacao)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def bairros(request):
    if request.method == 'GET':
        bairro = Bairro.objects.all()
        serializer = BairroSerializer(bairro, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BairroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def bairro(request, id):
    if request.method == 'DELETE':
        bairro = Bairro.objects.get(id=id)
        bairro.delete()
        return Response({'message': 'Bairro deletado com sucesso!'})
    elif request.method == 'PUT':
        bairro = Bairro.objects.get(id=id)
        serializer = BairroSerializer(bairro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        bairro = Bairro.objects.get(id=id)
        serializer = BairroSerializer(bairro)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def cardapios(request):
    if request.method == 'GET':
        cardapio = Cardapio.objects.all()
        serializer = CardapioSerializer(cardapio, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CardapioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def cardapio(request, id):
    if request.method == 'DELETE':
        cardapio = Cardapio.objects.get(id=id)
        cardapio.delete()
        return Response({'message': 'Cardápio deletado com sucesso!'})
    elif request.method == 'PUT':
        cardapio = Cardapio.objects.get(id=id)
        serializer = CardapioSerializer(cardapio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        cardapio = Cardapio.objects.get(id=id)
        serializer = CardapioSerializer(cardapio)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def categorias(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def categoria(request, id):
    if request.method == 'DELETE':
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        return Response({'message': 'Categoria deletada com sucesso!'})
    elif request.method == 'PUT':
        categoria = Categoria.objects.get(id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        categoria = Categoria.objects.get(id=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def cidades(request):
    if request.method == 'GET':
        cidade = Cidade.objects.all()
        serializer = CidadeSerializer(cidade, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def cidade(request, id):
    if request.method == 'DELETE':
        cidade = Cidade.objects.get(id=id)
        cidade.delete()
        return Response({'message': 'Cidade deletada com sucesso!'})
    elif request.method == 'PUT':
        cidade = Cidade.objects.get(id=id)
        serializer = CidadeSerializer(cidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        cidade = Cidade.objects.get(id=id)
        serializer = CidadeSerializer(cidade)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def clientes(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def cliente(request, id):
    if request.method == 'DELETE':
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return Response({'message': 'Cliente deletado com sucesso!'})
    elif request.method == 'PUT':
        cliente = Cliente.objects.get(id=id)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        cliente = Cliente.objects.get(id=id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def disponibilidades(request):
    if request.method == 'GET':
        disponibilidade = Disponibilidade.objects.all()
        serializer = DisponibilidadeSerializer(disponibilidade, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DisponibilidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def disponibilidade(request, id):
    if request.method == 'DELETE':
        disponibilidade = Disponibilidade.objects.get(id=id)
        disponibilidade.delete()
        return Response({'message': 'Disponibilidade deletada com sucesso!'})
    elif request.method == 'PUT':
        disponibilidade = Disponibilidade.objects.get(id=id)
        serializer = DisponibilidadeSerializer(disponibilidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'POST'])
def dispon_excecoes(request):
    if request.method == 'GET':
        dispon_excecao = DisponExcecao.objects.all()
        serializer = DisponExcecaoSerializer(dispon_excecao, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DisponExcecaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def dispon_excecao(request, id):
    if request.method == 'DELETE':
        dispon_excecao = DisponExcecao.objects.get(id=id)
        dispon_excecao.delete()
        return Response({'message': 'Disponibilidade Exceção deletada com sucesso!'})
    elif request.method == 'PUT':
        dispon_excecao = DisponExcecao.objects.get(id=id)
        serializer = DisponExcecaoSerializer(dispon_excecao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        dispon_excecao = DisponExcecao.objects.get(id=id)
        serializer = DisponExcecaoSerializer(dispon_excecao)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def empreendimentos(request):
    if request.method == 'GET':
        nome_busca = request.GET.get('query_name', None)
        if nome_busca:
            empreendimento = Empreendimento.objects.filter(dcr_nome_fantasia__icontains=nome_busca)
            serializer = EmpreendimentoSerializer(empreendimento, many=True)
        else:
            empreendimento = Empreendimento.objects.all()
            serializer = EmpreendimentoSerializer(empreendimento, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmpreendimentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def empreendimento(request, id):
    if request.method == 'DELETE':
        empreendimento = Empreendimento.objects.get(cod_empreedimento=id)
        empreendimento.delete()
        return Response({'message': 'Empreendimento deletado com sucesso!'})
    elif request.method == 'PUT':
        empreendimento = Empreendimento.objects.get(cod_empreedimento=id)
        serializer = EmpreendimentoSerializer(empreendimento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        empreendimento = Empreendimento.objects.get(cod_empreedimento=id)
        serializer = EmpreendimentoSerializer(empreendimento)
        return Response(serializer.data)

@api_view(['GET'])
def emprd_disponibilidade(request, id_empreendimento):
    emprd_disponibilidade = Disponibilidade.objects.filter(cod_empreedimento=id_empreendimento)
    serializer = DisponibilidadeSerializer(emprd_disponibilidade, many=True)
    return Response(serializer.data)


def categorias_json(request, id_empreendimento):
    categorias = Categoria.objects.filter(cod_empreedimento=id_empreendimento)
    categorias_data = []

    for categoria in categorias:
        produtos = categoria.produto_set.all()
        produtos_data = []
        for produto in produtos:
            produtos_data.append(produto)
        categorias_data.append({
            'cod_categoria': categoria.cod_categoria,
            'dcr_categoria': categoria.dcr_categoria,
            'img_categoria': categoria.img_categoria,
            'produtos': ProdutoSerializer(produtos_data, many=True).data
        })

    return JsonResponse(categorias_data, safe=False)



@api_view(['GET', 'POST'])
def emprend_funcionarios(request):
    if request.method == 'GET':
        emprend_funcionario = EmprendFuncionario.objects.all()
        serializer = EmprendFuncionarioSerializer(emprend_funcionario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmprendFuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def emprend_funcionario(request, id):
    if request.method == 'DELETE':
        emprend_funcionario = EmprendFuncionario.objects.get(id=id)
        emprend_funcionario.delete()
        return Response({'message': 'Funcionário do empreendimento deletado com sucesso!'})
    elif request.method == 'PUT':
        emprend_funcionario = EmprendFuncionario.objects.get(id=id)
        serializer = EmprendFuncionarioSerializer(emprend_funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        emprend_funcionario = EmprendFuncionario.objects.get(id=id)
        serializer = EmprendFuncionarioSerializer(emprend_funcionario)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def entregas(request):
    if request.method == 'GET':
        entrega = Entrega.objects.all()
        serializer = EntregaSerializer(entrega, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EntregaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def entrega(request, id):
    if request.method == 'DELETE':
        entrega = Entrega.objects.get(id=id)
        entrega.delete()
        return Response({'message': 'Entrega deletada com sucesso!'})
    elif request.method == 'PUT':
        entrega = Entrega.objects.get(id=id)
        serializer = EntregaSerializer(entrega, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        entrega = Entrega.objects.get(id=id)
        serializer = EntregaSerializer(entrega)
        return Response(serializer.data)
    
    
@api_view(['GET', 'POST'])
def eventos(request):
    if request.method == 'GET':
        evento = Evento.objects.all()
        serializer = EventoSerializer(evento, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def evento(request, id):
    if request.method == 'DELETE':
        evento = Evento.objects.get(id=id)
        evento.delete()
        return Response({'message': 'Evento deletado com sucesso!'})
    elif request.method == 'PUT':
        evento = Evento.objects.get(id=id)
        serializer = EventoSerializer(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        evento = Evento.objects.get(id=id)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def formas_pagto(request):
    if request.method == 'GET':
        forma_pagto = FormaPagto.objects.all()
        serializer = FormaPagtoSerializer(forma_pagto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FormaPagtoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def forma_pagto(request, id):
    if request.method == 'DELETE':
        forma_pagto = FormaPagto.objects.get(id=id)
        forma_pagto.delete()
        return Response({'message': 'Forma de pagamento deletada com sucesso!'})
    elif request.method == 'PUT':
        forma_pagto = FormaPagto.objects.get(id=id)
        serializer = FormaPagtoSerializer(forma_pagto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        forma_pagto = FormaPagto.objects.get(id=id)
        serializer = FormaPagtoSerializer(forma_pagto)
        return Response(serializer.data)


def funcionarios(request):
    if request.method == 'GET':
        funcionario = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def funcionario(request, id):
    if request.method == 'DELETE':
        funcionario = Funcionario.objects.get(id=id)
        funcionario.delete()
        return Response({'message': 'Funcionário deletado com sucesso!'})
    elif request.method == 'PUT':
        funcionario = Funcionario.objects.get(id=id)
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        funcionario = Funcionario.objects.get(id=id)
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def itens_pedido(request):
    if request.method == 'GET':
        item_pedido = ItemPedido.objects.all()
        serializer = ItemPedidoSerializer(item_pedido, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ItemPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def item_pedido(request, id):
    if request.method == 'DELETE':
        item_pedido = ItemPedido.objects.get(id=id)
        item_pedido.delete()
        return Response({'message': 'Item do pedido deletado com sucesso!'})
    elif request.method == 'PUT':
        item_pedido = ItemPedido.objects.get(id=id)
        serializer = ItemPedidoSerializer(item_pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        item_pedido = ItemPedido.objects.get(id=id)
        serializer = ItemPedidoSerializer(item_pedido)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def localidades(request):
    if request.method == 'GET':
        localidade = Localidade.objects.all()
        serializer = LocalidadeSerializer(localidade, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LocalidadeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def localidade(request, id):
    if request.method == 'DELETE':
        localidade = Localidade.objects.get(id=id)
        localidade.delete()
        return Response({'message': 'Localidade deletada com sucesso!'})
    elif request.method == 'PUT':
        localidade = Localidade.objects.get(id=id)
        serializer = LocalidadeSerializer(localidade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        localidade = Localidade.objects.get(id=id)
        serializer = LocalidadeSerializer(localidade)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def pedidos(request):
    if request.method == 'GET':
        pedido = Pedido.objects.all()
        serializer = PedidoSerializer(pedido, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def pedido(request, id):
    if request.method == 'DELETE':
        pedido = Pedido.objects.get(id=id)
        pedido.delete()
        return Response({'message': 'Pedido deletado com sucesso!'})
    elif request.method == 'PUT':
        pedido = Pedido.objects.get(id=id)
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        pedido = Pedido.objects.get(id=id)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def produtos(request):
    if request.method == 'GET':
        nome_busca = request.GET.get('query_name', None)
        if nome_busca:
            produtos = Produto.objects.filter(dcr_produto__icontains=nome_busca)
            serializer = ProdutoSerializer(produtos, many=True)
        else:
            produtos = Produto.objects.all()
            serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def produto(request, id):
    if request.method == 'DELETE':
        produto = Produto.objects.get(id=id)
        produto.delete()
        return Response({'message': 'Produto deletado com sucesso!'})
    elif request.method == 'PUT':
        produto = Produto.objects.get(id=id)
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        produto = Produto.objects.get(id=id)
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def rastreamentos_pedido(request):
    if request.method == 'GET':
        rastreamento_pedido = RastreamentoPedido.objects.all()
        serializer = RastreamentoPedidoSerializer(rastreamento_pedido, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RastreamentoPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def rastreamento_pedido(request, id):
    if request.method == 'DELETE':
        rastreamento_pedido = RastreamentoPedido.objects.get(id=id)
        rastreamento_pedido.delete()
        return Response({'message': 'Rastreamento do pedido deletado com sucesso!'})
    elif request.method == 'PUT':
        rastreamento_pedido = RastreamentoPedido.objects.get(id=id)
        serializer = RastreamentoPedidoSerializer(rastreamento_pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        rastreamento_pedido = RastreamentoPedido.objects.get(id=id)
        serializer = RastreamentoPedidoSerializer(rastreamento_pedido)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def secoes_cardapio(request):
    if request.method == 'GET':
        secao_cardapio = SecaoCardapio.objects.all()
        serializer = SecaoCardapioSerializer(secao_cardapio, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SecaoCardapioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def secao_cardapio(request, id):
    if request.method == 'DELETE':
        secao_cardapio = SecaoCardapio.objects.get(id=id)
        secao_cardapio.delete()
        return Response({'message': 'Seção do cardápio deletada com sucesso!'})
    elif request.method == 'PUT':
        secao_cardapio = SecaoCardapio.objects.get(id=id)
        serializer = SecaoCardapioSerializer(secao_cardapio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        secao_cardapio = SecaoCardapio.objects.get(id=id)
        serializer = SecaoCardapioSerializer(secao_cardapio)
        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
def secoes_produto(request):
    if request.method == 'GET':
        secao_produto = SecaoProduto.objects.all()
        serializer = SecaoProdutoSerializer(secao_produto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SecaoProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def secao_produto(request, id):
    if request.method == 'DELETE':
        secao_produto = SecaoProduto.objects.get(id=id)
        secao_produto.delete()
        return Response({'message': 'Seção do produto deletada com sucesso!'})
    elif request.method == 'PUT':
        secao_produto = SecaoProduto.objects.get(id=id)
        serializer = SecaoProdutoSerializer(secao_produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'GET':
        secao_produto = SecaoProduto.objects.get(id=id)
        serializer = SecaoProdutoSerializer(secao_produto)
        return Response(serializer.data)