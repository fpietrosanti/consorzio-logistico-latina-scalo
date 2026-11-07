# Brief di traduzione (tutte le lingue)

Sito: consorziologistico.it (Hugo multilingua). Sorgente: italiano. Destinazione: content/<lang>/, i18n/<lang>.toml,
data/profiles/<lang>.json. Elenco lingue, nomi e slug di sezione: tools/langs.json.

## Regole di stile
- Registro professionale B2B della stampa specializzata di logistica nella lingua di arrivo. Niente toni pubblicitari,
  niente emoji, niente punti esclamativi, niente superlativi aggiunti. Non aggiungere né togliere fatti.
- Forma di cortesia della lingua di arrivo dove serve (Sie, vous, usted, Pan/Pani, ecc.); in generale costrutti impersonali.
- Terminologia di settore corretta (es. EN: third-party logistics, pallet space, loading bays, cross-docking, last mile;
  DE: Kontraktlogistik, Palettenstellplatz, Laderampen, Lagerung; FR: logistique pour compte d'autrui, emplacement palette,
  quais de chargement; ES: logística para terceros, ubicación de palé, muelles de carga; ecc.).
- Toponimi italiani invariati (Latina Scalo, Aprilia, Castelli Romani, Agro Pontino, SS148 Pontina, Via della Dinamica).
  Per Roma/Rome, Napoli/Naples usare l'esonimo della lingua di arrivo. Sigle italiane (ZLS, DDT, CMR, ASI, MOF, ANAS, RFI,
  ISTAT) invariate, spiegate alla prima occorrenza se il testo italiano non lo fa già.
- Numeri e unità nel formato locale della lingua di arrivo (separatore decimale e delle migliaia); m², km, °C invariati.
- Cinese (zh): cinese semplificato, registro commerciale formale; toponimi italiani in caratteri latini, con resa cinese
  alla prima occorrenza solo per Roma (罗马), Napoli (那不勒斯), Italia (意大利), Lazio (拉齐奥大区).
- Mai nominare "Transitalia".

## Regole tecniche
1. Stesso percorso relativo del file italiano: content/it/servizi/stoccaggio.md -> content/<lang>/servizi/stoccaggio.md.
2. Front matter (YAML): tradurre title, linkTitle, description (max 160 caratteri), imageAlt, summary, faq[].q, faq[].a,
   faq[].group. Lasciare invariati layout, weight, image, date, area, subarea, place, sitemap.
3. url: "/<lang>/<sezione-tradotta>/<slug-tradotto>/" dove <sezione-tradotta> è il valore in tools/langs.json -> <lang> -> sec
   (servizi, settori, logistica, approfondimenti; per posizione.md usare sec.posizione, per domande-frequenti.md sec.faq).
   Lo slug è il titolo breve tradotto, minuscolo, ASCII, parole separate da trattini (traslitterare greco, bulgaro;
   per il cinese usare uno slug inglese). Per i file _index.md: url "/<lang>/<sezione-tradotta>/".
   Per content/it/_index.md (home) non mettere url. Esempi: /en/services/storage/, /de/leistungen/lagerung/,
   /de/logistik/pianura-pontina/ (i nomi di luogo restano come nello slug italiano).
4. Corpo Markdown: tradurre tutto il testo. I riferimenti interni {{< relref "/percorso" >}} vanno lasciati IDENTICI
   (sono percorsi di contenuto, non URL; Hugo li risolve nella lingua giusta). Tradurre solo il testo del link.
   Lasciare invariati iframe e HTML. Nelle sezioni "Fonti" tradurre l'intestazione e le parti descrittive, lasciare
   titoli dei documenti, enti e URL in lingua originale.
5. Glossario (approfondimenti/glossario-logistica.md): voce principale in italiano, seguita dall'equivalente nella lingua
   di arrivo tra parentesi; definizione tradotta; ordine alfabetico italiano invariato.
6. i18n/<lang>.toml: tradurre i valori di i18n/it.toml; chiavi identiche; segnaposto {{ .Name }}, {{ .Km }} ecc.
   identici; TOML valido (virgolette doppie, escape corretti). Le stringhe place_* sono template: devono restare frasi
   grammaticali con i segnaposto (in lingue con casi, scegliere costruzioni che non richiedono di declinare il nome del
   luogo, es. "per le imprese di {{ .Name }}" -> DE "für Unternehmen aus {{ .Name }}", PL "dla firm z miejscowości {{ .Name }}").
7. data/profiles/<lang>.json: stesse chiavi di data/profiles/it.json; tradurre solo "profile"; copiare "sectors" e
   "sources" invariati. JSON valido UTF-8.
8. Non toccare mai i file content/<lang>/logistica/<comune>.md con layout "place" né content/<lang>/crediti.md:
   sono generati da tools/gen_places.py.
9. Ripresa: se un file di destinazione esiste già ed è completo, saltarlo. Scrivere un file alla volta.
10. Validare alla fine: python -c "import tomllib;tomllib.load(open('i18n/<lang>.toml','rb'))" e json.load per i profili
    (interprete: C:/Users/admin/AppData/Local/Python/bin/python.exe, con PYTHONUTF8=1).
