# FACTS.md: verifica dei fatti per le pagine SEO

**Data di verifica:** 7 novembre 2026
**Ambito:** affermazioni sul territorio, sulle infrastrutture e sui regimi agevolativi da riusare nelle circa 100 nuove pagine di consorziologistico.it.
**Sede di riferimento:** Via della Dinamica snc, zona Tor Tre Ponti, Latina Scalo (LT), coordinate ≈ 41.5100, 12.9508.

**Scala dei verdetti**
- **VERO**: confermato da fonte primaria.
- **PARZIALE**: vero solo con le precisazioni indicate.
- **FALSO**: smentito da fonte primaria.
- **NON VERIFICABILE**: nessuna fonte primaria lo conferma. Non va usato come fatto.

**Avvertenza sulle distanze.** Le distanze stradali si calcolano a parte. I km indicati qui sono **ordini di grandezza** ("circa") per inquadrare i nodi. Prima di pubblicarli vanno sostituiti con i valori del calcolo di percorso.

---

## Sintesi operativa: cosa correggere subito sul sito attuale

| Dove | Testo attuale | Verdetto | Correzione |
|---|---|---|---|
| `themes/clls/layouts/index.html:275` | "Area ZES (Zona Economica Speciale) con agevolazioni fiscali" | **FALSO** | Latina non è in nessuna ZES. Al massimo: "Comune di Latina compreso (in parte) nella Zona Logistica Semplificata (ZLS) del Lazio". |
| `content/posizione.md:56` e `:3`, LinkedIn w01 | "L'area di Latina Scalo rientra nella ZLS" / "Operiamo all'interno della ZLS" | **PARZIALE / NON VERIFICATO per il nostro lotto** | La ZLS è definita per particella catastale: nel Comune di Latina copre 280 ha in aree precise. Non risulta verificato che il lotto di Via della Dinamica sia incluso. Serve il foglio e la particella del sito (vedi §1.4). |
| `content/posizione.md:58-72` | Credito d'imposta, "accesso preferenziale a bandi", "incentivi per l'occupazione" | **PARZIALE / FALSO** | Il credito d'imposta ZLS esiste, ma solo per beni strumentali in particelle ZLS che ricadono anche in area 107.3.c. "Accesso preferenziale a bandi" e "incentivi per l'occupazione" non sono previsti dalla ZLS: vanno tolti. |
| `content/posizione.md:85` | "Agevolazioni fiscali: ZLS attiva" | **PARZIALE** | Togliere, oppure riformulare come "credito d'imposta ZLS per investimenti ammissibili". |
| `index.html:262`, `posizione.md:3,18`, LinkedIn w01/w03 | "40 km dal Porto di Gaeta" | **FALSO** | La distanza su strada è dell'ordine di 75–80 km (da ricalcolare). |
| `posizione.md:30` | "Interporto di Frosinone: a 50 km, con servizi intermodali" | **FALSO** | Secondo il PRMTL della Regione Lazio l'Interporto di Frosinone è "abbandonato" e la sua società di gestione è in liquidazione. Esistono invece terminal ferroviari privati a Frosinone e a Ferentino (vedi §3). |
| `posizione.md:26` | "Raccordo ferroviario nell'area industriale per potenziale trasporto intermodale" | **PARZIALE** | Il terminal intermodale di Latina Scalo (ex zuccherificio) esiste, ma è **non operativo**. La sua messa in esercizio è un intervento previsto dal PRMTL. Va scritto così. |
| `index.html:260` | "SS148 Pontina, uscita Latina Scalo" | **NON VERIFICABILE** | Sulla Pontina non risulta uno svincolo denominato "Latina Scalo". Usare: "raggiungibile dalla SS148 Pontina e dalla SS7 Appia; la SS156 dei Monti Lepini collega Latina a Frosinone e al casello A1". |
| `posizione.md:21` | "SS148 Pontina, arteria a scorrimento veloce Roma–Terracina" | **PARZIALE** | Le carreggiate separate (2+2 corsie) ci sono solo tra Roma e Borgo Piave (Latina). Tra Borgo Piave e Terracina c'è una corsia per senso di marcia. |
| `posizione.md:31` | "Prossimità al futuro completamento dell'autostrada Roma–Latina" | **PARZIALE** | Il progetto è ancora in fase di revisione e non ha cantieri sulla tratta principale. Il cantiere aperto (da ottobre 2026) è quello della bretella Cisterna–Valmontone. |
| `posizione.md:80-83` | "Costo per mq fino al 40% inferiore", "Congestione assente", "Accesso TIR libero 24/7", "60 min (Pontina)" | **NON VERIFICABILE** | Sono affermazioni commerciali senza fonte. Vanno tolte o documentate. La Pontina è nota per traffico intenso e incidentalità, quindi "congestione assente" è rischioso. |
| `posizione.md:19` | "Roma Fiumicino (FCO), il principale aeroporto italiano" | **PARZIALE** | È il primo aeroporto italiano per **passeggeri**. Per le merci il primo è Milano Malpensa. Specificare "per passeggeri". |
| `posizione.md:9` | "area di sviluppo industriale della provincia di Latina" | **VERO con precisazione** | L'agglomerato "Latina Scalo" del Consorzio Industriale del Lazio (ex Consorzio ASI Roma-Latina) copre 448 ha. Non risulta verificato che Via della Dinamica ricada nel perimetro consortile (vedi §7). |

---

## 1. ZLS, ZES, Cassa per il Mezzogiorno e aiuti a finalità regionale

### 1.1 Stato della ZLS del Lazio — VERO (istituita e operativa)

- **Quadro normativo.**
  - L. 27 dicembre 2017, n. 205, art. 1, commi 61–65-bis.
  - DPCM 4 marzo 2024, n. 40 (regolamento ZLS).
- **Iter regionale.**
  - DGR n. 797 del 15/10/2024: prima perimetrazione, 49 comuni, ora superata.
  - **DGR n. 291 del 29/04/2025**: Piano di Sviluppo Strategico "A-Trazione Lazio", configurazione definitiva.
  - Decreto dirigenziale **G13120 dell'11/10/2025**.
