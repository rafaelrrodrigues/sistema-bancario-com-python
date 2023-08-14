menu = """
[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair

=> """

LIMITE_SAQUE_VALOR = 500
LIMITE_SAQUES = 3
valor_inicial = 1000

class Cliente:
    def __init__(self, nome, saldo) -> None:
        self.__nome = nome
        self.__saldo = saldo
        self.__extrato = []
        self.__saques = 0
        self.__valor = 0

    @property
    def nome(self):
        return self.__nome
    
    @property
    def extrato(self):
        return self.__extrato
    
    @extrato.setter
    def extrato(self, lancamento):
        print(lancamento)
        self.__extrato.append(lancamento)

    @property
    def saldo(self):
        return "{:.2f}".format(round(self.__saldo, 2))
    
    # Realiza o saque, incrementa o limite diario e envia para lançar o registro
    def sacar(self, valor_saque):
        self.__saldo = self.__saldo - round(valor_saque, 2)
        self.__saques = self.__saques + 1
        lancamento = "Saque    R$" + str("{:.2f}".format(valor_saque)) + " efetuado."
        self.extrato = lancamento

    # Realiza o deposito e envia para lancar o registro 
    def depositar(self, deposito):
        self.__saldo += deposito
        lancamento = "Deposito R$" + str("{:.2f}".format(deposito)) + " efetuado."
        self.extrato = lancamento

    # Verifica as Regras de Negocio para o saque
    def condicoesSaque(self):
        if self.__saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido")
            return False
        print("Saque")
        self.recebeValor()

        if self.__valor > LIMITE_SAQUE_VALOR or self.__valor < 0 or self.__valor > self.__saldo:
            print("Valor não permitido")
            return False
            
        else:
            self.sacar(self.__valor)
            return True
    
    # Verifica Regras de negocio para deposito (apenas se valor_deposito esta validado)
    def condicoesDeposito(self):
        valor_deposito = self.recebeValor()
        if not valor_deposito:
            print("Valor invalido")
            return False
        else:
            self.depositar(self.__valor)
            return True

    # Recebe os valores para Saque e Deposito. Se for valor valido, retorna True
    def recebeValor(self):
        self.__valor = False
        valor = float(input("Insira o valor desejado: "))
        if not self.validaValor(valor): 
            return False
        else:
            self.__valor = round(valor, 2)
            return True
    
    # Retorna True se o valor possuir 2 casas apos a virgula e for maior que zero
    def validaValor(self, valor):
        return True if len(str(valor).split('.')[-1]) <= 2 and valor > 0 else False


def main():
    user1 = Cliente("Rafael", valor_inicial)
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
