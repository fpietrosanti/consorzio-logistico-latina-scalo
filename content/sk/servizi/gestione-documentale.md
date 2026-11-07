---
linkTitle: "Správa dokumentácie"
title: "Správa dokumentácie a WMS pre logistiku v Latina Scalo"
description: "Správa dokumentácie v Latina Scalo (LT): DDT a dodacie listy, sledovateľnosť pohybov v systéme WMS a prepojenie s informačnými systémami objednávateľov."
url: "/sk/sluzby/sprava-dokumentacie/"
layout: "servizio"
weight: 8
image: "topics/inventario-barcode"
imageAlt: "Skladník eviduje kus v sklade prenosným terminálom, ilustračná fotografia"
faq:
  - q: "Aké doklady spravuje Consorzio Logistico Latina Scalo?"
    a: "Consorzio Logistico Latina Scalo spravuje v mene objednávateľov prepravné doklady (DDT) a dodacie listy, evidenciu skladových pohybov a sledovateľnosť jednotiek od príjmu po expedíciu, s prepojením na informačné systémy zákazníkov."
  - q: "Používa Consorzio Logistico Latina Scalo systém WMS?"
    a: "Áno. Consorzio Logistico Latina Scalo používa systém WMS (softvér na riadenie skladu) na evidenciu skladových miest, zásob a pohybov. V areáli v Latina Scalo systém pracuje na vyhradenej optike a priemyselnej Wi-Fi v skladových priestoroch."
  - q: "Dá sa WMS Consorzio Logistico Latina Scalo prepojiť s informačným systémom zákazníka?"
    a: "Consorzio Logistico Latina Scalo počíta s prepojením svojho systému WMS s informačnými systémami objednávateľov na výmenu kmeňových údajov, avíz príchodu, objednávok a potvrdení. Formát, frekvencia a spôsob prenosu údajov sa definujú pri spustení služby."
  - q: "Ako funguje sledovateľnosť tovaru v Latina Scalo?"
    a: "V areáli Consorzio Logistico Latina Scalo sa každá manipulačná jednotka pri príjme zaeviduje v systéme WMS a priradí ku kódu položky, množstvu, skladovému miestu a na požiadanie k šarži. Každý ďalší presun až po expedíciu zostáva zaznamenaný, takže cestu tovaru možno spätne zrekonštruovať."
  - q: "Aké údaje sú potrebné na nastavenie správy dokumentácie s Consorzio Logistico Latina Scalo?"
    a: "Na nastavenie správy dokumentácie Consorzio Logistico Latina Scalo požaduje informačný systém používaný objednávateľom, formát vymieňaných údajov, vystavované doklady, údaje o šaržiach alebo dátumoch spotreby, ktoré sa majú sledovať, a frekvenciu prehľadov o zásobách a pohyboch."
---

## Doklady, údaje a sledovateľnosť v jednej službe

Consorzio Logistico Latina Scalo spravuje v mene objednávateľov dokumentačnú a informačnú časť logistiky: vystavovanie prepravných dokladov (DDT) a dodacích listov, evidenciu skladových pohybov v systéme WMS (softvér na riadenie skladu), sledovateľnosť manipulačných jednotiek a prepojenie s informačnými systémami zákazníkov. Služba sprevádza [skladovanie]({{< relref "/servizi/stoccaggio" >}}), [manipuláciu]({{< relref "/servizi/handling" >}}) a [prepravu]({{< relref "/servizi/trasporto" >}}) zabezpečované v areáli vo Via della Dinamica, v zóne Tor Tre Ponti, v Latina Scalo (LT).

V areáli systém WMS pracuje na vyhradenej optike a priemyselnej Wi-Fi v skladových priestoroch; v kanceláriách a zasadacích miestnostiach pracuje personál, ktorý koordinuje doklady a informačné toky.

## Prepravné doklady a dodacie listy

### Pri príjme

Pri príjme pracovník porovná tovar s dokladom DDT dodávateľa a s avízom príchodu od objednávateľa. Rozdiely medzi deklarovaným a prijatým množstvom a prípadné poškodenia sa zapíšu ako výhrady do dokladu dopravcu a oznámia objednávateľovi s odkazom na dodávku.

### Pri výdaji

Pri nakládke Konzorcium vystaví prepravný doklad v mene objednávateľa s príjemcom, opisom tovaru, počtom kusov a hmotnosťou. Kópia podpísaná príjemcom sa po doručení vráti Konzorciu, ak doručenie zabezpečila vlastná flotila, a archivuje sa spolu s údajmi o zásielke.