- **Istituzione.** **DPCM 17 novembre 2025**, firmato dal sottosegretario Mantovano. Non ho trovato gli estremi di pubblicazione in Gazzetta Ufficiale: citare "DPCM 17 novembre 2025" senza numero di GU.
- **Governance.** Il Comitato di indirizzo è insediato. Ne fanno parte Regione, MIT e Autorità di Sistema Portuale. Il regolamento del Comitato è stato pubblicato ad agosto 2026.
- **Perimetro.**
  - **64 comuni**: 16 in provincia di Roma, 22 di Frosinone, 7 di Rieti, 15 di Latina, 4 di Viterbo.
  - Circa **4.026 ettari** complessivi (stima riportata nel Piano).
  - Porti inclusi: Civitavecchia, Fiumicino e Gaeta.
- **I 15 comuni della provincia di Latina e gli ettari di ciascuno** (Allegato 2 alla DGR 291/2025, "Estensione in ettari per Comune"):

| Comune | Ettari ZLS | Area 107.3.c |
|---|---|---|
| Aprilia | 167,00 | Sì |
| Castelforte | 11,64 | Sì |
| Cisterna di Latina | 192,00 | Sì |
| Fondi | 69,70 | Sì |
| Formia | 124,00 | Sì |
| Gaeta | 142,61 + 17,53 portuali | Sì |
| Itri | 3,70 | Sì |
| **Latina** | **280,00** | **Sì, in parte** |
| Minturno | 59,06 | Sì |
| Monte San Biagio | 12,80 | No |
| Pontinia | 78,17 | No |
| Santi Cosma e Damiano | 10,24 | Sì |
| Sermoneta | 128,00 | No |
| Sezze | 35,25 | No |
| Terracina | 12,89 | No |

**Fonti**
- Pagina ZLS della Regione Lazio: https://regione.lazio.it/zona-logistica-semplificata-ZLS
- Notizia della Regione sulla nascita della ZLS: https://regione.lazio.it/notizie/nasce-la-zona-logistica-semplificata-zls-del-lazio
- Piano di Sviluppo Strategico (ottobre 2025): https://politichecoesione.governo.it/media/pixdvzjt/piano-di-sviluppo-stratetegico.pdf
- Cartografie della provincia di Latina (aprile 2025, con il riepilogo degli ettari): https://politichecoesione.governo.it/media/b3tcef2r/cartografie-provincia-di-latina.pdf
- Analisi catastale (Allegato 1 alla DGR 291/2025): https://regione.lazio.it/sites/default/files/documentazione/2025/DGR-291-2025-allegato1-analisi-catastale.pdf
- Regolamento del Comitato di indirizzo, che cita il DPCM 17/11/2025: https://regione.lazio.it/sites/default/files/2026-08/Regolamento%20del%20Comitato%20di%20Indirizzo%20ZLS.pdf
- RomaToday sui 64 comuni: https://www.romatoday.it/politica/zona-logistica-semplificata-quali-comuni.html
- Il Caffè con l'elenco dei comuni di Latina: https://ilcaffe.tv/articolo/256491/credito-dimposta-e-procedure-piu-snelle-per-le-imprese-di-64-comuni-del-lazio

### 1.2 Latina Scalo e Tor Tre Ponti sono nella ZLS? — PARZIALE / NON VERIFICATO per il lotto

- Il Comune di Latina è nella ZLS **solo in parte**, per 280 ha. La perimetrazione è fatta **per foglio e particella catastale**.
- Nell'Allegato 1 (Analisi catastale), sezione "36. Comune di Latina", le aree incluse sono:
  - "AREA SICAMB": fogli 52 e 63;
  - **"AREA LATINA SCALO"**: fogli 63, 64, 113 e 114, solo 8 particelle;
  - "AREA FULGOR CAVI": foglio 114;
  - "AREA POZZI GINORI": fogli 114 e 116;
  - "AREA F2 PIAVE": fogli 116, 117, 133 e 136;
  - "AREA F2 EPITAFFIO": fogli 139 e 148;
  - "AREA F1 S.S.156": fogli 172, 174, 178, 179 e 180;
  - "PIP CAPOLUOGO".
- La località "Tor Tre Ponti" e Via della Dinamica **non sono nominate**.
- Il Piano (scheda LAZ4) indica come aree consortili nel Comune di Latina "Latina Scalo e Pontinia". La ZLS però non coincide con l'intero agglomerato consortile.
- **Conclusione.** Non si può affermare che il magazzino di Via della Dinamica sia in ZLS finché non si confrontano il suo foglio e la sua particella (visura catastale) con l'Allegato 1. Si può affermare con certezza che "il Comune di Latina è tra i 15 comuni pontini della ZLS del Lazio".

### 1.3 Benefici reali della ZLS — PARZIALE (il sito li descrive in modo impreciso)

**a) Credito d'imposta ZLS**
- **Norma.**
  - Art. 13 DL 7 maggio 2024, n. 60, convertito dalla L. 95/2024.
  - Prorogato dalla **L. 30 dicembre 2025, n. 199** (Legge di bilancio 2026), art. 1, commi 444–447, per gli investimenti **2026, 2027 e 2028**.
  - Limite di spesa di 100 milioni di euro l'anno, per tutte le ZLS italiane.
- **Cosa copre.** L'acquisto di **beni strumentali** destinati a strutture produttive esistenti o nuove nella ZLS, **"limitatamente alle zone ammissibili agli aiuti a finalità regionale a norma dell'articolo 107, paragrafo 3, lettera c), TFUE"**, come individuate dalla Carta degli aiuti 2022-2027 (Provvedimento AdE del 30/01/2026).
- **Intensità.** La massima consentita dalla Carta degli aiuti per la singola area.
- **Percentuali citate dalla stampa** ("25% grandi imprese, 35% PMI"): **non verificate su fonte primaria**. Non usarle.
- **Adempimenti.**
  - Comunicazione preventiva all'Agenzia delle Entrate dal 31 marzo al 30 maggio di ogni anno. La finestra 2026 è chiusa; la prossima va dal 31/03/2027 al 30/05/2027.
  - Comunicazione integrativa obbligatoria.
  - Il credito si usa in compensazione con F24.
