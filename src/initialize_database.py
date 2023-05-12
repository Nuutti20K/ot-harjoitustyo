from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa Scores tietokantataulun.

    Args:
        connection: tietokantayhteyden connection-olio
    """
    cursor = connection.cursor()
    cursor.execute("""
        drop table if exists Scores;
    """)
    connection.commit()


def create_tables(connection):
    """Luo Scores tietokantataulun.

    Args:
        connection: tietokantayhteyden connection-olio
    """
    cursor = connection.cursor()
    cursor.execute("""
        create table Scores (
            id integer primary key, 
            player text,
            score integer
        );
    """)
    connection.commit()


def initialize_database():
    """Alustaa Scores tietokantataulun."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
