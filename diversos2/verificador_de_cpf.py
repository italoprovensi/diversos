print('verificador de cpf')
cpf = input('digite o seu cpf ').replace('.', '').replace('-', '')
cpf_9_digitos = cpf[:9]
contagem_regre = 10
resultado = 0
try:
    for digito in cpf_9_digitos:
        resultado += (int(digito) * contagem_regre)
        contagem_regre -= 1
    resultado2 = resultado * 10 % 11
    digito1 = 0 if resultado2 > 9 else resultado2
    # parte 2
    resultado2_str = str(resultado2)
    cpf_parte_2 = cpf[:9]
    cpf_int2 = cpf_parte_2 + resultado2_str

    contagem_regre2 = 11
    resultado_parte2 = 0
    for digito_parte2 in cpf_int2:
        resultado_parte2 += (int(digito_parte2) * contagem_regre2)
        contagem_regre2 -= 1
        # print((int(digito2) * contagem_regre2))
    resultado2_parte2 = resultado_parte2 * 10 % 11
    digito2 = 0 if resultado2_parte2 > 9 else resultado2_parte2
    digito1_str = str(digito1)
    digito2_str = str(digito2)
    cpf_calculado = cpf_9_digitos + digito1_str + digito2_str

    if cpf == cpf_calculado:
        print(f'{cpf} cpf valido')
    else:
        print(f'{cpf} cpf invalido')

except Exception as erro:
    print(erro)
    print('coloque apenas os 11 numeros do cpf')
