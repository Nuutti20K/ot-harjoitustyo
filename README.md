# Matopeli

Matopelissä on tarkoitus ohjata matoa ja kerätä pellettejä. Aina kun mato syö pelletin sen kokonaispituus kasvaa, ja kun mato törmää itseensä tai seinään, peli loppuu.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Työaikakirjanpito](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/aikakirjanpito.md)

## Asennus
Tarvittavat riippuvuudet asennetaan komennolla:
```bash
poetry install
```
Tarvittavat alustukset tehdään komennolla:
```bash
poetry run invoke build
```
## Komentorivitoiminnot
Peli käynnistetään komennolla:
```bash
poetry run invoke start
```
Testit tehdään komennolla: 
```bash
poetry run invoke test
```
Kattavuusraportin saa komennolla: 
```bash
poetry run invoke coverage-report
```
Pylint tarkastukset voidaan tehdä komennnolla:
```bash
poetry run invoke lint
```
