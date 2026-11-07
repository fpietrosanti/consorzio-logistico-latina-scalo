---
linkTitle: "Upravljanje dokumentacijom"
title: "Upravljanje dokumentacijom i WMS za logistiku u mjestu Latina Scalo"
description: "Upravljanje dokumentacijom u mjestu Latina Scalo (LT): DDT i dostavnice, sljedivost kretanja u sustavu WMS i integracija s poslovnim sustavima naručitelja."
url: "/hr/usluge/upravljanje-dokumentacijom/"
layout: "servizio"
weight: 8
image: "topics/inventario-barcode"
imageAlt: "Djelatnik evidentira koleto u skladištu ručnim terminalom, arhivska fotografija"
faq:
  - q: "Kojom dokumentacijom upravlja Consorzio Logistico Latina Scalo?"
    a: "Consorzio Logistico Latina Scalo za naručitelje upravlja prijevoznim ispravama (DDT, talijanske otpremnice) i dostavnicama, evidencijom skladišnih kretanja i sljedivošću jedinica od zaprimanja do otpreme, uz integraciju s poslovnim sustavima klijenata."
  - q: "Koristi li Consorzio Logistico Latina Scalo WMS?"
    a: "Da. Consorzio Logistico Latina Scalo koristi sustav WMS (softver za upravljanje skladištem) za evidenciju lokacija, zaliha i kretanja. U središtu u mjestu Latina Scalo sustav radi preko namjenske optičke veze i industrijskog Wi-Fija u skladišnim prostorima."
  - q: "Integrira li se WMS Consorzio Logistico Latina Scalo s poslovnim sustavom klijenta?"
    a: "Consorzio Logistico Latina Scalo predviđa integraciju vlastitog sustava WMS s poslovnim sustavima naručitelja za razmjenu matičnih podataka, najava dolaska, narudžbi i potvrda. Format, učestalost i način prijenosa podataka utvrđuju se pri pokretanju usluge."
  - q: "Kako funkcionira sljedivost robe u mjestu Latina Scalo?"
    a: "U središtu Consorzio Logistico Latina Scalo svaka jedinica tereta evidentira se u sustavu WMS pri zaprimanju i povezuje sa šifrom artikla, količinom, lokacijom i, na zahtjev, serijom. Svako daljnje premještanje do otpreme ostaje zabilježeno, tako da se put robe može rekonstruirati."
  - q: "Koji su podaci potrebni za uspostavu upravljanja dokumentacijom s Consorzio Logistico Latina Scalo?"
    a: "Za uspostavu upravljanja dokumentacijom Consorzio Logistico Latina Scalo traži podatak o poslovnom sustavu koji naručitelj koristi, format razmjenjivanih podataka, isprave koje treba izdavati, podatke o seriji ili roku trajanja koje treba pratiti i učestalost izvješća o zalihama i kretanjima."
---

## Dokumentacija, podaci i sljedivost u istoj usluzi

Consorzio Logistico Latina Scalo za naručitelje upravlja dokumentacijskim i informacijskim dijelom logistike: izdavanjem prijevoznih isprava (DDT, talijanska otpremnica) i dostavnica, evidencijom skladišnih kretanja u sustavu WMS (softver za upravljanje skladištem), sljedivošću jedinica tereta i integracijom s poslovnim sustavima klijenata. Usluga prati [skladištenje]({{< relref "/servizi/stoccaggio" >}}), [manipulaciju]({{< relref "/servizi/handling" >}}) i [prijevoz]({{< relref "/servizi/trasporto" >}}) koji se obavljaju u središtu u ulici Via della Dinamica, u zoni Tor Tre Ponti, u mjestu Latina Scalo (LT).

U središtu WMS radi preko namjenske optičke veze i industrijskog Wi-Fija u skladišnim prostorima; u uredima i salama za sastanke smješteno je osoblje koje koordinira dokumentaciju i informacijske tokove.

## Prijevozne isprave i dostavnice

### Na ulazu

Pri zaprimanju djelatnik uspoređuje robu s DDT-om dobavljača i s najavom dolaska naručitelja. Razlike između prijavljenih i zaprimljenih količina, kao i eventualna oštećenja, bilježe se kao primjedbe na ispravi prijevoznika i dojavljuju naručitelju s oznakom isporuke.

### Na izlazu

Pri utovaru Konzorcij u ime naručitelja izdaje prijevoznu ispravu s primateljem, opisom robe, brojem koleta i masom. Primjerak koji je potpisao primatelj vraća se Konzorciju po završetku isporuke, ako ju je obavio vlastiti vozni park, i arhivira se zajedno s podacima o pošiljci.

