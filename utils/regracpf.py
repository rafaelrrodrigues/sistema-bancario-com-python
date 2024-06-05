validacao_ativa = False

def calculaDigito(vec_cpf, vec_calculo):
    soma = sum([a * b for a, b in zip(vec_cpf, vec_calculo)])
    n = soma // 11
    resto = soma % 11
    dig_valid = 0 if n < 2 else 11 - resto
    return dig_valid

# Valida se os 2 ultimos digitos do CPF estao corretos 
def verificaCPF(cpf):
    vetor = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2] # Vetor para calculo
    cpf_vetor = [int(i) for i in cpf[:-2]] # Transforma os 9 primeiros digitos em int

    # Verifica o primeiro digito de validacao
    cpf_vetor.append(calculaDigito(cpf_vetor, vetor[1::]))

    # Verifica o segundo digito de validacao
    cpf_vetor.append(calculaDigito(cpf_vetor, vetor))

    # Transforma o CPF validado em str novamente
    cpf_final = ''.join([str(i) for i in cpf_vetor])
 
    # Verifica se o numero gerado eh igual ao informado
    return cpf_final == cpf
