---
title: "E-handelslogistik i Lazio: flöden, cut-off, returer och kurirfirmor"
description: "Orderhantering för e-handel åt en näthandlare i Lazio: från godsmottagning till utleverans, brytpunkter, returer, kurirfirmor och vägavstånd från Rom."
date: 2026-10-02
url: "/sv/analyser/e-handelslogistik-lazio/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Interiör från ett distributionscenter med kollin klara för utleverans, arkivbild"
summary: "Orderhantering för e-handel som läggs ut på en tredjepartsoperatör följer ett standardflöde: integration av order, plock, packning, överlämning till kurirfirman och returhantering. För en näthandlare i Lazio är de avgörande variablerna brytpunkten för ordermottagning, kurirfirmornas upphämtningstid och vägavståndet till Romområdet."
faq:
  - q: "Vad är cut-off inom e-handelslogistik?"
    a: "Det är den sista tidpunkt då en order som lagret har tagit emot skickas samma dag. Den beror på kurirfirmans upphämtningstid och på den tid som krävs för plock och packning; order som kommer in efter cut-off skickas nästa arbetsdag."
  - q: "Hur lång tid har konsumenten på sig att returnera en vara som köpts på nätet?"
    a: "Den italienska konsumentlagen (Codice del Consumo, D.Lgs. 206/2005, art. 52) ger konsumenten 14 dagar att utöva ångerrätten utan att ange skäl, i regel räknat från leveransen av varan. Säljaren ska återbetala inom 14 dagar från frånträdet och får hålla inne återbetalningen tills varorna har mottagits eller bevis om att de har skickats har lämnats."
  - q: "Hur långt är det från Latina Scalo till Rom för e-handelsleveranser?"
    a: "Enligt ruttberäkning med OSRM för personbil ligger anläggningen på Via della Dinamica cirka 70 km från EUR (cirka 70 minuter), cirka 50 km från Pomezia (cirka 50 minuter) och cirka 34 km från Aprilia (cirka 36 minuter). För tunga fordon är tiderna längre."
  - q: "Hur stor är e-handeln med varor i Italien?"
    a: "Enligt Osservatorio eCommerce B2c Netcomm vid Politecnico di Milano uppskattas onlineköpen av varor i Italien 2025 till omkring 40,1 miljarder euro, en ökning med 6 % jämfört med 2024, motsvarande 11,2 % av de totala varuinköpen."
  - q: "Vilka uppgifter behövs för att starta en tjänst för e-handelslogistik?"
    a: "Antal artiklar (SKU), mått och vikter, genomsnittligt antal order och toppnivå per dag, rader per order, förväntad returandel, kurirfirmor som används, försäljningsplattform och sätt att utbyta order, krav på förpackning och reklammaterial."
---

Orderhantering för e-handel (fulfillment) är det segment inom tredjepartslogistik som har den mest fragmenterade driftsprofilen: många små order, en eller två rader per order, sändningar om ett enda kolli och en större andel returer än i traditionell handel. Enligt Osservatorio eCommerce B2c Netcomm vid Politecnico di Milano, citerat av AGI den 27 maj 2025, uppskattas onlineköpen av varor i Italien 2025 till omkring 40,1 miljarder euro, en ökning med 6 % jämfört med 2024, motsvarande 11,2 % av de totala varuinköpen.

För en näthandlare i Lazio avgörs valet av lager av ett fåtal mätbara parametrar: brytpunkten för order, kurirfirmornas upphämtningstid, returhanteringen och vägavståndet till slutkunderna och till kurirfirmornas terminaler.

## Flödet, från order till leverans

Cykeln för en e-handelsorder som hanteras av en tredjepartsoperatör består av sju steg:

1. **godsmottagning** från leverantören eller tillverkaren, med kvantitetskontroll, registrering av artiklarna (SKU) och inlagring;
2. **integration av order**: försäljningsplattformens order når operatörens WMS (lagerstyrningssystem) via en koppling, en fil eller ett IT-gränssnitt;
3. **plock (picking)**, normalt styckvis, där flera order samlas i en och samma plockrunda för att korta gångvägarna;
4. **kontroll och packning (packing)**, med val av kartong, utfyllnad samt iläggning av dokument och reklammaterial;
5. **etikettering** med kurirfirmans fraktsedel och generering av spårningskoden;
6. **överlämning till kurirfirman** vid den schemalagda upphämtningen och överföring av spårningsuppgifterna till plattformen;
7. **returhantering**: mottagning, kontroll, beslut om produktens vidare hantering och uppdatering av lagersaldot.

Plock, packning och etikettering beskrivs på sidan om tjänsten [godshantering]({{< relref "/servizi/handling" >}}); branschens särskilda behov på branschsidan [e-handel]({{< relref "/settori/ecommerce" >}}).

## Cut-off och upphämtningstid

**Cut-off** är den tidpunkt fram till vilken en mottagen order skickas samma dag. Den räknas baklänges från kurirfirmans upphämtningstid: om kurirfirman hämtar klockan 17 och lagret i genomsnitt behöver två timmar för att plocka, packa och samla kollina i en ordervåg kan cut-off inte ligga senare än klockan 15, och under toppdagar måste den tidigareläggas eller personalstyrkan utökas.

