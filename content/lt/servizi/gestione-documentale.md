---
linkTitle: "Dokumentų valdymas"
title: "Dokumentų valdymas ir WMS logistikai Latina Scalo"
description: "Dokumentų valdymas Latina Scalo (LT): DDT ir važtaraščiai, judėjimų atsekamumas WMS ir integracija su Konsorciumo užsakovų valdymo sistemomis."
url: "/lt/paslaugos/dokumentu-valdymas/"
layout: "servizio"
weight: 8
image: "topics/inventario-barcode"
imageAlt: "Operatorius sandėlyje nešiojamuoju terminalu registruoja pakuotę, archyvinė nuotrauka"
faq:
  - q: "Kokius dokumentus tvarko Consorzio Logistico Latina Scalo?"
    a: "Consorzio Logistico Latina Scalo užsakovų vardu tvarko transporto dokumentus (DDT, italų važtaraščius) ir pristatymo važtaraščius, sandėlio judėjimų registravimą ir vienetų atsekamumą nuo priėmimo iki išsiuntimo, su integracija į klientų valdymo sistemas."
  - q: "Ar Consorzio Logistico Latina Scalo naudoja WMS?"
    a: "Taip. Consorzio Logistico Latina Scalo naudoja WMS (sandėlio valdymo programinę įrangą) vietoms, atsargoms ir judėjimams registruoti. Latina Scalo centre sistema veikia per dedikuotą šviesolaidinę liniją ir pramoninį Wi-Fi sandėlio zonose."
  - q: "Ar Consorzio Logistico Latina Scalo WMS integruojama su kliento valdymo sistema?"
    a: "Consorzio Logistico Latina Scalo numato savo WMS integraciją su užsakovų valdymo sistemomis prekių duomenims, atvykimo pranešimams, užsakymams ir patvirtinimams keistis. Duomenų formatas, dažnumas ir perdavimo būdas nustatomi paslaugos paleidimo etape."
  - q: "Kaip veikia krovinių atsekamumas Latina Scalo?"
    a: "Consorzio Logistico Latina Scalo centre kiekvienas krovinio vienetas priėmimo metu registruojamas WMS ir susiejamas su prekės kodu, kiekiu, vieta ir, jei reikia, partija. Kiekvienas tolesnis perkėlimas iki išsiuntimo lieka užregistruotas, todėl galima atkurti krovinio kelią."
  - q: "Kokių duomenų reikia dokumentų valdymui su Consorzio Logistico Latina Scalo nustatyti?"
    a: "Dokumentų valdymui nustatyti Consorzio Logistico Latina Scalo prašo nurodyti užsakovo naudojamą valdymo sistemą, keičiamų duomenų formatą, išrašytinus dokumentus, sekamus partijos ar galiojimo duomenis ir atsargų bei judėjimų ataskaitų dažnumą."
---

## Dokumentai, duomenys ir atsekamumas vienoje paslaugoje

Consorzio Logistico Latina Scalo užsakovų vardu tvarko dokumentinę ir informacinę logistikos dalį: transporto dokumentų (DDT, italų važtaraščių) ir pristatymo važtaraščių išrašymą, sandėlio judėjimų registravimą WMS (sandėlio valdymo programinėje įrangoje), krovinio vienetų atsekamumą ir integraciją su klientų valdymo sistemomis. Paslauga papildo [sandėliavimą]({{< relref "/servizi/stoccaggio" >}}), [krovą]({{< relref "/servizi/handling" >}}) ir [transportą]({{< relref "/servizi/trasporto" >}}), vykdomus centre Via della Dinamica gatvėje, Tor Tre Ponti zonoje, Latina Scalo (LT).

Centre WMS veikia per dedikuotą šviesolaidinę liniją ir pramoninį Wi-Fi sandėlio zonose; biuruose ir posėdžių salėse dirba personalas, koordinuojantis dokumentus ir informacijos srautus.

## Transporto dokumentai ir važtaraščiai

### Įvežimas

Priimdamas krovinį operatorius palygina jį su tiekėjo DDT ir užsakovo atvykimo pranešimu. Deklaruotų ir gautų kiekių skirtumai bei galimi pažeidimai pažymimi kaip pastabos vežėjo dokumente ir pranešami užsakovui, nurodant pristatymo nuorodą.

### Išvežimas

Pakrovimo metu Konsorciumas užsakovo vardu išrašo transporto dokumentą, nurodydamas gavėją, krovinio aprašymą, pakuočių skaičių ir svorį. Gavėjo pasirašyta kopija po pristatymo grąžinama Konsorciumui, jei pristatymą atliko nuosavas parkas, ir archyvuojama kartu su siuntos duomenimis.

