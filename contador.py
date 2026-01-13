def repetir_mensagem(texto, limite):
    contador = 1
    while contador <= limite:     
        print(f'Repetição {contador}: {texto}')
        contador += 1

repetir_mensagem('Olá, Mundo!', 3)
   