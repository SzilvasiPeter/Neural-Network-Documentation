Backpropagation többrétegű hálózatnál (MLP)
===========================================

Egy processzáló elem szigmoid kimeneti nemlinearitással
-------------------------------------------------------

	.. image:: images/nonlinear_sigmoid.png
			:width: 350px
	 		:align: center
	 		:height: 200px
	 		:alt: Sigmoid

A hálózat felépítését az fenti ábrán láthatjuk. A súlymódosítást az LMS algoritmussal végezzük, a hibát a teljes hálózat kimenetén értelmezzük.

.. math::
	\varepsilon (k) = d(k) - y(k) = d(k) - sgm(s(k)) = d(k) - sgm(w^T (k)x(k))

A pillanatnyi gradiens tehát:

.. math::
	\dfrac{\partial \varepsilon ^2}{\partial w} = 2\varepsilon(-sgm'(s))x

ahol sgm'(s) a kimeneti nemlinearitás deriváltját jelöli.

A logisztikus függvény, ill. deriváltja:

.. math::
	y = sgm(s) = \dfrac{1}{1+e^{-s}},	y' = sgm'(s) = y(1-y)

A backpropagation algoritmus
----------------------------

	.. image:: images/backpropagation.png
			:width: 350px
	 		:align: center
	 		:height: 200px
	 		:alt: Backpropagation

A többrétegű hálózatok felépítése a fenti ábrán követhető. Az ábra egy két aktív régeteg tartalmazó hálózatot mutat, amelyben az első aktív rétegben - a rejetett rétegben - három, a második aktív rétegben - jelen esetben a kimeneti rétegben - két processzáló elem található. A hálózat tehát egy többrétegű előrecsatolt hálózat(FeedForward). A súlyvektorok meghatározása gradiens alapú ellenőrzött tanuló eljárással, tehát összetartozó (x,y) tanító párok felhasználásával történik.

A tanító eljárás bemutatásához vezessük be a következő jelöléseket: legyen *l* a réteg index, *i* a rétegen belüli processzáló elem (PE) indexe, *j* a PE bemeneteit megkülönböztető index - ez lesz egyben a megfelelő súlyvektor komponenseinek indexe -  ez lesz egyben a megfelelő súlyvektor komponenseinek indexe is - és *k* a diszkrét időindex.(pl. PE_i^(l) az l-edk réteg i-edik processzáló elemét jelöli, w_i^(l) (k) pedig az *l*-edik réteg, *i*-edik prcesszáló elemének súlyvektorát a *k*-adik időpillanatban és w_ij^(l) (k) ugyanezen súlyvektornak a j-edik komponensét jelöli.)

A hálózat tanítását két (aktív) rétegű hálózaton mutatjuk be. A kimenet hiba:

.. math::
	\varepsilon ^2 = \varepsilon_1^2 + \varepsilon_2^2 = (y_1 - d_1)^2 + (y_2 - d_2)^2

A súly módosításhoz a megfelelő pillanatnyi gradienseket kell kiszámítani.

.. math::
	\dfrac{\partial \varepsilon ^2}{\partial w_{ij}^{(l)}}

A *kimeneti szinten* (l=2) a pillanyatni gradiens:

.. math::
	dfrac{\partial \varepsilon ^2}{\partial w_{ij}^{(2)}} = -2\varepsilon_isgm'(s_i^{(2)})x_j^{(2)} = -2\delta_i^{(2)}x_j^{(2)}

A súlymódosítás tehát

.. math:: 
	w_i^{(2)}(k+1) = w_i^{(2)}(k) + 2\mu\varepsilon_i(k)sgm'(s_i^{(2)})x^{(2)}(k) = w_i^{(2)} + 2\mu\delta_i^{(2)}(k)x^{(2)}(k)

A rejtett réteg processzáló elemeinél a fenti összefüggések közvetlenül nem alkalmazhatók, mivel nem ismerjük az egyes processzáló elemek kimenetén fellépő hibát. A lánc szabály alkalmazásával azonban a deriváltak itt is meg tudjuk határozni, hiszen a rejtett réteg processzáló elemeinek súlytényezői befolyásolják ezen processzáló elemek lineáris (s) és nemlineáris (y) kimeneteit, továbbá ezen kimeneteken keresztül a későbbi rétegek kimeneteit is. Tehát a parciális deriváltak lépésenként számíthatók.

.. math::
	\dfrac{\partial \varepsilon ^2}{\partial w_{ij}^{(1)}} = \dfrac{\partial \varepsilon ^2}{\partial s_i^{(1)}}\dfrac{\partial s_i^{(1)}}{\partial w_{ij}^{(1)}}

így a súlymódosítás:

.. math::
	w_i^{(1)}(k+1)=w_i^{(1)}(k)+2\mu\delta_i^{(1)}(k)x^{(1)}(k)

ahol

.. math::
	\delta_i^{(1)} = (\delta_i^{(2)}w_{1i}^{(2)}+\delta_2^{(2)}w_{2i}^{(2)})sgm'(s_i{(1)})

âz ún. "visszaterjesztett hiba". a súlymódosítás tehát itt is az LMS algoritmussal formailag megegyező eljárással történik, a hiba helyén azonban súlyzott, "visszaterjesztett hiba" szerpel. A súlyozó együtthatók megegyeznek az adott hálózat-részben az előrecsatolásánál szereplő súlytényezőkkel. A súlymódosítás ennek alapján tetszőleges rétegre megadható:

.. math::
	w_i^{(l)}(k+1)=w_i^{(l)}+2\mu\delta_i^{(l)}(k)x^{(l)}(k)

Ha az l-edik réteg összes processzáló elemének súlyvektorait egy W^{(l)} mátrixba fogjuk össze, ahol tehát a mátrix i-edik sora az i-edik processzáló elem súlyvektora, akkor az l-edik réteg összes súlyvektorának módosítása tömören az alábbi formában adható meg:

.. math::
	W^{(l)}(k+1) = W^{(l)}(k)+2\mu\delta^{(l)}x^{(l)^T}(k)

Itt a \delta^{(l)} a visszaterjesztett "hibákból" képzett oszlopvektor.

Az előbbiekben bemutattuk a backpropagation hálózat felépítését, működését. A hálózat elvi alapjainak ismerete azonban még nem elegendő ahhoz, hoy e hálüzatokat hatékonyan alkalmazni is tudjuk különböző gyakorlati feladatok megoldására. A hálózattal kapcsolatos elméleti eredmények ugyanis a gyakorlati alkalmazással összefüggő kérdésekre általában nem adnak választ.

Ilyen kérdések lehetnek pl.:
	* mekkora (hány réteg, rétegenként hány processzáló elem) hálózatot válasszunk
	* hogyan válasszuk meg a tanulási aránytényező, \mu értékét
	* milyen kezdeti értékeket állítsunk be
	* hogyan válasszuk meg a tanító és a tesztelő minta készletet
	* hogyan használjuk fel a tanító pontokat, milyen gyakorisággal módosítsuk a hálózat súlyait
	* meddig tanítsuk a hálózatot, stb?

Áltlában az előbb feltett kérdéskre is csak tapasztalati válaszok adhatók. Ez az oka annak, hogy a neurális hálózatok sikeres alkalmazásához jelenleg meglehetősen sok tapasztalat szükséges, amit csak úgy szerezhetünk meg, ha számos, jellegében eltérő feladat megoldására vállalkozunk.

**A hálózat méretének megválasztása**. Az elméleti eredmények szerint legalább háromrétegű - két tanítható réteggel rendelkező - hálózatra van szükség. A réteg számának növelése azonban megkönnyítheti a feladat megoldását, illetve rétegenként kevesebb processzáló elem felhasználása is elegendőnek bizonyulhat.

A redundancia csökkentése azt jelenti, hogy megprobáljuk megkeresni a felesleges súlyokat, processzáló elemeket, esetleg rétegeket, majd ezeket a hálózatból kimetszve a processzáló elemeket, esetleg rétegeket, majd ezeket a hálózatból kimetszve a maradék, egyszerűsített hálózattal oldjuk meg a feladatot. Felesleges súlyoknak, processzáló elemeknek, esetleg rétegeknek azok a hálózatelemek tekinthetők, melyek kihagyásával a feladat megoldható, tehát amelyek vagy nem vesznek részt a kimenet elóállításában vagy amelyek szerepét más hálózatelem is betöltheti, így a hálózat képességeinek redukciója nélkül elhagyhatók.

A hálózatok bizonyos kimetszéssel történő csökkentésére alkalmazott módszereket két csoportba sorolhatjuk:
	* Az egyik csoportba tartozó eljárások a kimeneti hiba egyes súlyok szerinti érzékenységének becslésén alapulnak
	* A másik csoportba tartozó módszereknél a kritériumfüggvényhez egy újabb ún. büntető tagot adunk

Az érzékenység becslés alapján dolgozó eljárások a hibafelület súlyok szerinti Taylor-soros közelítéséből indulnak ki

A büntető tagot alkalmazó módszereknél a tanulás során a hálózat súlyainak csökkentésére is törekszünk. A kritériumfüggvény:

.. math::
	C_r(w) = C(w) + \lambda\sum_{i,j}|w_{ij}|

**A tanulási aránytényző, \mu megválasztására** sincs jelenleg egyértelműen javasolható egyszerű módszer. A legtöbb esetben \mu értékét tapasztalati úton határozzák meg általános tendeciá felhasználásával. A gyorsabb kezdeti konvergencia és a minimumhely megfelelő pontosságú megközelítése érhető változó, lépésfüggő \mu alkalmazásával. Ebben az esetben valamely kezdeti, viszonylag nagy értékből kiindulva valahány lépésenként csökkentjuük \mu -t.

.. math::
	\sum_{k=1}^{\infty}\mu(k) = \infty

Ebben az összefüggésben k nem feltétlenül a lépésindexet jelöli, \mu csökkentésére rendszerint csak néhány lépésenként kerül sor.

A tanulás konvergenciájának sebessége növelhető adaptív \mu választással is. Ha a hiba nem csökken, akkor \mu értéke túl nagy, csökkenteni kell. Ezzel szemben, ha több egymást követő tanító lépés során a hiba folyamatosan csökken, akkor lehetséges, hogy túl óvatosan választottuk meg \mu-t, valószínű nagyobb érték mellett is biztosított a hiba csökkenése, érdemes tehát nagyobb \mu-vel megkísérelni a tanítást.

**A kezdeti súlyok beállítására** - jelenleg szintén nincs matematikailag megfogalmazható összefüggés. A kezdeti súlyvektor a hibafelületen a kezdeti pont helyzetét határozza meg, így minnél messzebb van ez a pont a megoldás helyétől, annál lassabban tanul a hálózat. A véletlen kezdeti értékek a szimmetriák elkerülését biztosíthatják, megakadályozva, hogy különböző neuronok hasonló leképezést valósítsanak meg és így nemkívánt redundancia jelenjen meg a hálózatban.

**A tanító lépések számának meghatározása**. Általában előre nem határozható meg a hálózat hibájának alakulása a tanító lépések függvényében, így azt sem lehet megmondani, hogy megfelelő kis hiba eléréséhe hány tanító lépés szükséges. A hálózat "jóságának" kiértékelése amúgy is számos elméleti ésé gyakorlati problémát vet fel.

**A tanító pontok felhasználása**. További lehetőségeket jelent, hogy a súlymódosításokat pontonként, vagy kötegelt (batch) eljárás szerint, csak a teljes tanító készlet (epoch) felhasználása után végezzük. Ezek az eljárások a súlykorrekció gyakoriságában térnek el. A batch eljárásnál a teljes tanító készlet összes mintáját ráadva a hálózatra minden esetben kiszámítjuk a hibát. A mintánkénti tanítás mintegy zajt visz a rendszerbe.

További kérdés, hogy egyáltalán **hogyan minősitsünk egy hálózatot**. Adott tanító készlet mellett szükségünk van egy ún. minősítő, kiértékelő mintakészletre (validation set) is. A hálózat tanítására csaka  tanítókészlet mintáit használjuk, míg az adott számú tanító lépésben átesett hálózat minősítése a minősítő készletre adott válaszok alapján lehetséges. Amennyiben csak a tanító pontokra adott válaszok alapján értékelünk, túltaníthatjuk a hálózatot.

Túltanítás (overtraining) akkor lép fel, ha a tanító készlet mintáira már nagyon kis hibájú válaszokat kapunk, miközben a kiértékelő készletre egyre nagyobb hibával válaszol a hálózat. Ez azért következhet be, mert a hálózat válaszai túlzottan illeszkednek a véges számú tanító pont által megszabott lekéezéshez, miközben a közbenső válaszok jelentősen eltérhetnek a megfelelő kivánt válaszoktól.

	.. image:: images/overtraining.png
			:width: 350px
	 		:align: center
	 		:height: 200px
	 		:alt: OverTraining
