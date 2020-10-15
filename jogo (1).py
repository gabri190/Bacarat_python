#EP-Design de Software
#Individual-Gabriel de Araujo Alves
#Data:15/10/2020
#importar a biblioteca que permite o sorteio das cartas
import random
#montagem do baralho
def montarBaralho():
    copas = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    espadas = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    ouros = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    paus = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    baralho = [copas,espadas,ouros,paus]
    return baralho
#definir a quantidade de baralhos:1,6 ou 8 baralhos 
def quantBaralhos(quantidade,baralho):
    return baralho*quantidade
#definir a pontuação de cada carta        
def pontuacao(carta):
    if(carta == "A"):
        return 1
    elif(carta == "valete" or carta == "dama" or carta == "rei" or carta == 10):
        return 0
    else:
        return carta
#definir o sorteio do naipe
def sortearNaipe(baralho):
    j = len(baralho)-1
    return random.randint(0,j)
#depois de sorteada a carta precisa ser retirada para evitar repetição
def retirarCarta(baralho,naipe,carta):
    if(carta in baralho[naipe]):
       baralho[naipe].remove(carta)
    return baralho
#sorteio das 2 primeiras cartas do banco e do jogador            
def sortearCarta(baralho,naipe):
    j = len(baralho[naipe])-1
    sorteio = random.randint(0,j)
    return baralho[naipe][sorteio]
#se houver necessidade sorteio da terceira carta        
def sortearOutraCarta(baralho):
    naipe = sortearNaipe(baralho)
    carta = sortearCarta(baralho,naipe)
    return carta
#verificar quem foi o ganhador para o caso em que o jogador ou o banco possuem a soma das cartas em 8 ou 9
def verificarGanhadorCaso1(vencedor, pontosJ, pontosB,fichas):
    v1 = [8,9]
    ok = False
    if(pontosJ in v1) or (pontosB in v1):
        if(vencedor == "jogador") and (pontosJ > pontosB):
            ok = True
        elif(vencedor == "banco") and (pontosJ < pontosB):
            ok = True
        elif(vencedor == "empate")and (pontosJ == pontosB):
            ok = True
        return ok
#verificar quem foi o ganhador para o caso em que o jogador ou o banco possuem a soma das cartas em 6 ou 7
def verificaGanhadorCaso2(vencedor,pontosJ,pontosB, fichas, baralho,naipe):
    v2 = [6,7]
    if((pontosJ in v2) or (pontosB in v2)) and ((pontosJ<=10) and (pontosB<=10)):
        if(pontosJ <= 5):#se a soma das cartas do jogador for menor ou igual a 5 é sorteada outra carta
            carta3 = sortearOutraCarta(baralho)
            baralho = retirarCarta(baralho,naipe,carta3)
            print("Entrou")
            pontosJ+= pontuacao(carta3)
        if(pontosB <= 5):#se a soma das cartas do banco for menor ou igual a 5 é sorteada outra carta
            carta3 = sortearOutraCarta(baralho)
            baralho = retirarCarta(baralho,naipe,carta3)
            print("Entrou")
            pontosB+= pontuacao(carta3)
#retorna verdadeiro as condições de vitoria do jogador e retorna falso a derrota do jogador
        if(vencedor == "jogador") and (pontosJ > pontosB):
            return True
        elif(vencedor == "banco") and (pontosJ < pontosB):
            return True
        elif(vencedor == "empate")and (pontosJ == pontosB):
            return True
        else:
            return False
#pagamento do vencedor de acordo com a aposta e a comissão a ser paga para a mesa        
def ganho(vencedor,aposta,fichas, baralho):
    total = 0
    if(vencedor == "jogador"):
        if(baralho == 1):
            total = fichas + (apostas-0.0129 *apostas)
        elif(baralho == 6) or (baralho == 8):
            total = fichas + (aposta-0.0124 *aposta)
    elif(vencedor == "banco"):

        if(baralho == 1):
            total = fichas + (0.95*(aposta-0.0101 *aposta))
        elif(baralho == 6) or (baralho == 8):
            total = fichas + (0.95*(aposta-0.0106 *aposta))
        total = int(total)            
    elif(vencedor == "empate"):
        if(baralho == 1):
            total = fichas + (8*(aposta-0.1575*aposta))
        elif(baralho == 6):
            total = fichas + (8*(aposta-0.1444*aposta))
        else:
            total = fichas + (8*(aposta-0.1436*aposta))
    return total         
#finalizando o jogo        
def fimDeJogo():
    status = True
    print("FIM de jogo")
    cont = input("Deseja continuar? ")
    if(cont == "não"):
        status = False
    return status
#se a pontuação for maior ou igual a 10 é contada apenas a unidade ,ou seja,retira-se 10 do valor e o resto do jogo continua igual
def cortarPontuacao(valor):
    return valor-10
    


    
    
