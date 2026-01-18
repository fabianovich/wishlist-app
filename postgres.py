import psycopg2

import credentials

db_connection = psycopg2.connect(
    database=credentials.database,
    host=credentials.host,
    user=credentials.user,
    password=credentials.password,
    port=credentials.port,
)

cursor = db_connection.cursor()

# begin functions


def new_user(name):
    id = get_new_id()
    cursor.execute(f"insert into people values ({id}, '{name}')")
    db_connection.commit()


def get_new_id():
    cursor.execute("select max(id) from people")
    current_highest_id = cursor.fetchone()
    new_id = int(current_highest_id[0]) + 1
    return new_id


def sign_in(name, password_hash):
    cursor.execute(f"select id from people where name = {name}")
    id = cursor.fetchone()[0]


# end functions

new_user("Erica Kirk")
