---
kommun: regionhalland
organ: rs
datum: 2021-06-09
lopnr: null
typ: bilaga
namn: bilaga-3-variabelspecifikation
kallnyckel: meetingsplus:/welcome-sv/namnder-styrelser/regionstyrelsen/mote-2021-06-09/agenda/bilaga-3variabelspecifikationpdf-58050
tidigare_kallnycklar: []
arenden: null
kalla_url: https://politik.regionhalland.se/welcome-sv/namnder-styrelser/regionstyrelsen/mote-2021-06-09/agenda/bilaga-3variabelspecifikationpdf-58050?downloadMode=open
sha256: 8a45a4c14e093a2644983f6192c8a6493989baeacb746ce60ee70baa24a33f45
bytes: 224673
sidor: 7
hamtad: 2026-11-19T23:12:18+00:00
konverterad: 2026-11-19T23:12:19+00:00
pipeline: kommunhandlingar 0.12.0 / pdfplumber 0.11.10 / pdfminer.six 20260107
kvalitet: full
fel: null
kvalitet_per_sida: [ok, ok, ok, ok, ok, ok, ok]
tal_obekraftade: []
figurer: []
tolkade: []
granskad: null
---

<!-- sida 1 -->

Sid 1 av 7

Variabelspecifikation               2021-01-29   1(7)

Utlämning         av   data     från   Inera     till SCB

<!-- sida 2 -->

Sid 2 av 7

Variabelspecifikation               2021-01-29   2(7)

Versionshistorik

[Tabell 2-1](bilaga-bilaga-3-variabelspecifikation.tabeller/2-1.csv)

| Version | Datum | Ansvarig | Information om förändringar |
| --- | --- | --- | --- |
| 0.1 | 2021-01-26 | Victor Friberg | Första version |
| 0.2 | 2021-01-29 | Victor Friberg | Lagt till exempel |
| 1.0 | 2021-02-01 | Victor Friberg | Justerat uttaget efter kommentarer från 1177 Vårdguiden på<br>telefon |
|  |  |  |  |
|  |  |  |  |

<!-- sida 3 -->

Sid 3 av 7

Variabelspecifikation               2021-01-29   3(7)

Innehållsförteckning
1  VARIABELSPECIFIKATION FÖR EGEN PROVHANTERING ......................................................... 4

1.1  VARIABELINFORMATION ........................................................................................................................ 4
2  VARIABELSPECIFIKATION FÖR 1177 VÅRDGUIDENS E-TJÄNSTER ........................................ 6
2.1  VARIABELINFORMATION ........................................................................................................................ 6

3  VARIABELSPECIFIKATION FÖR 1177 VÅRDGUIDEN PÅ TELEFON .......................................... 7
3.1  VARIABELINFORMATION ........................................................................................................................ 7

<!-- sida 4 -->

Sid 4 av 7

Variabelspecifikation               2021-01-29   4(7)

1  Variabelspecifikation för Egen  provhantering

Statistiken för egen provhantering filtreras för att innehålla erbjudanden relaterade till Covid-19.

Data avser tidsperioden 2020-01-01 till 2022-12-31.

1.1 Variabelinformation

[Tabell 4-5-1](bilaga-bilaga-3-variabelspecifikation.tabeller/4-5-1.csv)

