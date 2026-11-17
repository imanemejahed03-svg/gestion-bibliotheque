
from database.connection import get_connection

# Appeler la fonction de connexion
conn = get_connection()

# Vérifier si la connexion existe
if conn is not None:

    print("Notre application est connectée à MySQL.")

    conn.close()

    print("Connexion fermée.")
