# Revisione lv (latviešu) – revisore A

Riferimento: content/it/ e docs/DOTAZIONI.md. I diacritici sono corretti. I problemi riguardano alcune desinenze dopo i numerali, l'incoerenza nei nomi di luogo italiani e la prima frase del Post 2.

## Issue

1. **Post 1** – `pārvalda loģistikas centru Via della Dinamica, Tor Tre Ponti rajonā, Latina Scalo (Latinas province).`
   - Categoria: grammar (il nome della via indeclinabile resta senza marca di caso; "province" è al nominativo in un contesto locativo)
   - Correzione: `pārvalda loģistikas centru Via della Dinamica ielā, Tor Tre Ponti rajonā, Latina Scalo (Latinas provincē).`
   - Confidenza: medium

2. **Post 1** – `Modulārās noliktavas ir no 500 līdz 3000 kvadrātmetriem lielas`
   - Categoria: unnatural phrasing
   - Correzione: `Modulāro noliktavu platība ir no 500 līdz 3000 kvadrātmetriem`
   - Confidenza: low

3. **Post 1** – `Latvijas pārvadātājiem, ekspeditoriem un izplatītājiem, kas apkalpo klientus Itālijas centrālajā un dienvidu daļā, centrs atrodas Tirēnu koridorā starp Romu un Neapoli.`
   - Categoria: unnatural phrasing (il dativo di interesse non regge "centrs atrodas")
   - Correzione: `Latvijas pārvadātājiem, ekspeditoriem un izplatītājiem, kas apkalpo klientus Itālijas centrālajā un dienvidu daļā, ir svarīgi, ka centrs atrodas Tirēnu jūras koridorā starp Romu un Neapoli.`
   - Confidenza: medium

4. **Post 1** – `ar kopējo pieredzi vairāk nekā piecdesmit gadu garumā uzglabāšanā`
   - Categoria: unnatural phrasing
   - Correzione: `ar vairāk nekā piecdesmit gadu kopējo pieredzi uzglabāšanā`
   - Confidenza: medium

5. **Post 2** – `Ražotāji, kas līdz šim piegādā preces Itālijas klientiem tieši no rūpnīcas, ar krājumu uz vietas var veikt daļējas un atsevišķas piegādes Itālijas iekšienē.`
   - Categoria: grammar ("līdz šim" con il presente) + unnatural phrasing ("Itālijas iekšienē", "daļējas un atsevišķas" poco chiaro)
   - Correzione: `Ražotāji, kas līdz šim preces Itālijas klientiem piegādājuši tieši no rūpnīcas, var veikt mazākas un biežākas piegādes Itālijā, ja krājumi atrodas uz vietas.`
   - Confidenza: high

6. **Post 2** – `piedāvā preču uzglabāšanu trešajām personām`
   - Categoria: terminology (in ambito business si usa "trešo pušu" / "pakalpojumu")
   - Correzione: `piedāvā preču uzglabāšanas pakalpojumus trešajām pusēm`
   - Confidenza: low

7. **Post 2** – `Krājumus pārvalda noliktavas vadības sistēmā (WMS).`
   - Categoria: unnatural phrasing
   - Correzione: `Krājumus pārvalda ar noliktavas vadības sistēmu (WMS).`
   - Confidenza: low

8. **Post 2, Post 3, description** – `ar savu autoparku`
   - Categoria: meaning vs fonte (la fonte dice "flotta dedicata", non "propria")
   - Correzione: `ar specializētu autoparku` (oppure va confermato che la flotta è di proprietà)
   - Confidenza: low

9. **Post 2** – `nepieciešamo paletu vietu vai kvadrātmetru skaits, termiņš un papildu pakalpojumi`
   - Categoria: terminology ("termiņš" significa scadenza; qui serve la durata)
   - Correzione: `nepieciešamo paletu vietu vai kvadrātmetru skaits, uzglabāšanas ilgums un papildu pakalpojumi`
   - Confidenza: medium

