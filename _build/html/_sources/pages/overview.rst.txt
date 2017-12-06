Történeti áttekintés
====================

Bevezetés
---------
A neurális hálózatok olyan számítási feladatok megoldására létrejött párhuzamos feldolgozást végző, adaptív eszközök, melyek eredete a biológiai rendszerektől származtatható.(ide a számtani adatok: gyorsaság összehasonlitása az emberi és a gépi neuronok átviteli sebesesége->emberi:kémiai, gépi:elektromos)

Kezdet
~~~~~~~~
Az alapgondolat, hogy a természetes neurális hálók mintájára hozzunk létre mesterséges számító rendszereket meglehetősen régi. A kezdeti lökést természetesen az idegsejtekkel kapcsolatos kutatási eredmények adták. Jónéhány évnek el kellet azonban telnie addig, amíg az első mesterséges neuron, majd a neurális hálozat megjelent.

Neuron modell
~~~~~~~~~~~~~
Az egyszerű neuron modell valójában nem más, mint egy többdimenziós bemenet komponenseinek súlyozott összegét meghatározó, tehát lineáris kombinációt megvalósító hálózat, amelyet egy nem lineáris leképezés követ. A kivánt müködés megfelelő konvergens iteratív eljárással, tanuló eljárással érhető el. A tanulás itt egyszerűen azt jelenti, hogy a kívánt működést reprezentáló, összetartozó be- és kimeneti értékek alapján a hálózat maga alakítja ki a megfelelő átvitelét, illetve a hálózat bemenetére kerülő adatokban önmaga probál valamilyen hasonlóságot felfedni.
Mintegy húsz évet kellet várni ahhoz, hogy ismét megélénküljön a neurális hálózatok iránti érdeklődés. Az érdeklődés felkeltésében a legfontosabb esemény talán az ún. Hopfield-háló(KÉP) publikálása volt, amely optimalizálási feladatokra volt képes. További jelentős eredmény az ún. hibavisszaterjesztéses (backpropagation)(KÉP) algoritmus "felfedezése", amely hatékonynak bizonyult a többrétegű hálózatok tanításánál. Az algoritmust 1986-ban publikálta a RumelHart, Hintor és Williams szerzőhármas és egyben be is mutatták az algoritmus hatékonyságát.

Kibontakozás
~~~~~~~~~~~~
A nyolcvanas évek második fele óta a neurális hálózatok kutatása reneszánszát éli. A neurális hálózatokat időnként úgy állítják be, mint bármilyen feladatra alkalmazható univerzális eszközöket, és olyan esetekben is alkalmazzák, vagy javasolják alkalmazni, amikor más, hagyományos eljárások hasznosabbnak bizonyulnak.

Alkalmazási területei
~~~~~~~~~~~~~~~~~~~~~
Az alkalmazási területei a különböző felismerési problémák, vagy az optimalizáló feladatok. Hasonlóan fontos alkalmazási terület a nemlineáris rendszerek vizsgálata, identifikációja, szabályozása. A neurális hálozatok tudománya egy fejlődésben lévő tudomány. Az újabban megélénkült kutatások eredményeképpen most már nemcsak sikerült bemutatni, hogy a neurális hálózatok komplex feladatok megoldásában igen hasznosnak bizonyulnak, hanem az ehhez szükséges elméleti alapokat is sikerült kidolgozni. Bizonyítható, hogy megfelelő tanulási algoritmussal, adott felépítésű hálózat alkalmassá tehető adatokban meglévő hasonlóságok felismerésére, osztályozási feladatok megoldásásra.

Kutatások
~~~~~~~~~
A neurális hálózatok kutatása számos pontos kapcsolódik az egyéb, lineáris és nemlineáris rendszerekkel foglalkozó kutatásokhoz. Így különösen sok kapcsolódási pont találtható a neurális hálózatok és az adaptív rendszerek között. Hasonlóan erős a kapcsolat a neurális információfeldolgozás és a parallel feldolhozás között. És az is természetes, hogy a neurális hálózatok kutatása kezdetektől fogva szoros kapcsolatban áll bizonyos biológiai kutatásokkal, első sorban az idegrendszeri- és agykutatásokkal, hiszen a mesterséges neurális hálók számos eredménye biológiai kutatásokon, megfigyeléseken alapul. Az intenzív kutatás következtében azonban várható, hogy egyre több kérdésre születik egzakt válasz, lehetővé téve így, hogy egyre pontosabban meghatározzák azon feladatok körét, ahol lehet és érdemes is neurális hálózatokat alkalmazni.

Fejlődési irányai(Végére vagy az elejére)
-----------------------------------------
A neuronhálók meglehetősen univerzális feladatmegoldó eszközök. Összetett, bonyolult gyakorlati problémák megoldásában azonban legtöbbszor önmagukban nem alkalmazhatók, inkább csak részfeladato megoldásában jelentenek nagy segítséget. A neurális számítástechnika fejlődésében több irány figyelhető meg. Az egyik fő irány a témakör minél egzaktabb matematikai megalapozásra törekszik. Ez elsősorban matematikai kutatásokat igényel, a hálózatok képességeinek minél pontosabb meghatározását célozza.
A fejlödés másik fő vonala arra írányul, hogy az egyre komplexebb feladatok megoldásához nyerjünk eszközöket. Ezen eszközök között a neurális hálózatok is megjelennek, de nem kizárólagosan, hanem kombinálva más számítási megközelítésekkel. A neuronhálók tudás alapú rendszerek, hiszen képességeiket adatokból tanulás utján nyerik. Egy feladat megoldásánál nem csak adatok formájában áll rendelkezésünkre a tudás. A más módon pl. szabályok formájában álló tudás felhasználása alapvetően fontos lehet.
A továbbfejlődés egy lehetséges útja a moduláris neurális hálók létrehozás és alkalmazása. A moduláris megközelítés alapgondolata, hogy a feladatot hálóval oldjuk meg, ahol az egyes hálók vagy segítik egymás vagy versenyeznek egymással. Így mind kooperatív, mind kompetetív moduláris rendszerek létrehozhazók.
A hibrid intelligens rendszerek között kell megemlíteni a neurofuzzy rendszereket is. A neurális hálózatok az adaptációs képesség tekintetében, az adatokból való tanulásban, a fuzzy rendszerek a szimbolikus tudás kezelésében mutatnak egyértelmű előnyöket. A két megközelítés előnyeit ötvöző neurofuzzy rendszerek leginkább a rendszermodellezés és szabályozás területén terjedtek el.