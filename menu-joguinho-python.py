import os

# ---------- Função para limpar a tela ----------
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------- Apresentação ----------
limpar_tela()
print("Boas vindas ao Joguinho Python!\n")
nome = input("Qual é o seu nome? ")
print(f"\nQue bom que você chegou, {nome}! Prepare-se para desafios incríveis!\n")
input("Pressione Enter para continuar...")

# ---------- Funções dos joguinhos ----------

def soma_dois():
    while True:
        limpar_tela()
        print("Desafio: Soma de dois números")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print(f"A soma é {n1 + n2}")
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

def par_ou_impar():
    while True:
        limpar_tela()
        print("Desafio: Par ou Ímpar")
        numero = int(input("Digite um número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

def maior_de_tres():
    while True:
        limpar_tela()
        print("Desafio: Maior de três números")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        n3 = int(input("Digite o terceiro número: "))
        print(f"O maior número é {max(n1, n2, n3)}")
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

def tabuada():
    while True:
        limpar_tela()
        print("Desafio: Tabuada")
        n = int(input("Digite um número para ver sua tabuada: "))
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

def contagem_regressiva():
    while True:
        limpar_tela()
        print("Desafio: Contagem regressiva")
        n = int(input("Digite um número: "))
        for i in range(n, -1, -1):
            print(i)
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

def soma_ate_n():
    while True:
        limpar_tela()
        print("💡 Desafio: Soma de 1 até N")
        n = int(input("Digite um número: "))
        print(f"A soma de 1 até {n} é {sum(range(1, n+1))}")
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

def fatorial():
    while True:
        limpar_tela()
        print("Desafio: Fatorial")
        n = int(input("Digite um número para calcular o fatorial: "))
        fat = 1
        for i in range(n, 0, -1):
            fat *= i
        print(f"O fatorial de {n} é {fat}")
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

def soma_varios():
    while True:
        limpar_tela()
        print("Desafio: Soma de vários números")
        soma = 0
        numero = int(input("Digite números (0 para parar): "))
        while numero != 0:
            soma += numero
            numero = int(input("Digite outro número (0 para parar): "))
        print(f"A soma total é {soma}")
        repetir = input("\nPressione Enter para voltar ao menu ou digite R para jogar novamente: ").lower()
        if repetir != 'r':
            break

# ---------- Menu Principal ----------
while True:
    limpar_tela()
    print(f"MENU DE JOGUINHOS - PLAYER: {nome}")
    print("1 - Soma de dois números")
    print("2 - Par ou Ímpar")
    print("3 - Maior de três números")
    print("4 - Tabuada")
    print("5 - Contagem regressiva")
    print("6 - Soma de 1 até N")
    print("7 - Fatorial")
    print("8 - Soma de vários números (até digitar 0)")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":
        soma_dois()
    elif opcao == "2":
        par_ou_impar()
    elif opcao == "3":
        maior_de_tres()
    elif opcao == "4":
        tabuada()
    elif opcao == "5":
        contagem_regressiva()
    elif opcao == "6":
        soma_ate_n()
    elif opcao == "7":
        fatorial()
    elif opcao == "8":
        soma_varios()
    elif opcao == "0":
        limpar_tela()
        print(f"\nAté logo, {nome}!Obrigado por jogar!")
        break
    else:
        input("Opção inválida. Pressione Enter para tentar novamente...")

