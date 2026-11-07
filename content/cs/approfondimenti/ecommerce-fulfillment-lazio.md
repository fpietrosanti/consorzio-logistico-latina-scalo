---
title: "E-commerce fulfillment v Laziu: toky, cut-off, vratky a kurýři"
description: "Vyřizování e-commerce objednávek pro obchodníka z Lazia: od příjmu po expedici, uzávěrky objednávek, vratky, kurýři a silniční vzdálenosti od Říma."
date: 2026-10-02
url: "/cs/analyzy/ecommerce-fulfillment-lazio/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Interiér distribučního centra se zásilkami připravenými k expedici, ilustrační foto"
summary: "Vyřizování e-commerce objednávek svěřené smluvnímu logistickému provozovateli probíhá ve standardním toku: integrace objednávek, vychystávání, balení, předání kurýrovi a zpracování vratek. Pro obchodníka z Lazia jsou rozhodujícími proměnnými čas uzávěrky příjmu objednávek, čas vyzvednutí kurýry a silniční vzdálenost od římské spádové oblasti."
faq:
  - q: "Co je cut-off v e-commerce fulfillmentu?"
    a: "Je to časová uzávěrka, do které musí sklad objednávku přijmout, aby byla expedována tentýž den. Závisí na čase vyzvednutí kurýrem a na době potřebné k vychystání a zabalení; objednávky přijaté po uzávěrce odcházejí následující pracovní den."
  - q: "Kolik času má spotřebitel na vrácení zboží zakoupeného online?"
    a: "Italský spotřebitelský zákoník Codice del Consumo (D.Lgs. 206/2005, čl. 52) přiznává spotřebiteli 14 dní na odstoupení od smlouvy bez udání důvodu, zpravidla od doručení zboží. Prodávající vrací peníze do 14 dní od odstoupení a může vrácení zadržet, dokud neobdrží zboží nebo doklad o jeho odeslání."
  - q: "Jak daleko je Latina Scalo od Říma pro e-commerce dodávky?"
    a: "Podle výpočtu trasy OSRM pro osobní automobil je areál na Via della Dinamica vzdálen přibližně 70 km od čtvrti EUR (přibližně 70 minut), přibližně 50 km od Pomezie (přibližně 50 minut) a přibližně 34 km od Aprilie (přibližně 36 minut). U nákladních vozidel jsou časy delší."
  - q: "Jakou hodnotu má e-commerce se zbožím v Itálii?"
    a: "Podle Osservatorio eCommerce B2c Netcomm při Politecnico di Milano se online nákupy zboží v Itálii v roce 2025 odhadují přibližně na 40,1 miliardy eur, o 6 % více než v roce 2024, což odpovídá 11,2 % celkových nákupů zboží."
  - q: "Jaké údaje jsou potřeba pro zahájení fulfillmentu?"
    a: "Počet položek (SKU), rozměry a hmotnosti, průměrný a špičkový počet objednávek za den, řádky na objednávku, očekávaná míra vratek, používaní kurýři, prodejní platforma a způsob předávání objednávek, požadavky na balení a propagační materiály."
---

Vyřizování e-commerce objednávek (fulfillment) je segment smluvní logistiky s nejroztříštěnějším provozním profilem: mnoho malých objednávek, jeden nebo dva řádky na objednávku, expedice po jednotlivých kusech a vyšší podíl vratek než v tradičním obchodě. Podle Osservatorio eCommerce B2c Netcomm při Politecnico di Milano, které 27. května 2025 citovala agentura AGI, se online nákupy zboží v Itálii v roce 2025 odhadují přibližně na 40,1 miliardy eur, o 6 % více než v roce 2024, což odpovídá 11,2 % celkových nákupů zboží.

Pro obchodníka z Lazia rozhoduje o volbě skladu několik měřitelných parametrů: časová uzávěrka objednávek, čas vyzvednutí kurýry, zpracování vratek a silniční vzdálenost ke koncovým zákazníkům a k depům kurýrů.

## Tok od objednávky k doručení

Cyklus e-commerce objednávky vyřizované smluvním provozovatelem se skládá ze sedmi kroků:

1. **příjem zboží** od dodavatele nebo výrobce s kontrolou množství, evidencí položek (SKU) a zaskladněním;
2. **integrace objednávek**: objednávky z prodejní platformy přicházejí do WMS (systému řízení skladu) provozovatele prostřednictvím konektoru, souboru nebo IT rozhraní;
3. **vychystávání (picking)**, zpravidla po kusech, se sdružením více objednávek do jedné vychystávací trasy pro zkrácení cest;
4. **kontrola a balení (packing)** s volbou krabice, výplní, vložením dokladů a propagačních materiálů;
5. **etiketování** nákladním listem kurýra a vygenerování sledovacího kódu;
6. **předání kurýrovi** při plánovaném vyzvednutí a přenos sledovacích údajů do platformy;
7. **zpracování vratek**: příjem, kontrola, rozhodnutí o dalším určení produktu a aktualizace zásoby.

Vychystávání, balení a etiketování popisuje stránka služby [manipulace]({{< relref "/servizi/handling" >}}); specifické požadavky segmentu stránka odvětví [e-commerce]({{< relref "/settori/ecommerce" >}}).

## Cut-off a čas vyzvednutí

