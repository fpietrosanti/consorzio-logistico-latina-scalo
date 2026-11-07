---
title: "E-commerce fulfillment v Laciju: tokovi, cut-off, vračila in kurirji"
description: "Izpolnjevanje spletnih naročil za trgovca iz Lacija: od prevzema do odpreme, končni roki, vračila, kurirji in cestne razdalje od Rima."
date: 2026-10-02
url: "/sl/analize/e-commerce-fulfillment-lacij/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Notranjost distribucijskega centra s paketi, pripravljenimi za odpremo, arhivska fotografija"
summary: "Izpolnjevanje spletnih naročil, zaupano izvajalcu za tretje osebe, poteka po standardnem toku: povezava naročil, odvzem, pakiranje, predaja kurirju in upravljanje vračil. Za trgovca iz Lacija so odločilne spremenljivke končni rok za sprejem naročil, čas prevzema pri kurirjih in cestna razdalja do rimskega gravitacijskega območja."
faq:
  - q: "Kaj je cut-off pri e-commerce fulfillmentu?"
    a: "To je končni čas, do katerega se naročilo, ki ga prejme skladišče, odpremi isti dan. Odvisen je od časa prevzema pri kurirju in od časa, potrebnega za odvzem in pakiranje; naročila, prejeta po cut-offu, se odpremijo naslednji delovni dan."
  - q: "Koliko časa ima potrošnik za vračilo izdelka, kupljenega na spletu?"
    a: "Italijanski zakonik o varstvu potrošnikov (Codice del Consumo, D.Lgs. 206/2005, čl. 52) potrošniku priznava 14 dni za uveljavljanje pravice do odstopa od pogodbe brez navedbe razlogov, praviloma od dobave blaga. Prodajalec povrne kupnino v 14 dneh od odstopa in lahko vračilo zadrži, dokler ne prejme blaga ali dokazila o odpremi."
  - q: "Kako daleč je Latina Scalo od Rima za spletne dostave?"
    a: "Po izračunu poti OSRM za osebni avtomobil je lokacija na Via della Dinamica oddaljena približno 70 km od četrti EUR (približno 70 minut), približno 50 km od Pomezie (približno 50 minut) in približno 34 km od Aprilie (približno 36 minut). Za tovorna vozila so časi daljši."
  - q: "Kolikšna je vrednost spletne prodaje izdelkov v Italiji?"
    a: "Po podatkih Osservatorio eCommerce B2c Netcomm milanske politehnike so spletni nakupi izdelkov v Italiji leta 2025 ocenjeni na približno 40,1 milijarde evrov, kar je 6 % več kot leta 2024 in 11,2 % vseh nakupov izdelkov."
  - q: "Kateri podatki so potrebni za zagon storitve fulfillmenta?"
    a: "Število artiklov (SKU), mere in mase, povprečno in največje število naročil na dan, vrstice na naročilo, pričakovani delež vračil, uporabljeni kurirji, prodajna platforma in način izmenjave naročil, zahteve za pakiranje in promocijsko gradivo."
---

Izpolnjevanje spletnih naročil (fulfillment) je segment logistike za tretje osebe z najbolj razdrobljenim operativnim profilom: veliko majhnih naročil, ena ali dve vrstici na naročilo, odprema posameznih paketov in delež vračil, ki je višji kot v tradicionalni trgovini. Po podatkih Osservatorio eCommerce B2c Netcomm milanske politehnike (Politecnico di Milano), ki jih je 27. maja 2025 navedla agencija AGI, so spletni nakupi izdelkov v Italiji leta 2025 ocenjeni na približno 40,1 milijarde evrov, kar je 6 % več kot leta 2024 in 11,2 % vseh nakupov izdelkov.

Za trgovca iz Lacija je izbira skladišča odvisna od nekaj merljivih parametrov: končnega roka za naročila, časa prevzema pri kurirjih, upravljanja vračil in cestne razdalje do končnih kupcev in središč kurirskih služb.

## Tok od naročila do dostave

Cikel spletnega naročila, ki ga upravlja izvajalec za tretje osebe, sestavlja sedem korakov:

1. **prevzem blaga** od dobavitelja ali proizvajalca, s količinskim pregledom, evidentiranjem artiklov (SKU) in uskladiščenjem;
2. **povezava naročil**: naročila iz prodajne platforme prispejo v izvajalčev WMS (sistem za upravljanje skladišča) prek povezovalnika, datoteke ali informacijskega vmesnika;
3. **odvzem (picking)**, praviloma po kosih, z združevanjem več naročil v en obhod odvzema za skrajšanje poti;
4. **pregled in pakiranje (packing)**, z izbiro škatle, polnilom, vstavljanjem dokumentov in promocijskega gradiva;
5. **etiketiranje** s tovornim listom kurirja in ustvarjanje kode za sledenje;
6. **predaja kurirju** ob načrtovanem prevzemu in posredovanje podatkov za sledenje platformi;
7. **upravljanje vračil**: prevzem, pregled, odločitev o nadaljnji usodi izdelka in posodobitev zaloge.

Dejavnosti odvzema, pakiranja in etiketiranja so opisane na strani storitve [manipulacije]({{< relref "/servizi/handling" >}}); posebne potrebe segmenta na strani panoge [e-commerce]({{< relref "/settori/ecommerce" >}}).

## Cut-off in čas prevzema

