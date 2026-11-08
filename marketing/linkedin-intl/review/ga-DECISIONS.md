# ga (irlandese) – decisioni di riconciliazione multi-LLM

Data: 2026-11-08. Revisori: A, B (Claude), ChatGPT, Qwen, DeepSeek (tutti e 5 disponibili).
Regola: si applica solo una correzione proposta da ≥2 revisori indipendenti (stesso punto, correzione compatibile) oppure un errore oggettivo singolo (ortografia/grammatica) verificabile. Nessuna nuova affermazione fattuale.

## Applicate (22 sostituzioni, 13 correzioni distinte)

| # | Dove | Prima | Dopo | Revisori | Motivo |
|---|---|---|---|---|---|
| 1 | tagline, description, P1 (×2), P2, P4 (×3) | `in Latina…` | `i Latina…` | A, B, DeepSeek | "in" solo davanti a vocale; davanti a L si usa "i" (la L non prende urú). "In 2025" invariato |
| 2 | P2 (×2), P3 | `pioc` (`an pioc orduithe`, `pioc, pacáil`, `stóráil, pioc agus`) | `piocadh` | A, B, ChatGPT, Qwen | serve il sostantivo verbale, coerente con "piocadh orduithe" della description |
| 3 | description, P2 | `raicíní` / `raicní` | `racaí` | A, B, ChatGPT | plurale standard di "raca" (focloir.ie); DeepSeek proponeva "raicní", Qwen "raic": minoritari |
| 4 | description | `i stórasú` | `i stóráil` | A, B, ChatGPT, Qwen, DeepSeek | forma non standard, unanime |
| 5 | description | `i gceantair dheisceart na príomhchathrach` | `i gceantair i ndeisceart na príomhchathrach` | ChatGPT, DeepSeek (A, Qwen segnalano lo stesso errore) | stessa correzione proposta da due revisori |
| 6 | description | `de chlóis amuigh` | `de chlóis oscailte` | A, Qwen | coerente con Post 1 |
| 7 | description | `Oibríonn Consorzio Logistico Latina Scalo láthair ar…` | `Tá láthair ag Consorzio Logistico Latina Scalo ar…` | ChatGPT, Qwen | stessa costruzione "Tá … ag", come nel Post 1 |
| 8 | P1 | `Tá Róimh EUR` | `Tá EUR na Róimhe` | A, ChatGPT, Qwen | "an Róimh" richiede l'articolo/genitivo |
| 9 | P1 | `aerfort na Róimhe Fiumicino` | `aerfort Fiumicino na Róimhe` | A, B, ChatGPT | ordine naturale |
| 10 | P1 | `bíonn an láthair ag obair 24 uair an chloig, 7 lá` | `bíonn an láthair ag feidhmiú 24 uair an chloig sa lá, 7 lá` | A, ChatGPT | formulazione compatibile proposta da due revisori |
| 11 | P2 | `nóta seachadta na hIodáile (DDT)` | `nóta seachadta Iodálach (DDT)` | A, DeepSeek | "la bolla italiana", non "dell'Italia" |
| 12 | P3 | `de réir anailís Chumann` | `de réir anailíse Chumann` | A, B, DeepSeek | "de réir" regge il genitivo (anailís → anailíse) |
| 13 | P4 | `an Chriosa Lóistíochta` | `an Chreasa Lóistíochta` | A (singolo, oggettivo) | genitivo di "crios" = "creasa" (errore morfologico verificabile); la parte "Shimplithe" proposta da A non è applicata (incerta) |

## Respinte

| Proposta | Revisori | Motivo |
|---|---|---|
| `cabhlach` → `flít` (P2, P3) | A, B | Qwen sostiene l'opposto (`flít` → `cabhlach`); disaccordo, lasciato com'è |
| `dáileachán míle deiridh` → 3 varianti diverse | A, DeepSeek, Qwen | errore segnalato da 3, ma correzioni incompatibili ("an mhíle dheiridh" / "dáileadh" / "seachadadh"): da far decidere a un madrelingua |
| `Thoirréineach` → `Thioréanach` / `Thirrénach` | B, Qwen | correzioni divergenti, nessuna verificabile |
| `idir phacáistiú, chomhpháirteanna…` (P3) | ChatGPT (nota, 85%), Qwen | correzioni diverse ("amhail…" / "…san áireamh"); da rivedere |
| `Is cuibhreannas é de chúig chomhlacht` | A, DeepSeek | correzioni diverse (aggiungere il soggetto / spostare "é") |
| `8 km ó lár bhaile Latina` | A, Qwen | correzioni diverse |
| `In 2025` → `I 2025` | DeepSeek | singolo; B lo considera corretto |
| `costais athraitheach` → `athraitheacha` | DeepSeek | l'aggettivo predicativo non si accorda al plurale: proposta errata |
| `aon seirbhísí breise` → `aon seirbhís bhreise` | DeepSeek | singolo, l'originale è accettabile |
| `bhí Latina ar an dara cúige` → `ba é Latina an dara cúige` | DeepSeek | singolo, stile |
| `Cumann Tráchtála` → `Seomra Tráchtála` | B | singolo; "cumann tráchtála" è il termine in uso per "camera di commercio" |
| `gar dá chéile` → `gar don láthair` (P3) | A | singolo, di significato (non ortografico): **da verificare da un madrelingua** |
| `Tugtar sonraí … ar iarratas` (P3) | B | rilievo fattuale, non linguistico; nessuna nuova affermazione aggiunta; segnalato per controllo |
| tutte le correzioni degli URL (`/ga/suíomh/` ecc.) | Qwen | gli slug sono URL reali del sito, ASCII per scelta |
| `láthair` → `láithreán`, `raic`, `airde shoiléir`, `cógais`, `acmhainn`, `Sonraíonn`, `Phontine`, `ó Chisterna`, `an mótarbhealach`, `i stóráil` (P1), virgole dopo "In 2025" | Qwen | singoli, non verificabili o errati |
| `Tugann … le chéile` (description), `airde ghlan … tá`, `faoi chúram oibreora`, `doiciméad iompair na hIodáile (DDT)`, `iarrthóir`, tagline "mar sheirbhísí" | ChatGPT | singoli / stilistici |
| tagline `do thríú páirtithe`, `ó dheas ón Róimh`, `is cúis le`, `duganna lódála agus díluchtaithe`, `inathraithe` | A | singoli / stilistici / bassa confidenza |
| `Napla`, `iompar bóthair`, `chomhtháthú`, `ag breathnú ar`, `Bia agus talmhaíocht` | B | singoli / stilistici |

## Stato dei post

Nessun post ha ricevuto il verdetto "da riscrivere" (A e B: tutti "pubblicabile con correzioni"; i revisori esterni non hanno dato verdetti di riscrittura). Le righe GA-P1…GA-P4 di `marketing/linkedin-calendar.csv` passano da `review` a `pending`.
