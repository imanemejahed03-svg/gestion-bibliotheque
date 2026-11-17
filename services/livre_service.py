
from database.connection import get_connection
import mysql.connector


# =====================================
# OBTENIR TOUS LES LIVRES
# =====================================

def obtenir_livres():

    conn = get_connection()

    if conn is None:
        return []

    cursor = None

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livre")

        livres = cursor.fetchall()

        return livres

    except mysql.connector.Error as error:
        print("Erreur MySQL :", error)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()


# =====================================
# AJOUTER UN LIVRE
# =====================================

def ajouter_livre(titre, auteur, annee_publication):

    conn = get_connection()

    if conn is None:
        return False, "Connexion à MySQL impossible."

    cursor = None

    try:
        cursor = conn.cursor()

        requete = """
            INSERT INTO livre (titre, auteur, annee_publication)
            VALUES (%s, %s, %s)
        """

        valeurs = (titre, auteur, annee_publication)

        cursor.execute(requete, valeurs)

        conn.commit()

        return True, "Livre ajouté avec succès !"

    except mysql.connector.Error as error:

        conn.rollback()

        return False, f"Erreur MySQL : {error.msg}"

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()


# =====================================
# MODIFIER UN LIVRE
# =====================================

def modifier_livre(
    id_livre,
    nouveau_titre,
    nouvel_auteur,
    nouvelle_annee
):

    conn = get_connection()

    if conn is None:
        return False, "Connexion à MySQL impossible."

    cursor = None

    try:
        cursor = conn.cursor()

        # Vérifier si le livre existe
        cursor.execute(
            "SELECT id_livre FROM livre WHERE id_livre = %s",
            (id_livre,)
        )

        if cursor.fetchone() is None:
            return False, "Livre introuvable."

        # Modifier les informations
        requete = """
            UPDATE livre
            SET titre = %s,
                auteur = %s,
                annee_publication = %s
            WHERE id_livre = %s
        """

        valeurs = (
            nouveau_titre,
            nouvel_auteur,
            nouvelle_annee,
            id_livre
        )

        cursor.execute(requete, valeurs)

        conn.commit()

        return True, "Livre modifié avec succès !"

    except mysql.connector.Error as error:

        conn.rollback()

        return False, f"Erreur MySQL : {error.msg}"

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()


# =====================================
# SUPPRIMER UN LIVRE
# =====================================

def supprimer_livre(id_livre):

    conn = get_connection()

    if conn is None:
        return False, "Connexion à MySQL impossible."

    cursor = None

    try:
        cursor = conn.cursor()

        requete = """
            DELETE FROM livre
            WHERE id_livre = %s
        """

        cursor.execute(requete, (id_livre,))

        if cursor.rowcount == 0:
            conn.rollback()
            return False, "Livre introuvable."

        conn.commit()

        return True, "Livre supprimé avec succès !"

    except mysql.connector.Error as error:

        conn.rollback()

        if error.errno == 1451:
            return False, (
                "Impossible de supprimer ce livre : "
                "il possède un historique d'emprunts."
            )

        return False, f"Erreur MySQL : {error.msg}"

    finally:
        if cursor is not None:
            cursor.close()

        conn.close()
