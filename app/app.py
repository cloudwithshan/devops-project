from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps World 🚀"

@app.route('/db')
def db():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="testdb"
        )
        return "Database Connected ✅"
    except:
        return "Database Connection Failed ❌"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)