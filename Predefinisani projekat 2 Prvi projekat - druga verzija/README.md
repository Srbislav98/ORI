# Pokretanje programa
Pokrenuti virtualni interpreter:<br />
*venv\Scripts\activate.ps1*<br />
Udji u folder src i pokrenuti program:<br />
*python credit_card.py*<br/>
# Objašnjenje kako smo uradili
U ovom projektu korišćen je K-means algoritam kako bi se grupisali korisnici koji imaju slično ponašanje.<br />
Za određivanje optimalnog broja klastera korišćena je metoda lakta.<br />
Prilikom grupisanja korisnika, izostavili smo CUSTID pošto je identifikacija korisnica i ne znači nam ništa.<br />
Odredili smo da postoje tri grupe tj. tri klastera i oni su:<br />
# Klaster 1-Studenti
Nemaju puno novca na racunu, normalno kupuju, duplo vise na rate nego odjednom,veoma rijetko uplacuju unaprijed<br/>
# Klaster 2-Radna klasa
Imaju dosta novca na racunu, normalno kupuju, isto i na rate i odjednom,stedljivi<br/>
# Klaster 3-Sopingholicari
Imaju najvise novca na racunu, cesto kupuju u velikim iznosima, isto i na rate i odjednom<br/>
