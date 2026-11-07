---
title: "E-kereskedelmi fulfillment Laziban: folyamatok, cut-off, visszárú és futárok"
description: "E-kereskedelmi rendelések teljesítése lazioi webáruház számára: az árufogadástól a kiszállításig, határidők, visszárú, futárok és közúti távolságok Rómától."
date: 2026-10-02
url: "/hu/elemzesek/e-kereskedelmi-fulfillment-lazio/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Elosztóközpont belseje feladásra kész csomagokkal, archív fotó"
summary: "A külső szolgáltatóra bízott e-kereskedelmi rendelésteljesítés szabványos folyamatot követ: rendelésintegráció, kiszedés, csomagolás, átadás a futárnak és a visszárú kezelése. Egy lazioi webáruház számára a döntő változók a rendelésfogadási határidő, a futárok átvételi időpontja és a római vonzáskörzettől mért közúti távolság."
faq:
  - q: "Mi a cut-off az e-kereskedelmi fulfillmentben?"
    a: "Az a határidő, ameddig a raktár által fogadott rendelést még aznap feladják. A futár átvételi időpontjától, valamint a kiszedéshez és csomagoláshoz szükséges időtől függ; a cut-off után érkezett rendelések a következő munkanapon indulnak."
  - q: "Mennyi ideje van a fogyasztónak egy online vásárolt termék visszaküldésére?"
    a: "Az olasz fogyasztóvédelmi kódex (D.Lgs. 206/2005, 52. cikk) 14 napot biztosít a fogyasztónak az indokolás nélküli elállási jog gyakorlására, általában az áru kézbesítésétől. Az eladó az elállástól számított 14 napon belül téríti vissza a vételárat, és a visszatérítést visszatarthatja, amíg az árut vagy a feladás igazolását meg nem kapja."
  - q: "Milyen messze van Latina Scalo Rómától az e-kereskedelmi kiszállítások szempontjából?"
    a: "Az OSRM személygépkocsira vonatkozó útvonalszámítása szerint a Via della Dinamica-i telephely mintegy 70 km-re van az EUR negyedtől (mintegy 70 perc), mintegy 50 km-re Pomeziától (mintegy 50 perc) és mintegy 34 km-re Apriliától (mintegy 36 perc). Nehéz tehergépjárművek esetén a menetidő hosszabb."
  - q: "Mekkora a termék-e-kereskedelem Olaszországban?"
    a: "A Politecnico di Milano Netcomm B2c e-kereskedelmi megfigyelőközpontja szerint 2025-ben a termékek online vásárlása Olaszországban mintegy 40,1 milliárd euróra becsülhető, ami 6%-os növekedés 2024-hez képest, és a teljes termékvásárlás 11,2%-a."
  - q: "Milyen adatok kellenek egy fulfillment-szolgáltatás elindításához?"
    a: "A cikkek (SKU-k) száma, méretek és súlyok, átlagos és csúcsnapi rendelésszám, rendelésenkénti sorok, várható visszárúarány, használt futárszolgálatok, értékesítési platform és a rendelésátadás módja, csomagolási igények és promóciós anyagok."
---

Az e-kereskedelmi rendelések teljesítése (fulfillment) a szerződéses logisztika legtöredezettebb működési profilú szegmense: sok kis rendelés, rendelésenként egy-két sor, egycsomagos feladás, a hagyományos kereskedelemnél magasabb visszárúarány. A Politecnico di Milano Netcomm B2c e-kereskedelmi megfigyelőközpontja szerint, amelyet az AGI 2025. május 27-én idézett, 2025-ben a termékek online vásárlása Olaszországban mintegy 40,1 milliárd euróra becsülhető, ami 6%-os növekedés 2024-hez képest, és a teljes termékvásárlás 11,2%-a.

Egy lazioi webáruház számára a raktár kiválasztása néhány mérhető paraméteren múlik: a rendelési határidőn, a futárok átvételi időpontján, a visszárú kezelésén, valamint a végső ügyfelektől és a futárszolgálatok elosztóközpontjaitól mért közúti távolságon.