Tre faktorer flyttar cut-off:

- **antalet upphämtningar** per dag och tiden för den sista upphämtningen, som avtalas med varje kurirfirma;
- **plockproduktiviteten**, som beror på hur lagerplatserna är organiserade: de mest sålda artiklarna bör placeras nära packstationen;
- **kvaliteten på uppgifterna** om vikt och mått, som avgör kartong och kurirtaxa utan manuella mätningar.

Serviceavtalet ska ange cut-off och det nyckeltal som mäter den, till exempel andelen order som tagits emot före brytpunkten och skickats samma dag. Se guiden om [avtalet om tredjepartslogistik och nyckeltal]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kurirfirmorna och Lazios geografi

Näthandlaren kan använda egna avtal med expresskurirer eller de avtal som logistikoperatören har förhandlat fram. De nationella kurirfirmorna hämtar i lagret och sorterar kollina i sina egna terminaler; för regionala B2B-leveranser eller för få men tunga kollin kan operatören använda en egen fordonsflotta.

För ett lager i Latina Scalo är vägavstånden till de viktigaste efterfrågeområdena, beräknade med ruttmotorn OSRM för personbil vid normal trafik, följande:

| Destination | Vägavstånd | Beräknad tid |
|---|---|---|
| Latinas centrum | cirka 8 km | cirka 13 minuter |
| Aprilia | cirka 34 km | cirka 36 minuter |
| Pomezia | cirka 50 km | cirka 50 minuter |
| Santa Palomba | cirka 55 km | cirka 57 minuter |
| Castel Romano | cirka 57 km | cirka 56 minuter |
| Rom EUR | cirka 70 km | cirka 70 minuter |
| Rom Ostiense | cirka 74 km | cirka 76 minuter |
| Fiumicino | cirka 90 km | cirka 86 minuter |

För tunga fordon och under rusningstid är tiderna längre. Huvudleden mot Rom är riksväg 148 Pontina, med två separerade körbanor mellan Rom och Borgo Piave; på sträckan mellan Pomezia och Latina nord har hastighetsgränsen sänkts från 110 till 80 km/h. Beskrivningarna av de enskilda områdena finns på sidorna [logistik i Rom]({{< relref "/logistica/roma" >}}), [södra Rom]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) och [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Returer

Konsumentens **ångerrätt** regleras av den italienska konsumentlagen (Codice del Consumo, D.Lgs. 206/2005). Art. 52 ger 14 dagar att frånträda avtalet utan att ange skäl, i regel räknat från leveransen av varan. Art. 56 ålägger säljaren att återbetala inom 14 dagar från frånträdet, med rätt att hålla inne återbetalningen tills varorna har mottagits eller bevis om att de har skickats har lämnats.

Lagret måste därför hantera returerna inom tider som är förenliga med dessa frister:

- **mottagning och registrering** av returen med det ursprungliga ordernumret;
- **kontroll** av produktens och förpackningens skick enligt kriterier som avtalats med näthandlaren;
- **vidare hantering**: återinlagring, renovering, ompackning, försäljning som andrasortering eller kassering;
- **meddelande** av resultatet till plattformen så att återbetalningen kan frisläppas.

En särskild returyta, skild från det säljbara lagret, förhindrar att okontrollerade varor åter blir tillgängliga för order.

## Säsongstoppar och kapacitet

E-handeln koncentrerar volymerna till några få perioder under året, kopplade till kampanjer och högtider. För operatören innebär det att planera för extra personal, reservlagerplatser och avtal med kurirfirmorna om extra upphämtningar. För näthandlaren innebär det att i god tid meddela försäljningsprognoser och kampanjkalendrar: en oannonserad topp är den vanligaste orsaken till att cut-off inte hålls.

## Anläggningen i Latina Scalo

Consorzio Logistico Latina Scalo, på Via della Dinamica i Latina Scalo (LT), har 19 000 kvadratmeter under tak och ett WMS-system för lagerstyrning. Tjänsterna omfattar lagring, plock, packning, etikettering och palletering, vägtransport med egen fordonsflotta och distribution för sista milen, samt dokumenthantering. Enligt Consorzio bedrivs verksamheten dygnet runt, sju dagar i veckan. Möjligheterna till integration med de enskilda försäljningsplattformarna ska kontrolleras i offertskedet. För distribution till Rom, se analysen om [sista milen mot södra Rom]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Källor

- AGI, ekonominyhet den 27 maj 2025 om onlineköp av varor 2025, uppgifter från Osservatorio eCommerce B2c Netcomm – Politecnico di Milano: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), artt. 52 och 56: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Avstånd och tider: ruttberäkning med OSRM (Open Source Routing Machine) från anläggningen på Via della Dinamica, personbil, normal trafik; Consorzios egen bearbetning.
- SS148 Pontina, körbanor och hastighetsgränser: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (uppgifter från ANAS)
- Tjänster och drift: uppgifter från Consorzio Logistico Latina Scalo.
