
class Cliente:
    def __init__(self, nome, nascimento, cpf, endereco) -> None:
        self.__nome = nome
        self.__nascimento = nascimento
        self.__cpf = cpf
        self.__endereco = endereco
        self.__agencia = "0001"
        self.__ativo = True

    @property
    def recuperaCpf(self):
        return self.__cpf