#importar a biblioteca de sorteio das cartas
import random
#montagem do baralho
def montarBaralho():
    copas = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    espadas = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    ouros = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    paus = ["A",2,3,4,5,6,7,8,9,10,"valete","dama","rei"]
    baralho = [copas,espadas,ouros,paus]
    return baralho
#defini a quantidade de baralhos:1,6 ou 8
def quantBaralhos(quantidade,baralho):
    return baralho*quantidade

#defini a pontuacao(valor) de cada carta        
def pontuacao(carta):
    if(carta == "A"):
        return 1
    elif(carta == "valete" or carta == "dama" or carta == "rei" or carta == 10):
        return 0
    else:
        return carta

#sorteia primeiramente o naipe da carta
def sortearNaipe(baralho):
    j = len(baralho)-1
    return random.randint(0,j)
#a retirada da carta e necessaria para não haver repetição no sorteio
def retirarCarta(baralho,naipe,carta):
    if(carta in baralho[naipe]):
       baralho[naipe].remove(carta)
    return baralho
            
            
    
#depois a carta e sorteada(2 cartas para o banco e 2 cartas para o jogador)
def sortearCarta(baralho,naipe):
    j = len(baralho[naipe])-1
    sorteio = random.randint(0,j)
    return baralho[naipe][sorteio]
        
#sorteio de uma 3 carta se preciso        
def sortearOutraCarta(baralho):
    naipe = sortearNaipe(baralho)
    carta = sortearCarta(baralho,naipe)
    return carta
#caso em que a soma das cartas do jogador ou banco é igual a 8 ou 9:nesse caso o jogo termina
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
#caso em que a soma das cartas do jogador ou banco é igual a 6 ou 7 (definindo o vencedor)
def verificaGanhadorCaso2(vencedor,pontosJ,pontosB):
    v2 = [6,7]
    ok = False
    if((pontosJ in v2) or (pontosB in v2)) and ((pontosJ > 5) and (pontosB > 5)):
        if(vencedor == "jogador") and (pontosJ > pontosB):
            ok = True
        elif(vencedor == "banco") and (pontosJ < pontosB):
            ok = True
        elif(vencedor == "empate")and (pontosJ == pontosB):
            ok = True
        return ok
        
# definindo o pagamento das apostas de acordo com as regras basicas e avançadas de pagamento de comissão  
def ganho(vencedor,aposta,fichas, baralho):
    total = 0
    if(vencedor == "jogador"):
        if(baralho == 1):
            total = fichas + (aposta-0.0129 *aposta)
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
#final de jogo        
def fimDeJogo():
    status = True
    print("FIM de jogo")
    cont = input("Deseja continuar? ")
    if(cont == "não"):
        status = False
    return status

#se a soma das cartas for maior que 10 só a unidade e contada ,ou seja,valor-10    
def cortarPontuacao(valor):
    return valor-10
    


    
    