- **Soglia minima.** Secondo una scheda informativa (fonte secondaria) i progetti sotto i 200.000 euro non sono agevolabili. Da confermare prima di citarla.

**b) Semplificazioni**
- Il DPCM 40/2024 e il Piano prevedono:
  - procedure semplificate e accelerate;
  - un **SUAP ZLS** come autorità procedente;
  - l'autorizzazione unica e accordi di insediamento con modello standard.
- Formula prudente da usare: "procedure amministrative semplificate e sportello unico (SUAP) dedicato alla ZLS".

**c) Cosa la ZLS NON prevede**
- "Accesso preferenziale a bandi regionali": non trovato.
- "Incentivi per l'occupazione": il bonus assunzioni riguarda la ZES Unica, non la ZLS Lazio.

**Fonti**
- Provvedimento AdE ZLS 2026-2028: https://www.informazionefiscale.it/IMG/pdf/provvedimento_credito_d_imposta_zls_2026-2028.pdf
- Fiscal Focus sulla proroga al 2028: https://www.fiscal-focus.it/quotidiano/il-quotidiano/articoli-fisco/zls-come-funziona-la-proroga-al-2028-del-credito-d-imposta-per-gli-investimenti,3,180669
- Assolombarda, scadenze e comunicazione integrativa: https://www.assolombarda.it/servizi/fisco/scadenze/crediti-d2019imposta-zls-e-zes-unica-mezzogiorno-2013-comunicazione-integrativa
- Scheda sulla soglia dei 200.000 euro (fonte secondaria): https://cafinforma.it/credito-imposta-zls-2026-comunicazione-30-maggio/

### 1.4 Verifica da fare (azione per il cliente)

1. Recuperare dalla visura catastale il **foglio e la particella** del lotto di Via della Dinamica.
2. Cercarli nella sezione "36. Comune di Latina" dell'Allegato 1, intorno a pagina 114 del PDF.
3. Solo se la particella è presente e marcata "Compresa" (area TFUE 107.3.c) si potrà scrivere: "il nostro sito ricade nella ZLS del Lazio, in area ammissibile al credito d'imposta".

### 1.5 Latina è in una ZES? — FALSO

- La **ZES Unica** (art. 9 DL 124/2023) comprende Abruzzo, Basilicata, Calabria, Campania, Molise, Puglia, Sicilia e Sardegna.
- Dal 20/11/2025 comprende anche **Marche e Umbria** (L. 18 novembre 2025, n. 171).
- **Il Lazio non c'è.** Prima del 2024 non esistevano ZES laziali: le ZES regionali erano solo nel Mezzogiorno.
- La CGIL Lazio ha anzi criticato il governo proprio per l'esclusione del Lazio dalla ZES.
- **Fonti**
  - Camera dei Deputati, tema ZES Unica (aggiornato al 14/07/2026): https://temi.camera.it/leg19/temi/zona-economica-speciale-per-il-mezzogiorno-zes-unica.html
  - Estensione a Marche e Umbria: https://www.partitaiva.it/zes-marche-umbria-domande-agevolazioni/
  - CGIL Lazio: https://lazio.cgil.it/2025/11/lazio-di-cola-cgil-senza-zes-governo-mortifica-il-territorio/

### 1.6 Ex Cassa per il Mezzogiorno — VERO (fatto storico, senza effetti oggi)

- La provincia di Latina, insieme a quella di Frosinone, rientrava nel territorio d'intervento della Cassa per il Mezzogiorno (L. 646/1950 e successive modifiche, attiva fino al 1984–1992).
- Oggi non dà diritto ad alcuna agevolazione: va usato solo come contesto storico.
- **Fonti**
  - Atti parlamentari sull'art. 3 della L. 646/1950: https://www.senato.it/service/PDF/PDFServer/DF/261976.pdf
  - Il Fatto Quotidiano, 2012 (fonte secondaria): https://www.ilfattoquotidiano.it/2012/07/29/economia-e-politica-locale/309589/

### 1.7 Aiuti a finalità regionale 107.3.c — PARZIALE

- Nella Carta degli aiuti a finalità regionale 2022-2027 il Comune di Latina risulta area 107.3.c **"Sì, in parte"**.
- Nell'Analisi catastale ZLS quasi tutte le particelle ZLS di Latina sono "Compresa" nell'area TFUE. Fanno eccezione alcune particelle dell'"AREA F1 S.S.156" (foglio 172 e la particella 18 del foglio 174).
- Pontinia, Sermoneta, Sezze, Terracina e Monte San Biagio **non** sono in area 107.3.c.
- **Fonti**
  - Piano ZLS, tabella "Area 107.3 lett. C" (pp. 57–58).
  - Mappa interattiva della Carta degli aiuti: https://politichecoesione.governo.it/it/politica-di-coesione/la-programmazione-2021-2027/risorse-2021-2027/aiuti-a-finalita-regionale-2022-2027/

---

## 2. Rete stradale

### 2.1 SS148 Pontina — VERO con precisazioni

- È una strada statale lunga **109,2 km**, da Roma a Terracina.
- **Gestore.** ANAS, che l'ha ripresa il **21 gennaio 2019** dopo la gestione regionale (ASTRAL dal 2007).
- **Carreggiate.**
  - **Roma–Borgo Piave (Latina)**: due carreggiate separate con due corsie ciascuna, con caratteristiche di superstrada.
  - **Borgo Piave–Terracina**: una corsia per senso di marcia, con spartitraffico in alcuni tratti.
- **Limite di velocità.** Nel tratto Pomezia–Latina nord è stato abbassato da 110 a 80 km/h.
- Nella tabella del percorso compaiono le voci "Piattaforma Logistica Integrata" e "Dogana – Latina Scalo". Uno **svincolo denominato "Latina Scalo"** non è confermato.
- Secondo il PRMTL, l'area del terminal di Latina Scalo è "raggiungibile attraverso la SS 148 Pontina e la SS 7 Appia", e "la SS 156 Monti Lepini lo unisce allo snodo autostradale di Frosinone".
- **Fonti**
  - Wikipedia, SS148 (fonte secondaria, dati ANAS): https://it.wikipedia.org/wiki/Strada_statale_148_Pontina
  - PRMTL Lazio, "Il Sistema della Logistica", §3.1.7: https://www.regione.lazio.it/sites/default/files/2022-11/Il-Sistema-Logistica.pdf

