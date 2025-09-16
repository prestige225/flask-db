

# from flask import Flask, jsonify
# import mysql.connector

# app = Flask(__name__)

# # 🔑 Config base de données (Clever Cloud)
# db_config = {
#     "host": "bvav4zaafpxb0cwgpb8u-mysql.services.clever-cloud.com",
#     "user": "u2z6tmasp3yrszsi",
#     "password": "5yARZs3hF8PlCrhHu1hO",
#     "database": "bvav4zaafpxb0cwgpb8u",
#     "port": 3306
# }

# # Fonction connexion
# def get_db_connection():
#     conn = mysql.connector.connect(**db_config)
#     return conn

# @app.route("/")
# def index():
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()
#         cursor.execute("SELECT NOW();")  # Test simple
#         result = cursor.fetchone()
#         cursor.close()
#         conn.close()
#         return jsonify({
#             "message": "Connexion MySQL réussie 🚀",
#             "time": str(result[0])
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# 🔑 Config MySQL Clever Cloud
db_config = {
    "host": "bvav4zaafpxb0cwgpb8u-mysql.services.clever-cloud.com",
    "user": "u2z6tmasp3yrszsi",
    "password": "5yARZs3hF8PlCrhHu1hO",
    "database": "bvav4zaafpxb0cwgpb8u",
    "port": 3306
}

# Fonction pour se connecter à la base
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# 🔹 Route test
@app.route("/")
def home():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")  # test simple
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({"message": "Connexion MySQL réussie 🚀", "time": str(result[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

# 🔹 Route pour lister tous les utilisateurs
@app.route("/users", methods=["GET"])
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})

# 🔹 Route pour ajouter un utilisateur
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Utilisateur ajouté ✅"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
