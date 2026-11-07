---
linkTitle: "Dokumenthåndtering"
title: "Dokumenthåndtering og WMS til logistik i Latina Scalo"
description: "Dokumenthåndtering i Latina Scalo (LT): DDT og følgesedler, sporbarhed af bevægelser i WMS og integration med kundernes forretningssystemer."
url: "/da/ydelser/dokumenthaandtering/"
layout: "servizio"
weight: 8
image: "topics/inventario-barcode"
imageAlt: "Medarbejder, der registrerer et kolli på lageret med en håndterminal, arkivfoto"
faq:
  - q: "Hvilke dokumenter håndterer Consorzio Logistico Latina Scalo?"
    a: "Consorzio Logistico Latina Scalo håndterer på vegne af kunderne transportdokumenter (DDT) og følgesedler, registrering af lagerbevægelser og sporbarhed af enhederne fra modtagelse til afsendelse med integration til kundernes forretningssystemer."
  - q: "Bruger Consorzio Logistico Latina Scalo et WMS?"
    a: "Ja. Consorzio Logistico Latina Scalo bruger et WMS-system (lagerstyringssystem) til at registrere lokationer, beholdninger og bevægelser. I logistikcentret i Latina Scalo kører systemet på dedikeret fiber og industrielt Wi-Fi i lagerområderne."
  - q: "Kan WMS-systemet hos Consorzio Logistico Latina Scalo integreres med kundens forretningssystem?"
    a: "Consorzio Logistico Latina Scalo tilbyder integration mellem sit WMS og kundernes forretningssystemer til udveksling af stamdata, ankomstadviser, ordrer og bekræftelser. Format, hyppighed og overførselsmetode for data fastlægges ved opstarten af ydelsen."
  - q: "Hvordan fungerer sporbarheden af varer i Latina Scalo?"
    a: "I logistikcentret hos Consorzio Logistico Latina Scalo registreres hver lasteenhed i WMS-systemet ved modtagelsen og knyttes til varenummer, mængde, lokation og, hvis det ønskes, parti. Hver efterfølgende flytning frem til afsendelse forbliver registreret, så varernes vej kan rekonstrueres."
  - q: "Hvilke oplysninger kræves for at opsætte dokumenthåndtering med Consorzio Logistico Latina Scalo?"
    a: "For at opsætte dokumenthåndteringen beder Consorzio Logistico Latina Scalo om kundens forretningssystem, formatet for de udvekslede data, de dokumenter, der skal udstedes, de parti- eller udløbsdata, der skal spores, og hyppigheden af rapporter om beholdninger og bevægelser."
---

## Dokumenter, data og sporbarhed i samme ydelse

Consorzio Logistico Latina Scalo håndterer på vegne af kunderne den dokument- og informationsmæssige del af logistikken: udstedelse af transportdokumenter (DDT, det italienske følgedokument) og følgesedler, registrering af lagerbevægelser i WMS-systemet (lagerstyringssystemet), sporbarhed af lasteenheder og integration med kundernes forretningssystemer. Ydelsen ledsager [lagring]({{< relref "/servizi/stoccaggio" >}}), [varehåndtering]({{< relref "/servizi/handling" >}}) og [transport]({{< relref "/servizi/trasporto" >}}) i logistikcentret i Via della Dinamica, området Tor Tre Ponti, i Latina Scalo (LT).

I logistikcentret kører WMS-systemet på dedikeret fiber og industrielt Wi-Fi i lagerområderne; kontorer og mødelokaler huser det personale, der koordinerer dokumenter og informationsstrømme.

## Transportdokumenter og følgesedler

### Indgående

Ved modtagelsen sammenholder medarbejderen varerne med leverandørens DDT og kundens ankomstadvis. Forskelle mellem angivne og modtagne mængder samt eventuelle skader noteres som forbehold på fragtførerens dokument og meddeles kunden med henvisning til leveringen.

### Udgående

Ved lastningen udsteder Konsortiet transportdokumentet på kundens vegne med modtager, varebeskrivelse, antal kolli og vægt. Den kopi, modtageren har underskrevet, returneres til Konsortiet efter leveringen, hvis den er udført med den egne vognpark, og arkiveres sammen med forsendelsens data.

