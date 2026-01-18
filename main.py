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

cursor.execute("SELECT * FROM wishlists")

records = cursor.fetchall()
print(records)
