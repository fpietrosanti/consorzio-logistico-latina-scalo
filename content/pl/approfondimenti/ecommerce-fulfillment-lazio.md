---
title: "Fulfillment e-commerce w Lacjum: przepływy, cut-off, zwroty i kurierzy"
description: "Realizacja zamówień e-commerce dla sprzedawcy z Lacjum: od przyjęcia do wysyłki, godziny graniczne, zwroty, kurierzy i odległości drogowe od Rzymu."
date: 2026-10-02
url: "/pl/analizy/fulfillment-ecommerce-lacjum/"
layout: "articolo"
image: "topics/centro-distribuzione"
imageAlt: "Wnętrze centrum dystrybucyjnego z paczkami gotowymi do wysyłki, zdjęcie archiwalne"
summary: "Realizacja zamówień e-commerce powierzona operatorowi zewnętrznemu przebiega według standardowego schematu: integracja zamówień, kompletacja, pakowanie, przekazanie kurierowi i obsługa zwrotów. Dla sprzedawcy z Lacjum decydujące są godzina graniczna przyjmowania zamówień, godzina odbioru przez kurierów i odległość drogowa od aglomeracji rzymskiej."
faq:
  - q: "Czym jest cut-off w fulfillmencie e-commerce?"
    a: "To godzina graniczna, do której zamówienie otrzymane przez magazyn zostaje wysłane tego samego dnia. Zależy od godziny odbioru przez kuriera i od czasu potrzebnego na kompletację i pakowanie; zamówienia otrzymane po godzinie granicznej wyjeżdżają następnego dnia roboczego."
  - q: "Ile czasu ma konsument na zwrot produktu kupionego online?"
    a: "Włoski kodeks konsumencki (D.Lgs. 206/2005, art. 52) przyznaje konsumentowi 14 dni na odstąpienie od umowy bez podania przyczyny, zwykle od dostarczenia towaru. Sprzedawca zwraca płatność w ciągu 14 dni od odstąpienia i może wstrzymać zwrot do chwili otrzymania towaru lub dowodu jego odesłania."
  - q: "Jaka jest odległość z Latina Scalo do Rzymu w dostawach e-commerce?"
    a: "Według wyznaczenia trasy OSRM dla samochodu osobowego obiekt przy Via della Dinamica znajduje się około 70 km od dzielnicy EUR (około 70 minut), około 50 km od Pomezii (około 50 minut) i około 34 km od Aprilii (około 36 minut). Dla pojazdów ciężarowych czasy przejazdu są dłuższe."
  - q: "Jaka jest wartość e-commerce produktowego we Włoszech?"
    a: "Według Osservatorio eCommerce B2c Netcomm Politechniki Mediolańskiej zakupy produktów online we Włoszech szacuje się w 2025 r. na około 40,1 mld euro, o 6% więcej niż w 2024 r., co stanowi 11,2% całkowitych zakupów produktów."
  - q: "Jakie dane są potrzebne do uruchomienia usługi fulfillmentu?"
    a: "Liczba artykułów (SKU), wymiary i wagi, średnia i szczytowa dzienna liczba zamówień, liczba linii na zamówienie, oczekiwany wskaźnik zwrotów, wykorzystywani kurierzy, platforma sprzedażowa i sposób wymiany zamówień, wymagania dotyczące pakowania i materiałów promocyjnych."
---

Realizacja zamówień e-commerce (fulfillment) to segment logistyki kontraktowej o najbardziej rozdrobnionym profilu operacyjnym: wiele małych zamówień, jedna lub dwie linie na zamówienie, wysyłka pojedynczych paczek i udział zwrotów wyższy niż w handlu tradycyjnym. Według Osservatorio eCommerce B2c Netcomm Politechniki Mediolańskiej, cytowanego przez AGI 27 maja 2025 r., zakupy produktów online we Włoszech szacuje się w 2025 r. na około 40,1 mld euro, o 6% więcej niż w 2024 r., co stanowi 11,2% całkowitych zakupów produktów.

Dla sprzedawcy z Lacjum wybór magazynu zależy od kilku mierzalnych parametrów: godziny granicznej przyjmowania zamówień, godziny odbioru przez kurierów, obsługi zwrotów oraz odległości drogowej od klientów końcowych i od sortowni kurierów.

