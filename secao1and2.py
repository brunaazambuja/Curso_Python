"""
isto eh um comentario, lembrar que nao pode ter acentos em comentarios, pois da syntaxError
inclusive acentos nas mensagens printadas, da syntaxError
"""

print("Hello World!")
print(2 ** 3) # para a operacao matematica de exponenciacao devemos usar **

x = 3
y = 2
z = 10

if x <= y or x >= z and z == y:
    print("if")
elif x < z:
    
    if y < x:
        print("if dentro do elif")
    else:
        print("else dentro do elif")
    print("elif")

else:
    print("else")


while x < 10:
    print(x)
    x += 3

lista = [0, "ola", 9.90, 23, "lista pode ter qualquer tipo de dado"]
for i in lista:
    print(i)

for i in range(0,10, 2): #vai do 0 ate o 10, de 2 em 2
    print(i)

numero1 = int(input("Digite um inteiro: "))
numero2 = float(input("Digite um ponto flutuante: "))
print(numero1, numero2)

algo = input("Digite algo: ") #deve ser uma string
print(algo)
tamanho = len(algo) # para imprimir o tamanho da string
print(tamanho) 
print(algo[1:3]) # para imprimir apenas parte da string

algo = "Bruna Azambuja  "
print(algo.lower()) #tudo em letras minusculas
print(algo.upper()) #tudo em letras maiusculas
print(algo.strip()) #tira os caracteres especiais no comeco e final da string
print(algo.split()) #separa a string nos espacos em uma lista
print(algo.find("Azambuja")) #retorna a posicao da palavra encontrada, -1 caso nao encontre
print(algo.replace("Bruna", "replace")) #substitui as palavras




