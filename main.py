#criar um dicionário
from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Autor": "Lucca",
    "Ano": 2005
}
livro_02: Dict[str, Any] ={
    "Titulo": "Star Wars",
    "Autor": "Dom",
    "Ano": 2001
}

lista_livros = []

lista_livros.append(livro_01)
lista_livros.append(livro_02)

print(lista_livros)

lista_livro_usuario:dict = {
    "livro_01": {"Titulo": "Game of Thrones",
    "Autor": "Lucca",
    "Ano": 2005},

    "livro_02": {
    "Titulo": "Star Wars",
    "Autor": "Dom",
    "Ano": 2001}
}

print(lista_livro_usuario["livro_01"]["Titulo"])

###############################################################

#Informações de um livro
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

############################################################

#Contar ocorrências de caracteres

def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

#outra forma

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)

##############################################################

#Preço total da lista de compras

lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

###############################################################

#Eliminação de Duplicatas
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

#################################################################

#Filtragem de Dados

idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)

###################################################################

#Ordenação Personalizada

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

############################################################

#Divisão de Dados em Grupos

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)

#######################################################

#Atualização de Dados

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)

########################################################

#Fusão de Dicionários

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