## A folyamat a rendeléstől a kézbesítésig

A külső szolgáltató által kezelt e-kereskedelmi rendelés ciklusa hét lépésből áll:

1. **az áru fogadása** a beszállítótól vagy a gyártótól, mennyiségi ellenőrzéssel, a cikkek (SKU-k) rögzítésével és betárolással;
2. **rendelésintegráció**: az értékesítési platform rendelései csatlakozón, fájlon vagy informatikai interfészen keresztül jutnak el a szolgáltató WMS-ébe (raktárirányítási szoftver);
3. **kiszedés (picking)**, általában darabra, több rendelés egyetlen kiszedési körbe vonásával a bejárt útvonalak csökkentése érdekében;
4. **ellenőrzés és csomagolás (packing)**, a doboz kiválasztásával, kitöltéssel, dokumentumok és promóciós anyagok elhelyezésével;
5. **címkézés** a futár fuvarlevelével és a nyomkövetési kód generálása;
6. **átadás a futárnak** az ütemezett átvételkor, és a nyomkövetési adat továbbítása a platformnak;
7. **a visszárú kezelése**: fogadás, ellenőrzés, döntés a termék sorsáról és a készlet frissítése.

A kiszedési, csomagolási és címkézési tevékenységeket az [anyagmozgatási]({{< relref "/servizi/handling" >}}) szolgáltatás oldala, az ágazat sajátos igényeit az [e-kereskedelem]({{< relref "/settori/ecommerce" >}}) ágazati oldal ismerteti.

## A cut-off és az átvételi időpont

A **cut-off** az a határidő, ameddig a fogadott rendelést még aznap feladják. A futár átvételi időpontjától visszafelé számítják: ha a futár 17 órakor érkezik, és a raktárnak átlagosan két órára van szüksége egy rendeléshullám csomagjainak kiszedéséhez, csomagolásához és összevonásához, a cut-off legkésőbb 15 óra lehet, csúcsnapokon pedig korábbra kell hozni, vagy növelni kell a létszámot.

Három tényező módosítja a cut-offot:

- a napi **átvételek száma** és az utolsó átvétel időpontja, amelyet minden futárszolgálattal egyeztetnek;
- a **kiszedés termelékenysége**, amely a tárolóhelyek szervezésétől függ: a legkelendőbb cikkeket a csomagolóterület közelében kell elhelyezni;
- a súly- és méretadatok **minősége**, amelyek kézi mérés nélkül határozzák meg a dobozt és a futár díját.

A szolgáltatási szerződésnek tartalmaznia kell a cut-offot és az azt mérő mutatót, például a határidőig beérkezett és aznap feladott rendelések arányát. A témáról a [szerződéses logisztikai szerződésről és a KPI-kről]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}) szóló útmutató szól.

## A futárok és Lazio földrajza

A webáruház használhat saját szerződést az expressz futárszolgálatokkal, vagy a logisztikai szolgáltató által kialkudottakat. Az országos futárszolgálatok a raktárban veszik át a csomagokat, és saját elosztóközpontjaikban válogatják szét őket; a regionális B2B-kiszállításoknál vagy a kevés, nehéz csomagot tartalmazó szállítmányoknál a szolgáltató saját flottát is alkalmazhat.

Egy Latina Scalo-i raktár esetében a fő keresleti körzetek felé mért közúti távolságok, az OSRM útvonaltervezővel személygépkocsira, átlagos forgalom mellett számítva, a következők:

| Célállomás | Közúti távolság | Becsült menetidő |
|---|---|---|
| Latina központ | kb. 8 km | kb. 13 perc |
| Aprilia | kb. 34 km | kb. 36 perc |
| Pomezia | kb. 50 km | kb. 50 perc |
| Santa Palomba | kb. 55 km | kb. 57 perc |
| Castel Romano | kb. 57 km | kb. 56 perc |
| Róma EUR | kb. 70 km | kb. 70 perc |
| Róma Ostiense | kb. 74 km | kb. 76 perc |
| Fiumicino | kb. 90 km | kb. 86 perc |

