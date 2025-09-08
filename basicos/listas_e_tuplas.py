# .append() adiciona elementos ao final da lista
#exemplo
#
# lista = [1,2,3]
# lista.append(4)
#
# Resultado 
# [1,2,3,4]


# .insert() coloca um elemento em um posicao especifica
#exemplo
#
# lista = [1,2,3]
# lista.insert(1, 5)
#
# Resultado 
# [1,5,2,3]

#.remove() remove o primeiro elementos encontrado com o valor especificado
#exemplo
#
# lista = [1,2,3,2]
# lista.remove(2)
#
# Resultado 
# [1,3,2]

#.sort() Ordena os elementos da lista em ordem crescente
#exemplo
#
# lista = [3,1,2]
# lista.sort()
#
# Resultado 
# [1,2,3]

#.reverse() reverte a ordem dos elementos da lista
#exemplo
#
# lista = [1,2,3]
# lista.reverse()
#
# Resultado 
# [3,2,1]

#.pop() remove o numero especificado
#exemplo
#
# lista = [1,2,3]
# print(lista.pop(2))
#
# Resultado 
# [1,2]



#Exercicio 1
#Verifica se um item específico está presente na lista da despensa. O usuário digita um item e o programa informa se ele já está disponível ou precisa ser comprado, mostrando a lista completa no final.

despensa = ['leite', 'ovos', 'óleo', "açúcar"]
item = input("Digite o item que você quer verificar: ")

if item in despensa:
    print(f"O item {item} já está disponível na despensa.")
else:
    print(f"O item {item} precisa ser comprado.")
print(despensa)



#Exercicio 2
#Ordena uma lista de notas em ordem crescente usando o método sort(). O resultado é a exibição das notas organizadas do menor para o maior valor.

notas = [60 , 90 , 43 , 52 , 80]
notas.sort()

print(notas)



#Exercicio 3
#Cria uma lista de voluntários através de entrada do usuário. O loop continua até que o usuário digite "sair", adicionando cada nome à lista, que é exibida ao final.

voluntarios = []

while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    voluntarios.append(nome)  

print("\nVoluntários registrados:", voluntarios)



#Exercicio 4
#Combina duas listas de estoque usando o operador de concatenação +. Cria uma nova lista que contém todos os elementos das duas listas originais.

estoque_1 = ["Arroz", "Feijão", "Macarrão"]
estoque_2 =  ["Óleo", "Sal", "Açúcar"]

estoque = estoque_1 + estoque_2 

print(estoque)



#Exercicio 5
#Adiciona um novo convidado à lista existente usando o método append(). O usuário fornece o nome do novo convidado, que é adicionado ao final da lista.

lista_convidados = ["ana", "pedro" , "joao"]

novo_convidado = input("nome do novo convidado que deseja inserir")

lista_convidados.append(novo_convidado)

print(lista_convidados)



#Exercicio 6
#Inverte a ordem dos elementos em uma lista usando o método reverse(). A lista é reorganizada na ordem inversa da original.

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

eventos_registrados.reverse()

print(eventos_registrados)



#Exercio 7
#Realiza duas operações em uma lista: remove um nome específico usando remove() e adiciona um novo nome usando append(). Mostra a lista antes e depois das modificações.

lista_atualizada = ['Ana', 'João', 'Pedro']
print(lista_atualizada)

remover_nome = input("escreva o nome que deseja remover da lista")
lista_atualizada.remove(remover_nome)

adicionar_nome = input("escreva o nome que deseja adicionar a lista")
lista_atualizada.append(adicionar_nome)

print(lista_atualizada)

#Exercicio 8
#Remove o último elemento de uma lista usando o método pop() sem parâmetros. Remove "Sobremesa" da lista de pedidos.

pedidos_feitos = ["Sanduíche", "Suco", "Sobremesa"]

pedidos_feitos.pop()

print(pedidos_feitos)



#Exercicio 9
#Calcula a média aritmética de três notas fornecidas pelo usuário. Converte as entradas para float, soma as três notas e divide por 3 para obter a média.

nota1 = float(input("nota do aluno"))
nota2 = float(input("nota do aluno"))
nota3 = float(input("nota do aluno"))

media = nota1 + nota2 + nota3

media = media/3

print(media)



#Exercicio 10
#Processa dados de alunos em um formato específico. O usuário digita os dados separados por vírgula, o código divide a string em uma lista e percorre os dados em grupos de três elementos (nome, idade, nota), convertendo e exibindo cada informação formatada.

dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")

for i in range(0, len(dados), 3):
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")

    