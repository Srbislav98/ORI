import numpy as np
import csv



if __name__ == '__main__':
    kratko = open('credit_card_data.csv', encoding='utf-8')
    reader = csv.reader(kratko)
    listaBALANCE = []
    
    for row in reader:


    max_value = np.max(arr)
    print('Maximum value of the array is',max_value)