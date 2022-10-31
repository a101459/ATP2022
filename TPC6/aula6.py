import csv

def leObras(filename):
    file = open(filename,encoding = "UTF8")
    file.readline()

    csv_file = csv.reader(file,delimiter=";")

    lista = []
    for obra in csv_file:
        lista.append(tuple(obra))
    return lista

def tamanhoObras(obras):
    return len(obras)

def imprime (obras):
    print(f'| {"Nome":20} | {"Descrição":25} | {"Ano":8} | {"Compositor":15} |')
    for nome, desc, ano, _, comp, *_ in obras:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |")

def ordem(tuplo):
    return tuplo [0]

def titAno(obras):
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome, ano))

    lista.sort(key=ordem)
    return lista

def titAno2(obras):
    lista = []
    for nome, _, ano, *_ in obras:
        lista.append((nome, ano))

    lista.sort(key= lambda tuplo: tuplo[1])
    return lista

def ordemComp(obras):
    lista = []
    for _, _, _, _, comp, *_ in obras:
        lista.append(comp)

    lista.sort()
    return lista

def distPeriodo(obras):
    dici = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else:
            dici[periodo] = 1
    return dici

def distAno(obras):
    dici = {}
    for _, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano] = dici[ano] + 1
        else:
            dici[ano] = 1
    return dici

def distComp(obras):
    dici = {}
    for _, _, _, _, comp, *_ in obras:
        if comp in dici.keys():
            dici[comp] = dici[comp] + 1
        else:
            dici[comp] = 1
    return dici

import matplotlib.pyplot as plt

def plotDistrib(dist_periodo):
    plt.bar(dist_periodo.keys(), dist_periodo.values())
    plt.xticks([x for x in range(0, len(dist_periodo.keys()))], dist_periodo.keys(), rotation='vertical')
    plt.show()
    return

def plotDistrib1(dist_ano):
    graph = plt.figure(figsize=(30,15))
    plt.bar(dist_ano.keys(), dist_ano.values())
    plt.xticks([x for x in range(0, len(dist_ano.keys()))], dist_ano.keys(), rotation='vertical')
    plt.show()
    return

def plotDistrib2(dist_compositor):
    graph = plt.figure(figsize=(30,15))
    plt.bar(dist_compositor.keys(), dist_compositor.values())
    plt.xticks([x for x in range(0, len(dist_compositor.keys()))], dist_compositor.keys(), rotation='vertical')
    plt.show()
    return

def obrasComp(obras):
    dici = {}
    lista=[]
    for nome, _, _,_,comp, *_ in obras:
        if comp in dici.keys():
            dici[comp].append(nome)
        else:
            dici[comp] = [nome]
    for keys,values in dici.items():
        lista.append([keys] + [values])
    return lista
    