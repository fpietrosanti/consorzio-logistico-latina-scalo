# mt (maltese) – decisioni di riconciliazione multi-LLM

Data: 2026-11-08. Revisori: A, B (Claude), ChatGPT, Qwen, DeepSeek (tutti e 5 disponibili).
Regola: si applica solo una correzione proposta da ≥2 revisori indipendenti (stesso punto, correzione compatibile) oppure un errore oggettivo singolo verificabile. Nessuna nuova affermazione fattuale.

Nota sull'affidabilità: la revisione Qwen del maltese contiene errori evidenti (sostiene che "ħżin" significhi "brutto" — è "ħażin"; corregge "19,000 metru kwadru" in "metri kwadri", mentre con i numerali da 11 in su il maltese usa il singolare; corregge "mmaniġġjat" dopo vocale). È stata conteggiata solo dove concorda con altri revisori su correzioni plausibili.

## Applicate (11 sostituzioni, 10 correzioni distinte)

| # | Dove | Prima | Dopo | Revisori | Motivo |
|---|---|---|---|---|---|
| 1 | description | `pol b'19,000 metru kwadru koperti` | `ċentru b'19,000 metru kwadru ta' spazju kopert` | "pol"→"ċentru": A, B, ChatGPT (Qwen: "kumpless"); "ta' spazju kopert": A, ChatGPT | "pol" è un calco dell'italiano; "koperti" al plurale non concorda col singolare dopo il numerale |
| 2 | description | `Il-pol jinsab` | `Iċ-ċentru jinsab` | A, B, ChatGPT | come sopra |
| 3 | description | `tal-komuni fin-nofsinhar` | `tal-muniċipalitajiet fin-nofsinhar` | B, ChatGPT, Qwen | "komuni" è un italianismo |
| 4 | description | `b'interlokutur wieħed għall-klijent` | `b'punt ta' kuntatt wieħed għall-klijent` | A, Qwen (identica); B e ChatGPT segnalano lo stesso italianismo | calco di "interlocutore unico" |
| 5 | Post 1 | `il-portijiet tat-Tirren` | `il-portijiet tal-Baħar Tirren` | ChatGPT, Qwen (identica); B propone "Tirreniku" | il nome del mare richiede "Baħar"; coerente con "Baħar Tirren" del Post 4 |
| 6 | Post 2 | `minflok jirċievu` | `minflok ma jirċievu` | DeepSeek (singolo, oggettivo) | davanti a un verbo coniugato la congiunzione è "minflok ma" |
| 7 | Post 3 (×2) | `Kiwi Latina IGP` | `Kiwi Latina IĠP` | A, B | acronimo maltese ufficiale UE (Indikazzjoni Ġeografika Protetta). La denominazione "Kiwi Latina" resta invariata (ChatGPT proponeva "Kiwi di Latina": respinto, non è il nome registrato) |
| 8 | Post 3 | `f'muniċipji tal-provinċji` | `f'muniċipalitajiet tal-provinċji` | ChatGPT, Qwen | coerente con la description corretta |
| 9 | Post 4 | `jagħmlu parti mis-sistema tal-Awtorità tas-Sistema Portwali` | `jagħmlu parti mill-Awtorità tas-Sistema Portwali` | A, B (identica) | ripetizione di "sistema" |
| 10 | Post 4 | `agroalimentari friġġerati` | `agroalimentari refriġerati` | A, Qwen | "friġġerati" non è standard |

## Respinte

| Proposta | Revisori | Motivo |
|---|---|---|
| `baji` (P2, P3) → `bajjiet` / `bajs` / `baġi` | ChatGPT, DeepSeek, Qwen | tutti e tre segnalano la forma, ma con tre correzioni diverse: **da far decidere a un madrelingua** |
| `distribuzzjoni fuq skala kbira` → `bejgħ bl-imnut…` / `distribuzzjoni bl-ingrossa…` | B, ChatGPT | correzioni di senso opposto (dettaglio vs ingrosso). La GDO è grande distribuzione al dettaglio: B ha ragione nel merito, ma è singolo; da far decidere |
| `man-nofsinhar tar-reġjun Pontino` → `tal-Agro Pontino` / `taż-żona Pontina` | A, ChatGPT | correzioni diverse (entrambi rilevano che "Pontino" non è una regione): da far decidere |
| `tal-kwadrant tan-nofsinhar tal-belt kapitali` | A, ChatGPT | correzioni diverse |
| `ħżin` ↔ `ħażna` (uniformazione) | A (tutto "ħżin"), B e Qwen (tutto "ħażna") | posizioni opposte |
| `jaħdem bit-traffiku ro-ro…` → `jittratta…` / `jimmaniġġja…` | A, B | verbi diversi; applicato solo "refriġerati" |
| eliminare `l-awtostradi tal-baħar` (P4) | A | rilievo fattuale (non in content/it) di un solo revisore, B lo considera coerente; **segnalato per verifica** |
| `Għan-negozjanti` → `Għall-negozjanti` | DeepSeek | errato: "n" è lettera solare, l'assimilazione è corretta |
| `l-SS156` → `s-SS156` | DeepSeek | singolo; nel testo convivono "is-SS148" e "It-triq SS148": da uniformare con un madrelingua |
| `fi Via della Dinamica` → `f'Via` | A | singolo; entrambe le forme sono accettabili |
| `spazju miksi` → `kopert`, `kkombinata` → `komplessiva`, `muniċipji` → `komuni`, `awtomotiv`, `Gaeta` maschile | A | singoli / bassa confidenza |
| `Baħar Tirreniku`, `merkanzija voluminuża`, `maħażen modulari`, `sebat ijiem`, `mir-reġjun`, `jikkonsolidaw`, `ġestiet` | B | singoli / bassa confidenza |
| `esperjenza magħquda`, `tħejjija`, `jvarjaw`, `mgħammra…`, `manuvrar`, `postijiet għall-palits`, `mkessħa`, `kreditu fiskali`, `l-industrija agroalimentari` | ChatGPT | singoli / stilistici |
| `metri kwadri`, `immaniġġjat`, `fi Latina`, `maniġġar`, `pallets`, `ħxejjex`, `Semplifikata`, `muniċipalità`, ecc. | Qwen | singoli ed errati |

## Stato dei post

Nessun post ha ricevuto il verdetto "da riscrivere" (A e B: pubblicabile / pubblicabile con correzioni). Le righe MT-P1…MT-P4 di `marketing/linkedin-calendar.csv` passano da `review` a `pending`. Restano aperti per un madrelingua: plurale di "baji", "distribuzzjoni fuq skala kbira", "reġjun Pontino".