### 2.2 Autostrada Roma–Latina — PARZIALE ("futuro completamento" è fuorviante)

- Il progetto è stato rivisto: il bypass di Aprilia è stato eliminato e il tracciato seguirà quello della Pontina attuale.
- L'ingresso su Roma è ancora da progettare.
- A ottobre 2026 si dichiarava che non sarà conclusa entro l'attuale consiliatura regionale.
- **Nessuna data di apertura certa.**
- **Fonti**
  - Giornale del Lazio, 25/10/2026: https://www.giornaledellazio.it/partiti-i-lavori-della-cisterna-valmontone/
  - Giornale del Lazio sul taglio del bypass di Aprilia: https://www.giornaledellazio.it/roma-latina-confermato-il-taglio-del-bypass-su-aprilia-e-manca-il-progetto-sullaccesso-a-roma/
  - Consiglio regionale, commissione Lavori pubblici: https://www.consiglio.regione.lazio.it/?vw=commissioniNewsDettaglio&id=3832&cid=33

### 2.3 Bretella Cisterna–Valmontone — VERO (cantiere avviato a ottobre 2026)

- I lavori sono iniziati ai primi di ottobre 2026 dal cantiere di Campoverde, sulla Pontina.
- **Caratteristiche.**
  - Lunghezza circa 31,5–33 km.
  - Svincoli a Campoverde, Cisterna di Latina, Lariano e Labico.
  - Classificata come strada extraurbana principale, quindi **gratuita**.
  - Costo di circa 1,1 miliardi di euro.
- **Attuatore.** Il commissario straordinario Antonio Mallamo.
- **Tempi.**
  - Il Piano ZLS indicava la fine dei lavori al 2028.
  - Ad ottobre 2026 si parla di "fino a dieci anni" come tempo massimo, con aperture per tratti.
  - **Non indicare una data di apertura.**
- **Fonti**
  - Giornale del Lazio, 25/10/2026 (link sopra).
  - Piano ZLS, scheda LAZ4.

### 2.4 Caselli A1 di riferimento — PARZIALE (qualitativo; km da calcolare)

- I caselli A1 utili per i mezzi pesanti da Latina Scalo sono:
  - **Frosinone**, via SS156 dei Monti Lepini. È il collegamento citato dal PRMTL.
  - **Valmontone** e **Colleferro**, via Cisterna e Velletri sulla viabilità ordinaria, finché non sarà aperta la bretella Cisterna–Valmontone.
- Quale casello sia il "più vicino" dipende dal percorso: va stabilito con il calcolo stradale.
- **Fonti:** PRMTL §3.1.7; Piano ZLS, scheda Colleferro, che cita la "direttrice trasversale Cisterna-Valmontone" e l'A1.

---

## 3. Ferrovia e intermodalità

### 3.1 Stazione di Latina — VERO

- La stazione di Latina è a **Latina Scalo**, sulla linea **Roma–Formia–Napoli**.
- RFI gestisce l'infrastruttura, Trenitalia il servizio: regionali (FL7), Intercity e Intercity Notte.
- È dotata di scalo merci, con un raccordo verso un impianto industriale vicino.
- **Fonte:** https://it.wikipedia.org/wiki/Stazione_di_Latina, linea confermata anche dal PRMTL.

### 3.2 Raccordo e terminal di Latina Scalo — PARZIALE

- Sull'area dell'ex zuccherificio di Latina Scalo esiste un **terminal intermodale**:
  - ha lavorato dal 2000;
  - oggi è **non operativo**: il PRMTL lo indica tra i terminal "che al momento non sono operativi".
- **Dotazioni** (PRMTL):
  - fascio di 3 binari lungo oltre 500 m;
  - 2 magazzini per più di 9.000 mq;
  - raccordo con la stazione con raggio di curva di circa 150 m, smantellato per circa 60 m.
- Il PRMTL prevede la "**messa in esercizio del terminal di Latina Scalo**" come terminal del freddo per le filiere chimico-farmaceutica e agroalimentare.
- **Non ho trovato conferma** di un raccordo ferroviario attivo nella zona Tor Tre Ponti né al servizio del nostro sito.
- **Fonti**
  - PRMTL, pp. 17 e 36–37: https://www.regione.lazio.it/sites/default/files/2022-11/Il-Sistema-Logistica.pdf
  - Lestradeferrate.it: https://www.lestradeferrate.it/58formia/58latina.htm

### 3.3 Terminal intermodali e interporti più vicini

I km sono **indicativi**, su strada, da ricalcolare.

| Nodo | Fatti verificati | Distanza indicativa da Latina Scalo | Fonte |
|---|---|---|---|
| **Terminal Pomezia–Santa Palomba** (SGT, gruppo FS) | Primo terminal intermodale del Lazio, con circa 60.000 UTI/anno. È il principale scalo regionale per merci pericolose. Ha 6 binari intermodali e 5 tradizionali su circa 132.000 mq, ed è sulla linea Roma–Napoli via Formia. Il Piano ZLS indica un traffico orientativo di 2.080 coppie di treni/anno. È nodo **Core** della rete TEN-T (Pomezia). | circa 45 km | PRMTL p. 16; Piano ZLS pp. 51–52, 60 |
| **Terminal di Frosinone** (Gruppo Cianfrocca) e **Terminal di Ferentino** (TOTI Trans) | Raccordo privato con la stazione di Frosinone. Ferentino ha 6 binari da 400 m e un binario da 520 m, su circa 135.000 mq. Dal 2021 è collegato con treni intermodali a Busto Arsizio–Sacconago. | circa 65–70 km (SS156) | PRMTL p. 17; Malpensa News |
| **"Interporto di Frosinone"** | **Abbandonato**: la società di gestione è in liquidazione (PRMTL). | — | PRMTL p. 17 |
| **Terminal di Anagni** (DGL) | Polo logistico di circa 230.000 mq. | circa 70–80 km | PRMTL p. 17 |
| **Piattaforma logistica / Interporto Roma–Fiumicino** | Polo previsto per traffico gomma–ferro–mare–aereo con un obiettivo di 2,5 Mt/anno. Il terminal ferroviario è **allo studio**. È adiacente alla Cargo City di FCO. | circa 85–90 km | Piano ZLS pp. 49–50 |
| **Interporto Centro Italia Orte** | Vicino al casello A1. Ha un magazzino da 12.000 mq; la parte ferroviaria era in ultimazione nel 2022. Nodo TEN-T Comprehensive. | circa 150 km | PRMTL p. 17; Piano ZLS p. 51 |
| **Interporto Sud Europa (Marcianise, CE)** e **Interporto Campano (Nola, NA)** | I principali interporti campani. Non sono stati verificati dati aggiornati. | circa 170–200 km | — (solo inquadramento) |

