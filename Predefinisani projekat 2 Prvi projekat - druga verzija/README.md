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
### Klaster 2-Radna klasa
Imaju dosta novca na racunu, normalno kupuju, isto i na rate i odjednom,stedljivi<br/>
### Klaster 3-Sopingholicari
Imaju najvise novca na racunu, cesto kupuju u velikim iznosima, isto i na rate i odjednom<br/>

Eksplorativna analiza podataka:<br/>
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
  
