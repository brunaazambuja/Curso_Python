
def abre_arquivo():
    fp = open("arquivo.txt")
    print("Arquivo aberto!")
    return fp

def imprime_arquivo(fp):
    linhas = fp.readlines()
    for i in linhas:
        print(i)
    return

while(1):
    op = int(input("Escolha uma opcao:\n (1) le arquivo\n (2) imprimir arquivo\n (3) sair\n"))

    if (op == 1):
        fp = abre_arquivo()
    elif (op == 2):
        imprime_arquivo(fp)
    elif (op == 3):
        break
    else:
        print("Opcao invalida!\n")