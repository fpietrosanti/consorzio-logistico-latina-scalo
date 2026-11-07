---
title: "Verkkokaupan fulfillment Laziossa: tavaravirrat, cut-off, palautukset ja kuriirit"
description: "Verkkokauppatilausten käsittely lazioalaiselle verkkokauppiaalle: vastaanotosta lähetykseen, katkaisuajat, palautukset, kuriirit ja tieetäisyydet Roomasta."
date: 2026-10-02
url: "/fi/analyysit/verkkokaupan-fulfillment-lazio/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Jakelukeskuksen sisätila ja lähetysvalmiita kolleja, arkistokuva"
summary: "Sopimuslogistiikkaoperaattorille ulkoistettu verkkokauppatilausten käsittely noudattaa vakiintunutta kulkua: tilausten integrointi, keräily, pakkaus, luovutus kuriirille ja palautusten käsittely. Lazioalaiselle verkkokauppiaalle ratkaisevia muuttujia ovat tilausten vastaanoton katkaisuaika, kuriirien noutoaika ja tieetäisyys Rooman markkina-alueelta."
faq:
  - q: "Mitä cut-off tarkoittaa verkkokaupan fulfillmentissa?"
    a: "Se on katkaisuaika, johon mennessä varaston vastaanottama tilaus lähetetään samana päivänä. Se riippuu kuriirin noutoajasta sekä keräilyyn ja pakkaukseen tarvittavasta ajasta; katkaisuajan jälkeen vastaanotetut tilaukset lähtevät seuraavana arkipäivänä."
  - q: "Kuinka paljon aikaa kuluttajalla on palauttaa verkosta ostettu tuote?"
    a: "Italian kuluttajansuojalaki (Codice del Consumo, D.Lgs. 206/2005, 52 §) antaa kuluttajalle 14 päivää aikaa käyttää peruuttamisoikeuttaan ilmoittamatta syytä, yleensä tavaran toimituksesta lukien. Myyjä palauttaa maksun 14 päivän kuluessa peruuttamisesta ja voi pidättää palautuksen, kunnes se on vastaanottanut tavarat tai todisteen niiden lähettämisestä."
  - q: "Kuinka kaukana Latina Scalo on Roomasta verkkokaupan toimituksia ajatellen?"
    a: "OSRM-reittilaskelman mukaan henkilöautolla Via della Dinamican toimipaikasta on noin 70 km EUR:iin (noin 70 minuuttia), noin 50 km Pomeziaan (noin 50 minuuttia) ja noin 34 km Apriliaan (noin 36 minuuttia). Raskailla ajoneuvoilla ajoajat ovat pidempiä."
  - q: "Mikä on tuotteiden verkkokaupan arvo Italiassa?"
    a: "Politecnico di Milanon Osservatorio eCommerce B2c Netcomm -seurantaryhmän mukaan tuotteiden verkko-ostosten arvoksi Italiassa vuonna 2025 arvioidaan noin 40,1 miljardia euroa, mikä on 6 % enemmän kuin vuonna 2024 ja 11,2 % kaikista tuoteostoista."
  - q: "Mitä tietoja fulfillment-palvelun käynnistämiseen tarvitaan?"
    a: "Nimikkeiden (SKU) määrä, mitat ja painot, keskimääräiset ja huipputason päivittäiset tilausmäärät, rivit tilausta kohden, odotettu palautusaste, käytettävät kuriirit, myyntialusta ja tilausten välitystapa, pakkausvaatimukset ja markkinointimateriaalit."
---

Verkkokauppatilausten käsittely (fulfillment) on sopimuslogistiikan osa-alue, jonka toimintaprofiili on hajanaisin: paljon pieniä tilauksia, yksi tai kaksi riviä tilausta kohden, yhden kollin lähetykset ja suurempi palautusosuus kuin perinteisessä kaupassa. AGI:n 27. toukokuuta 2025 siteeraaman Politecnico di Milanon Osservatorio eCommerce B2c Netcomm -seurantaryhmän mukaan tuotteiden verkko-ostosten arvoksi Italiassa vuonna 2025 arvioidaan noin 40,1 miljardia euroa, mikä on 6 % enemmän kuin vuonna 2024 ja 11,2 % kaikista tuoteostoista.

