Tanulás
=======

Neurális hálózatok egyik legfőbb jellemzője az *adaptáció*\ s, tanulási képesség. Az a tulajdonság, hogy *viselkedésüket* valamely cél elérése érdekében *módosítani képesek*. *Neurális hálózat*\ okban a tanulás egyszerűen a rendszer valamilyen *képesség*\ ének *javítás*\ át jelenti. **Például** olyan paramétereket keresünk, amely mellet egy hálózat adott függvénynél minél jobb approximációjára lesz képes.
Neurális hálózatkoban a tanulás alábbi főbb formái:

	* tanulás tanítóval, *ellenőrzött* vagy felügyelt *tanulás*
	* tanulás tanító nélkül, *nemellenőrzött* vagy felügyelet nélküli *tanulás*
	* *analitikus tanulás*

Ellenőrzött tanulás (supervised learning)
-----------------------------------------

Tanítás azon alapszik, hogy ismertek a hálózatnak valamely *bemenet*\ ekre adandó kivánt válaszai, így a hálózat tényleges *válasz*\ a minden esetben közvetlenül *összehasonlítható* a kívánt válasszal. Az *összehasonlítás eredménye* felhasználható a *hálózat* olyan *módosítás*\ ára, hogy tényleges és a kivánt *válaszok* minél inkább *megegyezzenek*.
Ha *nem ismerjük* pontosan a *választ*, csak azt hogy *helyes vagy hibás*, akkor *megerősítő* (reinforcement) *tanulás*\ nak nevezzük.

1. Tanitóval történő tanítás

A tanítandó rendszer változtatása összetartozó be és kimeneti tanító mintapárok felhasználásával történik (modell-illesztési feladat).

	.. image:: images/learning.jpg
		    :width: 450px
		    :align: center
		    :height: 270px
		    :alt: Learning


**Kritériumfüggvények**:

Neurális hálózatoknál a súlytényezők megfelelő kialakítása a tanítás célja. Jelölések: w\* optimális, w a tényleges súlyvektor, hálózat jósága: C(w\*, w). A kritériumfügvények a hálózat kimenetének és kivánt válasznak (d) valamilyen összehasonlítását végzik: 

	.. math::
		C = f(y, d).

Leggyakoribb a négyzetes hibakritérium, melyet a zaj jelenléte miatt várható értékként értelmezzünk:

	.. math::
	
		C(d,y)=E{((d-y)^T)*(d-y)} = E{\sum_{j}(d_j - y_j)^2}

Előnye:
	* matematikai szempontból kedvező
	* jobban közelítő gradienst kapunk

Regularizáció: A regularizáció eljárás során a kritériumfüggvény egy újabb taggal bővül, és az így kapott eredő kritériumfüggvény minimumát keressük 

	.. math::
		C_r= C + \lambda *C_i

**A modell**:

	* Neurális hálózatokn alkalmazásánál az esetek döntő többségében olyan rendszerekkel állunk szembe, amelyekhez nem illeszthetők paramétereikben lineáris modellek. A szélsőérték-kereső eljárások lineáris modellek esetére vizsgálják.

	* Gradiens alapú szélsőérték-kereső eljárások:

		* A C(w\*, w) kritériumfüggvény minimumát, vagyis azt a **w** értéket keressük, ahol a kritériumfüggvény **w** szerinti gradiense 		zérus:

	.. math::
		\triangledown [C(w)] = \dfrac{\partial C}{\partial w} = 0.

	* LMS algoritmus:
		* Az átlagos négyzetes hiba helyett a pillanatnyi négyzetes hibából indulunk ki.
		* A pillanatnyi gradiens vektorral a "legmeredekebb lejtő" módszert alkalmazva a paraméter változtatás összefüggésére a következőt kapjuk:

		.. math::
			w(k+1)=w(k)-\mu\triangledown C(k)

		* Az LMS eljárás legnagyobb előnye az eddig látott eljárásokkal szemben, hogy alkalmazásához a mintapontokon kívül másra nincs szükség, továbbá, hogy nagyon egyszerűen megvalósítható.

	* Perceptron tanulás
		* LMS eljáráshoz hasonló módszer, alapvetően osztályozási feladatok megoldására szolgál
		* A tanitandó hálózatnak bináris (+1, -1) kimenetei vannak
		* Konvergál, ha lineáris tanítómintákat alkalmazunk
		* Különbség az LMS algoritmushoz képest
			* Az iteráció leáll, ha a tanítóminták szétválasztása befejeződött
			* A paraméterek nagyságát nem korlátozza
		
		.. math::
			w(k+1)=w(k)+\alpha \varepsilon (k)x(k)

