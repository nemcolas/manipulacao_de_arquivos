'''Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada
linha).'''

with open('numeros.txt', 'w', encoding='utf-8') as arquivo:
    for i in range(10):
        numero = int(input("Informe um número: "))
        arquivo.write(str(numero) + '\n')