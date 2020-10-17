#EP-Design de Software
#Individual-Gabriel de Araujo Alves
#Data:17/10/2020
#importar todas as funções do arquivo jogo
import jogo
#lista para definir a quantidade de baralhos a serem jogados
baralhos = [1,6,8]
#quantas fichas irão ser inseridas para o começo do jogo?
fichas = int(input("Quantas fichas você inserir ? "))
while(fichas <= 0):
    print("QUANTIDADE INVÁLIDA!")
    fichas = int(input("Quantas fichas você inserir ? "))
#continuação do jogo
continua = True
baralho = jogo.montarBaralho()
#defini a quantidade de baralhos
quantidadeCartas = int(input("Com quantos baralhos você deseja jogar? "))
while(quantidadeCartas not in baralhos):
    print("Entrada inválida! Tente novamente.")
    quantidadeCartas = int(input("Com quantos baralhos você deseja jogar? "))
baralho = jogo.quantBaralhos(quantidadeCartas,baralho)
#defini a quantidade de jogadores que irão participar
jogadores = int(input("Quantos jogadores irá partipar? "))
i = 1
while(i <= jogadores):
    while(continua) and (fichas > 0):
        print("Jogador", i)
        aposta = int(input("Quantas fichas você deseja apostar ? "))#quantidade da aposta
        while(aposta > fichas):
            print("Entrada Inválida!")
            aposta = int(input("Quantas fichas você deseja apostar ? "))
        vencedor = input("Quem você acredita que é o vencedor da partida ? banco, jogador ou empate? ")#definindo o vencedor da partida

#sorteio das 2 cartas do jogador
        naipe = jogo.sortearNaipe(baralho)
        cartaJ1 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaJ1)
        naipe = jogo.sortearNaipe(baralho)
        cartaJ2 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaJ2)

#sorteio das 2 cartas do banco
        naipe = jogo.sortearNaipe(baralho)
        cartaB1 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaB1)
        naipe = jogo.sortearNaipe(baralho)
        cartaB2 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaB2)

#soma das cartas do jogador e do banco ,respectivamente
        pontosJ = (jogo.pontuacao(cartaJ1)) + (jogo.pontuacao(cartaJ2))
        pontosB = (jogo.pontuacao(cartaB1)) + (jogo.pontuacao(cartaB2))
        print("Pontos Jogador:", pontosJ)
        print("Pontos Banco:", pontosB)
#se a soma das cartas do banco ou do jogador for maior que 10 só a unidade e contada
        if(pontosJ >= 10):
            pontosJ = jogo.cortarPontuacao(pontosJ)
            print("Pontuação do Jogador Cortada:", pontosJ)
        if(pontosB >= 10):
            pontosB = jogo.cortarPontuacao(pontosB)
            print("Pontuação do Banco Cortada:", pontosB)
#verificando o vencedor no caso de banco ou jogador ter soma das cartas 8 ou 9
        verifica = jogo.verificarGanhadorCaso1(vencedor, pontosJ, pontosB,fichas)
        if(verifica):
            fichas = jogo.ganho(vencedor,aposta,fichas, quantidadeCartas)
            print("O jogador venceu!")
            continua = jogo.fimDeJogo()
#verificando o vencedor caso banco ou jogador somem 6 ou 7        
        verifica2 = jogo.verificaGanhadorCaso2(vencedor,pontosJ,pontosB)    
        if(verifica!= True) and (verifica2):
            fichas = jogo.ganho(vencedor,aposta,fichas,quantidadeCartas)
            print("O jogador venceu!")
            continua = jogo.fimDeJogo()
#casos de distribuicao da 3° carta do banco ou do jogador(soma do jogador ser menor ou igual a 5 e a soma do banco ser diferente de 8 ou 9 ou as duas somas serem menores ou iguais a 5)    
        verifica3 = True
        if(verifica != True and verifica2 != True):
            verifica3 = False        
#só a carta do banco é sorteada            
            if(pontosB <=5) and (pontosJ>=6):
                naipe = jogo.sortearNaipe(baralho)
                carta3 = jogo.sortearCarta(baralho,naipe)
                baralho = jogo.retirarCarta(baralho,naipe,carta3)
                pontosB+= (jogo.pontuacao(carta3))
                print("A nova carta sorteada do banco foi:", carta3)
                if(pontosB >=10):
                    pontosB = jogo.cortarPontuacao(pontosB)
                    print("Pontuação Cortada: Pontos Banco:", pontosB)
 #carta do jogador e sorteada ,além disso pela regra de distribuição da 3° carta do banco haverá decisão se ela irá ou não ser distribuida           
            if(pontosJ <=5 and pontosB <=5):
                naipe = jogo.sortearNaipe(baralho)
                cartaJ = jogo.sortearCarta(baralho,naipe)
                baralho = jogo.retirarCarta(baralho,naipe,cartaJ)
                pontosJ+= (jogo.pontuacao(cartaJ))
                print("A nova carta sorteada do Jogador foi:", cartaJ)
                if(pontosJ >=10):
                    pontosJ = jogo.cortarPontuacao(pontosJ)
                    print("Pontuação Cortada: Pontos Jogador:", pontosJ)
 #3° carta do banco é distribuida               
                if(pontosB>=0 and pontosB<=2):
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)
#3° carta do banco é distribuida                 
                elif(pontosB == 3 and cartaJ!= 8):
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)       
#3° carta do banco é distribuida                
                elif(pontosB == 4) and (pontosJ!= 0 and pontosJ !=1 and pontosJ!=8 and pontosJ!=9):
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)                  
#3° carta do banco é distribuida                
                elif(pontosB == 5) and (pontosJ!= 0 and pontosJ !=1 and pontosJ!=2 and pontosJ!=3 and pontosJ!=8 and pontosJ!=9):
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)
                else:
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)
#dizendo quem foi o vencedor da partida definindo qual a maior pontuação:banco ou jogador               
            if(vencedor == "jogador") and (pontosJ > pontosB):
                fichas = jogo.ganho(vencedor,aposta,fichas,quantidadeCartas)
                print("O jogador venceu!")
                continua = jogo.fimDeJogo()
            elif(vencedor == "banco") and (pontosB > pontosJ):
                fichas = jogo.ganho(vencedor,aposta,fichas,quantidadeCartas)
                print("O jogador venceu!")
                continua = jogo.fimDeJogo()
            elif(vencedor == "empate") and (pontosJ == pontosB):
                fichas = jogo.ganho(vencedor,aposta,fichas,quantidadeCartas)
                print("O jogador venceu!")
                continua = jogo.fimDeJogo()
 #caso de derrota do jogador           
        if(verifica!= True) and (verifica2!=True) and (verifica3!=True):
            fichas-=aposta
            print("O jogador perdeu!")
            continua = jogo.fimDeJogo()
 #quantas fichas o jogador possui       
        print("Você possui Fichas:", fichas)

        if(fichas == 0):
            print("Você não tem mais fichas")
#loop para passar para o proximo jogador se houver mais de 1        
    if(continua!=True):
        i+=1
        continua = True

        
        
        
        
        
            
  
      
        
        
        
    
            
        
        
            

    

    



        
            
            
        

    
  

  
        
        
        

  
            
         
            

        
            
        



    
    

    
    
    
    
    

    
   
    
        
            
                
            
           
        

    
    
   
    
    
        
    
    
    
        
