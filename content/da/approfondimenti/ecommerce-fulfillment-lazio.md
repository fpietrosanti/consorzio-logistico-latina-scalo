---
title: "E-handelsfulfillment i Lazio: strømme, cut-off, returvarer og kurerer"
description: "Ekspedition af e-handelsordrer for en webshop i Lazio: fra varemodtagelse til forsendelse, cut-off-tider, returvarer, kurerer og vejafstande fra Rom."
date: 2026-10-02
url: "/da/analyser/e-handel-fulfillment-lazio/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Indersiden af et distributionscenter med kolli klar til forsendelse, arkivfoto"
summary: "Ekspedition af e-handelsordrer, der overlades til en tredjepartsoperatør, følger et standardforløb: integration af ordrer, plukning, pakning, overdragelse til kurer og håndtering af returvarer. For en webshop i Lazio er de afgørende variabler sidste frist for modtagelse af ordrer, kurerernes afhentningstidspunkt og vejafstanden til Rom-området."
faq:
  - q: "Hvad er cut-off i e-handelsfulfillment?"
    a: "Det er det seneste tidspunkt, hvor en ordre modtaget af lageret afsendes samme dag. Det afhænger af kurerens afhentningstidspunkt og af den tid, plukning og pakning kræver; ordrer modtaget efter cut-off afsendes den følgende arbejdsdag."
  - q: "Hvor lang tid har forbrugeren til at returnere en vare købt online?"
    a: "Den italienske forbrugerlov (Codice del Consumo, D.Lgs. 206/2005, art. 52) giver forbrugeren 14 dage til at udøve fortrydelsesretten uden at angive grunde, normalt regnet fra leveringen af varen. Sælgeren tilbagebetaler inden 14 dage efter fortrydelsen og kan tilbageholde betalingen, indtil varerne er modtaget eller der er dokumentation for returforsendelsen."
  - q: "Hvor langt er der fra Latina Scalo til Rom ved e-handelsleveringer?"
    a: "Ifølge ruteberegning med OSRM for personbil ligger anlægget på Via della Dinamica ca. 70 km fra EUR (ca. 70 minutter), ca. 50 km fra Pomezia (ca. 50 minutter) og ca. 34 km fra Aprilia (ca. 36 minutter). For lastbiler er køretiderne længere."
  - q: "Hvor stor er e-handlen med fysiske varer i Italien?"
    a: "Ifølge Osservatorio eCommerce B2c Netcomm ved Politecnico di Milano anslås onlinekøb af fysiske varer i Italien i 2025 til ca. 40,1 mia. euro, en stigning på 6 % i forhold til 2024, svarende til 11,2 % af det samlede køb af fysiske varer."
  - q: "Hvilke data skal der til for at starte en fulfillment-ydelse?"
    a: "Antal varenumre (SKU), mål og vægt, gennemsnitligt og maksimalt antal ordrer pr. dag, linjer pr. ordre, forventet returprocent, anvendte kurerer, salgsplatform og metode til udveksling af ordrer, krav til emballage og reklamemateriale."
---

Ekspedition af e-handelsordrer (fulfillment) er det segment af tredjepartslogistikken, der har den mest fragmenterede driftsprofil: mange små ordrer, en eller to linjer pr. ordre, forsendelse som enkeltkolli og en returandel, der er højere end i den traditionelle handel. Ifølge Osservatorio eCommerce B2c Netcomm ved Politecnico di Milano, citeret af nyhedsbureauet AGI den 27. maj 2025, anslås onlinekøb af fysiske varer i Italien i 2025 til ca. 40,1 mia. euro, en stigning på 6 % i forhold til 2024, svarende til 11,2 % af det samlede køb af fysiske varer.

For en webshop i Lazio afgøres valget af lager af få målbare parametre: sidste frist for ordrer, kurerernes afhentningstidspunkt, håndteringen af returvarer og vejafstanden til slutkunderne og til kurerernes terminaler.

## Forløbet fra ordre til levering

Forløbet for en e-handelsordre, der håndteres af en tredjepartsoperatør, består af syv trin:

1. **varemodtagelse** fra leverandøren eller producenten med mængdekontrol, registrering af varenumrene (SKU) og placering på lokation;
2. **integration af ordrer**: ordrerne fra salgsplatformen når frem til operatørens WMS (lagerstyringssystem) via connector, fil eller it-grænseflade;
3. **plukning (picking)**, normalt stykvis, hvor flere ordrer samles i én plukkerunde for at forkorte gangafstandene;
4. **kontrol og pakning (packing)** med valg af kasse, fyld og ilægning af dokumenter og reklamemateriale;
5. **etikettering** med kurerens fragtbrev og generering af sporingskoden;
6. **overdragelse til kureren** ved den planlagte afhentning og overførsel af sporingsdata til platformen;
7. **håndtering af returvarer**: modtagelse, kontrol, beslutning om varens videre skæbne og opdatering af beholdningen.

Plukning, pakning og etikettering er beskrevet på siden om ydelsen [håndtering]({{< relref "/servizi/handling" >}}); branchens særlige behov på brancheside for [e-handel]({{< relref "/settori/ecommerce" >}}).

## Cut-off og afhentningstidspunkt

