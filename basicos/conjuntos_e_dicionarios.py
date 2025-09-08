#Exercicio 1
# Este código cria um sistema para adicionar nomes de convidados a um conjunto (set). O usuário pode digitar nomes repetidamente, e quando digitar "sair", o loop é interrompido e todos os nomes únicos são #exibidos. O set automaticamente remove duplicatas.

convidados = set()

while True:
    nome_convidados = input("convidados ")
    if nome_convidados == "sair":
        break
    convidados.add(nome_convidados)

print(convidados)


#Exercicio 2
#Este código compara dois textos e encontra as palavras que aparecem em ambos. Ele converte todo o texto para minúsculas, divide em palavras individuais, transforma em conjuntos para remover duplicatas, e usa a interseção (&) para encontrar palavras comuns.



Texto_1 = "O sol brilha forte no céu azul"
Texto_2 = "O céu azul anuncia um dia de sol intenso"

#.lower Transforma os textos em conjuntos de palavras, todas em minúsculas 
#split divide os texto em palabras
#set olha para ver se tem repeticoes (e remove as repetiocoes)
palavras_1 = set(Texto_1.lower().split())
palavras_2 = set(Texto_2.lower().split())



# Encontra a interseção entre os conjuntos
palavras_comuns = palavras_1 & palavras_2

print("Palavras em comum:", palavras_comuns)


#Exercicio 3
#Compara duas listas de compras usando operações de conjunto. Encontra itens comuns a ambas as listas (interseção) e itens exclusivos de cada pessoa (diferença).

lista_de_laura = set(["leite", "pão", "café", "açúcar"])
lista_de_ana = set(["pão", "café", "biscoito", "chocolate"])

#igualdade entre as listas
itens_comuns = lista_de_laura.intersection(lista_de_ana) 

#diferenca entre as lista 
exclusivos_laura = lista_de_laura.difference(lista_de_ana)
exclusivos_ana = lista_de_ana.difference(lista_de_laura)

print(itens_comuns)
print("Exclusivos de Laura:", exclusivos_laura)
print("Exclusivos de Ana:", exclusivos_ana)


#Exercicios 4
#Verifica se um conjunto de permissões solicitadas é um subconjunto das permissões principais. O código trata entradas do usuário, removendo espaços em branco e convertendo para minúsculas antes da comparação.


permissoes_principais = set(input("Permissões principais: ").strip().lower().split(',')) 

permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(',')) 

for i in range(len(permissoes_principais)):  

    permissoes_principais[i] = permissoes_principais[i].strip() 

for i in range(len(permissoes_solicitadas)):  

    permissoes_solicitadas[i] = permissoes_solicitadas[i].strip() 

subconjunto = permissoes_solicitadas.issubset(permissoes_principais) 

if subconjunto:  

    print("As permissões solicitadas fazem parte das permissões principais.")  

else:  

    print("As permissões solicitadas não fazem parte das permissões principais.") 


#Exercicio 5
#Combina tarefas de duas equipes usando união de conjuntos, permite que o usuário remova uma tarefa específica, e exibe a lista final de tarefas.


equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}  

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}  

tarefas_combinadas = equipe_a.union(equipe_b) 

tarefa_remover = input("Tarefa a ser removida: ").lower()  

if tarefa_remover in tarefas_combinadas:  

    tarefas_combinadas.remove(tarefa_remover) 

print(f"Tarefas finais: {tarefas_combinadas}")


#Exercicio 6
#Cria um dicionário de produtos onde as chaves são os nomes dos produtos e os valores são as quantidades em estoque. Coleta dados do usuário para 3 produtos.

dicionario_produtos = {} 

for i in range(3): 

    nome = input("Digite o nome do produto: ") 

    quantidade = int(input("Digite a quantidade: ")) 

    dicionario_produtos[nome] = quantidade 

print(f"Dicionário de produtos: {dicionario_produtos}")


#Exercicio 7
#Permite atualizar a quantidade de um item específico no dicionário de estoque. Verifica se o item existe antes de tentar atualizá-lo e exibe o estoque completo após a operação.

estoque = {
    "Caderno universitário": 50,
    "Caneta azul": 120,
    "Borracha branca": 30
}

item_escolhido = input("Qual item você deseja atualizar? ")

if item_escolhido in estoque:
    novo_valor = int(input(f"Digite a nova quantidade para '{item_escolhido}': "))
    estoque[item_escolhido] = novo_valor
    print("\nEstoque atualizado:")
else:
    print("\nItem não encontrado no estoque.")

for item, quantidade in estoque.items():
    print(f"{item}: {quantidade}")



#Exercicio 8
#Exibe separadamente os nomes e idades dos participantes de um dicionário. Usa os métodos .keys() para acessar as chaves (nomes) e .values() para acessar os valores (idades).

participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 
} 

print(f"Nomes dos participantes: {', '.join(participantes.keys())}")
print(f"Idades dos participantes: {', '.join(str(idade) for idade in participantes.values())}")


#Exercicio 9
#Gerencia participantes de workshops organizados em um dicionário onde cada workshop é uma chave com um conjunto de participantes. Permite remover um nome de todos os workshops simultaneamente.

participantes = { 
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 
} 

# Mostrar os participantes
print("Participantes antes da remoção:")
for workshop, nomes in participantes.items():
    print(f"{workshop}: {', '.join(nomes)}")

nome_remover = input("\nDigite o nome que deseja remover da lista: ")

# Verifica e remove o nome de todos os workshops
foi_removido = False
for nomes in participantes.values():
    if nome_remover in nomes:
        nomes.discard(nome_remover)
        foi_removido = True


# Mostrar os participantes após a remoção
print("\nParticipantes atualizados:")
for workshop, nomes in participantes.items():
    print(f"{workshop}: {', '.join(nomes)}")
    

#Exercicio 10
#Calcula o valor total de vendas por categoria a partir de uma estrutura de dados complexa. O dicionário principal tem categorias como chaves, e cada categoria contém uma lista de dicionários com detalhes dos produtos vendidos. O código soma o valor total (quantidade × valor unitário) para cada categoria.

vendas = { 
    "Eletrônicos": [ 
        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000}, 
        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500} 
    ], 
    "Eletrodomésticos": [ 
        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000}, 
        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800} 
    ], 
    "Livros": [ 
        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50}, 
        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100} 
    ] 
}



for categoria, produtos in vendas.items():
    total_categoria = 0
    for produto in produtos:
        total_categoria += produto["quantidade"] * produto["valor_unitario"]
    
    print(f"- {categoria}: R$ {total_categoria:.2f}")