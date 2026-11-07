# Directory e piattaforme: Italia, pan-Europa, logistica

Verifica del 2026-11-07 (WebFetch/WebSearch, sola lettura). Dati completi in `italia-paneuropa-logistica.csv` (74 voci). Dove manca un dato verificato la voce riporta "non verificato".

## Top 15 priorità

| # | Piattaforma | Perché |
|---|---|---|
| 1 | Google Business Profile | Ricerche locali Latina/Roma Sud, Maps, risposte AI. È la base anche per Bing. |
| 2 | Bing Places | Import diretto da GBP. Alimenta Copilot e le ricerche AI basate su Bing. |
| 3 | Apple Business (ex Business Connect) | Apple Maps/Siri. Il portale ora si chiama business.apple.com. |
| 4 | Europages | Directory B2B europea in 26 lingue, con profilo base gratuito: utile per gli shipper esteri. |
| 5 | TIMOCOM (Borsa magazzini) | Permette di pubblicare offerte di spazio magazzino in tutta Europa, senza costi aggiuntivi rispetto all'abbonamento Marketplace. |
| 6 | Assologistica | È l'associazione dei magazzini conto terzi, con directory "Ricerca aziende" e un forte segnale di credibilità. |
| 7 | LinkedIn Company Page | Raggiunge i logistics manager e viene citata spesso dalle AI. |
| 8 | PagineGialle (+PagineBianche/Tuttocittà) | Una sola scheda Italiaonline, gratuita con P.IVA. |
| 9 | Kompass | Directory B2B con categorie "magazzini generali". Il sito blocca il fetch automatico. |
| 10 | Racklify | Directory 3PL/magazzini con pagine Italia. Claim gratuito e richieste di preventivo (RFP) incluse. |
| 11 | ALIS | Associazione logistica e intermodale, forte nel Centro-Sud. La domanda si fa online. |
| 12 | MePA + STELLA Lazio | Lead dalla PA (ASL, Comuni, Regione) per magazzinaggio e trasporti. Richiede firma digitale. |
| 13 | Trans.eu | Borsa carichi con account gratuito, per vendere il servizio trasporti. Non ha una borsa magazzini. |
| 14 | OpenStreetMap | Dati ripresi da molte app e modelli AI. Basta un nodo con sito web e telefono. |
| 15 | CargoLinked / Enterprise League | Listing gratuiti (Enterprise League "free forever", claim con email sul dominio aziendale) e backlink a basso sforzo. |

## Esclusi o da ridimensionare

- **Waredock** non è un marketplace: è un 3PL con rete propria nel Nord Europa, senza presenza in Italia.
- **Stowga** risulta dismesso (il dominio non risolve).
- **Log-hub** oggi fa solo software, non ha un marketplace.
- **wlw** accetta aziende con sede fuori dalla Germania solo tramite il Customer Care.
- **Kompass, Cylex, Infobel, Ufficiocamerale** hanno risposto 403 al fetch automatico. Vanno verificati a mano.

## Automazione

- **Alta fattibilità:** Hotfrog, Opendi, MisterImprese, Reteimprese, Cargopedia, CargoLinked, Enterprise League, Brownbook, alert TED.
- **Bassa fattibilità:** Google, Apple, borse trasporto (verifica aziendale), associazioni, MePA/STELLA (firma digitale). Richiedono intervento umano.
