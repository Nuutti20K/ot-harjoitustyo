# Matopeli

Matopelissä on tarkoitus ohjata matoa ja kerätä pellettejä. Aina kun mato syö pelletin sen kokonaispituus kasvaa, ja kun mato törmää itseensä tai seinään, peli loppuu.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Changelog](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Työaikakirjanpito](https://github.com/Nuutti20K/ot-harjoitustyo/blob/master/dokumentaatio/aikakirjanpito.md)

## Komentorivitoiminnot
Peli käynnistetään toiminnolla:
```bash
poetry run invoke start
```
Testien tekeminen: 
```bash
poetry run invoke test
```
Kattavuusraportti: 
```bash
poetry run invoke coverage-report
```
