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

Deve ser analizado se existe a quantidade de itens no pedido suficiente nas lojas

Se não tiver a quantidade nescessaria em uma loja devera pegar de outra

Se não tiver a quantidade nescessaria somando todas as lojas o pedido é cancelado

Para fins de facilitar a confecção do algoritmo o frete será unico para cada loja, independente da quantidade de itens comprado na mesma.

# Seleção



Na seleção selecionaremos dois individuos/cromossomos atravez de uma roleta aonde quanto melhores a avaliação mais "chances" ele terá de ser escolhido.

Exemplo em uma população de tamanho 10 o individuo com a melhor avaliação tera 10 chances, o sengundo melhor terá 9 chances, ..., e o ultimo terá apenas 1 chance de ser escolhido.

Isso garante que exista uma boa variabilidade genética. 

Mas se por acaso apareça algum individuo com uma avaliação melhor do que todas as outras descobertas esse individuo terá seu cromossomo armazenado a parte como uma possivel resposta.

Nota: para a seleção será usado o vetor de cromossomos da população e o top1 quando o top1 não for o melhor cromossomo da população. Caso sejam o mesmo será usado apenas o vetor de população.

# Cruzamento

O cruzamento mais comum é o por ponto aletatorio. Aonde é escolhido uma posição aleatoria nos cromossomos dos pais de forma que os genes a esquerda (ou direita) da posição indicada é adicionado a um cromossomo filho junto da parte oposta do segundo cromossomo.

Mas existe um problema ao fazer o cruzamento por ponto aletatorio nesse problema. O problema é que existe uma quantidade maxima de cartas por loja e o pedido pode pedir mais cartas do que uma loja tem, de forma que ao pedir 30 cartas x a loja y pode ter apenas 10 cartas x, sendo assim existe uma chance de que o cruzamento falhe. Ou seja, tem que ser validado a quantidade de cartas por loja para que o cromossomo não tenha mais cartas no pedido do que a loja realmente tenha. 

Uma solução para isso seria fazer o cruzamento por carta, de forma que ao fazer o cruzamento seja criada uma lista com os nomes (ids) das cartas e seja escolhido uma posição aleatoria dessa lista, e seja adicionada a cromossomo filho as cartas escolhida a esquerda (ou o contrario) da lista de cartas do primeiro cromossomo e as cartas a direita da lista de cartas do segundo cromossomo.

# Mutação

A mutação é quando mudamos o valor de algum gene de um cromossomo aleatoriamente. No caso seria mudar a loja onde comprariamos uma carta.

Mas a mutação nem sempre acontece, dessa forma temos que faze-la acontecer de forma aleatoria. Sendo assim foi programado para a chance de mutação ser de 1%.

# Inserção 

A inserção vai servir para 

# Programando em Python

O Python possui uma tipagem dinamica, o que faz com que objetos possam assumir varios tipos e serem mudados de acordo com a nescessidade do desenvolvedor, fazendo que seja extremamente simples criar scripts em Python graças a esse nivel de abstração. 

O que realmente reduz o desempenho do Python em relação a outras linguagens é justamente esse ponto.

A compilação de um codigo é deixar as intruções o mais claras possivel para a maquina, resolvendo o maximo de problemas possiveis de antemão. Deixando o codigo de maquina (bytecode) tão claro que possa rodar sem mais orientações do programador.

E como a abstração do PYthon é muito grande isso pesa muito ao ser compilado, por exemplo, o simples fato de não definir o tipo do objeto faz com que o compilador tenha mais trabalho para ele mesmo definir o comportamento da variavel. Desta forma, linguagens como o Java ou C que transferem o "trabalho bruto" para o programador se tornam muito mais eficientes

O Python usa a tecnica JIT (Just-in-Time), ela faz a compilação em tempo de execução assim podendo ser usado ao seu favor caracteristicas da maquina que está sendo usada e também pode traduzir blocos de código em vez de avaliar e executar linha por linha, incrementando assim a sua performance.


O principal problema para programar em python é a sua lentidão para rodar seus scripts.
