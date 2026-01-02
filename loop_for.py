class Elemento:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos

canal_lancode = Elemento('Lan Code', 'Códigos e gatos', 34000)
canal_eudo = Elemento('Suporte', 'telefones', 2500)

print(canal_lancode.nome)
print(canal_eudo.descricao)

 
