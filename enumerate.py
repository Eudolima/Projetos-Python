def listar_tarefas(tarefas):
    print('📋 Sua lista de afazeres:')
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f'{indice}. {tarefa}')

tarefas = ['Estudar Python', 'Fazer exercícios', 'Ler um livro', 'Praticar programação']
listar_tarefas(tarefas)