#Olá
#Encontrei dificuldades para a utilização do GitHub para monitorar a evolução do jogo, e acabei investimento meus esforços no jogo ao invés dessa configuração.
aposta = int(input('Coloque suas apostas: '))
#A aposta não deve ser maior que a quantidade de fichas que o jogador possui
v = input('Quem será o vencedor? ')
#o vencedor poderá ser o jogador, a banca ou o jogo terminará em empate
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
        lista_banca = []
        lista_jogador = []
        while i<4:           
            r = random.randint(0,51)
            print(cartas[r])  #retirar depois, apenas funcional para testes
            i = i + 1
            if i<2:
                cartas.remove(cartas[r])
                lista_banca.append(cartas[r])
            else:
                cartas.remove(cartas[r])
                lista_jogador.append(cartas[r])
           
            #Pode criar uma função que sorteia uma carta e remove do baralho
            #Como distribuir as cartas? Elas devem ser inseridas numa lista?
        if lista_jogador[0]+lista_jogador[1]==8 or lista_jogador[0]+lista_jogador[1]==9 or lista_banca[0]+lista_banca[1]==8 or lista_banca[0]+lista_banca[1]==9:
            #Agora o jogo termina e as apostas são pagas
            print('Fim de jogo')
            if v == jogador and lista_jogador[0]+lista_jogador[1]==8 or lista_jogador[0]+lista_jogador[1]==9:
                fichas = fichas + aposta
                print('Você possui {0} fichas'.format(fichas))
            elif v == jogador and lista_banca[0]+lista_banca[1]==8 or lista_banca[0]+lista_banca[1]==9:
                fichas = fichas - aposta
                print('Você perdeu! Resta {0} fichas'.format(fichas))
    
            