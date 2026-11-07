# STATE — Espansione SEO-GEO multilingua (avviata 2026-11-07)

Richiesta di Fabio (2026-11-07): strategia SEO-GEO aggressiva. Il Consorzio deve comparire nei motori
di ricerca e nelle AI come riferimento per spazi logistici a Latina e Roma Sud. Una pagina per ogni comune
e località di Roma Sud e della provincia di Latina; tutto tradotto nelle 24 lingue UE + cinese; immagini
reali con licenza libera (niente look "da AI"); stile editoriale delle 3 principali testate di settore.
Lavoro autonomo fino alla fine.

## Regole fisse
- Transitalia MAI sul sito (solo brand/brochure.html).
- Nessun fatto inventato: distanze/tempi da OSRM, dati comuni da Wikidata/ISTAT, fatti normativi con fonte in docs/FACTS.md.
- Foto da Wikimedia Commons / Openverse con licenza libera, attribuzione visibile; le foto generiche non vanno mai presentate come foto del nostro impianto.
- Commit + push a ogni fase.

## Fasi
- [ ] A1 Guida di stile dalle testate di settore → docs/STYLE-GUIDE.md (agente)
- [ ] A2 Verifica fatti (ZLS/ZES, poli logistici) → docs/FACTS.md (agente)
- [ ] A3 Dati comuni: elenco + coordinate + P18 immagine (Wikidata) → data/places.json
- [ ] A4 Distanze/tempi/strade OSRM dall'hub → data/places.json
- [ ] A5 Download immagini + attribuzioni → static/img/places/, data/images.json
- [ ] B  Ristrutturazione Hugo multilingua (content/it, i18n, layout geo/blog, hreflang, schema.org, selettore lingua)
- [ ] C  Contenuti IT: settori (8), blog (12+), hub geografici, FAQ, profili comuni
- [ ] D  Generatore pagine comuni (tools/gen_places.py) per tutte le lingue
- [ ] E  Traduzioni: 23 lingue UE + zh (un agente per lingua)
- [ ] F  Build, verifica, commit, push, verifica live
- [ ] G  LinkedIn: W1–W5 pubblicati il 2026-11-07; programmare W6+ con lo scheduler nativo

## Traduzioni (fase E) — coda
Brief: docs/TRANSLATION-BRIEF.md. Stato: `python tools/translation_status.py`. Gruppi per lingua: nucleo / settori-hub / articoli.
Dopo ogni lingua completa: `python tools/gen_places.py <lang>` (stub comuni + crediti), build, commit.
- Ondata 1 (avviata 2026-11-07): en, de, fr, es, zh, pt (3 gruppi), nl (nucleo, settori-hub).
- In coda: nl articoli; pl (3); ro, el, cs, hu, sv, bg, hr, sk, sl, da, fi, lt, lv, et, ga, mt (3 ciascuna).
- Limite: 20 sub-agenti concorrenti.

## Note per Fabio (da confermare con il Consorzio)
- docs/DOTAZIONI.md "Da confermare": certificazioni, range celle, posti pallet, tariffe, inclusione del lotto in ZLS/ASI.
- Post LinkedIn W1–W5 già pubblicati contenevano errori (Gaeta 40 km, "operiamo in ZLS", HACCP certificato): correggere.

## Log
- 2026-11-07: LinkedIn W1–W5 pubblicati sulla Company Page.
