import psycopg2
# Establish connection with postgres server
conn = psycopg2.connect("host=localhost dbname=sample_db port=5432 user=postgres password=Test6508")
#Create connection object
cur = conn.cursor()
'''
To execute commands on the Postgres database,
call the execute method on the Cursor object 
with a stringified SQL command.
'''
cur.execute('SELECT * FROM MOCK_DATA;')
one = cur.fetchone()
all = cur.fetchall()

print(one)