
# Visualização de dados em Python

import matplotlib.pyplot as pyplot

x1 = [1,2,5]
y1 = [6,3,7]

titulo = "Meu primeiro Gráfico!"
eixoX = "Eixo X"
eixoY = "Eixo Y"

# Título
plt.title(titulo)

# Eixos
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.plot(x, y) # gráfico linear
plt.bar(x, y) # gráfico de barras
plt.scatter(x, y) # gráfico de pontos
plt.show()
plt.savefig("figura1.png", dpi = 300)
plt.savefig("figura1.pdf")