2. Megerősitő tanulás

	Számos esetben nem rendelkezünk az adott bemenetekhez tartozó kivánt válaszokkal. Mindössze annyit tudunk, hogy adott bemenetekre a hálózat tényleges válasza helyes vagy hibás. A tanulás eljárása során csak arra elegendő, hogy eldöntsük: szükség van-e a hálózat módosítására vagy sem, de a módosítás mértékenek meghatározására már nem elegendő. A hiba mértéke és a kritériumfüggvény gradiense nem áll rendelkezésünkre.

3. Sztochasztikus szélsőérték-kereső eljárások
	A kedvező konvergencia-sebességet általában csak kvadratikus hibafelület mellet biztosítják, továbbá a minimumhely elérése csak akkor biztos, ha a felületen nincsenek lokális minimumok (unmodális felület).
	
	A lokális minimumok lehetősége fennállhatnak ez konvergencia szempontjából kedvezőtlen. A lokális minimumhelyekben való bennragadás elkerülésére sztochasztikus gradiens eljárásokat dolgoztak ki.

	Jellemzője hogy a kritériumfelületen valamilyen valószínűséggel a felfelé mozgást is megengedik, lehetővé téve a lokális minimumból való kiszabadulást. Gyakorlatban a hálózat súlyaihoz egy valószínűségi változó valamely aktuális értékét adjuk. A zaj felhasználása az egyik módja a súlyok véletlenszerű "megrázása".
	
	.. math::

		\C^~ (w) = C(w) + c(k) * \sum_{i=1}^{N} w_i * n_i(k)

	* Véletlen Keresés

		A paraméterek véletlenszerű megváltoztatásával probálkozunk. Ha egy próbálkozás eredményeképpen kapott paraméterhez tartozó kritériumérték az előző pontbelinél kisebb, az új pontot tekintjük a következő lépés kiinduló pontjának, ellenkező esetben a régi paramétert.

		A véletlen keresési módszer nem feltétlenül konvergálnak a globális minimumhoz.
	* Genetikus algoritmusok

		A természetes szelekciót utánozzák. A genetikus algoritmusok egyszerre több pontokban értékelik a kritériumfelületet. A megoldások egy adott lépésben érvényes halmazát *populáció*\ nak nevezik. Az egymást követő populációkat generációnak nevezik, tehát az algoritmus az egymást követő generációk során egyre jobb megoldás-halmazokat állít elő.

		.. image:: images/generation.png
			:width: 400px
	 		:align: center
	 		:height: 200px
	 		:alt: Generation

		A populáció elemeinek tulajdonságát *kromoszómák*\ kal reprezentálják. A kromoszómák jelenesetben olyan bitfüzérek, amelyekben minden egyes bit egy tulajdonságot reprezentál (1:tulajdonsággal rendelkezik, 0:tulajdonság hiánya).

		Fő jellemzői:

		* Egész paraméter készletekkel dolgozik
		* Keresés során, a megoldások egész halmazát adja meg
		* Csak a kritériumfüggvény egyes értékeit használja
		* Valószínűségi átmenetekkel dolgozik

		Az egymást követő populációk egyre jobb tulajdonságú stringekkel rendelkeznek. A stringhez hozzárendelhetünk egy "jóság" (*fitness*) értéket, ami a string által képviselt kritériumfüggvény értéke.

		A generációk közötti átmeneti operátorok:

		* reprodukció: Egy string a következő generáció részeként is megjelenik. Bekövetkezése a string jóságával kapcsolatos.
		* keresztezés: Két kromoszóma tulajdonságaik keresztezése révén hoznak létre új tulajdonságot.

		.. image:: images/reproduction.png
			:width: 400px
	 		:align: center
	 		:height: 200px
	 		:alt: Reproduction

		* mutáció: Egy string egy bitje véletlenszerűen megváltozik. az új bitkombinációk a megoldás tér olyan területeit is feltérképezhetik, amelyekre az eddigi populációk nem terjedtek ki.

