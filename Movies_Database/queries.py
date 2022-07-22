#pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()


def directors_count(db):
    query="SELECT COUNT(*) FROM directors d"
    db.execute(query)
    results=db.fetchone()
    return results[0]

def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query="SELECT d.name FROM directors d ORDER BY d.name"
    db.execute(query)
    results=db.fetchall()
    results2=[]
    for n in results:
        results2.append(n[0])
    return results2


def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = """


    SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title

    """
    db.execute(query)
    results=db.fetchall()
    results2=[]
    for n in results:
        results2.append(n[0])
    return results2


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = """
        SELECT COUNT(*)
        FROM directors
        WHERE name LIKE ?
    """
    db.execute(query, (f"%{name}%",))
    count = db.fetchone()
    return count[0]




def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order

    query=f"SELECT title FROM movies WHERE minutes > ? ORDER BY title"
    db.execute(query,(min_length,))
    results=db.fetchall()
    results2=[]
    for n in results:
        results2.append(n[0])
    print (results2)
    return results2

directors_list(db)
