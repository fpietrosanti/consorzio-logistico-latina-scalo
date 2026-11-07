---
title: "E-commerce fulfillment u Laziju: tokovi, cut-off, povrati i kurirske službe"
description: "Izvršenje e-commerce narudžbi za trgovca iz Lazija: od prijema do otpreme, krajnja vremena, povrati, kurirske službe i cestovne udaljenosti od Rima."
date: 2026-10-02
url: "/hr/analize/ecommerce-fulfillment-lazio/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Unutrašnjost distribucijskog centra s koletima spremnima za otpremu, arhivska fotografija"
summary: "Izvršenje e-commerce narudžbi povjereno operateru za treće strane slijedi standardni tok: integraciju narudžbi, komisioniranje, pakiranje, predaju kurirskoj službi i upravljanje povratima. Za trgovca iz Lazija odlučujuće varijable su krajnje vrijeme prihvata narudžbi, vrijeme preuzimanja kurirskih službi i cestovna udaljenost od rimskog gravitacijskog područja."
faq:
  - q: "Što je cut-off u e-commerce fulfillmentu?"
    a: "To je krajnje vrijeme do kojeg se narudžba koju je skladište primilo otprema istoga dana. Ovisi o vremenu preuzimanja kurirske službe i o vremenu potrebnom za komisioniranje i pakiranje; narudžbe primljene nakon cut-offa otpremaju se sljedeći radni dan."
  - q: "Koliko vremena potrošač ima za povrat proizvoda kupljenog na internetu?"
    a: "Talijanski Zakon o zaštiti potrošača (Codice del Consumo, D.Lgs. 206/2005, čl. 52.) daje potrošaču 14 dana za ostvarivanje prava na jednostrani raskid ugovora bez navođenja razloga, u pravilu od isporuke robe. Prodavatelj vraća novac u roku od 14 dana od raskida i može zadržati povrat dok ne primi robu ili dokaz o otpremi."
  - q: "Koliko je Latina Scalo udaljen od Rima za e-commerce isporuke?"
    a: "Prema izračunu rute OSRM za osobni automobil, lokacija u ulici Via della Dinamica udaljena je oko 70 km od četvrti EUR (oko 70 minuta), oko 50 km od Pomezije (oko 50 minuta) i oko 34 km od Aprilije (oko 36 minuta). Za teška vozila vremena su dulja."
  - q: "Kolika je vrijednost e-commercea proizvoda u Italiji?"
    a: "Prema opservatoriju Osservatorio eCommerce B2c Netcomm milanskog Politecnica, internetska kupnja proizvoda u Italiji 2025. procjenjuje se na oko 40,1 milijardu eura, uz rast od 6 % u odnosu na 2024., što je 11,2 % ukupne kupnje proizvoda."
  - q: "Koji su podaci potrebni za pokretanje usluge fulfillmenta?"
    a: "Broj artikala (SKU), dimenzije i mase, prosječan i vršni broj narudžbi dnevno, stavke po narudžbi, očekivana stopa povrata, kurirske službe koje se koriste, prodajna platforma i način razmjene narudžbi, zahtjevi pakiranja i promotivni materijali."
---

Izvršenje e-commerce narudžbi (fulfillment) segment je logistike za treće strane s najrascjepkanijim operativnim profilom: mnogo malih narudžbi, jedna ili dvije stavke po narudžbi, otprema u jednom koletu, udio povrata veći nego u tradicionalnoj trgovini. Prema opservatoriju Osservatorio eCommerce B2c Netcomm milanskog Politecnica, koji je 27. svibnja 2025. citirala agencija AGI, internetska kupnja proizvoda u Italiji 2025. procjenjuje se na oko 40,1 milijardu eura, uz rast od 6 % u odnosu na 2024., što je 11,2 % ukupne kupnje proizvoda.

Za trgovca iz Lazija izbor skladišta ovisi o nekoliko mjerljivih parametara: krajnjem vremenu za narudžbe, vremenu preuzimanja kurirskih službi, upravljanju povratima i cestovnoj udaljenosti od krajnjih kupaca i od sortirnih centara kurirskih službi.

## Tok, od narudžbe do isporuke

Ciklus e-commerce narudžbe kojom upravlja operater za treće strane sastoji se od sedam koraka:

1. **prijem robe** od dobavljača ili proizvođača, uz količinsku kontrolu, evidentiranje artikala (SKU) i uskladištenje;
2. **integracija narudžbi**: narudžbe s prodajne platforme stižu u operaterov WMS (softver za upravljanje skladištem) putem konektora, datoteke ili informatičkog sučelja;
3. **komisioniranje (picking)**, u pravilu po komadu, uz grupiranje više narudžbi u jedan krug komisioniranja radi skraćivanja putova;
4. **kontrola i pakiranje (packing)**, uz izbor kutije, ispunu, umetanje dokumenata i promotivnih materijala;
5. **označavanje** tovarnim listom kurirske službe i generiranje broja za praćenje;
6. **predaja kurirskoj službi** pri planiranom preuzimanju i prijenos podataka o praćenju na platformu;
7. **upravljanje povratima**: prijem, kontrola, odluka o daljnjem postupanju s proizvodom i ažuriranje zalihe.

Aktivnosti komisioniranja, pakiranja i označavanja opisane su na stranici usluge [manipulacije robom]({{< relref "/servizi/handling" >}}); posebni zahtjevi segmenta na stranici sektora [e-commerce]({{< relref "/settori/ecommerce" >}}).

## Cut-off i vrijeme preuzimanja