**Link alle fonti**
- Malpensa News (2021): https://www.malpensanews.it/2021/07/nuovo-traffico-intermodale-tra-i-terminal-di-sacconago-e-ferentino-tre-viaggi-a-settimana/864461/
- Anche il Mercato Ortofrutticolo di Fondi (MOF) e il CAR di Guidonia **non sono serviti dalla ferrovia** (PRMTL p. 17). Uno scalo ferroviario per il MOF è previsto dal PRMTL (§3.1.6).

---

## 4. Porti

### 4.1 Porto di Gaeta — VERO (porto commerciale). La distanza di 40 km è FALSA.

- Appartiene all'**Autorità di Sistema Portuale del Mar Tirreno Centro-Settentrionale** (sistema Civitavecchia–Fiumicino–Gaeta, "Porti di Roma e del Lazio"). **Non** appartiene all'AdSP del Mar Tirreno Centrale.
- **Traffico.**
  - 2025: **1.786.317 tonnellate** (−0,7% sul 2024), quasi solo rinfuse liquide e solide.
  - Primo semestre 2026: 935.202 t (+13%).
- È nodo **Comprehensive** della rete TEN-T. È incluso nella ZLS, con 17,53 ha di aree portuali.
- **Fonti**
  - Shipping Italy, 17/02/2026: https://www.shippingitaly.it/2026/02/17/nei-porti-del-lazio-oltre-131-mln-di-tonnellate-e-35-mln-di-crocieristi-nel-2025/
  - Shipping Italy, 18/08/2026: https://www.shippingitaly.it/2026/08/18/merci-15-e-crocieristi-89-in-aumento-a-civitavecchia-nella-prima-meta-del-2026/
  - Cartografie ZLS Latina.

### 4.2 Civitavecchia — VERO

- È il porto principale del Lazio e la porta del sistema AdSP del Mar Tirreno Centro-Settentrionale.
- **Traffico 2025 del sistema AdSP:** **13.128.936 t** (+0,3%), circa 3,5 milioni di crocieristi, automotive in crescita.
- **Ruolo per le merci.** Ro-Ro e autostrade del mare, automotive, agroalimentare refrigerato (Forest Fruit Terminal, banchina 24).
- Il Piano ZLS cita la tendenza del farmaceutico di Pomezia e Latina a guardare a Civitavecchia "come naturale nodo, anche grazie alle sue potenzialità nella catena del freddo".
- **Fonti**
  - Statistiche AdSP MTCS 2025: https://portidiroma.it/sites/default/files/allegati/Traffici%20AdSP%20del%20Mar%20Tirreno%20Centro%20Settentrionale%20-%20Anno%202025.pdf
  - Piano ZLS, scheda LAZ8.

### 4.3 Napoli e Salerno — PARZIALE (solo inquadramento)

- Sono i porti container e Ro-Ro della Campania, gestiti dall'AdSP del Mar Tirreno Centrale. Sono raggiungibili da Latina via A1 o via SS7/Formia.
- Nel 2025 Napoli ha registrato una forte crescita degli sbarchi di container (+39% secondo Shipping Italy).
- **Non ho dati primari verificati sui TEU 2025**: non citarne.
- **Fonte:** https://www.shippingitaly.it/2026/03/14/il-traffico-container-gateway-dei-porti-italiani-tornato-ai-livelli-del-2018/

---

## 5. Geografia logistica di Roma Sud e della provincia di Latina

### Santa Palomba / Pomezia
- È l'agglomerato del Consorzio Industriale del Lazio più esteso nell'area Roma-Latina: **483 ha** (318 industriali), tra Roma e Pomezia.
- Ci sono multinazionali come Johnson & Johnson, Procter & Gamble e Fiorucci, e operatori logistici come DHL Supply Chain, GLS, STEF, Rifline e Cab Log.
- Ci lavorano piattaforme della GDO per conto terzi: SMA-Auchan, Coop, Carrefour, Pam Panorama.
- Ha il terminal intermodale SGT (vedi §3.3). Pomezia è anche un polo chimico-farmaceutico (ACS Dobfar, Alfasigma, Menarini Biotech).
- **Fonti:** Piano ZLS pp. 35–36, 51–52; Consorzio, agglomerati: https://www.consorzioasi.com/agglomerati-industriali/

### Castel Romano
- È un agglomerato consortile nel Comune di Roma, al **km 23 della Pontina**, a sud-ovest della città.
- Superficie di **266 ha**, di cui 191 industriali.
- **Fonte:** https://www.consorzioasi.com/agglomerati-industriali/
- Non ho altre fonti primarie sugli operatori: non citare nomi di aziende.

### Aprilia
- Agglomerato consortile tra Aprilia e Lanuvio, di **256 ha** (184 industriali).
- Fa parte della sub-area ZLS LAZ4 (167 ha ZLS nel Comune, area 107.3.c). La specializzazione dell'area LAZ4 è "fabbricazione di medicinali e preparati farmaceutici".
- **Fonti:** Consorzio; Piano ZLS, scheda LAZ4; Allegato 2 alla DGR 291/2025.

### Cisterna di Latina
- Agglomerato consortile di **368 ha** (234 industriali), con 192 ha in ZLS, area 107.3.c.
- È il punto d'innesto della bretella Cisterna–Valmontone.
- Il Piano ZLS cita per Cisterna e Latina aziende come Nuova Ompi (Stevanato Group), BSP Pharmaceuticals e Plasta Rei.
- **Fonti:** Consorzio; Piano ZLS, LAZ4.

