# media, mediana e moda

def media(lista):
    soma = 0.0
    for i in range(len(lista)):
        soma += lista[i]
    soma /= float(len(lista))
    return soma

def mediana(lista):
    lista = sorted(lista)
    return lista[int(len(lista)/2)]
        
def moda(lista): #numero que mais se repete na lista

    dic = {}
    for l in lista:
        if l not in dic:
            dic[l] = 1
        else:
            dic[l] += 1

    maior = max(dic.values())

    for i in dic:
        if dic[i] == maior:
            return i
    