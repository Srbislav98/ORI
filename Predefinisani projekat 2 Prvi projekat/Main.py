import numpy as np
import csv
from Kartica import Kreditna_Kartica


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


    
    max_value = np.max(listaBALANCE)
    print('Maximum value of the array is',max_value)