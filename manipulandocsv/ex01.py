'''Exercício 1
Considere que o arquivo “notas.CSV” apresenta uma listagem com os dados dos alunos de uma turma.
Cada linha do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Veja abaixo um exemplo de arquivo de texto nesse formato: 
2101254,Benicio Pires,3.6,10.0,8.5,7,0
2101624,Bruna Goncalves,9.5,8.0,6.0,5.5
2101533,Danilo Jesus,7.8,8.7,6.5,9.0
2101969,Ana Carolina Silva,8.1,7.3,9.2,8.8
Implemente um programa que leia o arquivo indicado e, a partir desse arquivo, gere dois novos 
arquivos:
Arquivo “aprovados.CSV” contendo uma listagem dos alunos aprovados na disciplina, contendo 
RM,NOME,MEDIA do aluno
Arquivo “reprovados.CSV” contendo uma listagem dos nomes dos alunos reprovados na disciplina, 
contendo RM,NOME,MEDIA do aluno.
Para o aluno ser aprovado ele deve ter média igual ou superior a 6.0.'''
notas = open('notas.csv', 'r',encoding='utf-8')
aprovados = open('aprovados.csv', 'w', encoding='utf-8')
reprovados = open('reprovados.csv', 'w', encoding='utf-8')


notas.__next__() #Pula a primeira linha ao ler o arquivo


for linha in nota:
    dados = linha.split(' - ')
    print(dados)
    media = (float(dados[2] + float(dados[3]))) + float(dados[4]) + float(dados[5])/4
    print(media)
    if nota >= 6:
        aprovados.write(dados[0] + ',' + dados[1] + ',' + f'{media.2f}' + '\n')
    else:
        reprovados.write(dados[0] + ',' + dados[1] + ',' + f'{media.2f}' + '\n')



notas.close
aprovados.close
reprovados.close
