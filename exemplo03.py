with open('cadastro_alunos.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        rm = int(input("Informe o RM: "))
        if rm == 0:
            break
        nome = input("Informe o nome: ")
        arquivo.write(str(rm) + ' - '  + nome + '\n')