Nemellenőrzött tanulás (unsupervised learning)
----------------------------------------------

*Nem állnak rendelkezésünkre* adott bemenetekhez tartozó kivánt *válaszok*. Nincs vissza jelzés. Azt kell felfederítenünk, hogy van-e a hálózat bemenetére kerülő *adatok*\ ban *hasonlóság*, *korreláció*, *kategoriók* stb.

A hálózat képes önmaga módosítására, emiatt szokás önszervező hálózatoknak (*selforganizing networks*) is nevezni.

1. Hebb tanulás
	Két processzáló elem közötti kapcsolat erőssége (súlytényezők) a processzáló elemek aktivitásának szorzatával arányosan növekszik

	.. math::
		w_ij (k+1) = w_ij (k) + \mu * y_i * y_j

	ahol a w_ij az i-edik és a j-edik processzáló elem közötti súly és a y_i, ill. y_j a két processzáló elem kimenetének értéke. Ha a súly egy bemenet és egy processzáló elem között található

	.. math::
		w_ij (k+1) = w_ij(k) + \mu * x_i * y_j

	Bizonyos hálózatoknál alkalmazzák az anti-Hebb tanulást, amelynél a súlymódosítás hasonló csak negatív előjellel:

	.. math::
		w_ij (k+1) = w_ij(k) - \mu * x_i * y_j

2. Versengő tanulás
	Egy processzáló elem-elrendezésben egy győztest válasszunk ki. A versengő tanulás célja általában a bemeneti mintatér olyan tartoményokra osztása, szegmentálása, hogy minden egyes tartományba tartozó bemenet hatására egy és csakis egy processzáló elem aktivizálódjon.

	A versengő tanulás két lépésből áll:
		* Processzáló elemekből álló kimeneteket meghatározzuk a súlyvektorának felhasználásával.
		* A győztes kiválasztása.

	.. image:: images/competitiv_learning.png
			:width: 300px
	 		:align: center
	 		:height: 200px
	 		:alt: Competitiv
	
	A tényleges tanulás, vagyis a súlyvektor módosítása csak a győztes processzáló elem súlyvektorát módosítjuk.

Analitikus tanulás
------------------

A megfelelő viselkedést biztosító hálózat kialakítása *elméleti út*\ on, a feladatból határozható meg. Valójában ebben az esetben nem is beszélhetünk tanulásról, hiszen a *hálózat* megfelelő *kialakítása analitikus módszerekkel* végezhető el. Azokat a módszereket, amikor valamilyen energiafüggvény felírása képezi a súlyok meghatározásának alapját analitikus tanulásnak nevezzük.

* Hopfield hálózat
	A modell a legegyszerűbb neurális hálózat, amely asszociatív memóriát valósít meg. A hálózatot leggyakrabban autoasszociatív feladatok megoldására használjuk. Ilyenkor a memóriában mintákat, gyakran digitalizált képeket tárolunk. A neurális hálózattól azt várjuk, hogy a tárolt információ zajos, torzított, esetleg hiányos változatának megmutatásakor az eredeti mintára asszociáljon.
	
	.. image:: images/hopfield_net.png
			:width: 350px
	 		:align: center
	 		:height: 200px
	 		:alt: Hopfield