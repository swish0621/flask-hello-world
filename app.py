import psycopg
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World From Nicholas Swisher in 3308.'

@app.route('/db_test')
def db_test(): 
    conn = psycopg.connect("postgresql://lab10_database_l65b_user:6u5YCsT039jmaSE0knSRY6002qOUTPAP@dpg-d24e42ngi27c73dgfulg-a/lab10_database_l65b")
    conn.close()
    return "Database connection successful!"

@app.route('/create_db')
def create_db():
    conn = psycopg.connect("postgresql://lab10_database_l65b_user:6u5YCsT039jmaSE0knSRY6002qOUTPAP@dpg-d24e42ngi27c73dgfulg-a/lab10_database_l65b")
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Basketball(
                First varchar(225),
                Last varchar(225),
                City varchar(225),
                Name varchar(225),
                Number int
                ''')
    conn.commit()
    conn.close()
    return "Database created successfully!"