## WMS ir atsekamumas

### Vienetų registravimas

Kiekvienas priimtas krovinio vienetas registruojamas WMS ir susiejamas su prekės kodu, kiekiu ir vieta. Užsakovui pageidaujant, registruojama ir partija bei galiojimo pabaigos data, būtinos [žemės ūkio ir maisto]({{< relref "/settori/agroalimentare" >}}) bei [farmacijos]({{< relref "/settori/farmaceutico" >}}) tiekimo grandinėse.

### Judėjimai

Sistema registruoja kiekvieną tolesnį perkėlimą: padėjimą į vietą, paėmimo zonų papildymą, paėmimą pagal užsakymą, apdorojimo operacijas, pakrovimą. Taip galima atkurti vieneto ar partijos kelią nuo priėmimo iki išsiuntimo – ši informacija naudinga ir atšaukiant produktą ar sprendžiant ginčą su klientu.

### Inventorizacija

Užregistruotos atsargos periodiškai lyginamos su faktine inventorizacija pagal suderintą tvarkaraštį. Skirtumai pranešami užsakovui, nurodant prekę, partiją ir vietą.

## Integracija su valdymo sistemomis

Duomenų mainai tarp užsakovo valdymo sistemos (ERP) ir Konsorciumo WMS paprastai apima keturis srautus:

- **prekių duomenys**: prekių kodai, aprašymai, pakavimo vienetai, matmenys ir svoriai;
- **atvykimo pranešimai**: laukiamas krovinys su tiekėju, kiekiu ir numatoma data;
- **išvežimo užsakymai**: užsakymų eilutės, gavėjai ir pristatymo datos;
- **patvirtinimai**: atlikti priėmimai su galimomis pastabomis, atnaujintos atsargos, išsiųstos siuntos su dokumentų nuorodomis.

Failų formatas, perdavimo kanalas ir mainų dažnumas nustatomi paleidimo projekte, atsižvelgiant į užsakovo naudojamą sistemą. Pradiniuose etapuose arba esant nedideliems kiekiams mainai gali vykti ir standartiniais failais, siunčiamais suderintu laiku.

## Ataskaitos

Užsakovas suderintu periodiškumu gauna duomenis apie atsargas, įvežimus, išvežimus ir neatitikimus. Ataskaitų turinys nustatomas pagal užsakovo kontrolės poreikius, pavyzdžiui, prekių apyvartumą, artėjančio galiojimo pabaigos partijas ar per laikotarpį įvykdytus užsakymus.

## Paslaugos paleidimas

Paleidimas apima keturis žingsnius: prekių duomenų ir dokumentų formatų surinkimą; duomenų srautų ir atsakomybių nustatymą; mainų bandymą su užsakymų imtimi; perėjimą prie įprastos veiklos stebint pirmąsias savaites. Paslauga yra [trečiųjų šalių logistikos (3PL)]({{< relref "/servizi/logistica-3pl" >}}) modelio dalis ir taikoma taip pat [cross-docking]({{< relref "/servizi/cross-docking" >}}) bei [pridėtinės vertės operacijoms]({{< relref "/servizi/lavorazioni-valore-aggiunto" >}}).

## Sektoriai ir teritorija

Atsekamumas pagal partijas ypač svarbus žemės ūkio ir maisto bei farmacijos sektoriams; užsakymų integracija yra esminė [e. prekybai]({{< relref "/settori/ecommerce" >}}) ir [prekybos tinklams bei mažmeninei prekybai]({{< relref "/settori/gdo-retail" >}}), o kodų ir variantų valdymas aktualus [tekstilės ir mados]({{< relref "/settori/tessile-moda" >}}) sektoriui ir [automobilių pramonei]({{< relref "/settori/automotive" >}}). Centras aptarnauja [Latinos]({{< relref "/logistica/latina" >}}), [Aprilia]({{< relref "/logistica/aprilia" >}}), [Cisterna di Latina]({{< relref "/logistica/cisterna-di-latina" >}}) ir [Pomezia]({{< relref "/logistica/pomezia" >}}) įmones, taip pat [Latinos provinciją]({{< relref "/logistica/provincia-di-latina" >}}) ir [Pietų Romą]({{< relref "/logistica/roma-sud" >}}).

## Pasiūlymui gauti

Dokumentų valdymo pasiūlymui nurodykite naudojamą valdymo sistemą, duomenų formatą, kurį užsakovas gali siųsti ir priimti, išrašytinus dokumentus, sekamus partijos ar galiojimo duomenis, vidutinį užsakymų skaičių per dieną ir reikalaujamų ataskaitų periodiškumą. Užklausos siunčiamos per [kontaktinę formą]({{< relref "/" >}}#contatti).
