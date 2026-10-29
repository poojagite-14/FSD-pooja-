from flask import Flask
import psycopg2

app= Flask(__name__)

def db_connect():
    
    conn=psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    
    conn.close()
    return "database connected successfully"
    
@app.route("/")
def home():
    
    return db_connect()
if __name__ == "__main__":
    app.run(debug=True)