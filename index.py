#Entrada: Escolha
#Saída: 'You Win' or 'You Lose ;('
from random import choice
print('=============== ** JOKENPO ** ==============')
continuar = 1
condicion = True
while continuar == 1:
    while condicion:
        print('Faça a sua escolha, digite:\n1 == pedra\n2 == papel\n3 == tesoura')
        escolhaDoUsuario = int(input('-> '))

        if escolhaDoUsuario < 1 or escolhaDoUsuario > 3:
            print(' ==== ERROU, JUMENTO! =====')
            print('Qual parte de escolha 1, 2 ou 3 que você não entendeu? .')
            condicion = True
        elif escolhaDoUsuario == 1:
            escolhaDoUsuario = 'pedra'
            condicion = False
        elif escolhaDoUsuario == 2:
            escolhaDoUsuario = 'papel'
            condicion = False
        else:
            escolhaDoUsuario = 'tesoura'
            condicion = False

        escolha = choice(['pedra', "papel", "tesoura"])

        if escolha == escolhaDoUsuario:
            print('DRAW')
            print(f'Máquina: {escolha}\nVocê: {escolhaDoUsuario}')
        elif escolha == "pedra" and escolhaDoUsuario == "tesoura":
            print('YOU LOSE')
            print(f'Máquina: {escolha}\nVocê: {escolhaDoUsuario}')
        elif escolha == "pedra" and escolhaDoUsuario == "papel":
            print('YOU WIN')
            print(f'Máquina: {escolha}\nVocê: {escolhaDoUsuario}')
        elif escolha == "tesoura" and escolhaDoUsuario == "papel":
            print('YOU LOSE')
            print(f'Máquina: {escolha}\nVocê: {escolhaDoUsuario}')
        elif escolha == 'tesoura' and escolhaDoUsuario == 'pedra':
            print('YOU WIN')
            print(f'Máquina: {escolha}\nVocê: {escolhaDoUsuario}')
        elif escolha == 'papel' and escolhaDoUsuario == 'pedra':
            print('YOU LOSE')
            print(f'Máquina: {escolha}\nVocê: {escolhaDoUsuario}')
        elif escolha == 'papel' and escolhaDoUsuario == 'tesoura':
            print('YOU WIN')
            print(f'Máquina: {escolha}\nVocê: {escolhaDoUsuario}')
        continuar = int(input('Deseja continuar? 1 - SIM // 0 - NÃO: '))

print('=============== ** FIM DO PROGRAMA ** ===============')
