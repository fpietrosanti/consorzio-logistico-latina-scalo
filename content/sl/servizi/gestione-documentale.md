---
linkTitle: "Upravljanje dokumentacije"
title: "Upravljanje dokumentacije in WMS za logistiko v kraju Latina Scalo"
description: "Upravljanje dokumentacije v kraju Latina Scalo (LT): dobavnice DDT, sledljivost premikov v sistemu WMS in integracija s poslovnimi sistemi naročnikov."
url: "/sl/storitve/upravljanje-dokumentacije/"
layout: "servizio"
weight: 8
image: "topics/inventario-barcode"
imageAlt: "Operater evidentira tovorek v skladišču s prenosnim terminalom, arhivska fotografija"
faq:
  - q: "Katere dokumente upravlja Consorzio Logistico Latina Scalo?"
    a: "Consorzio Logistico Latina Scalo za naročnike upravlja prevozne dokumente (DDT) in dobavnice, evidentiranje skladiščnih premikov in sledljivost enot od prevzema do odpreme, z integracijo s poslovnimi informacijskimi sistemi strank."
  - q: "Ali Consorzio Logistico Latina Scalo uporablja WMS?"
    a: "Da. Consorzio Logistico Latina Scalo uporablja sistem WMS (programska oprema za upravljanje skladišča) za evidentiranje lokacij, zalog in premikov. V središču v kraju Latina Scalo sistem deluje prek namenske optične povezave in industrijskega Wi-Fi v skladiščnih prostorih."
  - q: "Ali se WMS Consorzio Logistico Latina Scalo povezuje s poslovnim sistemom stranke?"
    a: "Consorzio Logistico Latina Scalo predvideva integracijo med svojim sistemom WMS in poslovnimi sistemi naročnikov za izmenjavo matičnih podatkov, obvestil o prispetju, naročil in potrditev. Format, pogostost in način prenosa podatkov se določijo ob zagonu storitve."
  - q: "Kako deluje sledljivost blaga v kraju Latina Scalo?"
    a: "V središču Consorzio Logistico Latina Scalo se vsaka tovorna enota ob prevzemu evidentira v sistemu WMS in poveže s šifro artikla, količino, lokacijo in na zahtevo s serijo. Vsak nadaljnji premik do odpreme ostane zabeležen, tako da je mogoče rekonstruirati pot blaga."
  - q: "Kateri podatki so potrebni za vzpostavitev upravljanja dokumentacije s Consorzio Logistico Latina Scalo?"
    a: "Za vzpostavitev upravljanja dokumentacije Consorzio Logistico Latina Scalo potrebuje podatke o poslovnem sistemu, ki ga uporablja naročnik, formatu izmenjanih podatkov, dokumentih, ki jih je treba izdati, podatkih o seriji ali roku uporabnosti, ki jih je treba slediti, in pogostosti poročil o zalogah in premikih."
---

## Dokumenti, podatki in sledljivost v isti storitvi

Consorzio Logistico Latina Scalo za naročnike upravlja dokumentacijski in informacijski del logistike: izdajo prevoznih dokumentov (DDT, italijanska dobavnica) in dobavnic, evidentiranje skladiščnih premikov v sistemu WMS (programska oprema za upravljanje skladišča), sledljivost tovornih enot in integracijo s poslovnimi informacijskimi sistemi strank. Storitev spremlja [skladiščenje]({{< relref "/servizi/stoccaggio" >}}), [manipulacijo]({{< relref "/servizi/handling" >}}) in [prevoz]({{< relref "/servizi/trasporto" >}}), ki se opravljajo v središču na ulici Via della Dinamica, v območju Tor Tre Ponti, v kraju Latina Scalo (LT).

V središču WMS deluje prek namenske optične povezave in industrijskega Wi-Fi v skladiščnih prostorih; v pisarnah in sejnih sobah je osebje, ki usklajuje dokumente in informacijske tokove.

## Prevozni dokumenti in dobavnice

### Ob prevzemu

Ob prevzemu operater primerja blago z dobavnico DDT dobavitelja in z obvestilom o prispetju naročnika. Razlike med navedenimi in prejetimi količinami ter morebitne poškodbe se zabeležijo kot pridržki na dokumentu prevoznika in sporočijo naročniku s sklicem na dostavo.

### Ob odpremi

Ob nakladanju Konzorcij v imenu naročnika izda prevozni dokument s prejemnikom, opisom blaga, številom tovorkov in maso. Kopija, ki jo podpiše prejemnik, se ob koncu dostave, če jo opravi lastni vozni park, vrne Konzorciju in arhivira skupaj s podatki o pošiljki.

