# Käyttöohje

## Pelin käynnistäminen
Tarvittavat riippuvuudet asennetaan komennolla:
```bash
poetry install
```
Tarvittavat alustukset tehdään komennolla:
```bash
poetry run invoke build
```
Sitten pelin voi käynnistää komennolla:
```bash
poetry run invoke start
```

## Päävalikko
Päävalikossa voi aloittaa pelin painamalla start-painiketta vasemmalla hiiren näppäimellä. Lisäksi päävalikossa näkyy viisi parasta ennätystä.

## Varsinainen peli
Matoa ohjataan nuolinäppäimillä. Pelin tarkoituksena on kerätä mahdollisimman paljon valkoisia pellettejä törmäämättä seiniin tai madon ruumiiseen. Matoa ei voi kääntää päinvastaiseen suuntaan. Peli loppuu kun mato törmää seinään tai itseensä.

## Pisteiden tallennus
Pelin loputtua peli kysyy pelaajalta nimeä. Nimi kirjoitetaan näppäimistöllä ja painetaan enter kun nimi on valmis. Nimi kenttään mahtuu enintään kymmenen merkkiä. Jos nimikentän jättää tyhjäksi tai pelaaja ei ole saanut lainkaan pisteitä, ennätystä ei tallenneta.
