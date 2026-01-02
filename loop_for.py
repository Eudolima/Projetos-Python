with open('treino.txt', 'r', encoding='utf-8') as leitura:
    for linha in leitura:
        linha = linha.replace(',', '')
        print(linha)

 
