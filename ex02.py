'''Abra o arquivo de texto criado no exercício anterior. Leia o conteúdo do arquivo e mostre o somatório
de todos os números contidos no arquivo.
'''

with open('numeros.txt', 'r', encoding='utf-8') as arquivo:
    soma = 0
    for linha in arquivo:
        soma += int(linha)
    print(f'A soma dos números é {soma}')