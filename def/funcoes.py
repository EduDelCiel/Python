#Exercicio 1

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

idade = calcular_idade(ano_nascimento, ano_atual)
print("Sua idade é:", idade)

#Exercicio 2

palavra = input("Digite uma Palavra: ")

def conta_letras(palavra):
    return len(palavra)

tamanho = conta_letras(palavra)
print("A palavra tem", tamanho, "letras.")

#Exercicio 3

horario = int(input("Digite a hora atual (0-23): "))

def ola(horario):
    if 0 <= horario < 12:
        return "Bom dia!"
    elif 12 <= horario < 18:
        return "Boa tarde!"
    elif 18 <= horario < 24:
        return "Boa noite!"
    else:
        return "Hora inválida!"
    
mensagem = ola(horario)
print(mensagem)

#Exercicio 4

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 


def converter_telefones(lista):
   return [int(telefone) for telefone in lista]

def verifica(lista):
    for num in lista:
        if not isinstance(num, int):
            return "Erro na hora de converter"
    return "Todos os números foram convertidos com sucesso"

telefones_convertidos = converter_telefones(telefones)
resultado = verifica(telefones_convertidos)
print(resultado)
print(telefones_convertidos)

#Exercicio 5

valor_das_vendas = input("Digite o valor das vendas: ").split()
total_vendas = sum(map(float, valor_das_vendas))
print("O total das vendas é:", total_vendas)

#Exercicio 6

numbers = [1,2,3,4,5,6,7,8,9,10]

def par(numbers):
    return [num for num in numbers if num % 2 == 0]

def impar(numbers):
    return [num for num in numbers if num % 2 != 0]

print("Números pares:", par(numbers))
print("Números ímpares:", impar(numbers))

#Exercicio 7

produtos = input("Digite os produtos separados por vírgula: ").split(",")
precos = input("Digite os preços separados por vírgula: ").split(",")

for produto, preco in zip(produtos, precos):
    print(f"{produto.strip()}: {preco.strip()}")

#Exercicio 8

numero = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
operacao = input("Digite a operação (+, -, *, /): ")

def calcular(numero, numero2, operacao):
    if operacao == "+":
        return numero + numero2
    elif operacao == "-":
        return numero - numero2
    elif operacao == "*":
        return numero * numero2
    elif operacao == "/":
        return numero / numero2
    else:
        return "Operação inválida!"

resultado = calcular(numero, numero2, operacao)
print("O resultado é:", resultado)

#Exercicio 9

desconto = float(input("Digite o valor do desconto (em %): "))
preco = float(input("Digite o preço do produto: "))

def aplicar_desconto(preco, desconto):
    valor_desconto = preco * (desconto / 100)
    return preco - valor_desconto

preco_com_desconto = aplicar_desconto(preco, desconto)
print("O preço com desconto é:", preco_com_desconto)

#Exercicio 10

numero_recursivo = int(input("Digite um número: "))

def soma_recursiva(n):
   if n == 1:
       return 1
   return n + soma_recursiva(n - 1)

resultado_recursivo = soma_recursiva(numero_recursivo)
print("A soma dos números de 1 até", numero_recursivo, "é:", resultado_recursivo)