## WMS a sledovateľnosť

### Evidencia jednotiek

Každá prijatá manipulačná jednotka sa zaeviduje v systéme WMS a priradí ku kódu položky, množstvu a skladovému miestu. Ak to objednávateľ požaduje, evidencia zahŕňa aj šaržu a dátum spotreby, ktoré sú potrebné v [agropotravinárskom]({{< relref "/settori/agroalimentare" >}}) a [farmaceutickom]({{< relref "/settori/farmaceutico" >}}) reťazci.

### Pohyby

Systém zaznamenáva každý ďalší presun: uloženie, doplnenie vychystávacích zón, vychystanie podľa objednávky, doplnkové činnosti, nakládku. Takto možno zrekonštruovať cestu jednotky alebo šarže od príjmu po expedíciu, čo je užitočná informácia aj pri sťahovaní výrobku z trhu alebo pri reklamácii zákazníka.

### Inventúra

Evidované zásoby sa pravidelne porovnávajú s fyzickým stavom podľa dohodnutého kalendára. Rozdiely sa oznámia objednávateľovi s uvedením položky, šarže a skladového miesta.

## Prepojenie s informačnými systémami

Výmena údajov medzi informačným systémom objednávateľa (ERP) a systémom WMS Konzorcia sa spravidla týka štyroch tokov:

- **kmeňové údaje**: kódy položiek, opisy, baliace jednotky, rozmery a hmotnosti;
- **avíza príchodu**: očakávaný tovar s dodávateľom, množstvom a predpokladaným dátumom;
- **výdajové objednávky**: riadky objednávok, príjemcovia a dátumy doručenia;
- **potvrdenia**: vykonané príjmy s prípadnými výhradami, aktualizované zásoby, odoslané zásielky s číslami dokladov.

Formát súborov, prenosový kanál a frekvencia výmen sa definujú v projekte spustenia na základe systému, ktorý objednávateľ používa. V počiatočných fázach alebo pri menších objemoch môže výmena prebiehať aj prostredníctvom štandardných súborov posielaných v dohodnutých časoch.

## Prehľady

Objednávateľ dostáva v dohodnutej periodicite údaje o zásobách, príjmoch, výdajoch a nezhodách. Obsah prehľadov sa stanoví podľa kontrolných potrieb objednávateľa, napríklad obrátkovosť položiek, šarže blížiace sa k dátumu spotreby alebo vybavené objednávky za obdobie.

## Spustenie služby

Spustenie zahŕňa štyri kroky: zber kmeňových údajov a formátov dokladov; definovanie dátových tokov a zodpovedností; skúšku výmen na vzorke objednávok; prechod do prevádzky so sledovaním prvých týždňov. Služba je súčasťou modelu [zmluvnej logistiky (3PL)]({{< relref "/servizi/logistica-3pl" >}}) a platí aj pre [cross-docking]({{< relref "/servizi/cross-docking" >}}) a [činnosti s pridanou hodnotou]({{< relref "/servizi/lavorazioni-valore-aggiunto" >}}).

## Odvetvia a územie

Sledovateľnosť podľa šarží sa týka najmä agropotravinárstva a farmácie; prepojenie objednávok je kľúčové pre [e-commerce]({{< relref "/settori/ecommerce" >}}) a pre [obchodné reťazce a maloobchod]({{< relref "/settori/gdo-retail" >}}), kým správa kódov a variantov sa týka [textilu a módy]({{< relref "/settori/tessile-moda" >}}) a [automobilového priemyslu]({{< relref "/settori/automotive" >}}). Areál obsluhuje podniky z [Latiny]({{< relref "/logistica/latina" >}}), [Aprilie]({{< relref "/logistica/aprilia" >}}), [Cisterny di Latina]({{< relref "/logistica/cisterna-di-latina" >}}) a [Pomezie]({{< relref "/logistica/pomezia" >}}), ako aj z celej [provincie Latina]({{< relref "/logistica/provincia-di-latina" >}}) a [južného Ríma]({{< relref "/logistica/roma-sud" >}}).

## Cenová ponuka

Pre cenovú ponuku na správu dokumentácie je potrebné uviesť používaný informačný systém, formát údajov, ktoré objednávateľ dokáže posielať a prijímať, vystavované doklady, údaje o šaržiach alebo dátumoch spotreby, ktoré sa majú sledovať, priemerný počet objednávok za deň a požadovanú periodicitu prehľadov. Žiadosti sa posielajú cez [kontaktný formulár]({{< relref "/" >}}#contatti).
