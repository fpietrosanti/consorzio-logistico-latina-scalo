# Roadmap iscrizioni a directory e marketplace (bozza 2026-11-07)

Registro operativo: `registro-directory.csv` (365 voci; colonne `wave` e `status`). Fonti di dettaglio:
`italia-paneuropa-logistica.*`, `eu-ovest-nord.*`, `eu-centro-est-cina.*`.

## Cosa dice la mappatura
- 365 directory/marketplace/associazioni in 25 lingue. **141 escluse**: pagine gialle e registri nazionali esteri
  accettano solo aziende con sede o codice fiscale locale.
- Per un'azienda italiana i canali esteri che funzionano sono pochi e chiari:
  1. piattaforme paneuropee multilingua (Europages: un profilo, 26 lingue; Kompass; wlw per il DACH);
  2. mappe e motori: Google Business Profile, Bing Places, Apple Business, OpenStreetMap, Wikidata;
  3. **Camere di Commercio Italiane all'Estero** (una per Paese: ITKAM, CCI France, Cámara Madrid, CCIIP Polonia,
     Romania, Atene/Salonicco, Praga, Bratislava, Budapest, Sofia, Zagabria, Cina, Hong Kong…) e camere bilaterali
     con sede in Italia (AHK Italien, CCI France Italie): directory soci + eventi B2B, a pagamento (quota associativa);
  4. borse carichi/magazzini: TIMOCOM (borsa magazzini attiva in tutta Europa), Trans.eu (solo carichi), Wtransnet;
  5. associazioni di settore italiane (Assologistica, ALIS, Federlogistica, Confetra, Unindustria);
  6. gare: MePA (Consip), STELLA (Regione Lazio), TED (alert gratuiti);
  7. Cina: AMZ123 e Cifnews (sezioni 海外仓 Italia), JCtrans, account WeChat 服务号. 1688, Baidu Maps, Amap: no
     (serve licenza commerciale cinese).
- Non esistono directory B2B utili in irlandese o maltese: per Irlanda e Malta si usano l'inglese e le camere bilaterali.

## Ruoli (vincolo operativo)
Claude **non crea account e non inserisce password**, nemmeno su richiesta. Il flusso è quindi:
| Passo | Chi |
|---|---|
| Pacchetto dati per lingua (ragione sociale, indirizzo, telefono, P.IVA, descrizioni 160/500/1500 caratteri, categorie, link alle pagine del sito nella lingua giusta, orari, foto) | Claude |
| Apertura della pagina di iscrizione, in ordine di priorità | Claude |
| Creazione account: email dedicata, password (gestore password), CAPTCHA, SMS, clic sul link di conferma | Fabio |
| Compilazione e invio della scheda (descrizioni, categorie, foto, link) dopo ok per ogni lotto | Claude |
| Registro: stato, URL della scheda, backlink, data, note | Claude |
| Verifica mensile: schede online, dati coerenti (NAP), backlink indicizzati | Claude |
| Spese (abbonamenti, quote associative) | decisione di Fabio, proposta con costi |

Email dedicata: va bene (es. `directory@consorziologistico.it` o una casella separata). Claude può leggerla nel browser
per segnalare i link di conferma; il clic che completa l'iscrizione resta a Fabio. WhatsApp Business: +39 0773 316008,
indicato in tutte le schede.

## Prerequisiti (prima dell'ondata 1)
1. **Foto vere del sito** (8–15: esterni, capannoni, scaffalature, baie, piazzale, uffici) e logo in alta risoluzione.
   Le directory e Google premiano foto originali; le foto di repertorio del sito web non vanno usate nelle schede.
2. Dati societari certi: denominazione esatta, P.IVA, PEC, codice ATECO, orari, anno di costituzione, n. addetti (facoltativo).
3. Conferme dal Consorzio sulle dotazioni "da confermare" (docs/DOTAZIONI.md), per non pubblicare dati diversi
   da directory a directory.
4. Email dedicata attiva; gestore password condiviso.

## Ondate
**Ondata 1 – fondamenta (settimana 1–2, 23 voci, gratuite, priorità 4–5)**
Google Business Profile, Bing Places (import da Google), Apple Business, OpenStreetMap, LinkedIn (già attiva),
PagineGialle, Europages (profilo unico multilingua: copre PL, RO, GR, CZ, BG, HR, SI…), Kompass Italia/International,
wlw (verifica caso per caso per sede fuori Germania), Racklify, Trans.eu (account base), MePA, STELLA.
Obiettivo: NAP identico ovunque, scheda Google verificata, profilo Europages in 25 lingue con link alle pagine tradotte.

**Ondata 2 – canali con costo (settimana 3–6, 52 voci, decisione di spesa)**
Camere di Commercio Italiane all'Estero (scegliere 4–6 Paesi target: es. Germania, Francia, Polonia, Romania, Spagna,
Cina), TIMOCOM borsa magazzini (prova gratuita poi abbonamento), Assologistica, ALIS, Unindustria, uffici ICE (gratuiti:
contatto e segnalazione), AMZ123/Cifnews/JCtrans per la Cina, WeChat 服务号 (richiede verifica annuale).
Proposta: preventivo comparativo dei costi prima di procedere.

**Ondata 3 – rinforzo (settimana 6–10, 69 voci)**
Wikidata (voce azienda con coordinate e sito), PagineBianche/Tuttocittà, Hotfrog, Cylex, Enterprise League, CargoLinked,
TED alert, Kompass nazionali, marketplace di spazi (SpaceFill FR, Expozed1 DE, StoringCargo), associazioni logistiche
estere, D&B D-U-N-S.

**Ondata 4 – coda lunga (dal mese 3, 80 voci)**
Directory generaliste gratuite a basso valore (Opendi, MisterImprese, Reteimprese, Brownbook, go4WorldBusiness,
Firmania, Biznes.bg…), solo dove accettano azienda estera e non creano duplicati.

## Automazione
- Pacchetti dati generati da script (`tools/directory_pack.py`, da creare) a partire dai testi già tradotti del sito
  (description, servizi, settori) — nessun testo nuovo da inventare, coerenza garantita.
- Sessioni guidate nel browser: Claude apre la pagina di iscrizione, Fabio crea l'account e risolve CAPTCHA/SMS,
  Claude compila e invia la scheda dopo conferma; lotti da 5–10 directory per sessione.
- Registro aggiornato a ogni passo (status: da fare / account creato / scheda inviata / in verifica / online / respinta).
- Controllo mensile automatico dei link (HTTP + presenza di consorziologistico.it nella pagina) e dei backlink.
- Misura dei risultati: richieste da modulo/WhatsApp con campo "come ci ha conosciuto", traffico per lingua.