### Latina Scalo, Tor Tre Ponti, Borgo Piave e Mazzocchio
- **Agglomerato "Latina Scalo"**: 448 ha (306 industriali), nei Comuni di Latina, Sermoneta e Sezze.
- La sede del Consorzio Industriale del Lazio (ex ASI Roma-Latina) è in **Via Carrara 12/A, loc. Tor Tre Ponti, Latina**.
- **Agglomerato "Mazzocchio"**: 445 ha (259 industriali) a Pontinia, al confine con Priverno e Sonnino.
- **Agglomerato "Pontinia"**: 126 ha.
- "Borgo Piave" **non è un agglomerato consortile**. Compare però nella ZLS come "AREA F2 PIAVE" del Comune di Latina.
- Nella LAZ4 (Aprilia, Cisterna, Latina in parte, Pontinia) il Piano ZLS conta 40.286 unità locali e 150.336 addetti (dati 2022). Tra le specializzazioni c'è il "trasporto di merci su strada".
- **Fonti:** Consorzio; Piano ZLS, LAZ4.

### Pontinia e Sezze
- Pontinia (78,17 ha) e Sezze (35,25 ha) sono nella ZLS, ma **non** in area 107.3.c: niente credito d'imposta ZLS.
- **Fonte:** Allegato 2 alla DGR 291/2025.

### Fondi — MOF
- È il **Centro Agroalimentare all'Ingrosso di Fondi (MOF ScpA)**, classificato Mercato agroalimentare di Interesse Nazionale.
- **Dati dichiarati dal gestore:**
  - 335 ettari di superficie;
  - 93 aziende concessionarie, di cui 7 cooperative con circa 2.500 produttori;
  - "quasi 10 milioni di quintali" movimentati ogni anno, cioè circa 1 milione di tonnellate;
  - centrale frigorifera da 50.000 quintali;
  - 2 piattaforme a temperatura controllata da 7.000 mq con 38 baie.
- La formula **"uno dei più grandi d'Europa"** è diffusa ma **non verificata su fonte primaria**. Usare "tra i principali mercati ortofrutticoli all'ingrosso d'Italia" oppure citare i dati MOF con attribuzione.
- Non è servito dalla ferrovia (PRMTL).
- **Fonte:** https://www.mof.it/index.php/mof

### Colleferro e Valmontone
- Colleferro è un polo dell'industria aerospaziale (Avio).
- Ospita lo **SLIM**, il Sistema Logistico Integrato Multimodale di Colleferro, realizzato in parte.
- Le sue aree produttive sono tra la direttrice Cisterna–Valmontone e l'A1, vicino alla linea Roma–Cassino.
- È nella ZLS ma **non** in area 107.3.c.
- **Fonte:** Piano ZLS, scheda Colleferro e p. 52.

### Fiumicino
- La Cargo City dell'aeroporto Leonardo da Vinci è un gate internazionale. Accanto c'è la piattaforma logistica (Interporto) Roma–Fiumicino (vedi §3.3).
- FCO è nodo **Core** della rete TEN-T.
- **Fonte:** Piano ZLS pp. 49–50, 60; PRMTL §3.2.

### Farmaceutico (quadro provinciale)
- Nel 2025 **Latina è la 2ª provincia italiana** per export dell'industria farmaceutica, Frosinone la 4ª (Camera di Commercio Frosinone-Latina su dati ISTAT).
- Latina è il 19° esportatore provinciale d'Italia (1,6% dell'export nazionale).
- Latina e Frosinone insieme spiegano il **55,7% dell'export laziale**.
- **Fonte:** https://www.frlt.camcom.it/sites/default/files/contenuto_redazione/Osserfare/1_Pilloleconomiche%20EXPORT%202026.pdf

---

## 6. Agroalimentare dell'Agro Pontino

- **Kiwi Latina IGP.**
  - Registrato come IGP con Reg. (CE) n. 1486/2004. Varietà Hayward (Actinidia deliciosa).
  - La zona di produzione comprende comuni delle province di Latina e Roma (24 comuni secondo il disciplinare modificato nel 2018).
  - Resa massima: 380 q/ha.
  - L'Agro Pontino è stato tra i primi territori italiani con impianti specializzati di actinidia, negli anni '70.
  - **Fonti:**
    - Disciplinare (DM Mipaaf 27/02/2018): https://www.unionalimentari.com/wp-content/uploads/2024/09/Mipaaf-27.2.2018-disciplinare-Kiwi-LatinaCOMPL.pdf
    - Scheda ARSIAL: https://www.arsial.it/wp-content/uploads/2025/06/KiwiLatinaIGP.pdf
