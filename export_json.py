import json
import psycopg2

username = 'AntonK_KM_02'
password = '2222'
database = 'db_lab2_Kaznovskyi'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

data = {}
with conn:
    cur = conn.cursor()

    for table in ('certifications', 'courses', 'difficulty', 'organizations'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('Kaznovskyi_lab3_DB.json', 'w') as outf:
    json.dump(data, outf, default=str, indent=4)