## WMS og sporbarhed

### Registrering af enhederne

Hver accepteret lasteenhed registreres i WMS-systemet og knyttes til varenummer, mængde og lokation. Når kunden ønsker det, omfatter registreringen også parti og udløbsdato, som er nødvendige i forsyningskæderne for [fødevarer]({{< relref "/settori/agroalimentare" >}}) og [lægemidler]({{< relref "/settori/farmaceutico" >}}).

### Bevægelser

Systemet registrerer hver efterfølgende flytning: indlagring, genopfyldning af plukkeområder, plukning pr. ordre, værdiskabende ydelser og lastning. På den måde kan en enheds eller et partis vej rekonstrueres fra modtagelse til afsendelse, hvilket også er nyttigt ved tilbagekaldelse af et produkt eller en tvist med en kunde.

### Optælling

De registrerede beholdninger sammenholdes periodisk med den fysiske optælling efter den aftalte kalender. Afvigelser meddeles kunden med angivelse af vare, parti og lokation.

## Integration med forretningssystemer

Dataudvekslingen mellem kundens forretningssystem (ERP) og Konsortiets WMS omfatter normalt fire strømme:

- **stamdata**: varenumre, beskrivelser, emballageenheder, mål og vægt;
- **ankomstadviser**: forventede varer med leverandør, mængde og forventet dato;
- **udgående ordrer**: ordrelinjer, modtagere og leveringsdatoer;
- **bekræftelser**: gennemførte modtagelser med eventuelle forbehold, opdaterede beholdninger og afsendte forsendelser med dokumentreferencer.

Filformat, overførselskanal og udvekslingshyppighed fastlægges i opstartsprojektet ud fra det system, kunden anvender. I de indledende faser eller ved mindre mængder kan udvekslingen også ske med standardfiler, der sendes på aftalte tidspunkter.

## Rapportering

Kunden modtager med den aftalte hyppighed data om beholdninger, indgang, udgang og afvigelser. Rapporternes indhold fastlægges efter kundens kontrolbehov, for eksempel varernes omsætningshastighed, partier tæt på udløb eller ekspederede ordrer pr. periode.

## Opstart af ydelsen

Opstarten omfatter fire trin: indsamling af stamdata og dokumentformater; fastlæggelse af datastrømme og ansvarsfordeling; test af udvekslingen på et udsnit af ordrer; overgang til drift med overvågning de første uger. Ydelsen indgår i modellen for [tredjepartslogistik (3PL)]({{< relref "/servizi/logistica-3pl" >}}) og gælder også for [cross-docking]({{< relref "/servizi/cross-docking" >}}) og [værdiskabende ydelser]({{< relref "/servizi/lavorazioni-valore-aggiunto" >}}).

## Brancher og område

Sporbarhed pr. parti er især relevant for fødevarer og lægemidler; integrationen af ordrer er central for [e-handel]({{< relref "/settori/ecommerce" >}}) og for [dagligvarehandel og detail]({{< relref "/settori/gdo-retail" >}}), mens håndtering af varenumre og varianter vedrører [tekstil og mode]({{< relref "/settori/tessile-moda" >}}) og [automotive]({{< relref "/settori/automotive" >}}). Logistikcentret betjener virksomheder i [Latina]({{< relref "/logistica/latina" >}}), [Aprilia]({{< relref "/logistica/aprilia" >}}), [Cisterna di Latina]({{< relref "/logistica/cisterna-di-latina" >}}) og [Pomezia]({{< relref "/logistica/pomezia" >}}) samt oplandet i [provinsen Latina]({{< relref "/logistica/provincia-di-latina" >}}) og [det sydlige Rom]({{< relref "/logistica/roma-sud" >}}).

## Til et tilbud

Til et tilbud på dokumenthåndtering oplyses det anvendte forretningssystem, formatet for de data, kunden kan sende og modtage, de dokumenter, der skal udstedes, de parti- eller udløbsdata, der skal spores, gennemsnitligt antal ordrer pr. dag og den ønskede rapporteringshyppighed. Anmodninger sendes via [kontaktformularen]({{< relref "/" >}}#contatti).
