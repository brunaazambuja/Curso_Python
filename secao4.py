lista = [1,4,5,32,4]
lista.append(3)
print(lista)
del lista[4:]
print(lista)

lista.sort()
print(lista)
lista.reverse()
print(lista)

lista2 = ["cheur", "abacate", "banana"] #se nao for numerica, ordena a lista alfabeticamente 
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)

dicionario = {"a":"abacate", "b":"bola", "c":"cachorro"} #no dicionario voce localiza seus valores por chaves
print(dicionario["b"]) #imprime o valor correspondente a chave b = bola
for i in dicionario:
    print(i + "-" + dicionario[i])

arquivo = open("arquivo.txt")
linhas = arquivo.readlines() #le tudo do arquivo e armazena as linhas em uma lista
print(linhas)

for linha in linhas:
    print(linha)

print("------")

texto_completo = arquivo.read()
print(texto_completo)


w = open("arquivo.txt", "w")
w.write("Meu nome é Bruna Azambuja\n")
w.close()

#FUNCOES: --- devem ser declaradas antes da chamada das mesmas

def funcao(parametro1, parametro2):
    return (parametro1 + parametro2)

soma = funcao(-2, 3)
print(soma)

#TRATAMENTO DE EXCECOES:

a = 2
b = 0
try:
    print(a/b)
except:
    print("Não eh permitida divisao por zero!\n")

