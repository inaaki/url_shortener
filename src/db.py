import mysql.connector
import src.rand as rand


credentials = {
    'host': "localhost",
    'user': "akib",
    'password': "Akib119@@@",
    'database': "url_shorten"
}


cnx = mysql.connector.connect(**credentials)
cur = cnx.cursor()


def add_to_db(url):
    urls = check_url(url)
    # url already exists in the server
    if urls and urls[1] == url:
        # return url short form
        return urls[0]
    # generate random uuid
    id = rand.get_id()
    while check_url(id):
        id = rand.get_id()

    # add url to database
    query = """INSERT INTO long_to_short
               VALUES (%s, %s)
            """
    values = (id, url)
    cur.execute(query, values)
    cnx.commit()
    return id


def check_url(url):
    # check if url exists either in short form or in long form
    # returns "both url" or None
    query = f"SELECT * FROM long_to_short WHERE (shorty = '{url}' OR longy = '{url}');"
    cur.execute(query)
    return cur.fetchone()
