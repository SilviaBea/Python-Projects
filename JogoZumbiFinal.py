from email.errors import InvalidBase64PaddingDefect
from http.client import PRECONDITION_FAILED
import random
from re import X 
#Silvia Beatriz Pereira de Sousa // Análise e desenvolvimento de sistemas EAD 2022 \\ ATP II

#Listas e tuplas
tubo = ['dado_vermelho','dado_vermelho','dado_vermelho','dado_verde','dado_verde','dado_verde','dado_verde',
        'dado_verde','dado_verde','dado_amarelo','dado_amarelo','dado_amarelo','dado_amarelo']
vermelho = ('T','P','T','C','P','T')
verde = ('C','P','C','T','P','C')
amarelo = ('T','P','C','T','P','C')
dados_retirados = []
indice_cerebros = []
indice_passos = []

#Variaveis globais
dados_suficientes_nova_rolagem = 3
qnt_cerebro = 0
qnt_tiro = 0 
qnt_passos = 0 
aleatorio = 0
vencedor_empate = 0
rodadas = 0

#função para pegar os dados do tubo
def pegar_dados_tubo(dados_suficientes_nova_rolagem, qnt_passos):
    if indice_passos.__len__() != 0:
        dados_suficientes_nova_rolagem = trocar_posições(qnt_passos)
    if tubo.__len__()<dados_suficientes_nova_rolagem:
        devolver_dados_tubo()
    for i in range(dados_suficientes_nova_rolagem):
        contador = tubo.__len__() -1
        pegar_dado = random.randint(0,contador)
        dados_retirados.append(tubo.pop(pegar_dado))
    return 0

#função para devolver os dados de cerebro para o tubo quando necessário
def devolver_dados_tubo():
    for i in range(indice_cerebros.__len__()):
        tubo.append(dados_retirados[indice_cerebros[i]])
    for i in range(indice_cerebros.__len__()):
        if(dados_retirados[i] == 'C'):
            dados_retirados.pop

#função para rolar os dados
def rolar_dado():
    i = dados_retirados.__len__() -1
    while i > dados_retirados.__len__() - 4:
        aleatorio = random.randint(0,5)
        if dados_retirados[i] == 'dado_vermelho':
            verificar_face(vermelho[aleatorio],i)
        elif dados_retirados[i] == 'dado_verde':
            verificar_face(verde[aleatorio],i)
        else:
            verificar_face(amarelo[aleatorio],i)
        i = i -1

#função para verificar a face corresponde do dado     
def verificar_face(tipo, i):
    if tipo == 'C':
        print("Você devorou o cérebro da sua vítima")
        global qnt_cerebro 
        qnt_cerebro= qnt_cerebro + 1
        indice_cerebros.append(i)
    elif tipo == 'T':
        print("Você levou um tiro!")
        global qnt_tiro
        qnt_tiro = qnt_tiro + 1
    else:
        print("Sua vítima escapou!")
        global qnt_passos
        qnt_passos = qnt_passos + 1
        indice_passos.append(i)

#função para trocar dados com a face passo para o fim da lista para nova rolagem
def trocar_posições(qnt_passos):
    if qnt_passos<3:
        i = dados_retirados.__len__()-1
        while i >=0:
            for x in range(indice_passos.__len__()):
                if i == indice_passos[x]:
                    dados_retirados.append(dados_retirados.pop(i))
            i = i-1
    indice_passos.clear
    return 3 - qnt_passos

#função para marcar a pontuação
def marcar_pontuacao(qnt_cerebro,jogador):
    pontuacao[jogador] = pontuacao[jogador]+qnt_cerebro
    indice_cerebros.clear
    indice_passos.clear

''' Mensagem amistosa de boas vindas'''
print("BEM VINDO A ZOMBIE DICE!!!", end= '\n\n\n')
print("PARA JOGAR COLOQUE A QUANTIDADE DE JOGADORES!!", end= '\n\n\n') 

#bloco de barramento de jogadores
jogadores = int(input("Jogadores: ")) 
while jogadores <= 1: 
    print("Para jogar Zombie Dice é necessário 2 ou mais jogadores!") 
    jogadores = int(input("Digite a quantidade de jogadores: ")) 
    continue 
