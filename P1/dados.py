import csv

def acessos():
    X = []
    Y = []

    arq = open('acesso.csv', 'r')
    leitor = csv.reader(arq)

    for acessou_home,acessou_como_funciona,acessou_contato,comprou in leitor:
        if acessou_home != "acessou_home":
            X.append([int(acessou_home), int(acessou_como_funciona), int(acessou_contato)])
            Y.append(int(comprou))

    return X, Y