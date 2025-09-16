

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# 🔑 Config base de données (Clever Cloud)
db_config = {
    "host": "bvav4zaafpxb0cwgpb8u-mysql.services.clever-cloud.com",
    "user": "u2z6tmasp3yrszsi",
    "password": "5yARZs3hF8PlCrhHu1hO",
    "database": "bvav4zaafpxb0cwgpb8u",
    "port": 3306
}

# Fonction connexion
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")  # Test simple
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({
            "message": "Connexion MySQL réussie 🚀",
            "time": str(result[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
