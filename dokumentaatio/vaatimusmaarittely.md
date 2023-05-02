# Vaatimusmäärittely

## Pelin tarkoitus

Matopelissä on tarkoitus ohjata matoa ja kerätä pellettejä. Aina kun mato syö pelletin sen kokonaispituus kasvaa, ja kun mato törmää itseensä, peli loppuu. Kun peli loppuu peli tallentaa ennätyksen. Tavoitteena on jatkaa peliä mahdollisimman pitkään ja saavuttaa mahdollisimman hyvä piste-ennätys.

### Perusversion toiminnallisuus

- Aloitusvalikko, josta voi aloittaa uuden pelin tai katsoa aikaisempia ennätyksiä **TEHTY**
- Pelissä pelaaja voi ohjata matoa nuolinäppäimillä ylös, alas, vasemmalle ja oikealle **TEHTY**
    - Madon liikuminen on rajattu ruudukkoon **TEHTY**
- Pelialueelle ilmestyy satunnaisesti pelletti aina kun edellinen on kerätty **TEHTY**
- Kun pelletin kerää, madon pituus kasvaa **TEHTY**
- Kun mato törmää itseensä tai seinään, peli loppuu **TEHTY**
    - Pelin loppuessa pelaajalta kysytään nimeä, jonka jälkeen hänen pisteet tallennetaan **TEHTY**
    - Kun pisteet on tallennettu, peli palaa aloitusvalikkoon **TEHTY**

### Jatkokehitysideoita

- Nopeutus painike, jota pitämällä pohjassa mato liikkuu nopeammin
- Bonus pellettejä, joista saa enemmän pistetä, mutta ne katoavat tietyn ajan kuluttua
- Vaikeustason valinta, joka vaikuttaa madon nopeuteen
    - Edistyvä vaikeutuminen, jossa mato nopeutuu pelin edetessä
- Ylimääräisiä pelialueita joissa on erilaisia esteitä, kuten seiniä
    - Vaihtoehtoinen pelimuoto, jossa peli etenee kentästä toiseen
    - Kenttäeditori jossa pelaaja voi luoda omia kenttiä
        - Peli tallentaa pelaajan luomat kentät
- Liikkuvia vihollisia joita pitää väistellä
- Vaihtoehtoinen pelimuoto, jossa matoa voi ohjata vapaasti eikä sen liikkeitä ole rajattu ruudukkoon eikä pääilmansuuntiin
- Kaksinpeli, jossa kaksi pelaajaa ohjaa omia matoja