| Variabel | Beskrivning | Exempel |
| --- | --- | --- |
| PatientID | Personnummer för invånare | (personnummer borttaget) |
| OfferName | Namn på erbjudandet som använts.<br>(Källa LaboratoryOrder) | Covid-19 PCR: Hemtest för dig<br>som är sjuk<br>(Kod/beställningsnyckel fås i<br>appen "Alltid öppet") |
| OfferID | Id på erbjudandet som använts (Källa<br>LaboratoryOrder) | 474 |
| OfferValidForReside<br>ntsCountyCode | Erbjudandets länskod. Det län som<br>erbjudandet tillhör. (Källa<br>LaboratoryOrder) | 01 |
| OrderCreatedDateTi<br>me | Datum och klockslag när beställningen<br>gjordes av invånaren. (Källa<br>LaboratoryOrder) | 2020-11-17 11:02:03 |
| HandledDateTime | Tidsstämpel när beställningen hämtades<br>av provtagningssystemet. (Källa<br>LaboratoryOrder) | 2020-11-17 18:12:38 |
| MaterialHandling | Om det är en beställning av typen<br>Hemtest eller Provtagning på<br>provtagningsenhet (Källa<br>LaboratoryOrder) | Hemtest |
| MaterialHandlingLab<br>Name | Namn på system/lab som hämtat<br>beställningen från EP. (Källa<br>LaboratoryOrder) |  |
| ReportingLabUnitID | HSAID på Laboratoriet som skapat<br>svaret. Utgår från senaste labsvaret.<br>(Källa LaboratoryResult) | SE2321000016-DQSS |
| SampleDrawDateTim<br>e | Provtagningstid. Hämtas från labsvaret.<br>Utgår från senaste labsvaret. (Källa<br>LaboratoryResult) | 2020-11-17 18:12:38 |
| AnswerArrivedFromL<br>abDateTime | Tidpunkt när laboratoriet skickade<br>svaret. Utgår från senaste labsvaret.<br>(Källa LaboratoryResult) | 2020-11-17 18:12:38 |
| InsightResult (1) | Labsvarets insiktsresultat (ex<br>Negativt/Positivt/Tekniskt fel) | Positivt |
| InsightResult (2) | Labsvarets insiktsresultat om rapporten<br>innehåller flera insikter | Positivt |

<!-- sida 5 -->

Sid 5 av 7

Variabelspecifikation               2021-01-29   5(7)

<!-- sida 6 -->

Sid 6 av 7

Variabelspecifikation               2021-01-29   6(7)

2  Variabelspecifikation för 1177  Vårdguidens  e-tjänster

Statistiken för 1177 Vårdguidens e-tjänster filtreras för att innehålla ärenden relaterade till Covid-19.

Följande sökord appliceras som filter på variabel Ärendeundertyp:
{”covid”, ”PCR”, ”corona”,”Antikropp”,”SARS-COV-2”}

Data avser tidsperioden 2020-01-01 till 2022-12-31.

2.1 Variabelinformation

[Tabell 6-1](bilaga-bilaga-3-variabelspecifikation.tabeller/6-1.csv)

| Variabel | Beskrivning | Exempel |
| --- | --- | --- |
| SkapadDatumId | Datum då ärendet skapades | 20200101 |
| PersonID | Pnr för invånare ärendet berör | (personnummer borttaget) |
| Region | Administrativt ansvarig region för<br>enhet som ärendet berör | Region Stockholm |
| Flödestyp | Initierare av ärende (vård- eller<br>invånarinitierat ärende) | Vårdinitierat |
| Flödesundertyp | Typ av initiering (fråga eller<br>information) | Information |
| Ärendetyp | Ärendekategori | Provsvar |
| Ärendeundertyp | Namn på ärende | Provsvar covid-19 |

<!-- sida 7 -->

Sid 7 av 7

Variabelspecifikation               2021-01-29   7(7)

3  Variabelspecifikation för 1177 Vårdguiden   på telefon

Data avser tidsperioden 2019-01-01 till 2022-12-31.

3.1 Variabelinformation

[Tabell 7-1](bilaga-bilaga-3-variabelspecifikation.tabeller/7-1.csv)

| Variabel | Beskrivning | Exempel |
| --- | --- | --- |
| referralPriority | Brådskegrad | Omgående |
| referralCategory | Hänvisningsnivå | Primärvård |
| contactReason | Kontaktorsak | Feber – barn |
| personId | Personnummer | (personnummer borttaget) |
| personZipcode | Postnummer för invånares<br>folkbokföringsadress | 11860 |
| personGender | Kön för invånare (Heltal {0, 1, 2}) | 0 |
| documentCreatedTime | Tidsstämpel för skapande av<br>journalhandling. (DateTime<br>(YYYYMMDDhhmmss)) | 20150521150000 |
| StatQuestionAnswer2 | Svar på fråga 2 vid signering:<br>Gällde samtalet Corona covid-19? | Ja |
