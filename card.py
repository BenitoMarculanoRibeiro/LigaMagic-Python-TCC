class Card:
    ativo = False

    def __init__(self, nome, vetPreco, vetQtd) -> None:
        self.nome = nome
        self.vetPreco = vetPreco
        self.vetQtd = vetQtd

    def clone(self):
        cardClone = Card(self.nome, self.vetPreco, self.vetQtd)
        return cardClone


carta1 = Card("CounterSpell", [2.2, 12, 3, 2.3, 9], [1, 2, 4, 12, 2])
print(carta1.nome)
print(carta1.vetPreco)
print(carta1.vetQtd)

carta11 = carta1
print(carta11.nome)
print(carta11.vetPreco)
print(carta11.vetQtd)