- **Primato del Lazio nel kiwi.** Il Lazio è indicato come il distretto più importante d'Italia per la produzione di kiwi. La fonte è giornalistica (askanews, 2025), quindi la frase va **attribuita**. Non ho trovato la quota percentuale su dati ISTAT o CSO.
- **Moria del kiwi.** La fitopatia ha colpito soprattutto la provincia di Latina. La Regione ha stimato circa 215 milioni di euro di danni sul raccolto 2023 (fonte: Linkiesta, che cita la Regione; Regione Lazio: https://regione.lazio.it/notizie/moria-kiwi-ministero-agricoltura).
- **Ortofrutta e IV gamma.**
  - La provincia di Latina ha un ampio comparto in serra, concentrato a Sabaudia, Terracina e Fondi. L'ultimo dato trovato è di circa 2.300 ha, ma **risale al 2002**: non usare la cifra.
  - Non ho dati recenti verificati sulla IV gamma: usare solo formule qualitative.
- **Export agricolo.** L'agricoltura vale il 2,5% dell'export della provincia di Latina (CCIAA Frosinone-Latina, 2026).
- **Specializzazione logistica.** Il PRMTL individua per il terminal di Latina Scalo la "naturale vocazione" verso filiere a temperatura controllata (agroalimentare e chimico-farmaceutico).

---

## 7. Consorzio Industriale del Lazio (ex Consorzio ASI Roma-Latina)

- Il **Consorzio Industriale del Lazio** è il consorzio unico regionale.
  - È previsto dalla L.R. 7/2018, art. 40; il progetto di fusione è stato approvato con DGR 328 del 4/6/2021.
  - Risulta costituito il 1/12/2021.
  - Ha unito 5 consorzi: Roma-Latina, Sud Pontino, Frosinone, COSILAM (Cassino) e Rieti.
  - Dal 2024 è guidato da un Commissario straordinario (L.R. 23/2023).
- **Agglomerati in provincia di Latina e nell'ex area Roma-Latina** (ettari totali / industriali):

| Agglomerato | Superficie | Comuni |
|---|---|---|
| Aprilia | 256 / 184 ha | Aprilia, Lanuvio |
| Cisterna di Latina | 368 / 234 ha | Cisterna di Latina |
| Latina Scalo | 448 / 306 ha | Latina, Sermoneta, Sezze |
| Pontinia | 126 / 102 ha | Latina, Pontinia, Sabaudia |
| Mazzocchio | 445 / 259 ha | Pontinia |
| Castel Romano | 266 ha | Roma |
| Santa Palomba | 483 ha | Roma, Pomezia |

- **Ex Consorzio Sud Pontino** (circa 12 comuni):
  - Formia: Penitro, Ponzanello–Mamurrano e Castagneto (aree a servizio della portualità);
  - Minturno: Penitro e Parchi;
  - Gaeta: Monte Conca;
  - Santi Cosma e Damiano: Pantaniello;
  - Fondi: area industriale comunale.
  - Il Consorzio è proprietario della linea ferroviaria Formia–Gaeta (ex "Littorina"), che è in fase di riattivazione.
- **Fonti**
  - https://www.consorzioasi.com/agglomerati-industriali/
  - Piano ZLS, schede LAZ4 e LAZ5-7.
  - Piano regolatore dell'ex Consorzio Roma-Latina (portale trasparenza): https://consorziolazio.portaletrasparenza.net/it/trasparenza/pianificazione-e-governo-del-territorio/piano-regolatore-ex-consorzio-per-lo-sviluppo-industriale-roma-latina.html
  - Regione Lazio sul consorzio unico: https://regione.lazio.it/notizie/consorzio-industriale-unico-lazio
- **Da verificare.** Va controllato se il lotto di Via della Dinamica ricada nel perimetro dell'agglomerato "Latina Scalo" sulle tavole del Piano regolatore consortile. È plausibile, data la vicinanza alla sede consortile di Tor Tre Ponti, ma **non verificato**.

---

## Frasi approvate (riusabili così come sono)

1. Il Consorzio Logistico Latina Scalo opera in Via della Dinamica, nella zona di Tor Tre Ponti, a Latina Scalo (LT).
2. Latina Scalo ospita la stazione ferroviaria di Latina, sulla linea Roma–Formia–Napoli.
3. La stazione di Latina è servita da treni regionali e da collegamenti Intercity sulla direttrice tirrenica Roma–Napoli.
4. Latina Scalo è raggiungibile dalla SS148 Pontina e dalla SS7 Appia.
5. La SS156 dei Monti Lepini collega Latina a Frosinone e al sistema autostradale dell'A1.
6. La SS148 Pontina, gestita da ANAS, collega Roma a Terracina per circa 109 km.
7. Tra Roma e Latina (Borgo Piave) la Pontina ha due carreggiate separate a due corsie per senso di marcia.
8. Dall'ottobre 2026 è in costruzione la bretella Cisterna–Valmontone, che collegherà la Pontina all'A1 all'altezza di Valmontone.
9. La bretella Cisterna–Valmontone sarà una strada extraurbana principale, senza pedaggio, con svincoli a Campoverde, Cisterna di Latina, Lariano e Labico.
10. Il progetto dell'autostrada Roma–Latina è in fase di revisione: oggi la Pontina resta l'asse principale tra Roma e Latina.
11. La Zona Logistica Semplificata (ZLS) del Lazio, istituita con DPCM del 17 novembre 2025, comprende 64 comuni, di cui 15 in provincia di Latina.
12. Il Comune di Latina è tra i 15 comuni pontini inclusi in parte nella ZLS del Lazio, per circa 280 ettari individuati su base catastale.
13. In provincia di Latina la ZLS interessa, tra gli altri, Aprilia, Cisterna di Latina, Latina, Pontinia, Sermoneta, Sezze, Fondi, Formia e Gaeta.
14. Nelle aree ZLS ammissibili agli aiuti a finalità regionale, le imprese possono accedere a un credito d'imposta sugli investimenti in beni strumentali, prorogato per gli anni 2026–2028.
15. L'accesso al credito d'imposta ZLS dipende dalla particella catastale dell'investimento e richiede una comunicazione preventiva all'Agenzia delle Entrate.
16. La ZLS prevede procedure amministrative semplificate e uno sportello unico (SUAP) dedicato.
17. La ZLS del Lazio comprende i porti di Civitavecchia, Fiumicino e Gaeta.
18. Il porto di Gaeta fa parte dell'Autorità di Sistema Portuale del Mar Tirreno Centro-Settentrionale, insieme a Civitavecchia e Fiumicino.
19. Nel 2025 il porto di Gaeta ha movimentato circa 1,8 milioni di tonnellate di merci, soprattutto rinfuse.
20. Nel 2025 il sistema portuale di Civitavecchia, Fiumicino e Gaeta ha movimentato oltre 13 milioni di tonnellate di merci.
21. Civitavecchia è il principale porto del Lazio, con traffici Ro-Ro, automotive e una crescente vocazione per il freddo.
22. Il terminal intermodale di Pomezia–Santa Palomba è il primo del Lazio per unità di trasporto intermodale movimentate.
23. Santa Palomba è uno dei principali poli logistici del Lazio: ospita operatori logistici e piattaforme della grande distribuzione.
24. A Ferentino e Frosinone operano terminal ferroviari merci raccordati alla rete nazionale.
25. Il Piano regionale della mobilità, dei trasporti e della logistica del Lazio prevede la rimessa in esercizio del terminal ferroviario di Latina Scalo.
26. Il terminal di Latina Scalo è indicato dalla Regione come candidato a terminal per le filiere a temperatura controllata, agroalimentare e farmaceutica.
27. Il Consorzio Industriale del Lazio, nato dalla fusione di cinque consorzi industriali, ha sede operativa a Latina in località Tor Tre Ponti.
28. L'agglomerato industriale di Latina Scalo si estende per circa 448 ettari tra i comuni di Latina, Sermoneta e Sezze.
29. Nell'area tra Roma Sud e Latina si trovano gli agglomerati industriali di Castel Romano, Santa Palomba, Aprilia, Cisterna di Latina, Latina Scalo, Pontinia e Mazzocchio.
30. Nel 2025 Latina è la seconda provincia italiana per esportazioni dell'industria farmaceutica (elaborazioni della Camera di Commercio Frosinone-Latina su dati ISTAT).
31. Le province di Latina e Frosinone insieme generano oltre la metà dell'export del Lazio.
32. Il polo produttivo di Aprilia, Cisterna e Latina è specializzato nella fabbricazione di medicinali e preparati farmaceutici.
33. Il Kiwi Latina IGP, riconosciuto dall'Unione europea nel 2004, è prodotto in comuni delle province di Latina e Roma.
34. L'Agro Pontino è stato tra i primi territori italiani a ospitare impianti specializzati di kiwi, già negli anni Settanta.
35. Il Centro Agroalimentare all'Ingrosso di Fondi (MOF) è un Mercato agroalimentare di interesse nazionale e, secondo il gestore, movimenta quasi 10 milioni di quintali di merci l'anno.
36. Il MOF di Fondi dispone di una centrale frigorifera e di piattaforme logistiche a temperatura controllata.
37. Latina Scalo si trova lungo la direttrice tirrenica tra Roma e Napoli, a servizio del bacino produttivo pontino.
38. La provincia di Latina rientrava storicamente nell'area d'intervento della Cassa per il Mezzogiorno.

Avvertenze per l'uso:
- Le frasi 12–15 descrivono il regime e **non** affermano che il nostro sito vi rientri.
- Usare "il nostro sito è in ZLS" solo dopo la verifica del §1.4.

## Frasi vietate (false, imprecise o non verificabili)

1. "Area ZES (Zona Economica Speciale)", "in ZES", "ZES Lazio", "ZES Unica" riferito a Latina. **FALSO**: il Lazio non è nella ZES Unica.
2. "Agevolazioni ZES", "bonus assunzioni ZES", "decontribuzione Sud" per imprese insediate a Latina. **FALSO**.
3. "Latina Scalo (o Tor Tre Ponti) rientra nella ZLS" o "operiamo all'interno della ZLS". **NON VERIFICATO** finché manca il riscontro di foglio e particella (§1.4).
4. "Tutta Latina / tutta la provincia di Latina è ZLS". **FALSO**: solo 15 comuni, e Latina solo in parte (280 ha).
5. "Credito d'imposta ZLS per tutte le imprese della ZLS". **FALSO**: vale solo nelle particelle ZLS in area 107.3.c (escluse ad esempio Pontinia, Sermoneta, Sezze e Terracina) e solo per beni strumentali.
6. "Credito d'imposta del 25% (grandi imprese) / 35% (PMI)" o qualunque percentuale fissa. **NON VERIFICATO**: l'intensità dipende dalla Carta degli aiuti.
7. "Accesso preferenziale a bandi e finanziamenti regionali" e "incentivi per l'occupazione" come benefici della ZLS. **NON PREVISTI**.
8. "Agevolazioni fiscali: ZLS attiva" come vantaggio generico del nostro magazzino. **FUORVIANTE**.
9. "A 40 km dal Porto di Gaeta". **FALSO**: la distanza è dell'ordine di 75–80 km (da ricalcolare).
10. "Interporto di Frosinone a 50 km, con servizi intermodali". **FALSO**: l'Interporto di Frosinone è abbandonato.
11. "Raccordo ferroviario attivo / servizi intermodali disponibili a Latina Scalo". **FALSO allo stato**: il terminal non è operativo.
12. "Uscita Latina Scalo della Pontina" o "accesso diretto dalla SS148 Pontina". **NON VERIFICABILE**.
13. "Pontina a scorrimento veloce fino a Terracina" o "superstrada Roma–Terracina". **IMPRECISO**: le carreggiate separate arrivano solo fino a Borgo Piave.
14. "Prossimo / imminente completamento dell'autostrada Roma–Latina" o qualunque data di apertura. **NON VERIFICABILE**.
15. Una data di apertura della Cisterna–Valmontone (ad esempio "dal 2028"). **NON VERIFICABILE**.
16. "Fiumicino, il principale aeroporto italiano" senza "per passeggeri". **IMPRECISO**: per le merci il primo è Malpensa.
17. "Il MOF di Fondi è il più grande mercato ortofrutticolo d'Europa" o "uno dei più grandi d'Europa" come fatto. **NON VERIFICATO**: usare i dati MOF attribuiti.
18. "Latina è la prima provincia/regione per produzione di kiwi" con percentuali. **NON VERIFICATO** su ISTAT o CSO.
19. "Costi per mq fino al 40% inferiori a Roma", "congestione stradale assente", "accesso TIR libero 24/7", "Roma in 60 minuti". **NON VERIFICABILI**.
20. "Area ex Cassa del Mezzogiorno con agevolazioni". **FALSO**: oggi la Cassa non dà benefici; è solo un fatto storico.
21. "Latina Scalo è un interporto" o "polo intermodale operativo". **FALSO**.
22. "Porto di Gaeta, porto container" o "scalo del Tirreno meridionale gestito dall'AdSP di Napoli". **FALSO**: Gaeta movimenta soprattutto rinfuse e dipende dall'AdSP del Mar Tirreno Centro-Settentrionale.
23. Dati sulla IV gamma pontina in ettari o tonnellate (es. "2.300 ha di serre"). **NON AGGIORNATI**: il dato è del 2002.
24. "Il nostro sito è all'interno dell'agglomerato ASI di Latina Scalo". **NON VERIFICATO** sulle tavole del Piano regolatore consortile.
