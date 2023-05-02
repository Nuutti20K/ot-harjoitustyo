from database_connection import get_database_connection


class ScoreRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_scores(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Scores")
        rows = cursor.fetchall()
        scores = []
        for row in rows:
            scores.append((row["player"], row["score"]))

    def get_top_five(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from Scores order by score desc limit 5")
        rows = cursor.fetchall()
        scores = []
        for row in rows:
            scores.append((row["player"], row["score"]))
        return scores

    def add_score(self, player, score):
        if score > 0 and len(player) > 0:
            cursor = self.connection.cursor()
            cursor.execute(
                "insert into Scores (player, score) values (?, ?)",
                [player, score]
            )

            self.connection.commit()


score_repository = ScoreRepository(get_database_connection())