pontuacao=[0 for _ in range(jogadores)]
 

#início do jogo
while True:
    if pontuacao.__len__() > 0:
        print("PONTUAÇÃO ATUAL",pontuacao) #Score atual conforme rodadas
    rodadas = rodadas+1
    tubo.extend(dados_retirados)
    dados_retirados.clear
    qnt_vencedores = 0
    indice_jogadores_empatados = []
    for z in range (jogadores):
        if pontuacao[z] > 12: #se quando rodar a pontuação tiver algum score maior que 12
            qnt_vencedores = qnt_vencedores+1 #adiciona um vencedor na variavel de vencedores
            indice_jogadores_empatados.append(pontuacao[z]) #adiciona os que tiverem mais que 2 na lista
            
    
    if qnt_vencedores == 1:  #se a variavel for = 1 
        print("O jogador ", z," devorou todos os céééérebros ganhando Zombie Dice!") #alguem ganhou o jogo
        break
    elif qnt_vencedores > 1: #se for maior que um, temos um possível empate ou jogadores que fizeram mais que 13
        aux = 0
        qnt_vencedores = 0
        jogadores_empatados = []
        for g in range(indice_jogadores_empatados.__len__()): #correr a lista de jogadores que fixeram 13
            if pontuacao[indice_jogadores_empatados[g]] > aux:
                aux = pontuacao[indice_jogadores_empatados[g]]
        for k in range (pontuacao.__len__()):
            if aux == pontuacao[k]:
                qnt_vencedores = qnt_vencedores +1
                jogadores_empatados.append(k) #adiciona o jogador com a maior pontuação
        if qnt_vencedores == 1:
            print("O jogador ",jogadores_empatados[0]," ganhou o jogo devorando ", pontuacao[jogadores_empatados[0]]," cééééérebros!") #O jogador com a maior pontuação é o vencedor
            break
        else: #se houver empate, nova rodada para desempate
            aux = 0
            qnt_vencedores = 0
            vencedor_empate = 0
            for k in range(jogadores_empatados.__len__()):
                tubo.extend(dados_retirados)
                dados_retirados.clear
                qnt_cerebro = 0
                qnt_passos = 0
                pegar_dados_tubo()
                rolar_dado()
                pontuacao[jogadores_empatados[k]] = qnt_cerebro
            for g in range(indice_jogadores_empatados.__len__()):
                if pontuacao[indice_jogadores_empatados[g]] > aux:
                    aux = pontuacao[indice_jogadores_empatados[g]]
                    vencedor_empate = indice_jogadores_empatados[g] #vencedor empate recebe o valor do maior score da lista
            if qnt_vencedores == 1:
                print("O jogador que venceu o desempate foi o ",vencedor_empate," ganhou o jogo devorando ", pontuacao[vencedor_empate], " cééééééérebros!")
                break
    for i in range(jogadores):
        qnt_tiro = 0
        qnt_cerebro = 0
        qnt_passos = 0
        jogar = 's'
       
       #início do jogo
        while pontuacao[i] < 13: #enquanto ninguem fizem 13 pontos, o jogo segue
            if qnt_tiro >= 3: 
                print("Seu turno acabou, você levou ",qnt_tiro," tiros!\n\n") #se houver 3 tiros, acabou o turno
                qnt_cerebro = 0
                marcar_pontuacao(qnt_cerebro,i)
                break
            print("\nRodada",rodadas,"\nJogador",i+1, "\n")
            jogar = "n"
            jogar = input("Deseja rolar os dados ou parar?\n\n")    #deseja rolar ou dados ou parar      
            if jogar == 's':
                qnt_passos = pegar_dados_tubo(dados_suficientes_nova_rolagem, qnt_passos)
                rolar_dado()
                continue
            else:
                print("Você (Jogador", i+1, ") escolheu finalizar sua rodada. Você devorou ",qnt_cerebro,"cééééééérebros e levou",qnt_tiro,"tiros!\n\n") #score do fim da rodada
                marcar_pontuacao(qnt_cerebro,i)
                break
            