**Cut-off** je časová uzávěrka, do které musí být objednávka přijata, aby byla expedována tentýž den. Počítá se zpětně od času vyzvednutí kurýrem: pokud kurýr přijíždí v 17 hodin a sklad potřebuje v průměru dvě hodiny na vychystání, zabalení a konsolidaci zásilek jedné vlny objednávek, nemůže být uzávěrka později než v 15 hodin a ve špičkových dnech je třeba ji posunout dříve nebo posílit personál.

Uzávěrku posouvají tři faktory:

- **počet vyzvednutí** za den a čas posledního vyzvednutí, dohodnutý s každým kurýrem;
- **produktivita vychystávání**, která závisí na organizaci skladových pozic: nejprodávanější položky mají být umístěny blízko balicí zóny;
- **kvalita údajů** o hmotnosti a rozměrech, které bez ručního měření určují krabici a tarif kurýra.

Smlouva o službách má uvádět uzávěrku a ukazatel, který ji měří, například podíl objednávek přijatých do uzávěrky a expedovaných tentýž den. K tomuto tématu viz průvodce [smlouvou o smluvní logistice a ukazateli KPI]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kurýři a geografie Lazia

Obchodník může využívat vlastní smlouvy s expresními kurýry nebo smlouvy vyjednané logistickým provozovatelem. Celostátní kurýři vyzvedávají zásilky ve skladu a třídí je ve svých depech; pro regionální dodávky B2B nebo dodávky s malým počtem těžkých kusů může provozovatel nasadit vlastní vozový park.

Pro sklad v Latina Scalo jsou silniční vzdálenosti k hlavním spádovým oblastem poptávky, vypočtené trasovacím nástrojem OSRM pro osobní automobil za běžného provozu, následující:

| Místo určení | Silniční vzdálenost | Odhadovaný čas |
|---|---|---|
| Latina centrum | přibližně 8 km | přibližně 13 minut |
| Aprilia | přibližně 34 km | přibližně 36 minut |
| Pomezia | přibližně 50 km | přibližně 50 minut |
| Santa Palomba | přibližně 55 km | přibližně 57 minut |
| Castel Romano | přibližně 57 km | přibližně 56 minut |
| Řím EUR | přibližně 70 km | přibližně 70 minut |
| Řím Ostiense | přibližně 74 km | přibližně 76 minut |
| Fiumicino | přibližně 90 km | přibližně 86 minut |

U nákladních vozidel a ve špičce jsou časy delší. Hlavní osou do Říma je silnice SS148 Pontina se dvěma oddělenými jízdními pásy mezi Římem a Borgo Piave; v úseku mezi Pomezií a Latinou sever byla nejvyšší povolená rychlost snížena ze 110 na 80 km/h. Přehledy jednotlivých oblastí jsou na stránkách [logistika v Římě]({{< relref "/logistica/roma" >}}), [jih Říma]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) a [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Vratky

**Právo spotřebitele na odstoupení od smlouvy** upravuje spotřebitelský zákoník Codice del Consumo (D.Lgs. 206/2005). Čl. 52 poskytuje 14 dní na odstoupení bez udání důvodu, zpravidla od doručení zboží. Čl. 56 ukládá prodávajícímu vrátit peníze do 14 dní od odstoupení s možností zadržet platbu do obdržení zboží nebo dokladu o jeho odeslání.

Sklad proto musí zpracovávat vratky v časech slučitelných s těmito lhůtami:

- **příjem a evidence** vratky s původním číslem objednávky;
- **kontrola** stavu produktu a obalu podle kritérií dohodnutých s obchodníkem;
- **další určení**: vrácení do zásoby, renovace, přebalení, prodej jako zboží druhé jakosti nebo likvidace;
- **oznámení** výsledku platformě pro uvolnění vrácení peněz.

Vyhrazený prostor pro vratky, oddělený od prodejné zásoby, zabraňuje tomu, aby se nezkontrolované zboží znovu stalo dostupným pro objednávky.

## Sezónní špičky a kapacita

E-commerce soustřeďuje objemy do několika období roku spojených s akcemi a svátky. Pro provozovatele to znamená plánovat dodatečný personál, rezervní skladové pozice a dohody s kurýry o dodatečných vyzvednutích. Pro obchodníka to znamená předem sdělovat prodejní prognózy a kalendáře akcí: neohlášená špička je nejčastější příčinou nedodržení uzávěrky.

## Areál v Latina Scalo

Consorzio Logistico Latina Scalo na Via della Dinamica v Latina Scalo (provincie Latina) má 19 000 metrů čtverečních krytých ploch a systém WMS pro řízení skladu. Služby zahrnují skladování, vychystávání, balení, etiketování a paletizaci, silniční přepravu s vlastním vozovým parkem a distribuci poslední míle, jakož i správu dokumentace. Podle konsorcia je provoz zajištěn 24 hodin denně, 7 dní v týdnu. Způsoby integrace s jednotlivými prodejními platformami je třeba ověřit ve fázi nabídky. K distribuci do Říma viz analýzu [poslední míle na jih Říma]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Zdroje

- AGI, ekonomická zpráva z 27. května 2025 o online nákupech zboží v roce 2025, údaje Osservatorio eCommerce B2c Netcomm – Politecnico di Milano: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), čl. 52 a 56: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Vzdálenosti a časy: výpočet trasy OSRM (Open Source Routing Machine) z areálu na Via della Dinamica, osobní automobil, běžný provoz; zpracování konsorcia.
- SS148 Pontina, jízdní pásy a rychlostní limity: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (údaje ANAS)
- Služby a provoz: údaje Consorzio Logistico Latina Scalo.
