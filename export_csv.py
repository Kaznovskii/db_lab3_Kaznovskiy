import csv
import psycopg2

username = 'AntonK_KM_02'
password = '2222'
database = 'db_lab2_Kaznovskyi'
host = 'localhost'
port = '5432'

OUTPUT_FILE = 'Kaznovskyi_lab3_DB_{}.csv'

TABLES = [
    'certifications',
    'courses',
    'difficulty',
    'organizations'
]

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE.format(table_name), 'w', encoding='UTF-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])