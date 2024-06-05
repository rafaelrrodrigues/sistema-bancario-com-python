from models.cliente import Cliente
from models.conta import Conta

from utils.regracpf import verificaCPF

validacao_ativa = False

class Sistema:
    def __init__(self) -> None:
        self.clients = []
        self.cpfs = []
        self.contas = []
        pass
    
    def cadastraCliente(self):
        nome = input("Nome: ")
        nascimento = input("Data de Nascimento (dd/MM/yyyy): ")
        endereco = input("Endereco: ")
        cpf = input("CPF: ")
        if not self.validaCPF(cpf):
            print("Cadastro nao concluido")
        else:
            novoCliente = Cliente(nome, nascimento, cpf, endereco)
            self.clients.append(novoCliente)
            self.cpfs.append(cpf)

    def consultaCliente(self):
        # Pegar o indice do CPF a partir do valor
        # Solicitar senha do usuario
        # Exibir informacoes do Cliente
        pass

    def validaCPF(self, cpf):
        if not len(cpf) == 11:
            print("Quantidade invalida de digitos:", len(cpf))
            return False
        
        elif not verificaCPF(cpf) and validacao_ativa:
            print("CPF invalido:", len(cpf))
            return False
        
        elif not cpf in self.cpfs:
            print("CPF ja existente")
            return False
        
        else:    
            return True
    
    def criaNumeroConta(self):
        pass

    def registraContaCliente(self):
        pass

    def verificaCliente(self):
        cpf = input("Digite o CPF do cliente: ")
        if cpf not in self.cpfs:
            print("CPF nao encontrado")
            return False
        else:
            return True
        pass

    def criarConta(self):
        pass

    def interfaceCadastro(self):
        while True:
            print("Saldo:   R$" + conta.saldo)
            opcao_conta = input(menu_conta)

            # Cadastrar Cliente
            if opcao_conta == "1":
                if not conta.condicoesSaque():
                    print("Nao foi possivel realizar o saque")
                pass
            
            # Consultar Cliente
            elif opcao_conta == "2":
                if not conta.condicoesDeposito():
                    print("Nao foi possivel realizar o deposito")
                8

            # Editar Cliente
            elif opcao_conta == "3":
                extrat = conta.extrato
                for i in extrat:
                    print(i)
                pass

            # Criar Conta
            elif opcao_conta == "4":
                extrat = conta.extrato
                for i in extrat:
                    print(i)
                pass

            # Acessar Conta
            elif opcao_conta == "5":
                extrat = conta.extrato
                for i in extrat:
                    print(i)
                pass

            # Excluir Conta
            elif opcao_conta == "6":
                extrat = conta.extrato
                for i in extrat:
                    print(i)
                pass

            elif opcao_conta == "7":
                exit()

            else:
                print("Opcao invalida")

    def interfaceConta(self, conta):
        while True:
            print("Saldo:   R$" + conta.saldo)
            opcao_conta = input(menu_conta)

            # Saque
            if opcao_conta == "1":
                if not conta.condicoesSaque():
                    print("Nao foi possivel realizar o saque")
                pass
            
            # Deposito
            elif opcao_conta == "2":
                if not conta.condicoesDeposito():
                    print("Nao foi possivel realizar o deposito")
                pass

            # Extrato
            elif opcao_conta == "3":
                extrat = conta.extrato
                for i in extrat:
                    print(i)
                pass

            elif opcao_conta == "4":
                exit()

            else:
                print("Opcao invalida")
