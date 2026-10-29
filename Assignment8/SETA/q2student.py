from flask import Flask
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(
            dbname="student1",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(100),
    age INT
)
""")

conn.commit()
conn.close()
conn.close()

@app.route("/")
def home():
    return "Student table created successfully!"

if __name__ == "__main__":
    app.run(debug=True)