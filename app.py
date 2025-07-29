import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World From Nicholas Swisher in 3308.'

@app.route('db_test')
def db_test(): 
    conn = psycopg2.connect("postgresql://lab10_database_l65b_user:6u5YCsT039jmaSE0knSRY6002qOUTPAP@dpg-d24e42ngi27c73dgfulg-a/lab10_database_l65b")
    conn.close()
    return "Database connection successful!"