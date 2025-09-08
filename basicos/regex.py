#Exercicio 1
#Recebe o nome de um produto do usuário e converte para letras minúsculas usando o método .lower(). O f-string (f antes das aspas) permite inserir variáveis diretamente no texto.


#lower() {o lower deixa a toda a string em minusculo}
#("f") esse F serve para que possa aparecer a variavel dentro do print
produto = input("nome do produto: ")
produto_lower = produto.lower()

print(f"o nome do produto e {produto_lower}")



#Exercicio 2
#Coleta nome e cidade do usuário e exibe uma mensagem personalizada usando f-string para incorporar as variáveis diretamente no texto de saudação.

nome = input("digite seu nome: ")
cidade = input("digite a sua cidade:")

print(f"Ola, {nome}! Bem-Vinda ao sistema da cidade de {cidade}")



#Exercicio 3
#Usa slicing de strings para extrair as 3 primeiras letras ([:3]) e as 3 últimas letras ([-3:]) de uma senha. Demonstra como acessar partes específicas de uma string.


#esse simbolo depois de senha [] serve para que possa escolher ate qual caracter que eu quero que salve na minha nova variavel parte 1
#eu uso [:3] para pegar as 3 primeiras letras da variavel/ [-3:] para pegar as 3 ultimas da variavel 

senha = input("Crie uma senha com mais de 8 caracteres")

parte1 = senha[:3]
parte2 = senha[-3:]

print(f"as 3 primeiras letras da sua senha sao {parte1}")
print(f"as 3 ultimas letras da sua senha sao {parte2}")



#Exercicio 4
#Valida uma URL verificando se começa com "https://" (usando .startswith()) e termina com ".com" (usando .endswith()). Ambas as condições devem ser verdadeiras (operador and).


#utilizo o "startswith" para checar se a variavel que meu usuario colocou inicia com o dominio que eu quero
#utilizo o "endswith" para checar se a variavel termina com o que eu quero
#entre esse 2 termos coloco o "and" porque preciso que essa duas exigencias sejam atendidas

URL = input("digite aqui sua URL: ")

if URL.startswith("https://") and URL.endswith(".com"):
    print("sua URL e valida")
else:
    print("sua URL e invalida")



#Exercicio 5 
#Usa expressões regulares (re.findall()) para encontrar sequências de números (\d+) em um texto. O [0] pega a primeira sequência numérica encontrada.


#o "importe re" serve para que o nosso codigo possa carregar a bibilioteca de codigos regulares
#usamos o "re.findall" para vasculhar todos os numeros da string
#(r'\d+') o \d serve para encontrar os numeros na string/ ja o + da permissao que ele pegue mais de um numero na string
#ja o [0] serve para pegar a primeira sequencia de numero que aparece na string

import re

texto = input("digite a sua receita: ")
numero_receita = re.findall(r'\d+', texto)[0]

print(f"A receita {numero_receita} foi enviada pelo cliente")

#Exercicio 6
#Substitui uma palavra específica em um texto usando re.sub(). O \b garante que só substitua palavras completas (não partes de palavras). Usa rf-string para combinar raw string com variáveis.


#re.sub serve para substituir uma ocorrencia do padro por uma string 
#re.sub (r"\d+", "#", os numero sao 1234) repostas ---> os numeros sao ####

#rf combinacao desses 2
#r: Cria uma raw string, onde caracteres especiais, como barras invertidas, são interpretados literalmente.
#f: Permite usar variáveis dentro da string, com o formato {}.

import re

historia = input("escreva sua frase aqui: ")
palavra = input("qual palavra voce quer substituir? ")
palavra_nova = input("qual e a palavra voce deseja colocar no lugar? ")

historia = re.sub(rf'\b{palavra}\b', palavra_nova, historia)
print(f"{historia}")

#Exercicio 7
#Valida um nome verificando: 1) Primeira letra maiúscula (.isupper()), 2) Sem números, 3) Apenas caracteres alfanuméricos. A versão com regex é mais elegante usando [A-Z] para a primeira letra e [a-z]* para o restante.


#o (.isupper) serve para descobrir se o primeiro digito foi maisculo ou nao
#essa "all(not caractere.isdigit() for caractere in texto)" serve para descobrir se contem algum numero
#e por ultimo "all(caractere.isalnum() for caractere in texto)" essa serve para ver se a algum caracter especial

nome1 = input("seu nome: ")

if nome1[0].isupper() and all(not caractere.isdigit() for caractere in texto) and all(caractere.isalnum() for caractere in texto):
    print("cadastro aprovado")
else:
    print("cadastro negado")

#ou (mais simples)
#re.match serve para procurar palavras que tem certa conexao 
#entao ele usa [A-Z] maisculas para pegar a primeira letra
#e usa [a-z]m minuscula para as outra 
#ele identifica que deve continuar por conta do "*" que serve para ver ocorrencias dos padrao anterior

import re

nome2= input("Digite o nome do cliente para validação: ")  
if re.match(r'[A-Z][a-z]*', nome2):
    print("Nome válido!")
else:
    print("Nome inválido!")



#Exerciocio 8
#Valida o formato de um CPF usando regex. O padrão \d{3}\.\d{3}\.\d{3}\-\d{2} busca: 3 dígitos + ponto + 3 dígitos + ponto + 3 dígitos + hífen + 2 dígitos.


#\d{3}\ para ver a quantidade de caracter que tem a cada parte do cpf
#re.match para ver se esta batendo tudo certinho
#r na frente diz ao python para que ele trate tudo aquilo como uma string bruta


import re

cpf = input("seu cpf: ")

if re.match(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', cpf):
    print("cpf valido")
else:
    print("cpf invalido")

#Exercio 9
#Encontra todas as palavras que começam com uma letra específica usando re.findall(). O [a-zà-ÿ]* inclui letras acentuadas, e re.IGNORECASE torna a busca case-insensitive.


#re.findal serve para encontrar palavras com a letra informada
#re.ignorecase serve para que ele funcione com letras maisculas ou minusculas
#\b{letra}[a-zà-ÿ]* serve para pegar todas as letras sejam elas acentuadas ou nao

import re

livro = input("nome do livro")
letra = input("primeira letra do livro")
palavras = re.findal(rf'\b{letra}[a-zà-ÿ]*', texto, re.IGNORECASE)
print(palavras)



#Exercicio 10 
#Extrai informações específicas de um texto usando grupos de captura com regex. O padrão captura primeiro nome, sobrenome e ano de nascimento (4 dígitos) usando (\w+) para palavras e (\d{4}) para o ano.

#\w+ serve para pegar qualquer alfanumerico ate o primeiro espaco

import re

tudo = input("nome completo e o ano de nascimento")
comp = r' (\w+) (\w+) - (\d{4})'

result = re.search(comp, tudo)

if result:
    primeiro_nome = result.group(1)
    sobrenome = result.group(2)
    ano_nascimento = result.group(3)

    print(f"Primeiro Nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de Nascimento: {ano_nascimento}")
else:
    print("Formato inválido!")