## Przepływ od zamówienia do dostawy

Cykl zamówienia e-commerce obsługiwanego przez operatora zewnętrznego składa się z siedmiu etapów:

1. **przyjęcie towaru** od dostawcy lub producenta, z kontrolą ilościową, rejestracją artykułów (SKU) i odłożeniem na lokalizacje;
2. **integracja zamówień**: zamówienia z platformy sprzedażowej trafiają do systemu WMS (oprogramowania do zarządzania magazynem) operatora przez konektor, plik lub interfejs informatyczny;
3. **kompletacja (picking)**, zwykle na sztuki, z grupowaniem wielu zamówień w jedną ścieżkę pobrań w celu skrócenia tras;
4. **kontrola i pakowanie (packing)**, z doborem kartonu, wypełnieniem, dołączeniem dokumentów i materiałów promocyjnych;
5. **etykietowanie** listem przewozowym kuriera i wygenerowanie numeru śledzenia;
6. **przekazanie kurierowi** przy zaplanowanym odbiorze i przesłanie numeru śledzenia do platformy;
7. **obsługa zwrotów**: przyjęcie, kontrola, decyzja o dalszym przeznaczeniu produktu i aktualizacja stanu magazynowego.

Kompletację, pakowanie i etykietowanie opisano na stronie usługi [obsługi magazynowej]({{< relref "/servizi/handling" >}}); szczególne wymagania tej branży przedstawia strona [e-commerce]({{< relref "/settori/ecommerce" >}}).

## Cut-off i godzina odbioru

**Cut-off** to godzina, do której otrzymane zamówienie zostaje wysłane tego samego dnia. Wyznacza się ją wstecz od godziny odbioru przez kuriera: jeśli kurier przyjeżdża o 17:00, a magazyn potrzebuje średnio dwóch godzin na skompletowanie, spakowanie i skonsolidowanie paczek z jednej fali zamówień, cut-off nie może przypadać później niż o 15:00, a w dniach szczytu trzeba go przesunąć na wcześniej lub zwiększyć obsadę.

Godzinę graniczną przesuwają trzy czynniki:

- **liczba odbiorów** w ciągu dnia i godzina ostatniego odbioru, uzgadniane z każdym kurierem;
- **wydajność kompletacji**, zależna od organizacji lokalizacji: najlepiej sprzedające się artykuły należy umieszczać blisko strefy pakowania;
- **jakość danych** o wadze i wymiarach, które określają karton i stawkę kuriera bez ręcznych pomiarów.

Umowa o świadczenie usług powinna określać cut-off i mierzący go wskaźnik, na przykład odsetek zamówień otrzymanych przed godziną graniczną i wysłanych tego samego dnia. Temat omówiono w poradniku dotyczącym [umowy logistyki kontraktowej i wskaźników KPI]({{< relref "/approfondimenti/logistica-conto-terzi-pmi-contratto-kpi" >}}).

## Kurierzy i geografia Lacjum

Sprzedawca może korzystać z własnych umów z firmami kurierskimi lub z umów wynegocjowanych przez operatora logistycznego. Krajowi kurierzy odbierają przesyłki z magazynu i sortują je we własnych sortowniach; w przypadku regionalnych dostaw B2B lub niewielkiej liczby ciężkich przesyłek operator może korzystać z własnej floty.

Dla magazynu w Latina Scalo odległości drogowe do głównych obszarów popytu, obliczone przy użyciu silnika wyznaczania tras OSRM dla samochodu osobowego przy normalnym natężeniu ruchu, przedstawiają się następująco:

| Miejsce docelowe | Odległość drogowa | Szacowany czas |
|---|---|---|
| Latina, centrum | ok. 8 km | ok. 13 minut |
| Aprilia | ok. 34 km | ok. 36 minut |
| Pomezia | ok. 50 km | ok. 50 minut |
| Santa Palomba | ok. 55 km | ok. 57 minut |
| Castel Romano | ok. 57 km | ok. 56 minut |
| Rzym EUR | ok. 70 km | ok. 70 minut |
| Rzym Ostiense | ok. 74 km | ok. 76 minut |
| Fiumicino | ok. 90 km | ok. 86 minut |

