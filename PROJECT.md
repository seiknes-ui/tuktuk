# Tuktuk

_Opprettet: 2026-11-18_

## Formål

Et kort, absurd-komisk spill: To norske kjøreskolelærere vinner stort i Lotto og bestemmer seg for å starte en tuk-tuk-kjøreskole i Thailand. Etter en kort intro følger en tilnærmet uendelig kjøretur i sanntid. Den skal være langsom og kjedelig med vilje, med humoren i det monotone, slik som i *Desert Bus*-sjangeren.

## Konsept

### 1. Intro (ca. 1–3 min)

- Lottotrekningen: de to lærerne ser tallene komme opp ett for ett.
- Beslutningen: «Vi drar til Thailand og starter kjøreskole. Med tuk-tuk.»
- Ankomst: kjøreskolen åpner, og den første eleven setter seg i tuk-tuken.
- Stil: korte scener eller still-bilder med tekst, som spilleren kan klikke seg gjennom.

### 2. Hovedspill: den evige kjøreturen

- Spilleren kjører tuk-tuken på en lang, rett vei, for eksempel fra én by til en annen.
- Tuk-tuken trekker litt til siden hele tiden, så spilleren må korrigere styringen uten pause.
- Kan ikke pauses. Kjører spilleren av veien, slepes tuk-tuken tilbake til start i sanntid, eller turen starter på nytt.
- Én fullført tur gir **1 poeng**. Så går turen tilbake.
- Den andre læreren sitter på og kommer med sporadiske, repeterende kommentarer («Husk speilet.», «Blinklys!»).

### Tone og humor

- Tørr, norsk humor møter thailandsk setting.
- Komikken kommer fra kontrasten: millionærer som frivillig gjør verdens kjedeligste jobb.
- Små, sjeldne hendelser som belønner tålmodighet, for eksempel en insekt-splat på frontruta, en elefant langt borte eller en 7-Eleven som passerer.

## Mål

- [ ] Spillbar prototype av kjøreturen (styring, avdrift, avkjøring, poeng)
- [ ] Intro-sekvens med lottovinsten og ankomsten til Thailand
- [ ] Lærer-kommentarer og sjeldne hendelser underveis
- [ ] Ferdig, publiserbar versjon

## Omfang

**Med:**

- Én vei, én tuk-tuk, to lærere
- Kort intro og én endeløs kjøremodus
- Enkel grafikk og lyd (motordur, radio, kommentarer)

**Ikke med (foreløpig):**

- Åpen verden, flere ruter eller kjøretøy
- Flerspiller
- Avansert fysikk

## Oppgaver

| # | Oppgave | Ansvarlig | Status | Frist |
|---|---------|-----------|--------|-------|
| 1 | Velge plattform/teknologi | | Ferdig (HTML) | |
| 2 | Prototype: vei, styring og avdrift | | Prototype | |
| 3 | Avkjøring og krasj/omstart | | Prototype | |
| 4 | Karakter og tur/retur-logikk | | Prototype | |
| 5 | Intro: manus og scener | | Prototype | |
| 6 | Karakterer: navn, utseende og replikker | | Prototype | |
| 7 | Sjeldne hendelser og lærer-kommentarer | | Prototype | |
| 8 | Lyd: motor, radio, stemmer | | Påbegynt (motor + tut) | |
| 9 | Testing på telefon og publisering | | Publisert, må testes | |

## Milepæler

| Milepæl | Dato | Status |
|---------|------|--------|
| Spillbar kjøreprototype | | |
| Intro ferdig | | |
| Første komplette versjon | | |
| Lansering | | |

## Beslutninger

- 2026-11-18: Konsept valgt: kort intro, deretter en evig kjøretur i *Desert Bus*-sjangeren.
- 2026-11-18: Plattform er HTML (én fil, `index.html`, canvas 320×200), uten rammeverk.
- 2026-11-18: Grafikkstil er retro. Introen er 2D-scener i 90-talls adventure-stil, og kjøringen er pseudo-3D med thailandske gater.
- 2026-11-18: Spilleren er læreren Arve, som instruerer eleven Somchai. Somchai reagerer sent og blir nervøs av mas.
- 2026-11-18: Én tur varer ca. 3 minutter. Etterpå kjører man tilbake, i en uendelig løkke.
- 2026-11-18: Spillet lages for mobil i stående format, med spillskjerm øverst og knapper under. Det publiseres som en privat claude.ai-lenke.
- 2026-11-18: Lærerne heter Arve og André og bor i Sauda. De oppdager de sju rette på telefonen under et kaffeselskap ved et lavt, rundt bord, seks personer i alt. Kaffeselskapet er i verkstedhallen på Sauda VGS, der hvite lastebiler med skrift står parkert. Eleven Somchai har fortsatt et plassholdernavn.

## Åpne spørsmål

- Personlighetene til Arve og André, og hvem de fire vennene rundt bordet er.
- Vanskelighetsgrad: hvor mye skal Somchai vingle, og hvor raskt skal nervene stige?
- Skal det finnes en slutt, eller er turen bokstavelig talt evig?

## Notater

- Spillbar versjon (privat lenke): https://claude.ai/artifact/551u9TpZk1yft88iVdx3qT
- Kildefil: `index.html`. Publiser på nytt fra samme fil for å beholde lenken.

- Grafikk: originalene ligger i `grafikk/`. Ferdige spillfiler (uten rosa bakgrunn, nedskalert og delt opp) ligger i `grafikk/spill/` og lages med `python verktoy/klargjor_grafikk.py grafikk` (krever Pillow, NumPy og SciPy). Spillet bruker selvtegnet reservegrafikk for det som mangler.