Lazioalaiselle verkkokauppiaalle varaston valinta ratkeaa muutaman mitattavan muuttujan perusteella: tilausten katkaisuaika, kuriirien noutoaika, palautusten käsittely sekä tieetäisyys loppuasiakkaisiin ja kuriirien terminaaleihin.

## Kulku tilauksesta toimitukseen

Sopimuslogistiikkaoperaattorin käsittelemän verkkokauppatilauksen kierto koostuu seitsemästä vaiheesta:

1. **tavaran vastaanotto** toimittajalta tai valmistajalta, määrätarkastus, nimikkeiden (SKU) kirjaus ja hyllytys;
2. **tilausten integrointi**: myyntialustan tilaukset siirtyvät operaattorin WMS-järjestelmään (varastonhallintaohjelmisto) liittimen, tiedoston tai tietojärjestelmärajapinnan kautta;
3. **keräily (picking)**, yleensä kappaleittain, kokoamalla useita tilauksia yhteen keräilykierrokseen kulkumatkojen lyhentämiseksi;
4. **tarkastus ja pakkaus (packing)**: laatikon valinta, täytemateriaali sekä asiakirjojen ja markkinointimateriaalin lisääminen;
5. **merkintä** kuriirin rahtikirjalla ja seurantakoodin luominen;
6. **luovutus kuriirille** sovitussa noudossa ja seurantatietojen välittäminen myyntialustalle;
7. **palautusten käsittely**: vastaanotto, tarkastus, päätös tuotteen jatkokäsittelystä ja varastosaldon päivittäminen.

Keräily-, pakkaus- ja merkintätoiminnot kuvataan [tavarankäsittelyn]({{< relref "/servizi/handling" >}}) palvelusivulla; toimialan erityistarpeet toimialasivulla [verkkokauppa]({{< relref "/settori/ecommerce" >}}).

## Cut-off ja noutoaika

**Cut-off** on katkaisuaika, johon mennessä vastaanotettu tilaus lähetetään samana päivänä. Se lasketaan taaksepäin kuriirin noutoajasta: jos kuriiri käy kello 17 ja varastolta kuluu keskimäärin kaksi tuntia tilauserän kollien keräilyyn, pakkaamiseen ja kokoamiseen, katkaisuaika voi olla enintään kello 15, ja huippupäivinä sitä on aikaistettava tai henkilöstöä lisättävä.

Katkaisuaikaan vaikuttaa kolme tekijää:

- päivittäisten **noutojen määrä** ja viimeisen noudon aika, joista sovitaan kunkin kuriirin kanssa;
- **keräilyn tuottavuus**, joka riippuu varastopaikkojen järjestelystä: myydyimmät nimikkeet on sijoitettava lähelle pakkausaluetta;
- paino- ja mittatietojen **laatu**, sillä ne määräävät laatikon ja kuriiritariffin ilman käsin tehtäviä mittauksia.

Palvelusopimuksessa on ilmoitettava katkaisuaika ja sitä mittaava mittari, esimerkiksi niiden tilausten prosenttiosuus, jotka on vastaanotettu katkaisuaikaan mennessä ja lähetetty samana päivänä. Aiheesta kerrotaan oppaassa [sopimuslogistiikan sopimus ja KPI-mittarit]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kuriirit ja Lazion maantiede

Verkkokauppias voi käyttää omia sopimuksiaan pikakuriirien kanssa tai logistiikkaoperaattorin neuvottelemia sopimuksia. Valtakunnalliset kuriirit noutavat lähetykset varastosta ja lajittelevat kollit omissa terminaaleissaan; alueellisissa B2B-toimituksissa tai pienissä määrissä raskaita kolleja operaattori voi käyttää omaa kalustoaan.

Latina Scalossa sijaitsevasta varastosta tärkeimmille kysyntäalueille on seuraavat tieetäisyydet, jotka on laskettu OSRM-reittimoottorilla henkilöautolle normaalissa liikenteessä:

| Määränpää | Tieetäisyys | Arvioitu ajoaika |
|---|---|---|
| Latinan keskusta | noin 8 km | noin 13 minuuttia |
| Aprilia | noin 34 km | noin 36 minuuttia |
| Pomezia | noin 50 km | noin 50 minuuttia |
| Santa Palomba | noin 55 km | noin 57 minuuttia |
| Castel Romano | noin 57 km | noin 56 minuuttia |
| Rooma EUR | noin 70 km | noin 70 minuuttia |
| Rooma Ostiense | noin 74 km | noin 76 minuuttia |
| Fiumicino | noin 90 km | noin 86 minuuttia |

Raskailla ajoneuvoilla ja ruuhka-aikoina ajoajat ovat pidempiä. Pääväylä Roomaan on valtatie 148 Pontina, jolla on erilliset ajoradat Rooman ja Borgo Piaven välillä; Pomezian ja Latina nordin välisellä osuudella nopeusrajoitusta on laskettu 110 km/h:sta 80 km/h:iin. Alueiden kuvaukset ovat sivuilla [logistiikka Roomassa]({{< relref "/logistica/roma" >}}), [Rooman eteläosat]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) ja [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Palautukset

Kuluttajan **peruuttamisoikeutta** sääntelee Italian kuluttajansuojalaki (Codice del Consumo, D.Lgs. 206/2005). Sen 52 § antaa 14 päivää aikaa peruuttaa kauppa ilman perusteluja, yleensä tavaran toimituksesta lukien. Lain 56 § velvoittaa myyjän palauttamaan maksun 14 päivän kuluessa peruuttamisesta, ja myyjä voi pidättää palautuksen, kunnes se on vastaanottanut tavarat tai todisteen niiden lähettämisestä.

Varaston on siis käsiteltävä palautukset näiden määräaikojen kanssa yhteensopivassa ajassa:

- palautuksen **vastaanotto ja kirjaus** alkuperäisellä tilausnumerolla;
- tuotteen ja pakkauksen kunnon **tarkastus** verkkokauppiaan kanssa sovittujen kriteerien mukaan;
- **jatkokäsittely**: palautus myyntivarastoon, kunnostus, uudelleenpakkaus, myynti kakkoslaatuna tai hävittäminen;
- tuloksen **ilmoittaminen** myyntialustalle maksunpalautuksen vapauttamiseksi.

Palautuksille varattu erillinen alue, joka on erotettu myyntikelpoisesta varastosta, estää tarkastamattoman tavaran palaamisen tilausten käyttöön.

## Kausihuiput ja kapasiteetti

Verkkokauppa keskittää volyymit muutamaan vuoden jaksoon, jotka liittyvät kampanjoihin ja juhlapyhiin. Operaattorille tämä tarkoittaa lisähenkilöstön, varavarastopaikkojen ja kuriirien kanssa sovittujen lisänoutojen ennakointia. Verkkokauppiaalle se tarkoittaa myyntiennusteiden ja kampanja-aikataulujen ilmoittamista etukäteen: ennalta ilmoittamaton huippu on yleisin syy katkaisuajan pettämiseen.

## Latina Scalon toimipaikka

Consorzio Logistico Latina Scalolla on Via della Dinamicalla Latina Scalossa (LT) 19 000 neliömetriä katettua tilaa ja WMS-järjestelmä varastonhallintaan. Palveluihin kuuluvat varastointi, keräily, pakkaus, merkintä ja lavoitus, maantiekuljetukset omalla kalustolla ja viimeisen kilometrin jakelu sekä asiakirjahallinta. Konsortion mukaan toiminta on käynnissä ympäri vuorokauden, seitsemänä päivänä viikossa. Integraatiotavat yksittäisiin myyntialustoihin on tarkistettava tarjousvaiheessa. Jakelusta Roomaan kerrotaan analyysissa [viimeinen kilometri Rooman eteläosiin]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Lähteet

- AGI, talousuutinen 27. toukokuuta 2025 tuotteiden verkko-ostoksista vuonna 2025, Osservatorio eCommerce B2c Netcomm – Politecnico di Milanon tiedot: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), artt. 52 e 56: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Etäisyydet ja ajoajat: OSRM-reittilaskelma (Open Source Routing Machine) Via della Dinamican toimipaikasta, henkilöauto, normaali liikenne; konsortion laskelma.
- SS148 Pontina, ajoradat ja nopeusrajoitukset: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (ANASin tiedot)
- Palvelut ja toiminta-ajat: Consorzio Logistico Latina Scalon ilmoitukset.
