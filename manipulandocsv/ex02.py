with open('foods.csv', 'r', encoding='utf-8') as arquivo:
    arquivo.__next__()

    dicionario = {}
    for linha in arquivo:
        dados = linha.split(',')
        prato = dados[2].replace('\n,' ' ')

        if prato not in dicionario:
            dicionario[prato] = 1
        else:
            dicionario[prato] += 1
    print(dicionario)


    maior_quantidade = 0
    nome_prato = ''

    for prato, valor in dicionario.items():
        if prato > maior_quantidade:
            maior_quantidade = valor
            nome_prato = prato

print(f'{nome_prato} Quantidade: {maior_quantidade}')


