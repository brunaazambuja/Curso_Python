#exercicio 1:
""" 
escreva um programa que resolva uma equação de segundo grau
"""
"""
from math import sqrt


a = float(input("Digite os valores das constantes A, B e C da equacao de segundo grau: "))
b = float(input())
c = float(input())

delta = sqrt(b**2 - 4*a*c)
resultado1 = (delta - b)/(2*a)
resultado2 = (- delta - b)/(2*a)
print("O resultado eh: %f" %resultado1)
print(" e %f" %resultado2)
"""
#exercicio 2:
""" 
ordene uma lista usando selection sort
"""
lista = [3,5,7,2,5,1,6]

for i in range(len(lista)):
    
    menor = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    
    aux = lista[i]
    lista[i] = lista[menor]
    lista[menor] = aux

print(lista)    

#exercicio 3:
""" 
programa que recebe dois números e um sinal e faca a operacao
"""
num1 = float(input("Digite o primeiro numero: "))
sinal = input("Digite a operacao: ")
num2 = float(input("Digite o segundo numero: "))

if sinal == "+":
    print(num1+num2)
elif sinal == "-":
    print(num1-num2)
elif sinal == "*":
    print(num1*num2)
elif sinal == "/":
    print(num1/num2)
else:
    print("Uma falha aconteceu!")

