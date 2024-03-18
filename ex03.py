'''Faça um programa que crie um arquivo de texto denominado “arquivo.txt” e permita que o usuário
grave diversos caracteres nesse arquivo até que seja digitado o caractere “0” (zero).'''

with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        texto = input("Informe o texto: ")
        if texto == '0':
            break
        arquivo.write(texto + '\n')
