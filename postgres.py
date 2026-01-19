from imaplib import ParseFlags

import bcrypt
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


def new_user(name, password):
    id = get_new_id()
    password_hash = bcrypt.hashpw(password, bcrypt.gensalt())
    cursor.execute(f"insert into people values ({id}, '{name}', {password_hash})")
    db_connection.commit()


def get_new_id():
    cursor.execute("select max(id) from people")
    current_highest_id = cursor.fetchone()
    new_id = int(current_highest_id[0]) + 1
    return new_id


def sign_in(name, password):
    cursor.execute(f"select password_hash from people where name = {name}")
    password_hash = cursor.fetchone()[0]
    if bcrypt.checkpw(password, password_hash):
        print("match!!")


# end functions
