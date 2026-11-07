---
title: "E-commerce fulfillment v Laziu: toky, cut-off, vratky a kuriéri"
description: "Vybavovanie e-commerce objednávok pre obchodníka z Lazia: od príjmu po expedíciu, uzávierky objednávok, vratky, kuriéri a cestné vzdialenosti od Ríma."
date: 2026-10-02
url: "/sk/analyzy/ecommerce-fulfillment-lazio/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Interiér distribučného centra so zásielkami pripravenými na expedíciu, ilustračná fotografia"
summary: "Vybavovanie e-commerce objednávok zverené zmluvnému operátorovi sa riadi štandardným tokom: integrácia objednávok, vychystávanie, balenie, odovzdanie kuriérovi a spracovanie vratiek. Pre obchodníka z Lazia sú rozhodujúcimi premennými čas uzávierky prijímania objednávok, čas vyzdvihnutia kuriérmi a cestná vzdialenosť od rímskej spádovej oblasti."
faq:
  - q: "Čo je cut-off pri e-commerce fulfillmente?"
    a: "Ide o časovú uzávierku, do ktorej sa objednávka prijatá skladom expeduje v ten istý deň. Závisí od času vyzdvihnutia kuriérom a od času potrebného na vychystanie a zabalenie; objednávky prijaté po uzávierke sa odosielajú nasledujúci pracovný deň."
  - q: "Koľko času má spotrebiteľ na vrátenie produktu kúpeného online?"
    a: "Taliansky Zákonník o ochrane spotrebiteľa (D.Lgs. 206/2005, čl. 52) priznáva spotrebiteľovi 14 dní na odstúpenie od zmluvy bez uvedenia dôvodu, spravidla od dodania tovaru. Predávajúci vráti platbu do 14 dní od odstúpenia a môže ju zadržať, kým nedostane tovar alebo doklad o jeho odoslaní."
  - q: "Aká je vzdialenosť z Latina Scalo do Ríma pri e-commerce dodávkach?"
    a: "Podľa výpočtu trasy OSRM pre osobný automobil je areál na Via della Dinamica vzdialený približne 70 km od štvrte EUR (približne 70 minút), približne 50 km od Pomezie (približne 50 minút) a približne 34 km od Aprilie (približne 36 minút). Pre nákladné vozidlá sú časy dlhšie."
  - q: "Akú hodnotu má e-commerce s produktmi v Taliansku?"
    a: "Podľa Osservatorio eCommerce B2c Netcomm milánskej Politecnico sa online nákupy produktov v Taliansku v roku 2025 odhadujú približne na 40,1 miliardy eur, čo je nárast o 6 % oproti roku 2024 a 11,2 % celkových nákupov produktov."
  - q: "Aké údaje sú potrebné na spustenie služby fulfillmentu?"
    a: "Počet položiek (SKU), rozmery a hmotnosti, priemerný a špičkový denný počet objednávok, riadky na objednávku, očakávaná miera vratiek, používaní kuriéri, predajná platforma a spôsob výmeny objednávok, požiadavky na balenie a propagačné materiály."
---

Vybavovanie e-commerce objednávok (fulfillment) je segment zmluvnej logistiky s najroztrieštenejším prevádzkovým profilom: veľa malých objednávok, jeden alebo dva riadky na objednávku, expedícia po jednotlivých kusoch, podiel vratiek vyšší ako v tradičnom obchode. Podľa Osservatorio eCommerce B2c Netcomm milánskej Politecnico, ktoré citovala agentúra AGI 27. mája 2025, sa online nákupy produktov v Taliansku v roku 2025 odhadujú približne na 40,1 miliardy eur, čo je nárast o 6 % oproti roku 2024 a 11,2 % celkových nákupov produktov.

Pre obchodníka z Lazia sa výber skladu rozhoduje na niekoľkých merateľných parametroch: časová uzávierka objednávok, čas vyzdvihnutia kuriérmi, spracovanie vratiek a cestná vzdialenosť od koncových zákazníkov a od uzlov kuriérskych spoločností.

## Tok od objednávky po doručenie

Cyklus e-commerce objednávky spracovanej zmluvným operátorom sa skladá zo siedmich krokov:

1. **príjem tovaru** od dodávateľa alebo výrobcu s kvantitatívnou kontrolou, zaevidovaním položiek (SKU) a zaskladnením;
2. **integrácia objednávok**: objednávky z predajnej platformy prichádzajú do WMS (softvér na riadenie skladu) operátora cez konektor, súbor alebo informatické rozhranie;
3. **vychystávanie (picking)**, spravidla po kusoch, so zoskupením viacerých objednávok do jednej vychystávacej trasy na skrátenie prechodov;
4. **kontrola a balenie (packing)** s výberom škatule, výplňou, vložením dokladov a propagačných materiálov;
5. **etiketovanie** nákladným listom kuriéra a vygenerovanie sledovacieho kódu;
6. **odovzdanie kuriérovi** pri plánovanom vyzdvihnutí a odoslanie sledovacích údajov na platformu;
7. **spracovanie vratiek**: prijatie, kontrola, rozhodnutie o ďalšom určení produktu a aktualizácia zásoby.

Činnosti vychystávania, balenia a etiketovania opisuje stránka služby [manipulácie]({{< relref "/servizi/handling" >}}); osobitné potreby segmentu stránka odvetvia [e-commerce]({{< relref "/settori/ecommerce" >}}).

## Cut-off a čas vyzdvihnutia

