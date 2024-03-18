'''Solicite ao usuário diversos números inteiros (até que seja digitado o número zero). Armazene os
números pares em um arquivo e os números ímpares em outro arquivo.'''

with open('pares.txt', 'w', encoding='utf-8') as arquivo_pares:
    with open('impares.txt', 'w', encoding='utf-8') as arquivo_impares:
        while True:
            numero = int(input("Informe um número: "))
            if numero == 0:
                break
            if numero % 2 == 0:
                arquivo_pares.write(str(numero) + '\n')
            else:
                arquivo_impares.write(str(numero) + '\n')