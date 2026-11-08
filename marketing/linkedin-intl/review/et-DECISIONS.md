# et (estone) – decisioni di riconciliazione multi-LLM

Data: 2026-11-08. Revisori: A, B (Claude), ChatGPT, Qwen, DeepSeek (tutti e 5 disponibili).
Regola: si applica solo una correzione proposta da ≥2 revisori indipendenti (stesso punto, correzione compatibile) oppure un errore oggettivo singolo verificabile. Nessuna nuova affermazione fattuale.

## Applicate (12 correzioni)

| # | Dove | Prima | Dopo | Revisori | Motivo |
|---|---|---|---|---|---|
| 1 | description | `haldab Via della Dinamical Tor Tre Ponti piirkonnas keskust` | `haldab aadressil Via della Dinamica, Tor Tre Ponti piirkonnas, keskust` | tutti e 5 segnalano l'adessivo "-l" sul nome di via; DeepSeek e Qwen: "Via della Dinamica, Tor Tre Ponti"; A aggiunge "aadressil" | nome di via straniero non declinato; "aadressil" come nel Post 1 |
| 2 | description | `katusealust pinda` | `kaetud pinda` | A, B, Qwen (ChatGPT: "kaetud laopinda") | coerente con il Post 1 |
| 3 | description | `Rooma ja Pontina lõunaosaga` | `Rooma ja Pontina piirkonna lõunaosaga` | ChatGPT, Qwen (identica); A segnala lo stesso punto | evita la confusione con la strada SS148 Pontina citata subito prima |
| 4 | description | `Teenindatavad sektorid: Põllumajandus-` | `…: põllumajandus-` | A, B, ChatGPT, DeepSeek | minuscola dopo i due punti |
| 5 | Post 1 | `vahelisel Türreeni koridoril` | `vahelises Türreeni mere äärses koridoris` | ChatGPT, Qwen ("Türreeni mere äärses …koridoris"); A: serve l'inessivo | "Türreeni" da solo non identifica il corridoio; caso corretto |
| 6 | Post 2 | `kolmanda osapoole logistikat (3PL) ühe kontaktisikuga kliendi jaoks.` | `kolmanda osapoole logistikat (3PL), kusjuures kliendil on üks kontaktisik.` | A, ChatGPT ("…kliendil on üks kontaktisik"); Qwen segnala lo stesso punto | costruzione ambigua |
| 7 | Post 2 | `viimase miili jaotust` | `viimase miili tarneid` | B, ChatGPT, Qwen (identica) | termine d'uso |
| 8 | Post 2 | `käsitletakse kohapeal` | `hallatakse kohapeal` | A (alta), Qwen (identica), ChatGPT | "käsitlema" = trattare un argomento, non gestire |
| 9 | Post 2 | `…, mis sobib ettevõtetele, kes alles kasvatavad oma müüki Itaalias.` | (frase tolta) | A, B | affermazione commerciale non presente nella fonte italiana; si toglie, non si aggiunge nulla (la proposta di A di inserire le "condizioni minime contrattuali" non è applicata) |
| 10 | Post 3 | `WMS-süsteemis` | `laohaldussüsteemis (WMS)` | A, B, ChatGPT, Qwen | pleonasmo "WMS-system" |
| 11 | Post 4 | `umbes 280 hektariga,` | `umbes 280 hektari ulatuses,` | DeepSeek, ChatGPT ("280 hektari ulatuses") | costruzione più naturale; il dato resta invariato |
| 12 | Post 4 | `sõltub investeeringu katastriüksusest` | `sõltub investeeringu asukoha katastriüksusest` | ChatGPT, Qwen (identica) | la particella catastale è quella del luogo dell'investimento |

## Respinte

| Proposta | Revisori | Motivo |
|---|---|---|
| `sinna asuvatele` → `seal asuvatele` | DeepSeek, Qwen | due revisori concordi, ma la correzione cambia il senso: "sinna asuma" (illativo) = insediarsi, cioè le aziende che vi si trasferiscono, come nella fonte; "seal asuvatele" significherebbe "che si trovano lì". A e ChatGPT propongono altre riscritture ("tegevust rajavatele" / "tegevust üle viivatele"). Lasciato com'è; **da confermare con un madrelingua** |
| `Lisaks on kasutada` → `olemas` / `saadaval` | B, ChatGPT | correzioni diverse; "on kasutada" è accettabile |
| `lisaks B2B-tarnetele kogu Itaalias` → `ning teeb…` / `ning teostab…` | ChatGPT, Qwen | verbi diversi |
| `Konsortsium töötab lepingulise logistika alusel` | A, ChatGPT | riscritture diverse |
| `kaubaaluste moodustamist` | A, ChatGPT | riscritture diverse |
| `tootmisseadmetesse` → `põhivarasse` / `tootmisvarasse` | A, ChatGPT | termini diversi |
| struttura con dativo del Post 1 (`Eesti tootjatele … asub keskus`) | A, B | riscritture diverse |
| `välipinda` → `välisplatse` / `väliala pinda` | A, Qwen | correzioni diverse |
| `tellijale üks kontaktisik` (description) | ChatGPT, Qwen | correzioni diverse |
| `Kulud on muutuvad` → `muutlikud` / `Kulud sõltuvad` | DeepSeek, ChatGPT | "muutuvad kulud" è il termine contabile corretto (costi variabili) |
| `kelle` → `mille` (aziende), `(Latina provintsis)`, `Pomeziani/Apriliani`, `sadamaalasid`, togliere "umbes" da 280 ha, `Lazio ZLS –` | A | singoli / bassa confidenza (togliere "umbes" è un intervento fattuale: segnalato) |
| `Türreeni mere ranniku koridoril`, `sobib keskuse asukoht`, `olemas`, tagline "Kolmanda osapoole…" | B | singoli |
| `Ladustamisteenus`, `väliplatse`, `EUR-i linnaosani`, `A1-kiirteele`, `teenusepakkujale`, `koos koguse…`, `kaupade alustele paigutamist`, `reguleeritava temperatuuriga`, `ladustamisperioodi`, `sealhulgas 15`, `ettevõtlusteenuste kontaktpunkti`, `regionaalabi tingimustele`, ecc. | ChatGPT | singoli / stilistici |
| `(LT)` → `(IT)` | Qwen | errato: LT è la sigla della provincia di Latina |
| `kaubakäitlemine`, `suurkaubandus`, `välisplatsi pinda`, `kaubaaluste kohad`, `haldusmenetlusi`, `Eesti ettevõtted, kes müüvad…`, `mistõttu see sobib`, `hõlmates…` | Qwen | singoli / errati ("kaubaalusekoht" è un composto corretto) |
| `investeeringuobjekti` | DeepSeek | singolo; applicata la variante concorde (#12) |

## Stato dei post

Nessun post ha ricevuto il verdetto "da riscrivere" (A e B: pubblicabile / pubblicabile con correzioni). Le righe ET-P1…ET-P4 di `marketing/linkedin-calendar.csv` passano da `review` a `pending`.
