import os
import time
from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Permitir peticiones desde el frontend

def get_db_connection():
    # Intenta conectar a la base de datos con reintentos por si MySQL tarda en iniciar
    retries = 5
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'database'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', 'devops_pass'),
                database=os.getenv('DB_NAME', 'festival_db')
            )
            return connection
        except mysql.connector.Error:
            retries -= 1
            time.sleep(2)
    return None

@app.route('/api/artists', methods=['GET'])
def get_artists():
    conn = get_db_connection()
    if conn is None:
        # Fallback de emergencia por si la DB no está lista, para que la landing no falle
        return jsonify(["Artistas Locales (Modo Seguro)", "DevOps Band", "Docker Packets"])
    
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM artists;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    artists = [row[0] for row in result]
    return jsonify(artists)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)