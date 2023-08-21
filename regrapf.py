
def calculaDigito(vec_cpf, vec_calculo):
    soma = sum([a * b for a, b in zip(vec_cpf, vec_calculo)])
    n = soma // 11
    resto = soma % 11
    dig_valid = 0 if n < 2 else 11 - resto
    print(soma, n, resto, dig_valid)
    return dig_valid

cpf = "11144477735"
vetor = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
cpf_vetor = [int(i) for i in cpf[:-2]]

dig_valid1 = calculaDigito(cpf_vetor, vetor[1::])

cpf_vetor.append(dig_valid1)

dig_valid2 = calculaDigito(cpf_vetor, vetor)

cpf_vetor.append(dig_valid2)

cpf_final = ''.join([str(i) for i in cpf_vetor])

print(cpf_final == cpf)
