import random

print("Seja bem-vindo ao jogo adivinhe o numero da Vii!")
escolha_numero = input("Digite um numero maximo para o desafio: ")

if escolha_numero.isdigit():
    escolha_numero = int(escolha_numero)
else: 
    print("ERRO: O valor informado não é um numero. Por Favor execute novamente e informe um numero!")
    quit()

random_numero = random.randint(0, escolha_numero)

n_tentativas = 0

while True: 
    resp_usuario = input("Adivinhe o numero: ")

    if resp_usuario.isdigit():
        resp_usuario = int(resp_usuario)
    else:
        print("ERRO: O valor informado não é um numero. Favor informe um numero!")
        continue

    n_tentativas = n_tentativas + 1
    if resp_usuario == random_numero: 
        print("Você acertou!")
        break
    elif resp_usuario > random_numero: 
        print("Chutou alto, o numero é menor que esse...")
    else:
        print("Chutou baixo, o numero é maior que esse...")

print("Nº de tentativas foi: " + str(n_tentativas))