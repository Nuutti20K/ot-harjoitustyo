from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        drop table if exists Scores;
    """)
    connection.commit()


def create_tables(connection):
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
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
