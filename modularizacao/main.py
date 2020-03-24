import aleatorios as a
import media as m

lista = a.gera_lista(4)
print(lista)

print("A media da minha lista eh: " + str(m.media(lista)))
print("A mediana da minha lista eh: " + str(m.mediana(lista)))
print("A moda da minha lista eh: " + str(m.moda(lista)))