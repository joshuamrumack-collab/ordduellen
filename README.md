# Ordduellen ⚔️

Ett ordspel där elever duellerar med glosor (svenska ⇄ engelska). Skjut ord mot motståndaren – försvara dig genom att skriva översättningen innan ordet träffar.

**Spela:** https://joshuamrumack-collab.github.io/ordduellen/

## Det här finns

- **Spellägen:** mot bot, interaktiv guide, och online – duell, lagstrid och co-op mot en bot-armé
- **Fem banor med egen musik:** Månnatt, Vulkanen, Norrsken, Rymden och Solnedgång
- **Egen magiker:** eleverna samlar XP, går upp i nivå (1–30) och låser upp hattar, ansiktsdetaljer, kristaller och spår. 14 prestationer att jaga
- **Ordlistor:** egna ord, 12 färdiga kategorier, klistra in från Excel/Kalkylark, spara listor
- **Dela:** en lista blir en länk + QR-kod. I ett onlinerum visar "📱 QR" en kod till rummet för tavlan
- **Klassens listor:** lägg textfiler i [`listor/`](listor/) så dyker de upp i spelet (se instruktionerna där)
- **Helskärm** – även från Google Sites (öppnar spelet i en egen flik)

## Länkar som är bra att veta

| Länk | Vad den gör |
|---|---|
| `…/ordduellen/?rum=klass9b` | Öppnar spelet med rumskoden ifylld |
| `…/ordduellen/?lista=klader` | Öppnar listan `listor/klader.txt` direkt |

## Google Sites

Infoga → Bädda in → **Via webbadress** → klistra in spellänken.

## Tekniskt

Allt spel finns i `index.html` (fungerar även som fristående fil). Onlinespelet använder Firebase (Firestore + anonym inloggning). XP och utseende sparas i elevens webbläsare. Musiken och figurerna genereras i koden – inga bild- eller ljudfiler behövs. QR-koder: [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) (MIT).
