
from database.connection import get_connection
import mysql.connector


# =====================================
# AJOUTER UN ADHERENT
# =====================================

def ajouter_adherent(nom, prenom, email, telephone):

    conn = get_connection()

    if conn is None:
        return False, "Connexion à MySQL impossible."

    cursor = None

    try:
        cursor = conn.cursor()

        requete = """
            INSERT INTO adherent
            (nom, prenom, email, telephone)
            VALUES (%s, %s, %s, %s)
        """

        valeurs = (nom, prenom, email, telephone)

        cursor.execute(requete, valeurs)
        conn.commit()

        return True, "Adhérent ajouté avec succès !"

    except mysql.connector.Error as error:

        conn.rollback()

        if error.errno == 1062:
            return False, "Cette adresse email existe déjà."

        return False, f"Erreur MySQL : {error.msg}"

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()


# =====================================
# AFFICHER LES ADHERENTS
# =====================================

def afficher_adherents():

    adherents = obtenir_adherents()

    print("\n===== LISTE DES ADHERENTS =====")

    for adherent in adherents:

        print("-------------------------")
        print("ID :", adherent[0])
        print("Nom :", adherent[1])
        print("Prénom :", adherent[2])
        print("Email :", adherent[3])
        print("Téléphone :", adherent[4])


# =====================================
# OBTENIR LES ADHERENTS
# =====================================

def obtenir_adherents():

    conn = get_connection()

    if conn is None:
        return []

    cursor = None

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM adherent")

        return cursor.fetchall()

    except mysql.connector.Error as error:
        print("Erreur MySQL :", error)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()


# =====================================
# MODIFIER UN ADHERENT
# =====================================


def modifier_adherent(
    id_adherent,
    nouveau_nom,
    nouveau_prenom,
    nouvel_email,
    nouveau_telephone
):

    conn = get_connection()

    if conn is None:
        return False, "Connexion à MySQL impossible."

    cursor = None

    try:
        cursor = conn.cursor()

        # Vérifier si l'adhérent existe
        cursor.execute(
            "SELECT id_adherent FROM adherent WHERE id_adherent = %s",
            (id_adherent,)
        )

        if cursor.fetchone() is None:
            return False, "Adhérent introuvable."

        # Modifier les informations
        requete = """
            UPDATE adherent
            SET nom = %s,
                prenom = %s,
                email = %s,
                telephone = %s
            WHERE id_adherent = %s
        """

        valeurs = (
            nouveau_nom,
            nouveau_prenom,
            nouvel_email,
            nouveau_telephone,
            id_adherent
        )

        cursor.execute(requete, valeurs)
        conn.commit()

        return True, "Adhérent modifié avec succès !"

    except mysql.connector.Error as error:

        conn.rollback()

        if error.errno == 1062:
            return False, "Cette adresse email est déjà utilisée."

        return False, f"Erreur MySQL : {error.msg}"

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()



# =====================================
# SUPPRIMER UN ADHERENT
# =====================================

def supprimer_adherent(id_adherent):

    conn = get_connection()

    if conn is None:
        return False, "Connexion à MySQL impossible."

    cursor = None

    try:
        cursor = conn.cursor()

        requete = """
            DELETE FROM adherent
            WHERE id_adherent = %s
        """

        cursor.execute(requete, (id_adherent,))

        if cursor.rowcount == 0:
            conn.rollback()
            return False, "Adhérent introuvable."

        conn.commit()

        return True, "Adhérent supprimé avec succès !"

    except mysql.connector.Error as error:

        conn.rollback()

        if error.errno == 1451:
            return False, (
                "Impossible de supprimer cet adhérent : "
                "il possède un historique d'emprunts."
            )

        return False, f"Erreur MySQL : {error.msg}"

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()
