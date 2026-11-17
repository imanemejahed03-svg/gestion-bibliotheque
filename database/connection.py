
import os
import mysql.connector

def get_connection():

    try:
        connection = mysql.connector.connect(

            host=os.getenv("DB_HOST", "127.0.0.1"),

            port=int(os.getenv("DB_PORT", "3306")),

            user=os.getenv("DB_USER", "root"),

            password=os.getenv("DB_PASSWORD", ""),

            database=os.getenv("DB_NAME", "gestion_bibliotheque")
        )

        print("Connexion à MariaDB réussie !")

        return connection

    except mysql.connector.Error as error:

        print("Erreur de connexion :", error)

        return None
