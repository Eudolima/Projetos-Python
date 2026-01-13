def cronometro(segundos):
    while segundos > 0:
        print(f'Tempo restante: {segundos} segundos')
        segundos -= 1
    print('⏰ Tempo esgotado!')

cronometro(5)