## WMS i sljedivost

### Evidentiranje jedinica

Svaka prihvaćena jedinica tereta evidentira se u sustavu WMS i povezuje sa šifrom artikla, količinom i lokacijom. Kada to naručitelj zatraži, evidencija obuhvaća i seriju i rok trajanja, potrebne u [agroprehrambenom]({{< relref "/settori/agroalimentare" >}}) i [farmaceutskom]({{< relref "/settori/farmaceutico" >}}) lancu opskrbe.

### Kretanja

Sustav bilježi svako daljnje premještanje: smještaj, dopunu zona izuzimanja, izuzimanje po narudžbi, usluge obrade, utovar. Tako se može rekonstruirati put jedinice ili serije od zaprimanja do otpreme, što je korisno i u slučaju povlačenja proizvoda ili spora s kupcem.

### Inventura

Evidentirane zalihe periodično se uspoređuju s fizičkim stanjem, prema dogovorenom rasporedu. Razlike se dojavljuju naručitelju s pojedinostima o artiklu, seriji i lokaciji.

## Integracija s poslovnim sustavima

Razmjena podataka između poslovnog sustava naručitelja (ERP) i Konzorcijeva sustava WMS u pravilu obuhvaća četiri toka:

- **matični podaci**: šifre artikala, opisi, jedinice pakiranja, dimenzije i mase;
- **najave dolaska**: očekivana roba, s dobavljačem, količinom i predviđenim datumom;
- **izlazni nalozi**: stavke narudžbi, primatelji i datumi isporuke;
- **potvrde**: obavljena zaprimanja s eventualnim primjedbama, ažurirane zalihe, otpremljene pošiljke s oznakama isprava.

Format datoteka, kanal prijenosa i učestalost razmjene utvrđuju se u projektu pokretanja, na temelju sustava koji naručitelj koristi. U početnim fazama, ili pri manjim količinama, razmjena se može obavljati i standardnim datotekama koje se šalju u dogovoreno vrijeme.

## Izvješćivanje

Naručitelj u dogovorenim razmacima prima podatke o zalihama, ulazima, izlazima i odstupanjima. Sadržaj izvješća utvrđuje se prema potrebama kontrole naručitelja, primjerice obrtaj artikala, serije kojima uskoro istječe rok ili izvršene narudžbe po razdoblju.

## Pokretanje usluge

Pokretanje obuhvaća četiri koraka: prikupljanje matičnih podataka i formata isprava; utvrđivanje tokova podataka i odgovornosti; probu razmjene na uzorku narudžbi; prelazak u redovan rad uz praćenje prvih tjedana. Usluga je dio modela [ugovorne logistike (3PL)]({{< relref "/servizi/logistica-3pl" >}}) i primjenjuje se i na [cross-docking]({{< relref "/servizi/cross-docking" >}}) i [usluge dodane vrijednosti]({{< relref "/servizi/lavorazioni-valore-aggiunto" >}}).

## Sektori i područje

Sljedivost po seriji važna je osobito za agroprehrambeni i farmaceutski sektor; integracija narudžbi ključna je za [e-trgovinu]({{< relref "/settori/ecommerce" >}}) te za [veliku maloprodaju i maloprodaju]({{< relref "/settori/gdo-retail" >}}), dok se upravljanje šiframa i varijantama odnosi na [tekstil i modu]({{< relref "/settori/tessile-moda" >}}) i [automobilsku industriju]({{< relref "/settori/automotive" >}}). Središte opslužuje tvrtke iz [Latine]({{< relref "/logistica/latina" >}}), [Aprilije]({{< relref "/logistica/aprilia" >}}), mjesta [Cisterna di Latina]({{< relref "/logistica/cisterna-di-latina" >}}) i [Pomezije]({{< relref "/logistica/pomezia" >}}), kao i područja [pokrajine Latina]({{< relref "/logistica/provincia-di-latina" >}}) i [južnog Rima]({{< relref "/logistica/roma-sud" >}}).

## Za ponudu

Za ponudu za upravljanje dokumentacijom navesti poslovni sustav koji se koristi, format podataka koje naručitelj može slati i primati, isprave koje treba izdavati, podatke o seriji ili roku trajanja koje treba pratiti, prosječan broj narudžbi dnevno i traženu učestalost izvješća. Zahtjevi se šalju putem [kontaktnog obrasca]({{< relref "/" >}}#contatti).
