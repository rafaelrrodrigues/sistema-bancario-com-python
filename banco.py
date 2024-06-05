from models.sistema import Sistema


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
    sistema = Sistema()
    print("Bem-vindo")
    # user1.extrato = "Valor inicial R$ " + str("{:.2f}".format(round(valor_inicial, 2)))

    while True:
        print("Saldo:   R$" + user1.saldo)
        opcao_conta = input(menu_conta)
        
        # Saque
        if opcao_conta == "1":
            if not user1.condicoesSaque():
                print("Nao foi possivel realizar o saque")
            pass
        
        # Deposito
        elif opcao_conta == "2":
            if not user1.condicoesDeposito():
                print("Nao foi possivel realizar o deposito")
            pass

        # Extrato
        elif opcao_conta == "3":
            extrat = user1.extrato
            for i in extrat:
                print(i)
            pass

        elif opcao_conta == "4":
            exit()

        else:
            print("Opcao invalida")

if __name__ == "__main__":
    main()
