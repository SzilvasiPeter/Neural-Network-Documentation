A neurális hálózatok felépítése
===============================

Definíciója, működése
---------------------
*Neurális háló*\ nak nevezzük azt a hardver vagy szoftver megvalósítású párhuzamos, elosztott működésre képes *információ feldolgozó eszköz*\ t, amely:

* azonos, vagy hasonló típusú, lokális feldolgozást végző műveleti elemek, neuronok (processing element, **neuron**) általában rendezett topológiájú, nagymértékben összekapcsolt rendszeréből áll,
* rendelkezik tanulási algoritmussal (**learning algorithm**), amely általában minta alapján való tanulást jelent, és az információfeldolgozás módját határozza meg,
* rendelkezik a megtanult információ felhasználását lehetővé tevő információ előhívási, vagy röviden előhívási algoritmussal (**recall algorithm**)

Felépítés
---------
* felépítés
	* neuron: Több bemenetű, egy kimenetű eszköz. A *bemenet*\ i értékekből a hálózat az *aktiváló függvény* alkalmazásával hozza létre a *kimeneti* értéket.

		.. image:: images/neuron.png
		    :width: 300px
		    :align: center
		    :height: 150px
		    :alt: Neuron
	
	* aktivációs függvény: A neuronokban használt *nemlinear*\ itások, ami *küszöbfüggvény* jellegű leképezés(*ÉT*:valós számok halmaza, *ÉK*: R, korlátos részhalmaza)
		 * lépcsőfgv
		 * telítéses lineáris fgv							 
		 * tangens hiberbolikus fgv						
		 * logisztikus fgv

	 	.. image:: images/activation_functions.png
	 		:width: 300px
	 		:align: center
	 		:height: 150px
	 		:alt: Activation Function						
	* bemenetek
		* gerjesztő
		* gátló

* összekötetések: *Egy kimenet több bemenet*\ tel össze\ *köthető*\ , ekkor valamennyi bemenet ugyanazt a jelet kapja, *kimenetek*\ et egymással *nem* köthetünk össze.
* topológia: A neuronok összekapcsolási rendszerét irányított gráffal reprezentáljuk. A gráf csomópontja a neuronoknak felelnek meg, míg az összekötetéseket(súlytényezők) az éleknek felelnek meg.

Háromféle neuront különböztethetünk meg:

* *bemeneti neuronok*: Bemenetük a hálózat bemenete, kimenetük más neuronok meghajtására szolgál.
* *kimeneti neuronok*: Kimenete a környezet felé továbbítja a kivánt információt.
* *rejtett neuronok*: Bemeneteikkel, mind kimenetükkel kizárólat más neuronokhoz kapcsolódnak.

Réteg: A neuronokat sok esetben rétegekbe (layer) szervezzük, ahol egy rétegbe hasonló típusú neuronok tartoznak(kapcsolataik is hasonlóak). Ennek megfelelően beszélhetünk bemeneti(*input layer*\ ), rejtett(*hidden layer*\ ) és kimeneti rétegről(*output layer*\ )

	.. image:: images/hidden_layer.jpg
		:width: 300px
		:align: center
		:height: 150px
		:alt: Neural Network with Hidden Layer

Rétegenként súlyvektorok vannak a súlyvektorokat összefoglalhatjuk egy egész hálózatra kiterjedő súly mátrixra (**W**). A bemeneti, rejtett és kimeneti neuronok adatait is mátrixba tároljuk, majd ezekkel végezük a számításokat.
Topológia szerint két fő csoport van

	.. note::
		A visszacsatolt-visszacsatolatlan tulajdonságot megfogalmazhatjuk a súlytényezők W mátrix segítségével.

* visszacsatolt hálózatok (feedback recall): Ha a neuronok indexelésével elérhető hogy a W olyan háromszög mátrix legyen, melynek főátlóbeli elemei nullák.
	* Globális visszacsatolás
	* Lokális visszacsatolás: Három csoport van az elemi, a laterális és a rétegek közötti visszacsatolások.
* visszacsatolatlan hálózatok (feedforward recall)

Felhasználási területei
-----------------------
* **asszociatív memória**: Speciális memória, melybe *meghatározott mód*\ on (*tanulás*\ ) információt írunk be, majd *olvassuk ki* (*recall*\ )
* **optimalizáló rendszer**: Optimalizálás során általában valamilyen költséget kívánunk minimalizálni, a rendszer struktúrájának, illetve paramétereinek megfelelő megválasztásával. 
* **approximáló rendszer**: A megfelelő matematikai előállítása központi feladat a mérnöki alkalmazások számos területén, pl. képfeldolgozás, alakfelismerés, jelfeldolgozés stb. A hálózat képes minták alapján a keresett leképezés közelítő előállítására.
* **nem lineáris dinamikus rendszer**: Neurális hálót kiegészítjük dinamikus komponensekkel. A tanítás rendszerint a statikus esetben is lassú, nehézkes, de a dinamikus esetben még ehhez képest is sokkal komplikáltabb, lassabb.