**Cut-off** je čas, do katerega se prejeto naročilo odpremi isti dan. Izračuna se nazaj od časa prevzema pri kurirju: če kurir pride ob 17. uri in skladišče v povprečju potrebuje dve uri za odvzem, pakiranje in združitev paketov enega vala naročil, cut-off ne more biti pozneje kot ob 15. uri, ob konicah pa ga je treba pomakniti naprej ali povečati število osebja.

Trije dejavniki premikajo cut-off:

- **število prevzemov** na dan in čas zadnjega prevzema, dogovorjen z vsakim kurirjem;
- **produktivnost odvzema**, ki je odvisna od organizacije lokacij: najbolje prodajani artikli morajo biti blizu prostora za pakiranje;
- **kakovost podatkov** o masi in merah, ki brez ročnega merjenja določajo škatlo in tarifo kurirja.

Pogodba o storitvi mora navajati cut-off in kazalnik, ki ga meri, na primer delež naročil, prejetih do končnega roka in odpremljenih isti dan. Na to temo glejte vodnik o [pogodbi o logistiki za tretje osebe in kazalnikih KPI]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kurirji in geografija Lacija

Trgovec lahko uporablja lastne pogodbe s kurirskimi službami ali pogodbe, ki jih je izpogajal logistični izvajalec. Nacionalni kurirji prevzemajo v skladišču in pakete razvrščajo v svojih središčih; za regionalne dostave B2B ali dostave majhnega števila težkih kosov lahko izvajalec uporabi lasten vozni park.

Za skladišče v Latina Scalo so cestne razdalje do glavnih območij povpraševanja, izračunane z usmerjevalnikom OSRM za osebni avtomobil v običajnih prometnih razmerah, naslednje:

| Namembni kraj | Cestna razdalja | Ocenjeni čas |
|---|---|---|
| Latina, središče | približno 8 km | približno 13 minut |
| Aprilia | približno 34 km | približno 36 minut |
| Pomezia | približno 50 km | približno 50 minut |
| Santa Palomba | približno 55 km | približno 57 minut |
| Castel Romano | približno 57 km | približno 56 minut |
| Rim EUR | približno 70 km | približno 70 minut |
| Rim Ostiense | približno 74 km | približno 76 minut |
| Fiumicino | približno 90 km | približno 86 minut |

Za tovorna vozila in v prometnih konicah so časi daljši. Glavna os proti Rimu je državna cesta 148 Pontina z dvema ločenima voziščema med Rimom in Borgo Piave; na odseku med Pomezio in Latino sever je bila omejitev hitrosti znižana s 110 na 80 km/h. Opisi posameznih območij so na straneh [logistika v Rimu]({{< relref "/logistica/roma" >}}), [južni Rim]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) in [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Vračila

**Pravico potrošnika do odstopa od pogodbe** ureja italijanski zakonik o varstvu potrošnikov (Codice del Consumo, D.Lgs. 206/2005). Čl. 52 priznava 14 dni za odstop brez navedbe razloga, praviloma od dobave blaga. Čl. 56 prodajalcu nalaga vračilo kupnine v 14 dneh od odstopa, z možnostjo, da vračilo zadrži do prejema blaga ali dokazila o odpremi.

Skladišče mora zato vračila obdelovati v rokih, združljivih s temi roki:

- **prevzem in evidentiranje** vračila s številko prvotnega naročila;
- **pregled** stanja izdelka in embalaže po merilih, dogovorjenih s trgovcem;
- **nadaljnja usoda**: vrnitev v zalogo, obnova, prepakiranje, prodaja kot blago drugega razreda ali odstranitev;
- **sporočilo** o izidu platformi za sprostitev vračila kupnine.

Namenski prostor za vračila, ločen od prodajne zaloge, preprečuje, da bi nepregledano blago spet postalo na voljo za naročila.

## Sezonske konice in zmogljivost

Spletna prodaja zgošča količine v nekaj obdobij v letu, povezanih s promocijami in prazniki. Za izvajalca to pomeni predvideti dodatno osebje, rezervne lokacije in dogovore s kurirji o dodatnih prevzemih. Za trgovca pomeni vnaprej sporočiti napovedi prodaje in koledarje promocij: nenapovedana konica je najpogostejši vzrok za nespoštovanje cut-offa.

## Lokacija v Latina Scalo

Consorzio Logistico Latina Scalo na Via della Dinamica v Latina Scalo (LT) ima 19.000 kvadratnih metrov pokritih površin in sistem WMS za upravljanje skladišča. Storitve obsegajo skladiščenje, odvzem, pakiranje, etiketiranje in paletizacijo, cestni prevoz z lastnim voznim parkom in distribucijo na zadnjem kilometru ter upravljanje dokumentacije. Po navedbah Consorzio obratovanje poteka 24 ur na dan, 7 dni v tednu. Načine povezave s posameznimi prodajnimi platformami je treba preveriti v fazi priprave ponudbe. Za distribucijo v Rim glejte analizo o [zadnjem kilometru proti južnemu Rimu]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Viri

- AGI, gospodarska novica z dne 27. maja 2025 o spletnih nakupih izdelkov v letu 2025, podatki Osservatorio eCommerce B2c Netcomm – Politecnico di Milano: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), artt. 52 e 56: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Razdalje in časi: izračun poti OSRM (Open Source Routing Machine) od lokacije na Via della Dinamica, osebni avtomobil, običajen promet; obdelava Consorzio.
- SS148 Pontina, vozišča in omejitve hitrosti: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (podatki ANAS)
- Storitve in obratovanje: izjave Consorzio Logistico Latina Scalo.
