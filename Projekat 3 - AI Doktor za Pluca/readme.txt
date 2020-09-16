# **Poredjenje Rezultata Razlicitih Modela**

U ovom dokumentu cemo dati pregled razlicitih modela i porediti njihovu uspesnot pri testiranju.

**Kako je Nastao Prototip Model**

Prvi model koji smo napravili je bio sekvencialni (Sequential) model sa dva dvodimenzionalna isprepletena sloja (2D Convolution Layer) sa relu aktivatorom, 2 pool sloja velicine 2x2, jednim izravnavajucim (Flatten) slojem i jednim gustim (Dense) slojem sa sigmoid aktivatorom. Model se pokrenuo sa categorical crossentropy funkcijom gubitka, adam optimizatorom, i pracanje preciznosti funkcijom racunanja kvaliteta modela (metrics = [&#39;accuracy&#39;]).

![](RackMultipart20200916-4-17giowg_html_40cc04f0bc8d3161.png)

Slika 1. Prvi prototip modela

Da bi smo doboli najoptimalnije rezultate, provukli smo ga kroz 3 for petlje, menjajuci broj slojeva za svaki sloj u svakoj petlji.

![](RackMultipart20200916-4-17giowg_html_ffe2f3153abf2d4a.png)

Slika 2. Primer par modela nastalih tokom petlje iz gornjeg pasusa

Sve kombinacije modela su prvo testirane u 2 epohe (Epoch)

Za model sa 0 dense slojeva, 32 nodes i 1 conv sloj,
 Posle prve epohe : loss: 1.1279, accuracy: 0.7305, val\_loss: 0.4849, val\_accuracy: 0.7958
 Posle druge epohe: loss: 0.3876, accuracy: 0.8400, val\_loss: 0.5005, val\_accuracy: 0.7788

Za model sa 0 dense slojeva, 32 nodes i 2 conv slojeva,
 Posle prve epohe : loss: 0.6906, accuracy: 0.7219, val\_loss: 0.5290, val\_accuracy: 0.7543
 Posle druge epohe: loss: 0.4883, accuracy: 0.7965, val\_loss: 0.5098, val\_accuracy: 0.7750

Za model sa 0 dense slojeva,32 nodes i 3 conv slojeva,
 Posle prve epohe : loss: 0.6922, accuracy: 0.7072, val\_loss: 0.5050, val\_accuracy: 0.7826
 Posle druge epohe: loss: 0.4884, accuracy: 0.7917, val\_loss: 0.4616, val\_accuracy: 0.7996

Za model sa 0 dense slojeva,64 nodes i 1 conv sloj,
 Posle prve epohe : loss: 1.1844, accuracy: 0.7244, val\_loss: 0.5493, val\_accuracy: 0.7580
 Posle druge epohe: loss: 0.3973, accuracy: 0.8343, val\_loss: 0.5036, val\_accuracy: 0.7902

**Radi lakse citljivosti, stavicu ostale u tabelu**

Za 0 dense slojeva:

| **X** | **1 Conv** | **2 Conv** | **3 Conv** |
| --- | --- | --- | --- |
| **32 Nodes** | L:0.39 A: 0.84 VL: 0.50 VA: 0.78 | L: 0.49 A: 0.80 VL: 0.51 VA: 0.77 | L: 0.49 A: 0.79 VL: 0.46 VA: 0.80 |
| **64 Nodes** | L: 0.40 A: 0.83 VL: 0.50 VA: 0.79 | L: 0.48 A: 0.80 VL: 0.51 VL: 0.78 | L: 0.52 A: 0.78 VL: 0.46 VA: 0.79 |
| **128 Nodes** | L: 0.43 A: 0.82 VL: 0.54 VA: 0.77 | L: 0.47 A: 0.80 VL: 0.51 VA: 0.77 | L: 0.51 A: 0.78 VL: 0.47 VA: 0.78 |

L=loss, A= accuracy, VL= val\_loss, AL= val\_accuracy

Za 1 dense sloj:

| **X** | **1 Conv** | **2 Conv** | **3 Conv** |
| --- | --- | --- | --- |
| **32 Nodes** | L:0.47 A: 0.80 VL: 0.49 VA: 0.79 | L: 0.50 A: 0.78 VL: 0.51 VA: 0.78 | L: 0.50 A: 0.78 VL: 0.54 VA: 0.77 |
| **64 Nodes** | L: 0.41 A: 0.83 VL: 0.49 VA: 0.79 | L: 0.46 A: 0.80 VL: 0.51 VL: 0.79 | L: 0.48 A: 0.79 VL: 0.55 VA: 0.78 |
| **128 Nodes** | X | X | X |

L=loss, A= accuracy, VL= val\_loss, AL= val\_accuracy

Prateci patern smanjivanja preciznosti, odlucili smo da testiramo samo samo 128 nodes 1 conv model za 2 dense modele, koji je vraio L: 0.41 A: 0.82 VL: 0.51 VA: 0.76 kao rezultat.

Odabrali smo 0 dense, 32 nodes, 1 conv za najbolji model, i gledali kako broj epoha (epoch) utice na njega

| **Broj epoha** | **loss** | **accuracy** | **val\_loss** | **val\_accuracy** | **% tacnosti na testu** |
| --- | --- | --- | --- | --- | --- |
| **1** | 1.1297 | 0.7354 | 0.4790 | 0.7921 | 54.8% |
| **2** | 0.4004 | 0.8301 | 0.4663 | 0.8091 | 52.4% |
| **3** | 0.2237 | 0.9121 | 0.5870 | 0.7694 | 63.8% |
| **5** | 0.1123 | 0.9661 | 0.6508 | 0.7921 | 56.1% |
| **10** | 0.0019 | 1.0000 | 1.0245 | 0.7921 | 63.9% |
| **20** | 0.000106 | 1.0000 | 1.2167 | 0.7826 | 58.8% |

\*Test iz poslednjeg reda je radjen na podacima koje smo dobili na e-nastavi
