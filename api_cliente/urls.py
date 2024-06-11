from django.urls import path
from api_cliente.views import *

urlpatterns = [
    path('avaliacoes_pedido/', avaliacoes_pedido),
    path('avaliacao_pedido/<int:id>/', avaliacao_pedido),
    
    path('bairros/', bairros),
    path('bairro/<int:id>/', bairro),
    
    path('cardapios/', cardapios),
    path('cardapio/<int:id>/', cardapio),
    
    path('categorias/', categorias),
    path('categoria/<int:id>/', categoria),
    
    path('cidades/', cidades),
    path('cidade/<int:id>/', cidade),
    
    path('clientes/', clientes),
    path('cliente/<int:id>/', cliente),
    
    path('disponibilidades/', disponibilidades),
    path('disponibilidade/<int:id>/', disponibilidade),
    
    path('dispon_excecoes/', dispon_excecoes),
    path('dispon_excecao/<int:id>/', dispon_excecao),
    
    path('empreendimentos/', empreendimentos),
    path('empreendimento/<int:id>/', empreendimento),
    
    path('empreend_funcionarios/', emprend_funcionarios),
    path('empreend_funcionario/<int:id>/', emprend_funcionario),
    
    path('entregas/', entregas),
    path('entrega/<int:id>/', entrega),
    
    path('eventos/', eventos),
    path('evento/<int:id>/', evento),

    path('formas_pagto/', formas_pagto),
    path('forma_pagto/<int:id>/', forma_pagto),
    
    path('funcionarios/', funcionarios),
    path('funcionario/<int:id>/', funcionario),
    
    path('itens_pedido/', itens_pedido),
    path('item_pedido/<int:id>/', item_pedido),
    
    path('localidades/', localidades),
    path('localidade/<int:id>/', localidade),
    
    path('pedidos/', pedidos),
    path('pedido/<int:id>/', pedido),
   
    path('produtos/', produtos),
    path('produto/<int:id>/', produto),
    
    path('rastreamentos_pedido/', rastreamentos_pedido),
    path('rastreamento_pedido/<int:id>/', rastreamento_pedido),
    
    path('secoes_cardapio/', secoes_cardapio),
    path('secao_cardapio/<int:id>/', secao_cardapio),
    
    path('secoes_produto/', secoes_produto),
    path('secao_produto/<int:id>/', secao_produto),
]