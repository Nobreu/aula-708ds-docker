from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="meubanco",
        user="postgres",
        password="postgres"
    )

@app.route('/')
def home():
    return "API Flask conectada ao Postgres"

@app.route('/usuarios')
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM usuariosflask;')
    users = cur.fetchAll()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
    port=5000)
