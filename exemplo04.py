lista= [{'nome': 'João', 'idade':30, 'altura':1.75 },
              {'nome': 'Nicolas', 'idade':28, 'altura':1.58 },
              {'nome': 'Rafinha', 'idade':28, 'altura':2.90 }]

with open('pessoas.txt', 'w', encoding='utf-8')as arquivo:
    for dicionario in lista:
        arquivo.write(['nome']+ ' - '+ dicionario['idade'] + ' - '+ dicionario['altura'])