**Cut-off** er det tidspunkt, hvor en modtaget ordre senest skal foreligge for at blive afsendt samme dag. Det beregnes baglæns fra kurerens afhentningstidspunkt: hvis kureren kommer kl. 17, og lageret i gennemsnit bruger to timer på at plukke, pakke og samle kolli fra en ordrebølge, kan cut-off ikke ligge senere end kl. 15, og på spidsbelastningsdage skal det fremrykkes, eller bemandingen skal øges.

Tre elementer flytter cut-off:

- **antallet af daglige afhentninger** og tidspunktet for den sidste afhentning, aftalt med hver kurer;
- **plukkeproduktiviteten**, der afhænger af lokationernes organisering: de mest solgte varer skal placeres tæt på pakkeområdet;
- **kvaliteten af data** om vægt og mål, der bestemmer kasse og kurertakst uden manuel opmåling.

Servicekontrakten skal angive cut-off og den indikator, der måler det, f.eks. andelen af ordrer modtaget inden fristen og afsendt samme dag. Om emnet henvises til vejledningen om [kontrakten om tredjepartslogistik og KPI'er]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kurerer og geografien i Lazio

Webshoppen kan bruge egne aftaler med ekspreskurererne eller dem, logistikoperatøren har forhandlet. De nationale kurerer afhenter på lageret og sorterer kolli i deres egne terminaler; til regionale B2B-leveringer eller leveringer med få, tunge kolli kan operatøren bruge egen flåde.

For et lager i Latina Scalo er vejafstandene til de vigtigste efterspørgselsområder, beregnet med rutemotoren OSRM for personbil under normale trafikforhold, følgende:

| Destination | Vejafstand | Anslået køretid |
|---|---|---|
| Latina centrum | ca. 8 km | ca. 13 minutter |
| Aprilia | ca. 34 km | ca. 36 minutter |
| Pomezia | ca. 50 km | ca. 50 minutter |
| Santa Palomba | ca. 55 km | ca. 57 minutter |
| Castel Romano | ca. 57 km | ca. 56 minutter |
| Rom EUR | ca. 70 km | ca. 70 minutter |
| Rom Ostiense | ca. 74 km | ca. 76 minutter |
| Fiumicino | ca. 90 km | ca. 86 minutter |

For lastbiler og i myldretiden er køretiderne længere. Hovedforbindelsen mod Rom er statsvej 148 Pontina med to adskilte kørebaner mellem Rom og Borgo Piave; på strækningen mellem Pomezia og Latina nord er hastighedsgrænsen sænket fra 110 til 80 km/t. Oversigterne over de enkelte områder findes på siderne [logistik i Rom]({{< relref "/logistica/roma" >}}), [det sydlige Rom]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) og [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Returvarer

Forbrugerens **fortrydelsesret** er reguleret af den italienske forbrugerlov (D.Lgs. 206/2005). Art. 52 giver 14 dage til at fortryde uden begrundelse, normalt regnet fra leveringen af varen. Art. 56 forpligter sælgeren til at tilbagebetale inden 14 dage efter fortrydelsen, med ret til at tilbageholde betalingen, indtil varerne er modtaget, eller der er dokumentation for returforsendelsen.

Lageret skal derfor håndtere returvarer med tidsfrister, der er forenelige med disse frister:

- **modtagelse og registrering** af returvaren med det oprindelige ordrenummer;
- **kontrol** af varens og emballagens tilstand efter kriterier aftalt med webshoppen;
- **disponering**: tilbage på lager, istandsættelse, ompakning, salg som andensortering eller bortskaffelse;
- **meddelelse** af resultatet til platformen, så tilbagebetalingen kan frigives.

Et særskilt returområde, adskilt fra den salgbare beholdning, forhindrer, at ukontrollerede varer igen bliver tilgængelige for ordrer.

## Sæsonspidser og kapacitet

E-handlen koncentrerer mængderne i få perioder af året i forbindelse med kampagner og højtider. For operatøren betyder det ekstra personale, reservelokationer og aftaler med kurererne om ekstra afhentninger. For webshoppen betyder det at meddele salgsprognoser og kampagnekalendere på forhånd: en uanmeldt spidsbelastning er den hyppigste årsag til, at cut-off ikke overholdes.

## Anlægget i Latina Scalo

Consorzio Logistico Latina Scalo på Via della Dinamica i Latina Scalo (LT) råder over 19.000 overdækkede kvadratmeter og et WMS-system til lagerstyring. Ydelserne omfatter lagring, plukning, pakning, etikettering og palletering, vejtransport med egen flåde og distribution i sidste led samt dokumenthåndtering. Ifølge Consorzio er driften døgnåben, 7 dage om ugen. Mulighederne for integration med de enkelte salgsplatforme skal afklares i tilbudsfasen. Om distribution til Rom henvises til analysen om [sidste led mod det sydlige Rom]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Kilder

- AGI, økonominyhed af 27. maj 2025 om onlinekøb af fysiske varer i 2025, data fra Osservatorio eCommerce B2c Netcomm – Politecnico di Milano: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), artt. 52 og 56: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Afstande og køretider: ruteberegning med OSRM (Open Source Routing Machine) fra anlægget på Via della Dinamica, personbil, normal trafik; Consorzios egen beregning.
- SS148 Pontina, kørebaner og hastighedsgrænser: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (ANAS-data)
- Ydelser og drift: oplysninger fra Consorzio Logistico Latina Scalo.
