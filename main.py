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
