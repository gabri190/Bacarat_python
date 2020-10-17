import jogo
baralhos = [1,6,8]

fichas = int(input("Quantas fichas você inserir ? "))
while(fichas <= 0):
    print("QUANTIDADE INVÁLIDA!")
    fichas = int(input("Quantas fichas você inserir ? "))


continua = True
baralho = jogo.montarBaralho()
quantidadeCartas = int(input("Com quantos baralhos você deseja jogar? "))
while(quantidadeCartas not in baralhos):
    print("Entrada inválida! Tente novamente.")
    quantidadeCartas = int(input("Com quantos baralhos você deseja jogar? "))
baralho = jogo.quantBaralhos(quantidadeCartas,baralho)
jogadores = int(input("Quantos jogadores irá partipar? "))
i = 1

while(i <= jogadores):
    while(continua) and (fichas > 0):
        print("Jogador", i)
        aposta = int(input("Quantas fichas você deseja apostar ? "))
        while(aposta > fichas):
            print("Entrada Inválida!")
            aposta = int(input("Quantas fichas você deseja apostar ? "))
        vencedor = input("Quem você acredita que é o vencedor da partida ? banco, jogador ou empate? ")

        #jogada do jogador
        naipe = jogo.sortearNaipe(baralho)
        cartaJ1 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaJ1)
        naipe = jogo.sortearNaipe(baralho)
        cartaJ2 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaJ2)

        #jogada do banco
        naipe = jogo.sortearNaipe(baralho)
        cartaB1 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaB1)
        naipe = jogo.sortearNaipe(baralho)
        cartaB2 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaB2)


        pontosJ = (jogo.pontuacao(cartaJ1)) + (jogo.pontuacao(cartaJ2))
        pontosB = (jogo.pontuacao(cartaB1)) + (jogo.pontuacao(cartaB2))
        print("Pontos Jogador:", pontosJ)
        print("Pontos Banco:", pontosB)
  
        if(pontosJ >= 10):
            pontosJ = jogo.cortarPontuacao(pontosJ)
            print("Pontuação do Jogador Cortada:", pontosJ)
        if(pontosB >= 10):
            pontosB = jogo.cortarPontuacao(pontosB)
            print("Pontuação do Banco Cortada:", pontosB)

    
       
        verifica = jogo.verificarGanhadorCaso1(vencedor, pontosJ, pontosB,fichas)
        if(verifica):
            fichas = jogo.ganho(vencedor,aposta,fichas, quantidadeCartas)
            print("O jogador venceu!")
            continua = jogo.fimDeJogo()
        verifica2 = jogo.verificaGanhadorCaso2(vencedor,pontosJ,pontosB)    
        if(verifica!= True) and (verifica2):
            fichas = jogo.ganho(vencedor,aposta,fichas,quantidadeCartas)
            print("O jogador venceu!")
            continua = jogo.fimDeJogo()
        verifica3 = True
        if(verifica != True and verifica2 != True):
            verifica3 = False        
            if(pontosB <=5) and (pontosJ>=6):
                naipe = jogo.sortearNaipe(baralho)
                carta3 = jogo.sortearCarta(baralho,naipe)
                baralho = jogo.retirarCarta(baralho,naipe,carta3)
                pontosB+= (jogo.pontuacao(carta3))
                print("A nova carta sorteada do banco foi:", carta3)
                if(pontosB >=10):
                    pontosB = jogo.cortarPontuacao(pontosB)
                    print("Pontuação Cortada: Pontos Banco:", pontosB)
            if(pontosJ <=5 and pontosB <=5):
                naipe = jogo.sortearNaipe(baralho)
                cartaJ = jogo.sortearCarta(baralho,naipe)
                baralho = jogo.retirarCarta(baralho,naipe,cartaJ)
                pontosJ+= (jogo.pontuacao(cartaJ))
                print("A nova carta sorteada do Jogador foi:", cartaJ)
                if(pontosJ >=10):
                    pontosJ = jogo.cortarPontuacao(pontosJ)
                    print("Pontuação Cortada: Pontos Jogador:", pontosJ)
                if(pontosB>=0 and pontosB<=2):
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)
                elif(pontosB == 3 and cartaJ!= 8):
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)       
                elif(pontosB == 4) and (pontosJ!= 0 and pontosJ !=1 and pontosJ!=8 and pontosJ!=9):
                    naipe = jogo.sortearNaipe(baralho)
                    carta3 = jogo.sortearCarta(baralho,naipe)
                    baralho = jogo.retirarCarta(baralho,naipe,carta3)
                    pontosB+= (jogo.pontuacao(carta3))
                    print("A nova carta sorteada do banco foi:", carta3)
                    if(pontosB >=10):
                        pontosB = jogo.cortarPontuacao(pontosB)
                        print("Pontuação Cortada: Pontos Banco:", pontosB)                  
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
            
        if(verifica!= True) and (verifica2!=True) and (verifica3!=True):
            fichas-=aposta
            print("O jogador perdeu!")
            continua = jogo.fimDeJogo()
        
        print("Você possui Fichas:", fichas)

        if(fichas == 0):
            print("Você não tem mais fichas")
        
    if(continua!=True):
        i+=1
        continua = True

        
        
        
        
        
            
  
      
        
        
        
    
            
        
        
            

    

    



        
            
            
        

    
  

  
        
        
        

  
            
         
            

        
            
        



    
    

    
    
    
    
    

    
   
    
        
            
                
            
           
        

    
    
   
    
    
        
    
    
    
        
