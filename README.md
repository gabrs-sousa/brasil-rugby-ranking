# brasil-rugby-ranking
Biblioteca em Python para o cálculo do ranking brasileiro das equipes de rugby

Este código foi produzido para o site Portal do Rugby, um provedor de notícias sobre o Rugby brasileiro: http://www.portaldorugby.com.br/

Requer o pandas e o openpyxl.
O código é composto por três scripts: functions.py , run.py e utils.py
O arquivo run.py realiza os outros dois scripts. A variável "filename" deve ser substituída. O arquivo until.py realiza um processo de exploração dos dados à procura de padrões consistentes. Algumas erros são removidos no processo. O arquivo functions.py mapeia as partidadas consultando um glossário com os nomes das equipes ativas e suas variações. Posteriormente, implementa os cálculos de probabilidade e regras baseadas no sistema de troca de pontos.

Por exemplo: se a Poli perder para o SPAC por 30 a 3 no CEPEUSP

Pontuação da equipe A: 03
Pontuação da equipe B: 33
Jogo do Campeonato Brasileiro Série A: Falso
Classificação da equipe A antes do jogo: 90.14
Classificação da equipe B antes do jogo: 81.73
Classificação da equipe A após o jogo: 87.14
Classificação da equipe B após o jogo: 84.73
Alteração da equipe A: -3,00
Alteração da equipe B: +3,00