**Cut-off** je krajnje vrijeme do kojeg se primljena narudžba otprema istoga dana. Izračunava se unatrag od vremena preuzimanja kurirske službe: ako kurir dolazi u 17 sati, a skladištu su u prosjeku potrebna dva sata za komisioniranje, pakiranje i okrupnjavanje koleta jednog vala narudžbi, cut-off ne može biti kasnije od 15 sati, a u vršnim danima treba ga pomaknuti ranije ili povećati broj osoblja.

Tri elementa pomiču cut-off:

- **broj preuzimanja** dnevno i vrijeme zadnjeg preuzimanja, dogovoreno sa svakom kurirskom službom;
- **produktivnost komisioniranja**, koja ovisi o organizaciji lokacija: najprodavaniji artikli trebaju biti smješteni blizu zone pakiranja;
- **kvaliteta podataka** o masi i dimenzijama, koji bez ručnog mjerenja određuju kutiju i tarifu kurirske službe.

Ugovor o usluzi mora navesti cut-off i pokazatelj kojim se on mjeri, primjerice postotak narudžbi primljenih do krajnjeg vremena i otpremljenih istoga dana. O toj temi vidi vodič o [ugovoru o logistici za treće strane i KPI-jevima]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kurirske službe i zemljopis Lazija

Trgovac može koristiti vlastite ugovore s ekspresnim kurirskim službama ili one koje je ugovorio logistički operater. Nacionalne kurirske službe preuzimaju robu u skladištu i razvrstavaju kolete u svojim sortirnim centrima; za regionalne B2B isporuke ili za mali broj teških koleta operater može koristiti vlastiti vozni park.

Za skladište u Latina Scalu cestovne udaljenosti prema glavnim područjima potražnje, izračunate alatom za izračun rute OSRM za osobni automobil u uobičajenim prometnim uvjetima, jesu sljedeće:

| Odredište | Cestovna udaljenost | Procijenjeno vrijeme |
|---|---|---|
| Latina, središte | oko 8 km | oko 13 minuta |
| Aprilia | oko 34 km | oko 36 minuta |
| Pomezia | oko 50 km | oko 50 minuta |
| Santa Palomba | oko 55 km | oko 57 minuta |
| Castel Romano | oko 57 km | oko 56 minuta |
| Rim, EUR | oko 70 km | oko 70 minuta |
| Rim, Ostiense | oko 74 km | oko 76 minuta |
| Fiumicino | oko 90 km | oko 86 minuta |

Za teška vozila i u vršnim satima vremena su dulja. Glavna prometnica prema Rimu je državna cesta 148 Pontina, s dva odvojena kolnika između Rima i Borgo Piavea; na dionici između Pomezije i Latine sjever ograničenje brzine smanjeno je sa 110 na 80 km/h. Opisi pojedinih zona nalaze se na stranicama [logistika u Rimu]({{< relref "/logistica/roma" >}}), [južni Rim]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) i [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Povrati

**Pravo potrošača na jednostrani raskid ugovora** uređeno je talijanskim Zakonom o zaštiti potrošača (Codice del Consumo, D.Lgs. 206/2005). Članak 52. daje 14 dana za raskid bez obrazloženja, u pravilu od isporuke robe. Članak 56. obvezuje prodavatelja na povrat novca u roku od 14 dana od raskida, uz mogućnost zadržavanja povrata do primitka robe ili dokaza o otpremi.

Skladište stoga mora upravljati povratima u rokovima usklađenima s tim rokovima:

- **prijem i evidentiranje** povrata s izvornim brojem narudžbe;
- **kontrola** stanja proizvoda i ambalaže prema kriterijima dogovorenima s trgovcem;
- **daljnje postupanje**: vraćanje na zalihu, obnavljanje, prepakiravanje, prodaja kao roba druge klase ili zbrinjavanje;
- **obavijest** o ishodu platformi radi odobravanja povrata novca.

Posebna zona za povrate, odvojena od prodajne zalihe, sprječava da nekontrolirana roba ponovno postane dostupna za narudžbe.

## Sezonski vrhunci i kapacitet

E-commerce koncentrira količine u nekoliko razdoblja godine, vezanih uz promocije i blagdane. Za operatera to znači planiranje dodatnog osoblja, rezervnih lokacija i dogovora s kurirskim službama o dodatnim preuzimanjima. Za trgovca to znači unaprijed dostaviti prognoze prodaje i kalendare promocija: nenajavljeni vrhunac najčešći je uzrok nepoštivanja cut-offa.

## Lokacija u Latina Scalu

Consorzio Logistico Latina Scalo u ulici Via della Dinamica u Latina Scalu (LT) raspolaže s 19.000 četvornih metara natkrivenog prostora i sustavom WMS za upravljanje skladištem. Usluge obuhvaćaju skladištenje, komisioniranje, pakiranje, označavanje i paletizaciju, cestovni prijevoz vlastitim voznim parkom i distribuciju zadnje milje, uz upravljanje dokumentacijom. Prema navodima Consorzia, rad se odvija 24 sata dnevno, 7 dana u tjednu. Načine integracije s pojedinim prodajnim platformama treba provjeriti u fazi izrade ponude. Za distribuciju u Rimu vidi analizu o [zadnjoj milji prema južnom Rimu]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Izvori

- AGI, gospodarska vijest od 27. svibnja 2025. o internetskoj kupnji proizvoda u 2025., podaci Osservatorio eCommerce B2c Netcomm – Politecnico di Milano: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), čl. 52. i 56.: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Udaljenosti i vremena: izračun rute OSRM (Open Source Routing Machine) od lokacije u ulici Via della Dinamica, osobni automobil, uobičajen promet; obrada Consorzio Logistico Latina Scalo.
- SS148 Pontina, kolnici i ograničenja brzine: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (podaci ANAS-a)
- Usluge i rad: izjave Consorzio Logistico Latina Scalo.
