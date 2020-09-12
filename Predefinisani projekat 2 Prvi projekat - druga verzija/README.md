# Pokretanje programa
Naredne operacije izvršiti u powershell-u.<br />
Pokrenuti virtualni interpreter:<br />
*venv\Scripts\activate.ps1*<br />
Udji u folder src i pokrenuti program:<br />
*python credit_card.py*<br/>
# Objašnjenje kako smo uradili
U ovom projektu korišćen je K-means algoritam kako bi se grupisali korisnici koji imaju slično ponašanje.<br />
Za određivanje optimalnog broja klastera korišćena je metoda lakta.<br />
#### Odbacili smo atribute:
PURCHASE i PURCHASE FREQUENCY pošto imamo posebne načine kupovine, MINIMUM_PAYMENTS pošto ne kontribuira ništa, izostavili smo CUSTID pošto je identifikacija korisnica i ne znači nam ništa i još 5 atributa koji međusobno imaju slične vrednosti pa su uklonjeni.<br />
![Capture](https://user-images.githubusercontent.com/51791214/90976098-917d6700-e53a-11ea-9a7e-1a11822e98dd.PNG)<br />
(Ponekad se dobije malo drugaciji izgled ali vecinom slucaja budu sa 3 klastera)<br/> 
Odredili smo da postoje tri grupe tj. tri klastera i oni su:<br />
### Klaster 1-Studenti
Nemaju puno novca na racunu, normalno kupuju, duplo vise na rate nego odjednom,veoma rijetko uplacuju unaprijed<br/>
<table>
  <tr>
    <th>TIP</th>
  <th>BALANCE</th>
    <th>ONEOFF_PURCHASES</th>
    <th>INSTALLMENTS_PURCHASES</th>
    <th>CASH_ADVANCE</th>
    <th>ONEOFF_PURCHASES_FREQUENCY</th>
    <th>PURCHASES_INSTALLMENTS_FREQUENCY</th>
    <th>CASH_ADVANCE_TRX</th>
     <th>CREDIT_LIMIT</th>
    <th>PAYMENTS</th>
  </tr>
   <tr>
   <th>Srednja vrednost</th>
     <th>860.219644</th>
     <th>321.048980</th>
     <th>297.835035</th>
     <th>494.586902</th>
     <th>0.153346</th>
     <th>0.354902</th>
     <th>2.262298</th>
     <th>2632.523387</th>
     <th>1008.260350</th>
  </tr>
   <tr>
  <th>Minimum</th>
     <th>0</th>
     <th>0</th>
     <th>0</th>
     <th>0</th>
     <th>0</th>
     <th>0</th>
     <th>0</th>
     <th>50</th>
     <th>0</th>
  </tr>
   <tr>
     <th>Maksimum</th>
 <th> 4972.108843</th>
                     <th>8053.950000</th>
               <th>5463.730000</th>
                        <th> 7883.541720</th>
             <th> 1.000000</th>
       <th> 1.000000</th>
                      <th>123.000000</th>
                         <th>7000.000000</th>
                          <th>14229.882480</th>
  </tr>
 </table>
 
### Klaster 2-Radna klasa
Imaju dosta novca na racunu, normalno kupuju, isto i na rate i odjednom,stedljivi<br/>


<table>
  <tr>
    <th>TIP</th>
  <th>BALANCE</th>
    <th>ONEOFF_PURCHASES</th>
    <th>INSTALLMENTS_PURCHASES</th>
    <th>CASH_ADVANCE</th>
    <th>ONEOFF_PURCHASES_FREQUENCY</th>
    <th>PURCHASES_INSTALLMENTS_FREQUENCY</th>
    <th>CASH_ADVANCE_TRX</th>
     <th>CREDIT_LIMIT</th>
    <th>PAYMENTS</th>
  </tr>
   <tr>
   <th>Srednja vrednost</th>
    <th> 3181.064725</th>
                  <th>  961.908376</th>
              <th> 578.423335</th>
                     <th>  1841.554895</th>
           <th> 0.314813</th>
     <th> 0.381484</th>
                       <th>5.172742</th>
                     <th>   8872.859080</th>
                       <th>    2575.054639</th>
  </tr>
   <tr>
  <th>Minimum</th>
    <th> 0.0</th>
                    <th>  0.0</th>
               <th>  0.0</th>
                        <th>  0.0</th>
           <th> 0.0</th>
     <th>  0.0</th>
                    <th>  0.0</th>
                      <th> 3000.0</th>
                            <th>   0.0</th>
  </tr>
   <tr>
<th>Maksimum</th>
     <th> 18495.55855</th>
                 <th>  14215.00000</th>
             <th> 10009.93000</th>
                     <th>   14827.30716</th>
           <th>  1.00000</th>
    <th>   1.00000</th>
              <th>        123.00000</th>
               <th>       30000.00000</th>
                 <th>          12353.26546</th>
  </tr>
 </table>
 
### Klaster 3-Sopingholicari
Imaju najvise novca na racunu, cesto kupuju u velikim iznosima, isto i na rate i odjednom<br/>

<table>
  <tr>
    <th>TIP</th>
  <th>BALANCE</th>
    <th>ONEOFF_PURCHASES</th>
    <th>INSTALLMENTS_PURCHASES</th>
    <th>CASH_ADVANCE</th>
    <th>ONEOFF_PURCHASES_FREQUENCY</th>
    <th>PURCHASES_INSTALLMENTS_FREQUENCY</th>
    <th>CASH_ADVANCE_TRX</th>
     <th>CREDIT_LIMIT</th>
    <th>PAYMENTS</th>
  </tr>
   <tr>
   <th>Srednja vrednost</th>
    <th> 4909.721780</th>
                  <th>   5418.687803</th>
            <th>   2240.561618</th>
               <th>        6753.332289</th>
           <th>   0.441015</th>
     <th>  0.477293</th>
                 <th>     12.687861</th>
               <th>         11872.832370</th>
                <th>           16646.791715</th>
  </tr>
   <tr>
  <th>Minimum</th>
   <th>     4.382924</th>
                    <th>      0.000000</th>
             <th>      0.000000</th>
                <th>              0.000000</th>
           <th>    0.000000</th>
      <th>    0.000000</th>
            <th>              0.000000</th>
         <th>                 1200.000000</th>
            <th>                  7116.531862</th>

  </tr>
   <tr>
<th>Maksimum</th>
 <th>  19043.13856</th>
     <th>               40761.25000</th>
    <th>           22500.00000</th>
             <th>            47137.21176</th>
          <th>  1.00000</th>
  <th>     1.00000</th>
               <th>        123.00000</th>
              <th>           30000.00000</th>
               <th>              50721.48336</th>
  </tr>
 </table>
 
## Ukupni podaci:

<table>
  <tr>
    <th>TIP</th>
    <th>BALANCE</th>
    <th>BALANCE_FREQUENCY</th>
    <th>PURCHASES</th>
    <th>ONEOFF_PURCHASES</th>
    <th>INSTALLMENTS_PURCHASES</th>
    <th>CASH_ADVANCE</th>
    <th>PURCHASES_FREQUENCY</th>
    <th>ONEOFF_PURCHASES_FREQUENCY</th>
    <th>PURCHASES_INSTALLMENTS_FREQUENCY</th>
    <th>CASH_ADVANCE_FREQUENCY</th>
    <th>CASH_ADVANCE_TRX</th>
    <th>PURCHASES_TRX</th>
    <th>CREDIT_LIMIT</th>
    <th>PAYMENTS</th>
    <th>MINIMUM_PAYMENTS</th>
    <th>PRC_FULL_PAYMENT</th>
    <th>TENURE</th>
  </tr>
  <tr>
    <th>Srednja vrednost</th>
    <th>1564.474828</th>
                    <th>  0.877271</th>
                <th>           1003.204834</th>
              <th>      592.437371</th>
           <th>   411.067645</th>
           <th>          978.871112</th>
          <th>          0.490351</th>
         <th>    0.202458</th>
     <th>  0.364437</th>
       <th>          0.135144</th>
        <th>              3.248827</th>
            <th>             14.709832</th>
                <th>        4494.282473</th>
                    <th>        1733.143852</th>
                     <th>844.906767</th>
                   <th>    0.153715</th>
    <th>         11.517318</th>
  </tr>
  <tr>
    <th>Minimalna vrednost</th>
<th>                          0.000000</th>
    <th>               0.000000</th>
        <th>                   0.000000</th>
            <th>       0.000000</th>
      <th>       0.000000</th>
          <th>            0.000000</th>
              <th>   0.000000</th>
   <th>       0.000000</th>
   <th> 0.000000</th>
       <th>        0.000000</th>
           <th>         0.000000</th>
               <th>        0.000000</th>
                   <th>     50.000000</th>
                       <th>     0.000000</th>
   <th>                0.019163</th>
       <th>             0.000000</th>
           <th>                  6.000000</th>
  </tr>
  <tr>
    <th>Maksimalna vrednost</th>
  <th>                      19043.13856
      <th>               1.00000
          <th>             49039.57000
              <th>    40761.25000
<th>            22500.00000
    <th>              47137.21176
        <th>            1.00000
            <th>  1.00000
 <th>   1.00000
     <th>           1.50000
         <th>            123.00000
             <th>         358.00000
                 <th>      30000.00000
                     <th>      50721.48336
        <th>           76406.20752
            <th>           1.00000
                <th>                12.00000
  </tr>
  
  
  <th></th>
  <th></th>
</table>
  