Dla pojazdów ciężarowych i w godzinach szczytu czasy przejazdu są dłuższe. Główną osią w kierunku Rzymu jest droga krajowa 148 Pontina, z dwiema rozdzielonymi jezdniami między Rzymem a Borgo Piave; na odcinku między Pomezią a Latiną Północ ograniczenie prędkości obniżono ze 110 do 80 km/h. Opisy poszczególnych obszarów znajdują się na stronach [logistyka w Rzymie]({{< relref "/logistica/roma" >}}), [Rzym Południe]({{< relref "/logistica/roma-sud" >}}), [EUR]({{< relref "/logistica/eur" >}}) i [Pomezia]({{< relref "/logistica/pomezia" >}}).

## Zwroty

**Prawo odstąpienia od umowy** przysługujące konsumentowi reguluje włoski kodeks konsumencki (D.Lgs. 206/2005). Art. 52 przyznaje 14 dni na odstąpienie bez podania przyczyny, zwykle od dostarczenia towaru. Art. 56 zobowiązuje sprzedawcę do zwrotu płatności w ciągu 14 dni od odstąpienia, z możliwością wstrzymania zwrotu do chwili otrzymania towaru lub dowodu jego odesłania.

Magazyn musi zatem obsługiwać zwroty w terminach zgodnych z tymi wymogami:

- **przyjęcie i rejestracja** zwrotu z numerem pierwotnego zamówienia;
- **kontrola** stanu produktu i opakowania według kryteriów uzgodnionych ze sprzedawcą;
- **przeznaczenie**: ponowne przyjęcie na stan, odnowienie, przepakowanie, sprzedaż jako drugi gatunek lub utylizacja;
- **przekazanie** wyniku do platformy w celu odblokowania zwrotu płatności.

Wydzielona strefa zwrotów, oddzielona od zapasu przeznaczonego do sprzedaży, zapobiega sytuacji, w której niesprawdzony towar ponownie staje się dostępny dla zamówień.

## Sezonowe szczyty i przepustowość

E-commerce koncentruje wolumeny w kilku okresach roku, związanych z promocjami i świętami. Dla operatora oznacza to konieczność zaplanowania dodatkowego personelu, rezerwowych lokalizacji i uzgodnień z kurierami w sprawie dodatkowych odbiorów. Dla sprzedawcy oznacza to obowiązek wcześniejszego przekazania prognoz sprzedaży i kalendarza promocji: niezapowiedziany szczyt jest najczęstszą przyczyną niedotrzymania godziny granicznej.

## Obiekt w Latina Scalo

Consorzio Logistico Latina Scalo przy Via della Dinamica w Latina Scalo (prowincja Latina) dysponuje 19 000 metrów kwadratowych powierzchni krytej i systemem WMS do zarządzania magazynem. Usługi obejmują składowanie, kompletację, pakowanie, etykietowanie i paletyzację, transport drogowy dedykowaną flotą i dystrybucję ostatniej mili, a także obsługę dokumentacji. Według Konsorcjum obiekt działa 24 godziny na dobę, 7 dni w tygodniu. Sposoby integracji z poszczególnymi platformami sprzedażowymi należy zweryfikować na etapie oferty. Dystrybucję do Rzymu omówiono w analizie dotyczącej [ostatniej mili do południowej części Rzymu]({{< relref "/approfondimenti/ultimo-miglio-roma-da-latina" >}}).

## Źródła

- AGI, informacja gospodarcza z 27 maja 2025 r. o zakupach produktów online w 2025 r., dane Osservatorio eCommerce B2c Netcomm – Politecnico di Milano: [agi.it](https://www.agi.it/economia/news/2025-05-27/acquisti-online-crescono-miliardi-euro-2025-31592630/)
- D.Lgs. 6 settembre 2005, n. 206 (Codice del Consumo), art. 52 i 56: [normattiva.it](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-09-06;206)
- Odległości i czasy przejazdu: wyznaczenie trasy OSRM (Open Source Routing Machine) z obiektu przy Via della Dinamica, samochód osobowy, normalny ruch; opracowanie Konsorcjum.
- SS148 Pontina, jezdnie i ograniczenia prędkości: [Wikipedia, Strada statale 148 Pontina](https://it.wikipedia.org/wiki/Strada_statale_148_Pontina) (dane ANAS)
- Usługi i godziny pracy: deklaracje Consorzio Logistico Latina Scalo.
