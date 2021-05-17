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

Na seleção sera ordernado toda a população, e será removido os piores cromossomos até sobraro tamanho original da população.

Por exemplo em uma população de tamanho original de 100 com um total de 360 cromossomos (que foram adicionados no decorrer do programa), será ordenado e depois removido os piores 260 cromossomos.

# Cruzamento

O cruzamento mais comum é o por ponto aletatorio. Aonde é escolhido uma posição aleatoria nos cromossomos dos pais de forma que os genes a esquerda (ou direita) 
sejam adicionados a dois novos cromossomos, mas invertendo o as listas depois do ponto. Conforme ilustrado na imagem. 

![alt text](https://github.com/BenitoMarculanoRibeiro/LigaMagic-Python-TCC/blob/main/imgs/img2.png?raw=true)

Mas existe um problema ao fazer o cruzamento por ponto aletatorio nesse problema. O problema é que existe uma quantidade maxima de cartas por loja e o pedido pode pedir mais cartas do que uma loja tem, de forma que ao pedir 30 cartas x a loja y pode ter apenas 10 cartas x, sendo assim existe uma chance de que o cruzamento falhe. Ou seja, tem que ser validado a quantidade de cartas por loja para que o cromossomo não tenha mais cartas no pedido do que a loja realmente tenha. 

Uma solução para isso seria fazer o cruzamento por carta, de forma que ao fazer o cruzamento seja criada uma lista com os nomes (ids) das cartas e seja escolhido uma posição aleatoria dessa lista, e seja adicionada aos cromossomos filhos as cartas escolhida a esquerda (ou o contrario) da lista de cartas do primeiro cromossomo e as cartas a direita da lista de cartas do segundo cromossomo.

Será feito cruzamento com todas os cromossomos da população (vale mencionar que o cruzamento será feito em sequencia da seleção, ou seja o tamanho da população já foi reestabelecido para o tamanho original), escolhendo pares de cromossomos aleatoriamente pela população.

# Mutação

A mutação é quando mudamos o valor de algum gene de um cromossomo aleatoriamente. No caso seria mudar a loja onde comprariamos uma carta.

Mas a mutação nem sempre acontece, dessa forma temos que faze-la acontecer de forma aleatoria. Sendo assim foi programado para a chance de mutação ser de 3%.

E a mutação ainda pode falhar, já que podem escolher uma loja que não tem mais cartas. Nesse caso, a mutação é interrempida.

# Inserção 

A inserção vai servir para adicionar novos cromossomos aleatorios a população. Seram adicionados o tamanho original da população na população existente. 

# Programando em Python

O Python possui uma tipagem dinamica, o que faz com que objetos possam assumir varios tipos e serem mudados de acordo com a nescessidade do desenvolvedor, fazendo que seja extremamente simples criar scripts em Python graças a esse nivel de abstração. 

O Python é interpretador e compilado, o compilador do Python, o CPython, compila o codigo fonte para um código de nível intermediário chamado códigos de bytes (arquivos .pyc). Esse codigo de bytes é interpretador por uma maquina virtual do Python, conhecida como PVM ( Python Virtual Machine). É usado a técnica JIT (Just-in-Time), ela faz a compilação em tempo de execução, assim podendo ser usado ao seu favor caracteristicas da maquina que está sendo usada e também pode traduzir blocos de código em vez de avaliar e executar linha por linha, incrementando assim a sua performance.

O que realmente reduz o desempenho do Python em relação a outras linguagens é justamente esse ponto.

A compilação de um codigo é deixar as intruções o mais claras possivel para a maquina, resolvendo o maximo de problemas possiveis de antemão. Deixando o codigo de maquina (bytecode) tão claro que possa rodar sem mais orientações do programador.

Enquanto em linguaguens de programação como C ou Java deixam a declaração de tipos das variaveis, e outros pontos chaves para o programador escrever. O Python por outro lado deixa essa essa carga para ser resolvida com o CPython, interpretador padrão do python, assim deixando o codigo mais facil de ser escrito e lido. Ou seja, o CPython terá que descobrir qual o tipo da variavel, onde inicia e termina os blocos de codigo, e varios outros pontos que teram de ser definidos antes de passar as instruções para a maquina. E como a interpretação é feita em tempo de execução, isso deixa muito trabalho para ser executado ao mesmo tempo, assim afetando o desenpenho.

E como a abstração do Python é muito grande isso pesa muito ao ser interpretado, por exemplo, o simples fato de não definir o tipo do objeto faz com que o compilador tenha mais trabalho para ele mesmo definir o comportamento da variavel. Desta forma, linguagens como o Java ou C que transferem o "trabalho bruto" para o programador se tornam muito mais eficientes

O principal problema para programar em python é a sua lentidão para rodar seus scripts.

Porem escrever programas em python é mais facil de escrever, ler, compreender. O fator de ter que identar o codigo, não precisar declarar variaveis, não precisar terminar linhas com ";", abrir e fechar trechos do codigo, e outros fatores deixa bem menos poluido o codigo.

# Programando em Java

O Java é compilado e interpretado, o compilador do Java, o Javac, compila o codigo fonte para um código de nível intermediário chamado códigos de bytes (arquivos .class). Esse codigo de bytes é interpretador por uma maquina virtual do Java, conhecida como JVM (Java Virtual Machine). É usado a técnica JIT (Just-in-Time) para fazer melhor aproveitamento do codigo de bytes.

O Java possui uma tipagem estatica, tendo que declarar os tipos das variaveis em qualquer situação que o Java julgue ambiguo, no caso as IDEs separam em dois niveis, erros e avisos. Os erros são situações em que a IDE identifica identifica incoerencias ou erros graves na logica, como declarar duas variaveis com o mesmo nome, ou passar um objeto String para Inteiro sem fazer o tratamento adequado. Os avisos são para quando as incoerencias ou ambiguidades são mais seguras, como instanciar um objeto e não usar.

Em relação ao Python o Java deixa mais trabalho para o programador, fazendo-o definir muitas coisas para o programa funcionar. Assim poluindo a tela com informações que o programador não prescisa. Mas por outro lado, ainda apresenta uma linguagem clara e logica, o que permite que escrevamos codigos eficientes. 

# Anotações 

Funcionamento do Python
Primeiro escrevemos o script (codigo fonte .py)
Depois executamos o script por um interpretador python, onde é compilado para o chamado "código de byte" (arquivo .pyc) e em seguida roteado para uma "maquina virtual Python" (PVM)

![alt text](https://github.com/BenitoMarculanoRibeiro/LigaMagic-Python-TCC/blob/main/imgs/img1.jpg?raw=true)

Vale ressaltar que os arquivos pré-compilados .pyc não são código binário de maquina, o código de byte é uma representação especifica do Python.
O motivo do código em Python ser tão lento é por causa do loop PVM, ele tem que interpretar o código em byte, e as instruções do código de byte requerem mais trabalho do que as instruções da CPU.
Livro: Learning Python, FOURTH EDITION, by Mark Lutz



CPython é o interpretador padrão do python
https://docs.python.org/pt-br/3/glossary.html#term-cpython


https://qastack.com.br/software/24558/is-python-interpreted-or-compiled

Como evitar arquivos .pyc? Basta usar a opção -B ao iniciar o programa usando o interpretador Python.
Exemplo: python -B main.py
https://qastack.com.br/programming/154443/how-to-avoid-pyc-files