10. **Post 3, Post 4, description** – `līdz Pomecijai`, `līdz Santa Palombai`, `līdz Castel Romano`, `līdz Aprilijai` vs description `34 km no Aprilia`
    - Categoria: spelling/consistency (adattamento e declinazione dei toponimi incoerenti)
    - Correzione: uniformare. Nella description: `34 km no Aprilijas`. Per Castel Romano si può lasciare la forma originale indeclinata, ma allora va resa esplicita: `līdz Castel Romano rūpniecības zonai`.
    - Confidenza: medium

11. **Post 3** – `Itālijā nepieciešamos transporta dokumentus izsniedz uz vietas`
    - Categoria: terminology
    - Correzione: `Itālijā nepieciešamos transporta dokumentus sagatavo uz vietas`
    - Confidenza: low

12. **Post 4** – `ir pirmais Lacio reģionā pēc apstrādāto intermodālo transporta vienību skaita`
    - Categoria: unnatural phrasing
    - Correzione: `ir lielākais Lacio reģionā pēc apstrādāto intermodālo transporta vienību skaita`
    - Confidenza: medium

13. **Post 4** – `Lacio reģiona Rūpniecības konsorcija industriālās zonas`
    - Categoria: spelling (maiuscola a metà di un nome proprio)
    - Correzione: `Lacio rūpniecības konsorcija (Consorzio Industriale del Lazio) industriālās zonas`
    - Confidenza: low

14. **Post 4** – `kravu apstrādi, cross-docking un autopārvadājumus`
    - Categoria: terminology/grammar (anglicismo non declinato in una serie di accusativi)
    - Correzione: `kravu apstrādi, kravu pārkraušanu bez uzglabāšanas (cross-docking) un autopārvadājumus`
    - Confidenza: low

15. **Tagline** – `Uzglabāšana, kravas apstrāde un pārvadājumi`
    - Categoria: consistency (altrove "kravu apstrāde")
    - Correzione: `Uzglabāšana, kravu apstrāde un pārvadājumi`
    - Confidenza: low

16. **Description** – `ar 19 000 kvadrātmetru slēgtām un 25 000 kvadrātmetru atklātām platībām`
    - Categoria: grammar (dopo un numerale con "kvadrātmetru" serve il genitivo) + terminology ("slēgtas" significa chiuse; il Post 1 usa "segtas", coperte)
    - Correzione: `ar 19 000 kvadrātmetru segtu un 25 000 kvadrātmetru atklātu platību`
    - Confidenza: high

17. **Description** – `uz līnijas Roma–Formia–Neapole`
    - Categoria: spelling/consistency (il Post 1 usa "Formija", che è la trascrizione lettone)
    - Correzione: `uz līnijas Roma–Formija–Neapole`
    - Confidenza: medium

18. **Description** – `savieno objektu ar Romu un Pontīnas dienvidu daļu`
    - Categoria: terminology (riferimento geografico vago)
    - Correzione: `savieno objektu ar Romu un Pontīnas līdzenuma dienvidu daļu`
    - Confidenza: low

19. **Description** – `Apkalpotās nozares: Lauksaimniecības un pārtikas nozare, farmācija, autobūve, … lielā mazumtirdzniecība`
    - Categoria: spelling + terminology (in lettone dopo i due punti si scrive minuscolo; "autorūpniecība" e "lielie mazumtirdzniecības tīkli" sono le forme d'uso)
    - Correzione: `Apkalpotās nozares: lauksaimniecības un pārtikas nozare, farmācija, autorūpniecība, … lielie mazumtirdzniecības tīkli`
    - Confidenza: low

## Verdetto per post

- Post 1: pubblicabile con correzioni
- Post 2: pubblicabile con correzioni (riscrivere la prima frase)
- Post 3: pubblicabile con correzioni
- Post 4: pubblicabile con correzioni
- Tagline: pubblicabile
- Description: pubblicabile con correzioni