## WMS in sledljivost

### Evidentiranje enot

Vsaka sprejeta tovorna enota se evidentira v sistemu WMS in poveže s šifro artikla, količino in lokacijo. Kadar to zahteva naročnik, evidenca obsega tudi serijo in rok uporabnosti, ki sta potrebna v dobavnih verigah [agroživilstva]({{< relref "/settori/agroalimentare" >}}) in [farmacije]({{< relref "/settori/farmaceutico" >}}).

### Premiki

Sistem beleži vsak nadaljnji premik: uskladiščenje, dopolnjevanje komisionirnih con, komisioniranje po naročilu, storitve z dodano vrednostjo, nakladanje. Tako je mogoče rekonstruirati pot enote ali serije od prevzema do odpreme, kar je koristno tudi v primeru odpoklica izdelka ali spora s stranko.

### Inventura

Evidentirane zaloge se redno primerjajo s fizičnim štetjem po dogovorjenem koledarju. Razlike se sporočijo naročniku s podrobnostmi o artiklu, seriji in lokaciji.

## Integracija s poslovnimi sistemi

Izmenjava podatkov med poslovnim sistemom naročnika (ERP) in sistemom WMS Konzorcija običajno zajema štiri tokove:

- **matični podatki**: šifre artiklov, opisi, enote pakiranja, mere in mase;
- **obvestila o prispetju**: pričakovano blago, z dobaviteljem, količino in predvidenim datumom;
- **izhodna naročila**: vrstice naročil, prejemniki in datumi dostave;
- **potrditve**: opravljeni prevzemi z morebitnimi pridržki, posodobljene zaloge, odpremljene pošiljke s sklici na dokumente.

Format datotek, kanal prenosa in pogostost izmenjav se določijo v projektu zagona, na podlagi sistema, ki ga uporablja naročnik. V začetnih fazah ali pri manjših količinah lahko izmenjave potekajo tudi s standardnimi datotekami, poslanimi ob dogovorjenih urah.

## Poročanje

Naročnik v dogovorjenih časovnih presledkih prejema podatke o zalogah, prevzemih, odpremah in nepravilnostih. Vsebina poročil se določi glede na potrebe nadzora naročnika, na primer obračanje artiklov, serije, ki se jim izteka rok uporabnosti, ali izvršena naročila po obdobjih.

## Zagon storitve

Zagon obsega štiri korake: zbiranje matičnih podatkov in formatov dokumentov; določitev podatkovnih tokov in odgovornosti; preizkus izmenjav na vzorcu naročil; prehod v redno obratovanje s spremljanjem prvih tednov. Storitev je del modela [pogodbene logistike (3PL)]({{< relref "/servizi/logistica-3pl" >}}) in velja tudi za [cross-docking]({{< relref "/servizi/cross-docking" >}}) in [storitve z dodano vrednostjo]({{< relref "/servizi/lavorazioni-valore-aggiunto" >}}).

## Panoge in območje

Sledljivost po serijah je pomembna zlasti za agroživilstvo in farmacijo; integracija naročil je osrednja za [e-trgovino]({{< relref "/settori/ecommerce" >}}) in za [veliko trgovino na drobno in maloprodajo]({{< relref "/settori/gdo-retail" >}}), upravljanje šifer in različic pa zadeva [tekstil in modo]({{< relref "/settori/tessile-moda" >}}) ter [avtomobilsko industrijo]({{< relref "/settori/automotive" >}}). Središče oskrbuje podjetja iz krajev [Latina]({{< relref "/logistica/latina" >}}), [Aprilia]({{< relref "/logistica/aprilia" >}}), [Cisterna di Latina]({{< relref "/logistica/cisterna-di-latina" >}}) in [Pomezia]({{< relref "/logistica/pomezia" >}}) ter z območij [pokrajine Latina]({{< relref "/logistica/provincia-di-latina" >}}) in [južnega Rima]({{< relref "/logistica/roma-sud" >}}).

## Za ponudbo

Za ponudbo za upravljanje dokumentacije je treba navesti uporabljeni poslovni sistem, format podatkov, ki jih naročnik lahko pošilja in prejema, dokumente, ki jih je treba izdati, podatke o seriji ali roku uporabnosti, ki jih je treba slediti, povprečno število naročil na dan in pogostost zahtevanih poročil. Povpraševanja se pošiljajo prek [kontaktnega obrazca]({{< relref "/" >}}#contatti).
