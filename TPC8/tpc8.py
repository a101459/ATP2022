#Questão 1
#Recebe duas strings, _s1_ e _s2_, e retorna o comprimento da substring inicial de _s1_ que não contem nenhum caráter de _s2_

def inicDiferente(s1, s2):
    res = 0
    str1 = []
    str2 = []
    n = 0
    for caracter in s1:
        str1.append(caracter)
    for caracter in s2:
        str2.append(caracter)
    while str1[n] != str2[n]:
        n = n + 1
        res = res + 1
    return res

#Recebe um parâmetro _n_ e lê _n_ números inteiros; no fim retorna quantos dos números lidos são superiores à média dos números lidos

def acimaMedia(n):
    res = 0
    tam = n
    x = 0
    lista = []
    while tam > 0:
        num = int(input("Introduza valor do número"))
        lista.append(num)
        x = x + num
        tam = tam - 1
    media = x/n
    for n in lista:
        if n > media:
            res = res + 1
    return res

#Faz o merge de duas listas ordenadas, retornando uma lista ordenada com os elementos das duas listas

def merge(l1, l2):
    lista = l1 + l2
    tamLista = len(lista)
    listaSort = []
    while len(listaSort) < tamLista:
        menor = lista[0]
        for elem in lista[1:]:
            if elem < menor:
                menor = elem
        listaSort.append(menor)
        lista.remove(menor)
    return print(listaSort)

#Recebe o nome de dois ficheiros de texto, _f1_ e _f2_, e indica se são iguais (__True__) no seu conteúdo ou se são diferentes (__False__)

def figuais(f1, f2):
    txt1 = open(f1, encoding='utf-8')
    txt2 = open(f2, encoding='utf-8')
    listatxtf1 = []
    listatxtf2 = []
    n = 0
    x = True
    for linha in txt1:
        listatxtf1.append(linha)
    for linha in txt2:
        listatxtf2.append(linha) 
    while n < len(listatxtf1):
        if listatxtf1[n] != listatxtf2[n]:
            return False       
        n = n + 1
    return x

#Questão 2

Filme1 = ("Meet the Parents", 2000, ["Ben Stiller","Robert De Niro",
      "Blythe Danner","Teri Polo","Owen Wilson"], ["Comedy", "Drama"])
Filme2 = ("Men of Honor", 2000, ["Robert De Niro","Cuba Gooding, Jr.",
      "Charlize Theron"], ["Biography", "Drama", "Thriller"])
Filme3 = ("Analyze That", 2002, ["Robert De Niro","Billy Crystal",
      "Lisa Kudrow"], ["Comedy"])
CineUM = [Filme1, Filme2, Filme3]

#Devolve uma lista dos atores participantes nos filmes armazenados, ordenada alfabeticamente e sem repetições

def atores(cinemateca):
    Elenco=[]
    for filme in cinemateca:
        _,_,elenco,_ = filme
        for ator in elenco:
            if ator not in Elenco:
                Elenco.append(ator)
    Elenco.sort()
    return Elenco
print("Atores participantes nos filmes armazenados:", atores(CineUM))

#Devolve uma lista de todos os títulos dos filmes, em ordem alfabética, e de um determinado género passado como argumento

def listarPorGenero(cinemateca, genero):
    Genero = []
    for filme in cinemateca:
        tit,_,_,gen = filme
        if genero in gen:
            Genero.append(tit)
    Genero.sort()
    return Genero
print("Filmes de Comédia:", listarPorGenero(CineUM, "Comedy"))

#Devolve o título do filme com o maior elenco

def maiorElenco(cinemateca):
    Atores = 0
    for filme in cinemateca:
        tit,_,elenco,_ = filme
        x = len(elenco)
        if x >= Atores:
            Atores = x
            maiorElenco = tit
    return maiorElenco
print("O filme com o maior elenco é:",maiorElenco(CineUM))

#Calcula a distribuição de filmes por Género

def filmePorGenero(cinemateca):
    distribgenero = {}
    for filme in cinemateca:
        _,_,_,gen = filme
        for genero in gen:
            if genero in distribgenero.keys():
                distribgenero[genero] = distribgenero[genero] + 1
            else:
                distribgenero[genero] = 1
    return distribgenero
print("Distribuição de filmes por género:", filmePorGenero(CineUM))

#Represente num gráfico de barras a distribuição calculada na alínea anterior

import matplotlib.pyplot as plt

def graph(distrib):
    plt.bar(distrib.keys(), distrib.values(), color = ['blue','red', 'orange','yellow'])
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys())
    plt.title("Distribuição dos filmes por género")
    plt.show()
    return
graph(filmePorGenero(CineUM))