**Cut-off** je časová uzávierka, do ktorej sa prijatá objednávka expeduje v ten istý deň. Počíta sa spätne od času vyzdvihnutia kuriérom: ak kuriér prichádza o 17. hodine a sklad potrebuje v priemere dve hodiny na vychystanie, zabalenie a konsolidáciu zásielok jednej vlny objednávok, uzávierka nemôže byť neskôr ako o 15. hodine a v dňoch špičky sa musí posunúť skôr alebo sa musí zvýšiť počet pracovníkov.

Uzávierku posúvajú tri prvky:

- **počet vyzdvihnutí** za deň a čas posledného vyzdvihnutia dohodnutý s každým kuriérom;
- **produktivita vychystávania**, ktorá závisí od organizácie skladových pozícií: najpredávanejšie položky treba umiestniť blízko baliacej zóny;
- **kvalita údajov** o hmotnosti a rozmeroch, ktoré určujú škatuľu a tarifu kuriéra bez ručného merania.

Zmluva o poskytovaní služieb musí uvádzať uzávierku a ukazovateľ, ktorý ju meria, napríklad percento objednávok prijatých do uzávierky a expedovaných v ten istý deň. K tejto téme pozri príručku k [zmluve o zmluvnej logistike a KPI]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kuriéri a geografia Lazia

Obchodník môže používať vlastné zmluvy s expresnými kuriérmi alebo zmluvy vyjednané logistickým operátorom. Celoštátni kuriéri vyzdvihujú zásielky v sklade a triedia ich vo svojich uzloch; pri regionálnych dodávkach B2B alebo pri malom počte ťažkých kusov môže operátor nasadiť vlastný vozový park.

Pre sklad v Latina Scalo sú cestné vzdialenosti do hlavných spádových oblastí dopytu, vypočítané navigačným nástrojom OSRM pre osobný automobil pri bežnej premávke, tieto:

| Cieľ | Cestná vzdialenosť | Odhadovaný čas |
|---|---|---|
| Latina, centrum | približne 8 km | približne 13 minút |
| Aprilia | približne 34 km | približne 36 minút |
| Pomezia | približne 50 km | približne 50 minút |
| Santa Palomba | približne 55 km | približne 57 minút |
| Castel Romano | približne 57 km | približne 56 minút |
| Rím EUR | približne 70 km | približne 70 minút |
| Rím Ostiense | približne 74 km | približne 76 minút |
| Fiumicino | približne 90 km | približne 86 minút |

Pre nákladné vozidlá a v dopravnej špičke sú časy dlhšie. Hlavnou osou smerom do Ríma je štátna cesta 148 Pontina s dvoma oddelenými jazdnými pásmi medzi Rímom a Borgo Piave; na úseku medzi Pomeziou a severnou Latinou bola rýchlosť znížená zo 110 na 80 km/h. Stránky jednotlivých oblastí sú [logistika v Ríme]({{< relref "/logistica/roma" >}}), [južný Rím]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) a [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Vratky

**Právo spotrebiteľa na odstúpenie od zmluvy** upravuje taliansky Zákonník o ochrane spotrebiteľa (D.Lgs. 206/2005). Článok 52 poskytuje 14 dní na odstúpenie bez uvedenia dôvodu, spravidla od dodania tovaru. Článok 56 ukladá predávajúcemu vrátiť platbu do 14 dní od odstúpenia s možnosťou zadržať ju do prijatia tovaru alebo dokladu o jeho odoslaní.

Sklad preto musí spracúvať vratky v lehotách zlučiteľných s týmito termínmi:

- **prijatie a zaevidovanie** vratky s pôvodným číslom objednávky;
- **kontrola** stavu produktu a obalu podľa kritérií dohodnutých s obchodníkom;
- **určenie**: vrátenie na sklad, renovácia, prebalenie, predaj ako druhá akosť alebo likvidácia;
- **oznámenie** výsledku platforme na uvoľnenie vrátenia platby.

Vyhradený priestor pre vratky, oddelený od predajnej zásoby, zabraňuje tomu, aby sa neskontrolovaný tovar opäť stal dostupným pre objednávky.

## Sezónne špičky a kapacita

E-commerce sústreďuje objemy do niekoľkých období roka spojených s akciami a sviatkami. Pre operátora to znamená plánovať dodatočný personál, rezervné skladové pozície a dohody s kuriérmi o dodatočných vyzdvihnutiach. Pre obchodníka to znamená vopred oznamovať predajné prognózy a kalendáre akcií: neohlásená špička je najčastejšou príčinou nedodržania uzávierky.

## Areál v Latina Scalo

Consorzio Logistico Latina Scalo na Via della Dinamica v Latina Scalo (LT) má 19 000 metrov štvorcových krytej plochy a systém WMS na riadenie skladu. Služby zahŕňajú skladovanie, vychystávanie, balenie, etiketovanie a paletizáciu, cestnú prepravu vlastným vozovým parkom a distribúciu na poslednej míli, ako aj správu dokladov. Podľa konzorcia je prevádzka nepretržitá, 24 hodín denne, 7 dní v týždni. Spôsoby integrácie s jednotlivými predajnými platformami treba overiť pri príprave cenovej ponuky. K distribúcii do Ríma pozri analýzu o [poslednej míli do južného Ríma]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Zdroje

- AGI, ekonomická správa z 27. mája 2025 o online nákupoch produktov v roku 2025, údaje Osservatorio eCommerce B2c Netcomm – Politecnico di Milano: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), čl. 52 a 56: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Vzdialenosti a časy: výpočet trasy OSRM (Open Source Routing Machine) z areálu na Via della Dinamica, osobný automobil, bežná premávka; spracovanie konzorcia.
- SS148 Pontina, jazdné pásy a rýchlostné limity: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (údaje ANAS)
- Služby a prevádzka: vyhlásenia Consorzio Logistico Latina Scalo.
