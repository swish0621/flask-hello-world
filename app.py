import psycopg
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Nicholas Swisher in 3308.'

@app.route('/db_test')
def db_test(): 
    conn = psycopg.connect("postgresql://lab10_database_l65b_user:6u5YCsT039jmaSE0knSRY6002qOUTPAP@dpg-d24e42ngi27c73dgfulg-a/lab10_database_l65b")
    conn.close()
    return "Database connection successful"

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
                );
    ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg.connect("postgresql://lab10_database_l65b_user:6u5YCsT039jmaSE0knSRY6002qOUTPAP@dpg-d24e42ngi27c73dgfulg-a/lab10_database_l65b")
    cur = conn.cursor()
    cur.execute('''
                INSERT INTO Basketball (First, Last, City, Name, Number)
                Values
                ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball table succcessfully poplated"

@app.route('/db_select')
def db_select():
    conn = psycopg.connect("postgresql://lab10_database_l65b_user:6u5YCsT039jmaSE0knSRY6002qOUTPAP@dpg-d24e42ngi27c73dgfulg-a/lab10_database_l65b")
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string

@app.route('/db_drop')
def db_drop():
    conn = psycopg.connect("postgresql://lab10_database_l65b_user:6u5YCsT039jmaSE0knSRY6002qOUTPAP@dpg-d24e42ngi27c73dgfulg-a/lab10_database_l65b")
    cur = conn.cursor()
    cur.execute('''
                DROP TABLE Basketball;
                ''')
    conn.commit()
    conn.close()
    return "Basketball table successfully dropped"