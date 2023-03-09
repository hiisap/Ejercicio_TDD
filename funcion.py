"""
Your module description
"""

def menor(lista):
    menor = lista[0]
    for a in lista:
        if a < menor:
            menor=a
    return menor
    
numeros = [2,31,8,4,1]

print(menor(numeros))