with open ('nomes.txt', 'r', encoding='utf-8') as arquivo:
    lista = []
    for linha in arquivo:
        lista.append(linha.replace('\n',''))

print(lista)


