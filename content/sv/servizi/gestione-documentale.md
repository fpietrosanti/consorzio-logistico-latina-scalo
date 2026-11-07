---
linkTitle: "Dokumenthantering"
title: "Dokumenthantering och WMS för logistik i Latina Scalo"
description: "Dokumenthantering i Latina Scalo (LT): DDT och följesedlar, spårbarhet för rörelser i WMS och integration med uppdragsgivarnas affärssystem."
url: "/sv/tjanster/dokumenthantering/"
layout: "servizio"
weight: 8
image: "topics/inventario-barcode"
imageAlt: "Operatör som registrerar ett kolli i lagret med en handterminal, arkivbild"
faq:
  - q: "Vilka dokument hanterar Consorzio Logistico Latina Scalo?"
    a: "Consorzio Logistico Latina Scalo hanterar på uppdragsgivarnas vägnar transportdokument (DDT) och följesedlar, registreringen av lagerrörelser och spårbarheten för enheterna från mottagning till utleverans, med integration mot kundernas affärssystem."
  - q: "Använder Consorzio Logistico Latina Scalo ett WMS?"
    a: "Ja. Consorzio Logistico Latina Scalo använder ett WMS (lagerstyrningssystem) för att registrera lagerplatser, saldon och rörelser. Vid anläggningen i Latina Scalo körs systemet över dedikerad fiberanslutning och industriellt Wi-Fi i lagerytorna."
  - q: "Kan WMS hos Consorzio Logistico Latina Scalo integreras med kundens affärssystem?"
    a: "Consorzio Logistico Latina Scalo planerar för integration mellan sitt WMS och uppdragsgivarnas affärssystem för utbyte av grunddata, ankomstaviseringar, order och bekräftelser. Dataformat, frekvens och överföringssätt fastställs vid tjänstens uppstart."
  - q: "Hur fungerar spårbarheten för godset i Latina Scalo?"
    a: "Vid anläggningen hos Consorzio Logistico Latina Scalo registreras varje lastbärare i WMS vid mottagningen och kopplas till artikelnummer, kvantitet, lagerplats och vid behov batch. Varje efterföljande förflyttning fram till utleverans registreras, så att godsets väg kan rekonstrueras."
  - q: "Vilka uppgifter behövs för att lägga upp dokumenthanteringen med Consorzio Logistico Latina Scalo?"
    a: "För att lägga upp dokumenthanteringen efterfrågar Consorzio Logistico Latina Scalo vilket affärssystem uppdragsgivaren använder, formatet för de data som utbyts, vilka dokument som ska utfärdas, vilka batch- eller utgångsdata som ska spåras och hur ofta rapporter om saldon och rörelser ska lämnas."
---

## Dokument, data och spårbarhet i samma tjänst

Consorzio Logistico Latina Scalo hanterar på uppdragsgivarnas vägnar logistikens dokument- och informationsdel: utfärdande av transportdokument (DDT, italienska följesedlar) och följesedlar, registrering av lagerrörelser i WMS (lagerstyrningssystemet), spårbarhet för lastbärarna och integration med kundernas affärssystem. Tjänsten kompletterar [lagringen]({{< relref "/servizi/stoccaggio" >}}), [godshanteringen]({{< relref "/servizi/handling" >}}) och [transporten]({{< relref "/servizi/trasporto" >}}) vid anläggningen på Via della Dinamica, i området Tor Tre Ponti i Latina Scalo (LT).

Vid anläggningen körs WMS över dedikerad fiberanslutning och industriellt Wi-Fi i lagerytorna; kontor och mötesrum rymmer den personal som samordnar dokument och informationsflöden.

## Transportdokument och följesedlar

### Vid inleverans

Vid mottagningen jämför operatören godset med leverantörens DDT och med uppdragsgivarens ankomstavisering. Skillnader mellan angivna och mottagna kvantiteter, liksom eventuella skador, antecknas som förbehåll på transportörens dokument och meddelas uppdragsgivaren med leveransens referens.

### Vid utleverans

Vid lastningen utfärdar konsortiet transportdokumentet på uppdragsgivarens vägnar, med mottagare, varubeskrivning, antal kollin och vikt. Det av mottagaren underskrivna exemplaret återkommer till konsortiet efter leveransen, om den har utförts med den egna fordonsflottan, och arkiveras tillsammans med sändningsuppgifterna.

