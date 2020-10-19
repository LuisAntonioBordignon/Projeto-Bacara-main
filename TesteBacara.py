# EP - Design de Software
# Aluno: Luis Antonio Bordignon de Oliveira                   :)
# Data: 18/10/2020

#O vencedor poderá ser o jogador, o banco ou o jogo terminará em empate
#Mesa embaralha 52 cartas
fichas = 100

import random

#Definindo o baralho

print('Você possui 100 fichas!')

A = 1
J = 0
Q = 0
K = 0
cartas = [A, 2, 3, 4, 5, 6, 7, 8, 9, 0, J, Q, K]
cartas = cartas + cartas + cartas + cartas


#Desde que o jogador aposte fichas possíveis, o jogo rodará dentro do while
invalido = True
while invalido and fichas>0:
    aposta = int(input('Coloque sua aposta: '))
    if aposta>fichas:
        invalido = False
        print('Você não pode apostar o que não tem!')
       
    else:
        #Embaralhando as cartas
        random.shuffle(cartas)

        v = input('Quem será o vencedor? jogador, banco ou empate? ')

        #Criando as listas
        lista_banco = []
        lista_jogador = []

        lista_jogador.append(cartas[0])
        lista_jogador.append(cartas[1])
        lista_banco.append(cartas[2])
        lista_banco.append(cartas[3])

        #Colocando as somas das listas dentro de variáveis
        j = sum(lista_jogador)
        b = sum(lista_banco)
       
        #Caso a banca ou jogador tenham uma soma igual a 8 ou 9
        if j==8 or j==9 or b==8 or b==9:
           #Abaixo, estão as possibilidades da escolha do jogador: 'jogador, banco ou empate'. Dentro dessas, estão outras possibilidade da soma das listas serem iguais, maiores ou menores.
            if v=='jogador':
                if j>b:
                    fichas = fichas + aposta
                    x = input('Parabéns, você ganhou e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif b>j:
                    fichas = fichas - aposta
                    x = input('Que pena, você perdeu e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif j==b:
                    fichas = fichas - aposta
                    x = input('Deu empate! Agora você tem {0} fichas. Quer jogar de novo?'.format(fichas))
          
            elif v=='banco':
                if j<b:
                    fichas = fichas + 0.95*aposta
                    fichas = int(fichas)
                    x = input('Parabéns, você ganhou e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif b<j:
                    fichas = fichas - aposta
                    x = input('Que pena, você perdeu e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif j==b:

                    fichas = fichas - aposta
                    x = input('Deu empate! Agora você tem {0} fichas. Quer jogar de novo?'.format(fichas))

            elif v=='empate':
                if j!=b:
                    fichas = fichas - aposta
                    x = input('Que pena, você perdeu e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif j==b:
                    fichas = fichas + 8*aposta
                    x = input('Parabéns, você ganhou e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
        
        #Caso as somas das cartas da banca ou do jogador sejam iguais ou menores que 5, será necessário adicionar mais uma carta e fazer uma nova soma
        elif j<=5 or b<=5:
            if b!=8 and b!=9 and b!=18 and j!=6 and j!=7:
                lista_jogador.append(cartas[4])
                j = sum(lista_jogador)
                jstr = str(j)
                if j>9:
                    j = jstr[1]
                    j = int(j)
                else:
                    j = jstr[0]
                    j = int(j)
            elif j!=8 and j!=9 and j!=18 and b!=6 and b!=7:
                lista_banco.append(cartas[5])
                b = sum(lista_banco)
                bstr = str(b)
                if b>9:
                    b = bstr[1]
                    b = int(b)
                else:
                    b = bstr[0]
                    b = int(b)



        #Vamos ver quem ganhou!
            if v=='jogador':
                if j>b:
                    fichas = fichas + aposta
                    x = input('Parabéns, você ganhou e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif b>j:
                    fichas = fichas - aposta
                    x = input('Que pena, você perdeu e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif j==b:
                    fichas = fichas - aposta
                    x = input('Deu empate! Agora você tem {0} fichas. Quer jogar de novo?'.format(fichas))


            elif v=='banco':
                if j<b:
                    fichas = fichas + 0.95*aposta
                    fichas = int(fichas)
                    x = input('Parabéns, você ganhou e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif b<j:
                    fichas = fichas - aposta
                    x = input('Que pena, você perdeu e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif j==b:
                    fichas = fichas - aposta
                    x = input('Deu empate! Agora você tem {0} fichas. Quer jogar de novo?'.format(fichas))

            elif v=='empate':
                if j!=b:
                    fichas = fichas - aposta
                    x = input('Que pena, você perdeu e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))
                elif j==b:
                    fichas = fichas + 8*aposta
                    x = input('Parabéns, você ganhou e agora possui {0} fichas! Quer jogar de novo? '.format(fichas))

    if x == 'não':
        invalido =  False

        

       
        

                

                

    





  


            
            
            
            
            
            
            
            
            
            
            
    
            