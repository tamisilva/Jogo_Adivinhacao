print('*********************************')
print('Bem vindo ao jogo de Adivinhação!')
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas > 0:
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute: int = int(input('Digite o seu número: '))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print('Você digitou', chute)

    if acertou:
        print('Você acertou!')
    else:
        if maior:
            print('Você errou! O seu chute foi maior do que o número secreto.')
        elif menor:
            print('Você errou! O seu chute foi menor do que o número secreto')

    rodada = rodada +1

print('Fim de jogo!')
