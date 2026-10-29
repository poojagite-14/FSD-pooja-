from flask import Flask, request
import psycopg2

app = Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname = 'employee',
        user = 'postgres',
        password = 'root',
        host = 'localhost',
        port = '5432'
    )
@app.route('/create_table')
def create_table():
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS Employee(
                emp_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                department VARCHAR(100),
                salary FLOAT
            ); """)
        conn.commit()
        cur.close()
        conn.close()
        return "Employee table created successfully!!"

@app.route('/insert records')
def insert_records():
        conn = db_connect()
        cur = conn.cursor()

        employees = [
            ("pooja gite", "ITI", 78000),
            ("sneha raut", "MQ", 89000),
            ("priya shinde", "Transport", 30000),
            ("sonali golhar", "sales", 50000),
            ("urmila sharma", "operator", 20000)
        ]

        cur.executemany("INSERT INTO Employee (name, department, salary) VALUES(%s,%s,%s);", employees)

        conn.commit()
        cur.close()
        conn.close()

        return "5 Record inserted sucessfully!!"

@app.route('/search_employee/<int:eid>')
def search_employee(eid):
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Employee WHERE emp_id = %s;",(eid,))

        employee = cur.fetchone()

        cur.close()
        conn.close()

        if employee:
            return f"Employee ID: {employee[0]}, Name: {employee[1]}, Department: {employee[2]}, Salary: {employee[3]}"
        conn.commit()
        conn.close()
        conn.close()
if __name__ == '__main__':
    app.run(debug= True, use_reloader =False)