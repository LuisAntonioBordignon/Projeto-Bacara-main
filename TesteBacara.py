aposta = int(input('Coloque suas apostas: '))
#A aposta não deve ser maior que a quantidade de fichas que o jogador possui
v = input('Quem será o vencedor? ')
#o vencedor poderá ser o jogador, o banco ou o jogo terminará em empate
#mesa embaralha 52 cartas
fichas = 100

invalido = True
while invalido:
    if aposta>=fichas:
        invalido = False
        print('Você não pode apostar o que não tem!')
    else:
#Colocar comentários explicando o que cada bloco do código faz

        import random 

        A = 1
        J = 0
        Q = 0
        K = 0
        cartas = [A, 2, 3, 4, 5, 6, 7, 8, 9, 0, J, Q, K]
        cartas = cartas + cartas + cartas + cartas

        i = 0
        sorteio = []
        lista_banco = []
        lista_jogador = []
        while i<4:           
            r = random.randint(0,51)
            print(cartas[r])  #retirar depois, apenas funcional para testes
            i = i + 1
            if i<2:
                lista_banco.append(cartas[r])
                cartas.remove(cartas[r])                                                                                            
            else:
                lista_jogador.append(cartas[r])
                cartas.remove(cartas[r])
            
        if sum(lista_jogador)==8 or sum(lista_jogador)==9 or sum(lista_banco)==8 or sum(lista_banco)==9:
            #Agora o jogo termina e as apostas são pagas
            print('Fim de jogo')

            #Agora, quem obter a soma mais perto de 9 ganha

            if v == jogador:
                if sum(lista_jogador) > sum(lista_banco):
                    fichas = fichas + aposta
                    print('Você possui {0} fichas'.format(fichas))
                elif  sum(lista_jogador) < sum(lista_banco):
                    fichas = fichas - aposta
                    print('Você possui {0} fichas'.format(fichas))
                elif sum(lista_jogador) == sum(lista_banco):
                    print('Empate!')
            
            elif v == banco:
                if  sum(lista_jogador) > sum(lista_banco):
                    fichas = fichas - aposta
                    print('Você possui {0} fichas'.format(fichas))
                elif  sum(lista_jogador) <  sum(lista_banco):
                    fichas = fichas + aposta
                    print('Você possui {0} fichas'.format(fichas))
                elif   sum(lista_jogador) <sum(lista_banco):
                    print('Empate!')
            
            elif v == empate:
                if  sum(lista_jogador) == sum(lista_banco):
                    fichas = fichas + fichas*8
                    
                else:
                    #Tenho que colocar alguma condição aqui ou o jogo termina?

        elif sum(lista_jogador) < 8 or sum(lista_banco) < 8:
            if sum(lista_jogador) == 6 or sum(lista_jogador) == 7:
                #Não distribui novas cartas para o jogador
            elif sum(lista_banco)==6 orsum(lista_banco)==7:
                #Não distribui novas cartas para o banco
            elif sum(lista_banco)<6:
                r2 = random.randint(0,51)
                lista_banco.append(cartas[r2])
            elif sum(lista_jogador)<6:
                r3 = random.randint(0,51)
                lista_banco.append(cartas[r3])

                #Eu acho que tem aque colocar mais coisa ali em cima

        elif sum(lista_jogador) > 9:
            #A soma será igual ao último algarismo do número, mas como fazer isso?
        elif sum(lista_banco) > 9:
             #A soma será igual ao último algarismo do número, mas como fazer isso?





             lista_jogador[0]+lista_jogador[1]<6 
            


            

            r2 = random.randint(0,51)
            lista_banco.append(cartas[r2])
            lista_jogador.append(cartas[r2])

            
            



            

                


            
            
            
            
            
            
            
            
            
            
            
    
            