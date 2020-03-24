
lista = [1,4,2,7,6,4]
quadrados = []

for i in range(len(lista)):
    quadrados.append(lista[i]**2)

print(quadrados)

# LIST COMPREHENSION:

#crie uma lista que obtenha o triplo dos valores da outra, porem apenas os numeros impares
lista2 = [1,4,2,7,6,4]
impares = [i*3 for i in lista if (i*3)%2 == 1] # acao, laco de repeticao e condicionamento
print(impares)

# ZIP: 

lista1 = [1, 2, 3, 4, 5]
lista2 = ["bola", "cachorro", "elefante", "arvore", "aviao"]
lista3 = ["dois reais", "quarenta reais", "vinte reais", "zero reais", "mil reais"]
for num, objeto, valor in zip(lista1, lista2, lista3):
    print(str(num) + "-" + str(objeto) + "-" + str(valor))

# MAP:
# recebe uma funcao e um valor para ser aplicado em cada um
def dobro(i):
    return i*2

valor = list(map(dobro, lista1))
print(valor)

# LAMBDA:

#valor = map(Lambda i: i*2, lista1)
#valor = List(valor)
#print(valor)