## WMS och spårbarhet

### Registrering av enheter

Varje mottagen lastbärare registreras i WMS och kopplas till artikelnummer, kvantitet och lagerplats. När uppdragsgivaren begär det omfattar registreringen även batch och bäst före-datum, vilket krävs inom [livsmedels-]({{< relref "/settori/agroalimentare" >}}) och [läkemedelskedjorna]({{< relref "/settori/farmaceutico" >}}).

### Rörelser

Systemet registrerar varje efterföljande förflyttning: inlagring, påfyllning av plockplatser, plockning per order, bearbetning och lastning. På så sätt kan en enhets eller en batchs väg rekonstrueras från mottagning till utleverans, vilket också är användbart vid en produktåterkallelse eller en tvist med en kund.

### Inventering

De registrerade saldona jämförs regelbundet med den fysiska räkningen, enligt avtalat schema. Avvikelser rapporteras till uppdragsgivaren med uppgift om artikel, batch och lagerplats.

## Integration med affärssystem

Datautbytet mellan uppdragsgivarens affärssystem (ERP) och konsortiets WMS omfattar normalt fyra flöden:

- **grunddata**: artikelnummer, beskrivningar, förpackningsenheter, mått och vikter;
- **ankomstaviseringar**: förväntat gods, med leverantör, kvantitet och beräknat datum;
- **utleveransorder**: orderrader, mottagare och leveransdatum;
- **bekräftelser**: utförda mottagningar med eventuella förbehåll, uppdaterade saldon, avgångna sändningar med dokumentreferenser.

Filformat, överföringskanal och frekvens för utbytet fastställs i uppstartsprojektet, utifrån det system som uppdragsgivaren använder. I inledningsskedet, eller vid mindre volymer, kan utbytet också ske med standardfiler som skickas vid avtalade tidpunkter.

## Rapportering

Uppdragsgivaren får med avtalad periodicitet uppgifter om saldon, inleveranser, utleveranser och avvikelser. Rapporternas innehåll fastställs efter uppdragsgivarens kontrollbehov, till exempel artiklarnas omsättningshastighet, batcher nära utgångsdatum eller expedierade order per period.

## Uppstart av tjänsten

Uppstarten omfattar fyra steg: insamling av grunddata och dokumentformat; fastställande av dataflöden och ansvarsfördelning; test av utbytet på ett urval av order; övergång till drift med uppföljning under de första veckorna. Tjänsten ingår i modellen för [tredjepartslogistik (3PL)]({{< relref "/servizi/logistica-3pl" >}}) och gäller även för [cross-docking]({{< relref "/servizi/cross-docking" >}}) och [mervärdestjänster]({{< relref "/servizi/lavorazioni-valore-aggiunto" >}}).

## Branscher och område

Spårbarhet per batch berör särskilt livsmedels- och läkemedelsbranschen; orderintegrationen är central för [e-handeln]({{< relref "/settori/ecommerce" >}}) och för [dagligvaru- och detaljhandeln]({{< relref "/settori/gdo-retail" >}}), medan hanteringen av artikelnummer och varianter gäller [textil och mode]({{< relref "/settori/tessile-moda" >}}) och [fordonsindustrin]({{< relref "/settori/automotive" >}}). Anläggningen betjänar företag i [Latina]({{< relref "/logistica/latina" >}}), [Aprilia]({{< relref "/logistica/aprilia" >}}), [Cisterna di Latina]({{< relref "/logistica/cisterna-di-latina" >}}) och [Pomezia]({{< relref "/logistica/pomezia" >}}), liksom i [provinsen Latina]({{< relref "/logistica/provincia-di-latina" >}}) och i [södra Rom]({{< relref "/logistica/roma-sud" >}}).

## Offertförfrågan

För en offert på dokumenthantering anges vilket affärssystem som används, i vilket format uppdragsgivaren kan skicka och ta emot data, vilka dokument som ska utfärdas, vilka batch- eller utgångsdata som ska spåras, genomsnittligt antal order per dag och önskad periodicitet för rapporterna. Förfrågningar skickas via [kontaktformuläret]({{< relref "/" >}}#contatti).
