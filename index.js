var jogador_1 = [3, 4, 3]
var jogador_2 = [8, 1, 1]
var jogador_3 = [2, 4, 4]
var jogador_4 = [3, 3, 4]
var jogador_5 = [2, 2, 6]
var jogadores = [jogador_1, jogador_2, jogador_3, jogador_4, jogador_5]
var resultados = []

jogadores.forEach(jogador => {
    var temp = []
    jogador.forEach(jogada => {
        for (let index = 0; index < jogada; index++) {
            temp.push(jogador.indexOf(jogada))
        }
    });
    resultados.push(temp)
});
console.log(resultados)