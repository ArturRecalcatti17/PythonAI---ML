import random

def starter():

    global aleatoryNumber
    aleatoryNumber = random.randint(1, 100)
    print('''    bem vindo ao jogo de números aleatórios, neste jogo, o computador irá
    gerar um número aleatório de 1 à 100, e você, jogador irá chutar números até acertar, caso o número
    que você chutou seja inferior ao número gerado, o computador irá dizer "Maior" e o mesmo para números
    menores
            ''')
    inputuser = input('digite um número: ')
    verifyer(inputuser)

def verifyer(number):

    if int(number) < aleatoryNumber:
       print('Maior')
       resposta = input('digite um número: ')
       verifyer(resposta)

    if int(number) > aleatoryNumber:
       print('Menor')
       resposta = input('digite um número: ')
       verifyer(resposta)


    if int(number) == aleatoryNumber:
       print('Acertou')
       print('''deseja jogar novamente?
       s(sim) n(não)
       ''')
       resposta = input('Resposta: ')

       if resposta.lower() == 's':
           starter()
       elif resposta.lower() == 'n':
           print('Obrigado por jogar!')
       else:
           print('Resposta inválida. Obrigado por jogar!')

starter()
