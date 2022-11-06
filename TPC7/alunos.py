import csv

def leAlunos(filename):
    f = open(filename, encoding='utf-8')
    f.readline()

    csv_reader = csv.reader(f, delimiter=',')

    lista1 = []
    for aluno in csv_reader:
        lista1.append(tuple(aluno))
    return lista1

Alunos = leAlunos("datasets/alunos.csv")

def distribPorCurso(alunos):
    distCurso = {}
    for aluno in alunos:
            _,_,curso,*_ = aluno
            if curso in distCurso.keys():
                distCurso[curso] = distCurso[curso] + 1
            else:
                distCurso[curso] = 1

    return distCurso

def mediaAluno(alunos):
    lista2 = []
    for id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4 in alunos:
        media = (int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4))/4
        if 1 <= media < 4:
            aluno=(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"E")
        elif 4 <= media < 8:
            aluno=(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"D")
        elif 8 <= media < 12:
            aluno=(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"C")
        elif 12 <= media < 16:
            aluno=(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"B")
        elif 16 <= media <= 20:           
            aluno=(id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,"A") 
        lista2.append(aluno)
    return lista2

def distEscalao(alunos):
    distesc = {}
    for aluno in alunos:
        _, _, _, _, _, _, _, _, escalao = aluno
        if escalao in distesc.keys():
           distesc[escalao] = distesc[escalao]+ 1
        else:
            distesc[escalao] = 1
    return distesc

import matplotlib.pyplot as plt

def grafico(dist):
    plt.bar(dist.keys(), dist.values(), color = "pink", width = 0.4)
    plt.xticks([x for x in range (0, len(dist.keys()))], dist.keys(), rotation = "vertical")
    plt.ylabel("Número de Alunos")
    plt.show()
    return

def tabela(dist):
    for x in dist.keys():
        print(f" {x:^10} | {dist[x]:<5}")
    return

def menu():
    print("""Menu:
(1) Dados dos Alunos    
(1) Número de Alunos por Curso
(2) Média e Escalão dos Alunos
(4) Distribuição de Alunos por Curso
(5) Distribuição de Alunos por Escalão
(6) Gráfico da Distribuição de Alunos por Curso
(7) Gráfico da Distribuição de Alunos por Escalão
(0) Sair""")
    return
