def procurar_numero(alvo, limite_maximo):
    print(f'Procurando o número {alvo} até o limite de {limite_maximo}')

    for numero in range(limite_maximo):
        if numero == alvo:
            print(f'Número {alvo} encontrado!')
            break
        print(f'Testando: {numero}...')

    print('Fim da execução')

procurar_numero(5, 10)