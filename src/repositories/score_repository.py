from database_connection import get_database_connection


class ScoreRepository:
    """Luokka, joka vastaa pisteiden tallentamisesta ja noutamisesta.

    Attributes
        connection: Sqlite yhteys-olio.
    """

    def __init__(self, connection):
        self.connection = connection

    def get_top_five(self):
        """Hakee tietokannasta viisi parasta ennätystä.

        Returns:
            viisi parasta ennätystä tupleina, jossa on ensin pelaajan nimi ja toisena pisteet.
        """
        cursor = self.connection.cursor()
        cursor.execute("select * from Scores order by score desc limit 5")
        rows = cursor.fetchall()
        scores = []
        for row in rows:
            scores.append((row["player"], row["score"]))
        return scores

    def add_score(self, player, score):
        """Lisää ennätyksen tietokantaan.

        Args:
            player: Pelaajan nimi.
            score: Pelaajan pisteet
        """
        if score > 0 and len(player) > 0:
            cursor = self.connection.cursor()
            cursor.execute(
                "insert into Scores (player, score) values (?, ?)",
                [player, score]
            )

            self.connection.commit()


score_repository = ScoreRepository(get_database_connection())
