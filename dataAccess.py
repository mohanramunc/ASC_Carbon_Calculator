import os
import psycopg2

print(os.environ)
conn = psycopg2.connect(os.environ['DATABASE_URL'])

cur = conn.cursor()

cur.execute("select * from mathclub")
mathclub = cur.fetchall()

#Proof of concept: The transformed data is in the database

for row in mathclub:
    print(row[0], row[1], row[2], row[3], row[4])

conn.commit()

cur.close()
conn.close()
