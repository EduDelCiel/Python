#Exercicio 1
# Percorre uma lista de clientes usando um loop for e imprime cada nome individualmente. O loop itera sobre cada elemento da lista, atribuindo-o à variável nome a cada iteração.

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for nome in clientes:
    print(f"{nome}")



#Exercicio 2
# Usa um loop while para processar dados de 1 a 9. O contador inicia em 1 e incrementa a cada iteração até atingir 10, quando o loop termina e exibe a mensagem final.

contador = 1

while contador < 10:
    print(f"Processando dados {contador}")
    contador = contador + 1

print("dados processados")



#Exercicio 3
#Demonstra duas formas de exibir uma mensagem de boas-vindas 5 vezes: usando um loop while com contador e usando um loop for com a função range(5).

contador_bem = 0

while contador_bem < 5:
    print("Bem-vindo ao Buscante!")
    contador_bem += 1

#ou

for i in range(5):
    print("Bem-vindo ao Buscante!")



#Exercicio 4
#Calcula a soma total de valores em uma lista usando um loop for. A variável soma acumula o valor de cada elemento da lista durante as iterações.

valores = [10, 20, 30, 40, 50]

soma = 0

for numero in valores:
    soma += numero

print(f"A soma total das receitas é: {soma}")



#Exercicio 5
#Percorre uma lista de projetos e verifica se algum elemento é None usando is None. Exibe mensagens diferentes para projetos válidos e para valores ausentes (None).

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("projeto ausente")
    else:
        print(f"{projeto}")



#Exercicio 6
#Procura por um livro específico ("O Hobbit") em uma lista. Quando encontra o livro, imprime uma mensagem e usa break para sair do loop imediatamente, sem percorrer os elementos restantes.

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"Livro encontrado: {livro}")
        break



#Exercicio 7
#Simula um processo de vendas onde o estoque diminui a cada venda. O loop while continua enquanto houver estoque, decrementando o contador a cada iteração até chegar a zero.

Contador_estoque = 5

while contador > 0:
    print(f"Venda realizada! Estoque restante: {Contador_estoque}")
    Contador_estoque -= 1

print("esotque esgotado")



#Exercicio 8
#Cria uma contagem regressiva de 10 a 1 segundos, com mensagens diferentes para números pares e ímpares. Mostra duas implementações: uma com while e outra com for usando range(10, 0, -1) para contar decrescentemente.

contador_oportunidades = 10

while contador_oportunidades > 0:
    if contador_oportunidades%2 == 0:
        print(f"Faltam apenas {contador_oportunidades} segundos - Não perca essa oportunidade!")
        contador_oportunidades -= 1
    else:
        print(f"A contagem continua: {contador_oportunidades} segundos restantes.")
        contador_oportunidades -= 1

print("aproveite a promocao")

#ou

for segundos in range(10, 0, -1):  
    if segundos % 2 == 0: 
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else: 
        print(f"A contagem continua: {segundos} segundos restantes.")

print("Aproveite a promoção agora!")



#Exercicio 9
#Percorre uma lista de dicionários representando livros e seus estoques. Usa continue para pular livros com estoque zero, exibindo apenas os livros disponíveis.

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")



#Exercicio 10
# Cria um sistema de cadastro com validação. Usa um loop infinito while True que só é interrompido (break) quando ambos os campos atendem aos requisitos mínimos de tamanho (nome: 5+ caracteres, senha: 8+ caracteres). O continue faz o loop retornar ao início se alguma validação falhar.

#A função len() em Python retorna o número de caracteres de uma string.

while True:
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break