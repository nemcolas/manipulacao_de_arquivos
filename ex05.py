'''Faça um programa que abra os dois arquivos criados no exercício anterior e copie-os para um novo
arquivo, colocando-os em ordem crescente.
'''

with open('pares.txt', 'r', encoding='utf-8') as arquivo_pares:
    with open('impares.txt,', 'r' encoding = 'utf-8') as arquivos_impar:
        with open('crescente.txt', 'w', encoding='utf-8') as arquivo_crescente:
