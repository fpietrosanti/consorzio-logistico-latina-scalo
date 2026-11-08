# lv (lettone) – decisioni di riconciliazione multi-LLM

Data: 2026-11-08. Revisori: A, B (Claude), ChatGPT, Qwen, DeepSeek (tutti e 5 disponibili).
Regola: si applica solo una correzione proposta da ≥2 revisori indipendenti (stesso punto, correzione compatibile) oppure un errore oggettivo singolo verificabile. Nessuna nuova affermazione fattuale.

## Applicate (16 correzioni)

| # | Dove | Prima | Dopo | Revisori | Motivo |
|---|---|---|---|---|---|
| 1 | description | `slēgtām` (platībām) | `segtām` | A, B, ChatGPT | "slēgts" = chiuso; per le superfici coperte si usa "segts", come nei post |
| 2 | description | `Roma–Formia–Neapole` | `Roma–Formija–Neapole` | A, ChatGPT, DeepSeek, Qwen | trascrizione lettone, coerente con il Post 1 |
| 3 | description | `34 km no Aprilia` | `34 km no Aprilijas` | A, DeepSeek | toponimo declinato come in "līdz Aprilijai" (Post 4) |
| 4 | description | `Pontīnas dienvidu daļu` | `Pontīnas līdzenuma dienvidu daļu` | A, ChatGPT (identica) | riferimento geografico (pianura Pontina), evita confusione con la SS148 Pontina |
| 5 | description | `Apkalpotās nozares: Lauksaimniecības…` | `…: lauksaimniecības…` | A, B, DeepSeek, Qwen | minuscola dopo i due punti |
| 6 | description | `lielā mazumtirdzniecība` | `lielie mazumtirdzniecības tīkli` | A, ChatGPT (identica) | forma d'uso per la GDO |
| 7 | Post 1 | `Via della Dinamica, Tor Tre Ponti rajonā` | `Via della Dinamica ielā, Tor Tre Ponti rajonā` | A, B | il nome di via straniero indeclinabile richiede "ielā" |
| 8 | Post 1 | `Modulārās noliktavas ir no 500 līdz 3000 kvadrātmetriem lielas,` | `Modulāro noliktavu platība ir no 500 līdz 3000 kvadrātmetriem,` | A, ChatGPT (identica) | formulazione innaturale |
| 9 | Post 1 | `Tirēnu koridorā` | `Tirēnu jūras piekrastes koridorā` | B, ChatGPT (A: "Tirēnu jūras koridorā") | "Tirēnu" da solo non identifica il corridoio |
| 10 | Post 1 | `ar kopējo pieredzi vairāk nekā piecdesmit gadu garumā` | `ar vairāk nekā piecdesmit gadu kopējo pieredzi` | A, DeepSeek (stesso riordino; ChatGPT segnala lo stesso punto) | innaturale; ora identico alla description |
| 11 | Post 2 | `ar krājumu uz vietas var veikt` | `veidojot krājumus uz vietas, var veikt` | Qwen, ChatGPT ("izveidojot preču krājumus uz vietas") | costruzione con participio, stessa correzione nella sostanza |
| 12 | Post 2 (×2) | `paletu` (`paletu plauktiem`, `paletu vietu`) | `palešu` | ChatGPT (singolo, oggettivo); DeepSeek segnala lo stesso punto | genitivo plurale di "palete" (V declinazione, -te → -šu) è "palešu" |
| 13 | Post 2 | `25 000 kvadrātmetru atklātu laukumu būvmateriāliem` | `25 000 kvadrātmetru atklāts laukums būvmateriāliem` | DeepSeek, ChatGPT (entrambi: serve il nominativo, soggetto di "Pieejamas") | concordanza di caso; applicata la forma minima di DeepSeek |
| 14 | Post 4 | `Rūpniecības konsorcija` | `rūpniecības konsorcija` | A, B | maiuscola a metà di un nome comune |
| 15 | Post 4 | `cross-docking` | `kravu pārkraušanu bez ilgstošas uzglabāšanas (cross-docking)` | ChatGPT, A ("bez uzglabāšanas"), B ("tiešo pārkraušanu") | anglicismo non declinato in un elenco di accusativi; spiegazione lettone + termine inglese, nessun contenuto nuovo |

(La tabella elenca 15 righe; la #12 copre 2 occorrenze: 16 sostituzioni in totale.)

## Respinte

| Proposta | Revisori | Motivo |
|---|---|---|
| prima frase del Post 2 (`kas līdz šim piegādā`, `daļējas un atsevišķas piegādes … iekšienē`) | A (alta), B, ChatGPT | tutti la segnalano ma con riscritture diverse ("piegādājuši" / togliere "līdz šim"; "mazākas un biežākas" / "pa daļām" / "mazāku partiju"): applicata solo la parte concorde (#11). **Da far rileggere a un madrelingua** |
| `termiņš` → `uzglabāšanas ilgums` / `uzglabāšanas termiņš` | A, ChatGPT | sostantivi diversi |
| `noliktavas vadības sistēmā (WMS)` | A, ChatGPT | riscritture diverse |
| `ir pirmais Lacio reģionā` → `lielākais` / `ieņem pirmo vietu` | A, ChatGPT | correzioni diverse |
| `izsniedz uz vietas` → `sagatavo` / `noformē` | A, ChatGPT | correzioni diverse |
| `veic vietējais operators` (Post 3) | B | rilievo di significato di un solo revisore (il servizio è del Consorzio): **segnalato per verifica** |
| `Latinas province` → `provincē`; ristrutturazione dativo Post 1; `autorūpniecība`; `trešajām pusēm`; `ar specializētu autoparku` | A | singoli / bassa confidenza |
| `Frozinoni` → `Frozinone`; toponimi non declinati; `pretielaušanās`; `apsardzes`; `mazākas piegādes pa daļām` | B | singoli; "uz Frozinoni" è accusativo corretto |
| `trešo personu uzdevumā`, `(Latinas province)` nel tagline, `rūpnieciskajā zonā`, `Apkalpojamās`, `pa autoceļu`, `organizēšana Romā`, `tālsatiksmes pārvadājums`, ecc. | ChatGPT | singoli / stilistici |
| `paletes vietu`; `Aprilija` nell'elenco del Post 4 | DeepSeek | singoli; per "paletu" applicata la forma corretta "palešu" |
| `nepieciešamais … skaits` | Qwen | errata: "nepieciešamo" concorda con "paletu vietu" |
| `3 000` con spazio; `Pomēcija`; `Frozīni`; `kopēju`; `(LT)` → `(Latina, Itālija)`; `konsorciju` | Qwen | singoli / non verificabili |

## Stato dei post

Nessun post ha ricevuto il verdetto "da riscrivere" (A: tutti "pubblicabile con correzioni", con la nota di riscrivere la prima frase del Post 2; B: pubblicabile / con correzioni). Le righe LV-P1…LV-P4 di `marketing/linkedin-calendar.csv` passano da `review` a `pending`. Resta raccomandata una rilettura madrelingua della prima frase del Post 2.
