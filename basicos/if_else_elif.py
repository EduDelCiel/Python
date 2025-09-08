#Exercicio 1
#Compara as vendas de maçãs e bananas usando estrutura condicional if-elif-else. Verifica qual fruta vendeu mais ou se as vendas foram iguais.

macas = int(input("Digite a quantidade de maçãs vendidas: "))
bananas = int(input("Digite a quantidade de bananas vendidas: "))

if macas > bananas:
    print("As maçãs tiveram mais vendas.")
elif bananas > macas:
    print("As bananas tiveram mais vendas.")
else:
    print("As vendas foram iguais.")


#Exercicio 2
#Calcula o tempo total de um projeto com validação de entrada. Verifica se algum valor é negativo usando operador or antes de somar os dias.

atividade_A = int(input("Informe os dias para a atividade A: "))
atividade_B = int(input("Informe os dias para a atividade B: "))
atividade_C = int(input("Informe os dias para a atividade C: "))

if atividade_A < 0 or atividade_B < 0 or atividade_C < 0:
    print("Erro: Os dias não podem ser negativos.")
else:
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"O tempo total do projeto é de {tempo_total} dias.")



#Exercicio 3
#Sistema de alerta de temperatura. Verifica se a temperatura está acima de 25°C e emite alerta ou mensagem de segurança.


temperatura = float(input("Digite a temperatura atual: "))

if temperatura > 25:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print("Temperatura dentro do limite seguro.")


#Exercicio 4
#Calcula o IMC (Índice de Massa Corporal) e classifica em três categorias: abaixo do peso, peso normal e acima do peso usando if-elif-else.

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")


#Exercicio 5
#Controle de orçamento pessoal. Compara as despesas com um limite pré-definido e alerta se houve ultrapassagem.

limite = 3000.0
despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > limite:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do orçamento.")


#Exercicio 6
#Sistema de controle de acesso baseado no horário. Permite acesso apenas entre 8h e 18h usando operadores de comparação combinados.

hora_atual = int(input("Digite a hora atual (formato 24 horas): "))

if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")

#Exercicio 7
#Sistema de avaliação escolar. Calcula a média e classifica o aluno em aprovado, recuperação ou reprovado com condições específicas.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado")

#Exercicio 8
#Calculadora de pedágio com faixas de preço baseadas na distância percorrida. Usa condições encadeadas para determinar o valor.

distancia = float(input("Digite a distância percorrida (em km): "))

if distancia <= 100:
    print("Valor do pedágio: R$ 10,00")
elif 100 < distancia <= 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 30,00")

#Exercicio 9
#Verificador de paridade. Usa o operador módulo % para verificar se um número é divisível por 2 (par) ou não (ímpar).

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#Exercicio 10
#Sistema de análise de crédito. Verifica dois critérios: renda mínima (R$2000) e parcela não superior a 30% da renda usando operador and.

renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada: "))

if renda > 2000 and parcela <= 0.3 * renda:
    print("Empréstimo aprovado!")
elif renda <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")
