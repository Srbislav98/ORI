from __future__ import print_function
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kmeans import KMeans as KMeans2
from sklearn.decomposition import PCA
import pandas as pd


# --- UCITAVANJE I PRIKAZ IRIS DATA SETA --- #
podaci= pd.read_csv('../data/credit_card_data.csv')
#id je nebitan a i sadrzi tekst
podaci.drop('CUST_ID', axis=1,inplace=True)
# neke vrijednosti ne postoje pa su dodate median vrijednosti tih podataka na tu vrijednost
podaci['BALANCE'].fillna(podaci['BALANCE'].median(), inplace=True)
podaci['BALANCE_FREQUENCY'].fillna(podaci['BALANCE_FREQUENCY'].median(), inplace=True)
podaci['PURCHASES'].fillna(podaci['PURCHASES'].median(), inplace=True)
podaci['ONEOFF_PURCHASES'].fillna(podaci['ONEOFF_PURCHASES'].median(), inplace=True)
podaci['INSTALLMENTS_PURCHASES'].fillna(podaci['INSTALLMENTS_PURCHASES'].median(), inplace=True)
podaci['CASH_ADVANCE'].fillna(podaci['CASH_ADVANCE'].median(), inplace=True)
podaci['PURCHASES_FREQUENCY'].fillna(podaci['PURCHASES_FREQUENCY'].median(), inplace=True)
podaci['ONEOFF_PURCHASES_FREQUENCY'].fillna(podaci['ONEOFF_PURCHASES_FREQUENCY'].median(), inplace=True)
podaci['PURCHASES_INSTALLMENTS_FREQUENCY'].fillna(podaci['PURCHASES_INSTALLMENTS_FREQUENCY'].median(), inplace=True)
podaci['CASH_ADVANCE_FREQUENCY'].fillna(podaci['CASH_ADVANCE_FREQUENCY'].median(), inplace=True)
podaci['CASH_ADVANCE_TRX'].fillna(podaci['CASH_ADVANCE_TRX'].median(), inplace=True)
podaci['PURCHASES_TRX'].fillna(podaci['PURCHASES_TRX'].median(), inplace=True)
podaci['CREDIT_LIMIT'].fillna(podaci['CREDIT_LIMIT'].median(), inplace=True)
podaci['PAYMENTS'].fillna(podaci['PAYMENTS'].median(), inplace=True)
podaci['MINIMUM_PAYMENTS'].fillna(podaci['MINIMUM_PAYMENTS'].median(), inplace=True)
podaci['PRC_FULL_PAYMENT'].fillna(podaci['PRC_FULL_PAYMENT'].median(), inplace=True)
podaci['TENURE'].fillna(podaci['TENURE'].median(), inplace=True)

# --- ODREDJIVANJE OPTIMALNOG K --- #
"""
plt.figure()
sum_squared_errors = []
for n_clusters in range(1, 10):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(podaci)
    #sse = kmeans.sum_squared_error()
    sum_squared_errors.append(kmeans.inertia_)

plt.plot(range(1,10),sum_squared_errors)
plt.xlabel('# of clusters')
plt.ylabel('SSE')
plt.show()
"""
pca = PCA(n_components=2)
#Vazno
transformisaniPodaci = pca.fit_transform(podaci)
plt.figure()
sum_squared_errors = []
for n_clusters in range(1, 10):
    kmeans2 = KMeans2(n_clusters=n_clusters, max_iter=100)
    kmeans2.fit(transformisaniPodaci)
    sse = kmeans2.sum_squared_error()
    sum_squared_errors.append(sse)

plt.plot(range(1,10), sum_squared_errors)
plt.xlabel('# of clusters')
plt.ylabel('SSE')
plt.show()

# --- INICIJALIZACIJA I PRIMENA K-MEANS ALGORITMA --- #
#brojKlastera = eval(raw_input('Unesite broj klastera:'))
brojKlastera=3
kmeans = KMeans(n_clusters=brojKlastera)
rez=kmeans.fit_predict(podaci)
pca = PCA(n_components=2)
#Vazno
transformisaniPodaci = pca.fit_transform(podaci)
#---
skaliraniPodaci = pd.DataFrame(data=transformisaniPodaci, columns=['x_axis', 'y_axis'])

kmeans2 = KMeans2(n_clusters=brojKlastera, max_iter=100)
kmeans2.fit(transformisaniPodaci, normalize=True)
colors = {0: 'red', 1: 'green', 2:'blue'}
markeri = {0: '*', 1:'+',2: 'X' }
plt.figure()
for idx, cluster in enumerate(kmeans2.clusters):

    plt.scatter(cluster.center[0], cluster.center[1], c='black', marker=markeri[idx], s=200)  # iscrtavanje centara
    for tacka in cluster.data:  # iscrtavanje tacaka
        plt.scatter(tacka[0], tacka[1], c=colors[idx])

plt.xlabel('X osa')
plt.ylabel('Y osa')

plt.show()

podaci['KLASTER']=rez

print("UKUPNI PODACI-sr. vrednosti")
print(podaci.mean(axis=0))
print("UKUPNI PODACI-min vrednosti")
print(podaci.min(axis=0))
print("UKUPNI PODACI-max vrednosti")
print(podaci.max(axis=0))

klaster1=podaci.loc[podaci['KLASTER']==0]
print("KLASTER 1")
print(klaster1.mean(axis=0))

klaster2=podaci.loc[podaci['KLASTER']==1]
print("KLASTER 2")
print(klaster2.mean(axis=0))

klaster3=podaci.loc[podaci['KLASTER']==2]
print("KLASTER 3")
print(klaster3.mean(axis=0))

