import copy

import numpy as np
import csv
from Kartica import Kreditna_Kartica
import matplotlib.pyplot as plt

def slicno(broj, broj2, koliko):
    temp = broj + koliko
    temp2 = broj - koliko
    if broj2<temp and broj2>temp2:
        return True
    else:
        return False

if __name__ == '__main__':
    kratko = open('credit_card_data.csv', encoding='utf-8')
    reader = csv.reader(kratko)
    listaCUSTID = []
    listaBALANCE = []
    listaBALANCEFREQUENCY   = []
    listaPURCHASES  = []
    listaONEOFFPURCHASES  = []
    listaINSTALLMENTSPURCHASES  = []
    listaCASHADVANCE  = []
    listaPURCHASESFREQUENCY  = []
    listaONEOFFPURCHASESFREQUENCY  = []
    listaPURCHASESINSTALLMENTSFREQUENCY  = []
    listaCASHADVANCEFREQUENCY  = []
    listaCASHADVANCETRX  = []
    listaPURCHASESTRX  = []
    listaCREDITLIMIT  = []
    listaPAYMENTS  = []
    listaMINIMUM_PAYMENTS  = []
    listaPRCFULLPAYMENT  = []
    listaTENURE  = []
    listaSvega = []

    for row in reader:
        if row[0] == "CUST_ID":
            continue
        else:
            listaCUSTID.append(row[0])
            listaBALANCE.append(float(row[1]))
            listaBALANCEFREQUENCY.append(float(row[2]))
            listaPURCHASES.append(float(row[3]))
            listaONEOFFPURCHASES.append(float(row[4]))
            listaINSTALLMENTSPURCHASES.append(float(row[5]))
            listaCASHADVANCE.append(float(row[6]))
            listaPURCHASESFREQUENCY.append(float(row[7]))
            listaONEOFFPURCHASESFREQUENCY.append(float(row[8]))
            listaPURCHASESINSTALLMENTSFREQUENCY.append(float(row[9]))
            listaCASHADVANCEFREQUENCY.append(float(row[10]))
            listaCASHADVANCETRX.append(float(row[11]))
            listaPURCHASESTRX.append(float(row[12]))
            if row[13] == "":
                row[13] = 0
            listaCREDITLIMIT.append(float(row[13]))
            listaPAYMENTS.append(float(row[14]))

            if row[15]=="":
                row[15]=0
                listaMINIMUM_PAYMENTS.append(0)
            else:
                listaMINIMUM_PAYMENTS.append(float(row[15]))

            listaPRCFULLPAYMENT.append(float(row[16]))
            listaTENURE.append(float(row[17]))
            listaSvega.append(Kreditna_Kartica(row[0],float(row[1]),float(row[2]),float(row[3]),float(row[4]),
                                               float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),
                                               float(row[10]),float(row[11]),float(row[12]),float(row[13]),float(row[14]),float(row[15]),
                                               float(row[16]),float(row[17])))

    lista = listaSvega
    temp = [[]]

    for i in range(6):
        k = -1
        if i == 0:
            print("Ova grupa kupuje skupe proizvode i ima veliki limit na kreditnim karticama:\n")
            temp.append([])
            plt.figure("Ova grupa kupuje skupe proizvode i ima veliki limit na kreditnim karticama")
            for j in lista:
                k+=1
                if j.ULISTI:
                    continue
                if j.CREDITLIMIT>=9000 and j.PURCHASES>=4900:
                    temp[0].append(j)
                    plt.scatter(j.PURCHASES, j.CREDITLIMIT)
                    #print(j.To_String())
                    lista[k].ULISTI = True
            plt.xlabel('Celokupna kupovina')
            plt.ylabel('Limit kredita')
            plt.show()
        elif i==1:
            print("Grupa koje kupuje na rate, Koliko cesto to radi:\n")
            temp.append([])
            plt.figure("Korisnici koji često plaćanje preko rate")
            for j in lista:
                k+=1
                if j.ULISTI:
                    continue
                if j.PURCHASESINSTALLMENTSFREQUENCY>=0.70:
                    #print(j.To_String())
                    plt.scatter(j.PURCHASESINSTALLMENTSFREQUENCY, j.INSTALLMENTSPURCHASES )
                    temp[1].append(j)
                    lista[k].ULISTI = True
            plt.xlabel('Koliko često kupuje na rate')
            plt.ylabel('Koliko je platio na rate korisnik')
            plt.show()
        elif i==2:
            print("Grupa koja koristi cash advance dosta:\n")
            temp.append([])
            plt.figure("Korisnici koji često koriste cash advance")
            for j in lista:
                k+=1
                if j.ULISTI:
                    continue
                if j.CASHADVANCEFREQUENCY>=0.70:
                    #print(j.To_String())
                    plt.scatter(j.CASHADVANCEFREQUENCY, j.CASHADVANCE)
                    temp[2].append(j)
                    lista[k].ULISTI = True
            plt.xlabel('Koliko često kupuje preko keša (cash advance)')
            plt.ylabel('Koliko je platio preko cash advance korisnik')
            plt.show()
        elif i==3:
            print("Grupa koja koristi jednokratno cesto:\n")
            temp.append([])
            plt.figure("Korisnici koji često koriste one-off purchase")
            for j in lista:
                k+=1
                if j.ULISTI:
                    continue
                if j.ONEOFFPURCHASESFREQUENCY>=0.70:
                    #print(j.To_String())
                    plt.scatter(j.ONEOFFPURCHASESFREQUENCY, j.ONEOFFPURCHASES)
                    temp[3].append(j)
                    lista[k].ULISTI = True
            plt.xlabel('Koliko često kupuje preko one-off purchase')
            plt.ylabel('Koliko je platio preko one-off korisnik')
            plt.show()
        elif i == 4:
            print("Grupa gde korisnik ima  procenat da uplati na kraticu i Koliko je uplatio:\n")
            temp.append([])
            plt.figure("Korisnik ima određen procenat da uplati na kraticu i Koliko je uplatio")
            for j in lista:
                k+=1
                if j.ULISTI:
                    continue
                if j.PRCFULLPAYMENT>0:
                    #print(j.To_String())
                    plt.scatter(j.PRCFULLPAYMENT, j.PAYMENTS)
                    temp[4].append(j)
                    lista[k].ULISTI = True
            plt.xlabel('Procenat ukupnog iznosa koji korisnik treba da uplati na karticu')
            plt.ylabel('Koliko je uplatio na karticu')
            plt.show()
        elif i == 5:
            print("Ostalo:\n")
            temp.append([])
            for j in lista:
                k += 1
                if j.ULISTI:
                    continue
                temp[5].append(j)
                #print(j.To_String())
                lista[k].ULISTI = True
    for i in temp:
        print(str(len(i)) + "\n")

    """
    plt.figure()
    for i in range(len(listaCUSTID)):
        plt.scatter(listaBALANCE[i], listaPURCHASES[i])
        print("radi!")

    print("Zavrsio je!")
    plt.xlabel('Sepal width')
    plt.ylabel('Petal length')
    plt.show()

    lista = listaSvega
    temp = [[]]
    k = -1
    for i in lista:
        if i.ULISTI:
            continue
        k += 1
        temp.append([])
        temp[k].append(i)
        l = -1
        for j in lista:
            l+=1
            if i.ULISTI:
                continue
            if i.CUSTID == j.CUSTID:
                continue
            if slicno(i.BALANCEFREQUENCY, j.BALANCEFREQUENCY, 0.1):
                if slicno(i.PURCHASESFREQUENCY, j.PURCHASESFREQUENCY, 0.1):
                    if slicno(i.ONEOFFPURCHASESFREQUENCY, j.ONEOFFPURCHASESFREQUENCY, 0.1):
                        if slicno(i.PURCHASESINSTALLMENTSFREQUENCY, j.PURCHASESINSTALLMENTSFREQUENCY, 0.1):
                            if slicno(i.CASHADVANCEFREQUENCY, j.CASHADVANCEFREQUENCY, 0.1):
                                if slicno(i.CASHADVANCETRX, j.CASHADVANCETRX, 2):
                                    if slicno(i.PURCHASESTRX, j.PURCHASESTRX, 3):
                                        if slicno(i.CREDITLIMIT, j.CREDITLIMIT, 1000):
                                            if slicno(i.MINIMUM_PAYMENTS, j.MINIMUM_PAYMENTS, 350):
                                                if slicno(i.PRCFULLPAYMENT, j.PRCFULLPAYMENT, 0.1):
                                                    if slicno(i.TENURE, j.TENURE, 1):
                                                        temp[k].append(j)
                                                        lista[l].ULISTI = True

    for i in temp:
        print("Lista: \n")
        for j in i:
            print(j.To_String())
        print("Kraj liste \n")
    """