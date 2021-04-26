# LigaMagic-TCC

Atualmente existe uma ampla variedade de opções quando se fazem compras, diversas lojas, produtos, opções de entrega, promoções e cupons. O que faz com que exista inúmeras possibilidades de combinações para uma única lista de compras, na qual dificilmente conseguiríamos descobrir em um tempo útil a combinação mais barata avaliando cada possibilidade.
Tal problema necessita de uma solução que faça a menor quantidade de comparações de combinações, mas que ache um resultado próximo do resultado perfeito. O que faz com que o Algoritmo Genético seja uma solução para este problema, já que o mesmo constitui uma técnica de busca e otimização.
Com base no nisso, essa pesquisa tem como objetivo analisar o desenvolvimento do Algoritmo Genético nas linguagens de programação Python e Java, com a finalidade de identificação do consumo de recursos humanos para o desenvolvimento do Algoritmo Genético.



# Problema

O problema a ser resolvido será APLICAÇÃO DE ALGORITMO GENÉTICO PARA A SOLUÇÃO DO PROBLEMA DE MÚLTIPLAS POSSIBILIDADES DE COMPRAS
O problema de fazer uma compra pode parecer algo simples, mas se analisado melhor verá que se trata de algo mais complexo.
Quando vamos comprar um produto na internet aparece diversas possibilidades de compra de um unico produto em diversas lojas.
Mas a solução é simples, basta comprar o produto em uma loja confivel na qual o preço final (preço do produto + frete + outra taxa se tiver) seja mais barato.
Entretanto quando vamos comprar uma lista de produtos o problema fica mais dificil de acordo com a quantidades de produto na lista por que as possibilidades vão aumentando de acordo com a oferta e com o tamanho da lista de compras. De forma que com uma lista de compras podemos ter milhares, as vezes milhões de possibilidades de compras, assim ficando dificil alcançar um valor ideal em tempo util.
Outros fatores podem complicar ainda mais, como ao querer comprar uma certa quantidade de um item as lojas podem não ter o quantidade nescessaria, assim sendo nescessario comprar em outras lojas.
Ou mesmo pode haver o problema de gerenciamento do pedido.
Mas o problema pode ter uma solução paleativa, uma familia de algoritmos conhecidos como algoritmos geneticos
Os algoritmos geneticos funcionam nesse problema em especifico basicamente gerando diversas possibilidades do pedidos de forma aleatoria, mas sempre suprindo suas nescessidades.
Os melhores resultados são selecionados e usados como base para gerar resultados parecidos, mas com pequenas "mutações" com o fim de tentarem melhorar.
O algoritmo genetico normalmente não acha o melhor resultado, mas não é essa a intenção.
O verdadeiro objetivo é achar a solução mais próxima possivel da combinação perfeita no menor tempo possivel.

# Observações

Para a elaboração do projetos temos uma base de dados fixa:

arquivos/ligamagicFrete.txt
arquivos/ligamagicPedido1.txt
arquivos/ligamagicPedido2.txt
arquivos/ligamagicPedido3.txt
arquivos/ligamagicPedido4.txt
arquivos/ligamagicPreco.txt
arquivos/ligamagicQtd.txt

Os arquivos estavam incompletos corrigi eles usando o programa `concertar.py`.
Como o objetivo e verificar a eficiencia do algoritmo em python en comparação ao mesmo algoritmo em java, não analisarei o processo de ler os arquivos, pois esse não é o objetivo.
Deve ser analizado se existe a quantidade de itens no pedido suficiente nas lojas.
Se não tiver a quantidade nescessaria em uma loja devera pegar de outra.
Se não tiver a quantidade nescessaria somando todas as lojas o pedido é cancelado.
Para fins de facilitar a confecção do algoritmo o frete será unico para cada loja, independente da quantidade de itens comprado na mesma.

