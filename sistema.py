from cliente import Cliente
from conta import Conta

menu = """
[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair

=> """

"""
pegar itens de um dicionário de forma iterativa

for chave, valor in dicionario.items()
    print(chave, valor)

.copy()

"""

LIMITE_SAQUE_VALOR = 500
LIMITE_SAQUES = 3
valor_inicial = 1000

def main():
    user1 = Conta("Rafael", valor_inicial)
    print("Bem-vindo", user1.nome)
    user1.extrato = "Valor inicial R$ " + str("{:.2f}".format(round(valor_inicial, 2)))

    while True:
        print("Saldo:   R$" + user1.saldo)
        opcao = input(menu)
        
        # Saque
        if opcao == "1":
            if not user1.condicoesSaque():
                print("Nao foi possivel realizar o saque")
            pass
        
        # Deposito
        elif opcao == "2":
            if not user1.condicoesDeposito():
                print("Nao foi possivel realizar o deposito")
            pass

        # Extrato
        elif opcao == "3":
            extrat = user1.extrato
            for i in extrat:
                print(i)
            pass

        elif opcao == "4":
            exit()

        else:
            print("Opcao invalida")

if __name__ == "__main__":
    main()

def criaNumeroConta():
    pass

def registraUsuarios():
    pass

def criarConta():
    pass

def validaCPF():
    pass