Nehéz tehergépjárművek esetén és csúcsidőben a menetidő hosszabb. A Róma felé vezető fő útvonal az SS148 Pontina főút, amely Róma és Borgo Piave között osztott pályás; a Pomezia és Latina nord közötti szakaszon a sebességhatárt 110-ről 80 km/h-ra csökkentették. Az egyes körzetek adatlapjai a [logisztika Rómában]({{< relref "/logistica/roma" >}}), a [Dél-Róma]({{< relref "/logistica/roma-sud" >}}), az [EUR]({{< relref "/logistica/eur" >}}) és a [Pomezia]({{< relref "/logistica/pomezia" >}}) oldalon találhatók.

## A visszárú

A fogyasztó **elállási jogát** az olasz fogyasztóvédelmi kódex (Codice del Consumo, D.Lgs. 206/2005) szabályozza. Az 52. cikk 14 napot biztosít az indokolás nélküli elállásra, általában az áru kézbesítésétől. Az 56. cikk kötelezi az eladót, hogy az elállástól számított 14 napon belül visszatérítsen, azzal a joggal, hogy a visszatérítést az áru megérkezéséig vagy a feladás igazolásáig visszatarthatja.

A raktárnak ezért e határidőkkel összeegyeztethető idő alatt kell kezelnie a visszárut:

- a visszárú **fogadása és rögzítése** az eredeti rendelési számmal;
- a termék és a csomagolás állapotának **ellenőrzése** a webáruházzal egyeztetett szempontok szerint;
- **a termék sorsa**: visszavétel készletre, felújítás, átcsomagolás, értékesítés másodosztályúként vagy ártalmatlanítás;
- az eredmény **közlése** a platformmal a visszatérítés feloldásához.

Az értékesíthető készlettől elkülönített visszárúterület megakadályozza, hogy az ellenőrizetlen áru ismét a rendelések számára elérhetővé váljon.

## Szezonális csúcsok és kapacitás

Az e-kereskedelem az év néhány, akciókhoz és ünnepekhez kötődő időszakára koncentrálja a mennyiségeket. A szolgáltató számára ez kiegészítő személyzet, tartalék tárolóhelyek és a futárokkal kötött, többletátvételekre vonatkozó megállapodások tervezését jelenti. A webáruház számára azt, hogy előre közölnie kell az értékesítési előrejelzéseket és az akciós naptárt: a be nem jelentett csúcs a cut-off be nem tartásának leggyakoribb oka.

## A Latina Scalo-i telephely

A Latina Scalo-i (LT) Via della Dinamicán működő Consorzio Logistico Latina Scalo 19 000 négyzetméter fedett területtel és raktárirányítási WMS-rendszerrel rendelkezik. A szolgáltatások közé tartozik a raktározás, a kiszedés, a csomagolás, a címkézés és a raklapozás, a saját flottával végzett közúti szállítás és az utolsó mérföldes disztribúció, valamint a dokumentumkezelés. A Consorzio szerint a működés a hét minden napján, napi 24 órában folyik. Az egyes értékesítési platformokkal való integráció módját az árajánlat elkészítésekor kell ellenőrizni. A Rómába irányuló disztribúcióról az [utolsó mérföld Dél-Róma felé]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}) című elemzés szól.

## Források

- AGI, 2025. május 27-i gazdasági hír a termékek 2025-ös online vásárlásáról, az Osservatorio eCommerce B2c Netcomm – Politecnico di Milano adatai: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), 52. és 56. cikk: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Távolságok és menetidők: OSRM (Open Source Routing Machine) útvonalszámítás a Via della Dinamica-i telephelytől, személygépkocsi, átlagos forgalom; a Consorzio feldolgozása.
- SS148 Pontina, pályák és sebességhatárok: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (ANAS-adatok)
- Szolgáltatások és működés: a Consorzio Logistico Latina Scalo nyilatkozatai.
