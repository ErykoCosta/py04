lista_numeros: list = [40,50,60,70,0,-4582,1,50]
lista_numeros2: list = [1,2,35,9584,-25,35,95652,9564]

def ordenar_lista_numeros(numeros: list) -> list:

    nova_lista_numeros = numeros.copy()
    for i in range(len(nova_lista_numeros)):
        for j in range(i+1, len(nova_lista_numeros)):
            if nova_lista_numeros[i] > nova_lista_numeros[j]:
                nova_lista_numeros[i], nova_lista_numeros[j] = nova_lista_numeros[j], nova_lista_numeros[i]
    return nova_lista_numeros

nova_lista = ordenar_lista_numeros(lista_numeros)
nova_lista2 = ordenar_lista_numeros(lista_numeros2)
print(nova_lista)
print(nova_lista2)