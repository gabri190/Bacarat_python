#EP-Design de Software
#Individual-Gabriel de Araujo Alves
#Data:15/10/2020
#importar o jogo e as funções definidas
import jogo
baralhos = [1,6,8]#lista com a quantidade de baralhos permitidas para o jogo:1,6 ou 8
#definindo a quantidade de fichas para começar o jogo
fichas = int(input("Quantas fichas você inserir ? "))
while(fichas <= 0):
    print("QUANTIDADE INVÁLIDA!")
    fichas = int(input("Quantas fichas você inserir ? "))
#continuar o jogo
continua = True
baralho = jogo.montarBaralho()
quantidadeCartas = int(input("Com quantos baralhos você deseja jogar? "))#quantidade de baralhos a ser jogado 
while(quantidadeCartas not in baralhos):
    print("Entrada inválida! Tente novamente.")
    quantidadeCartas = int(input("Com quantos baralhos você deseja jogar? "))
baralho = jogo.quantBaralhos(quantidadeCartas,baralho)
jogadores = int(input("Quantos jogadores irá partipar? "))#quantos jogadores participarão do jogo
i = 1
while(i <= jogadores):
    while(continua and fichas>0):#condições necessárias para a continuação do jogo
        print("Jogador", i)
        aposta = int(input("Quantas fichas você deseja apostar ? "))#quanto será a aposta?
        while(aposta > fichas):
            print("Entrada Inválida!")
            aposta = int(input("Quantas fichas você deseja apostar ? "))
        vencedor = input("Quem você acredita que é o vencedor da partida ? banco, jogador ou empate? ")#definindo quem será o vencedor

        #sorteio das cartas do jogador
        naipe = jogo.sortearNaipe(baralho)
        cartaJ1 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaJ1)
        naipe = jogo.sortearNaipe(baralho)
        cartaJ2 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaJ2)

        #sorteio das cartas do banco
        naipe = jogo.sortearNaipe(baralho)
        cartaB1 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaB1)
        naipe = jogo.sortearNaipe(baralho)
        cartaB2 = jogo.sortearCarta(baralho,naipe)
        baralho = jogo.retirarCarta(baralho,naipe,cartaB2)
        #soma dos pontos do jogador e do banco
        pontosJ = (jogo.pontuacao(cartaJ1)) + (jogo.pontuacao(cartaJ2))
        pontosB = (jogo.pontuacao(cartaB1)) + (jogo.pontuacao(cartaB2))
        #se a pontuação for maior que 10 considera-se só a unidade e o jogo continua normalmente
        if(pontosJ >= 10):
            pontosJ = jogo.cortarPontuacao(pontosJ)
        if(pontosB >= 10):
            pontosB = jogo.cortarPontuacao(pontosB)

        #mostrar a pontuação do banco e do jogo
        print("Pontos Jogador:", pontosJ)
        print("Pontos Banco:", pontosB)
        verifica = jogo.verificarGanhadorCaso1(vencedor, pontosJ, pontosB,fichas)#caso1:jogador ou banco possuem soma 8 ou 9 das cartas
        if(verifica):
            fichas = jogo.ganho(vencedor,aposta,fichas, baralho)
            print("O jogador venceu!")
            continua = jogo.fimDeJogo()
#caso2:soma das cartas do banco ou jogador diferente de 8 ou 9
        verifica2 = jogo.verificaGanhadorCaso2(vencedor,pontosJ,pontosB, fichas, baralho,naipe)
        if(verifica!= True) and (verifica2):
            fichas = jogo.ganho(vencedor,aposta,fichas,baralho)
            print("O jogador venceu!")
            continua = jogo.fimDeJogo()
    

        # Condições que fazem o jogador perder o jogo       
        if(verifica != True and verifica2 != True):
            fichas-=aposta
            print("O jogador perdeu!")
            continua = jogo.fimDeJogo()
        #mostrar na tela a quantidade de fichas do jogador
        print("Você possui Fichas:", fichas)
        if(fichas==0):#o jogo não continua se houver 0 fichas pois assim o jogador não pode mais jogar
            print("voce nao possui mais fichas")
    if(continua!=True):#se o primeiro jogador não quiser continuar passa a vez para o 2 jogador e assim por diante até ser atingida a quantidade de jogadores pedidos
        i+=1
        continua = True

        
        
        
        
        
            
  
      
        
        
        
    
            
        
        
            

    

    



        
            
            
        

    
  

  
        
        
        

  
            
         
            

        
            
        



    
    

    
    
    
    
    

    
   
    
        
            
                
            
           
        

    
    
   
    
    
        
    
    
    
        
