
from database.connection import get_connection
from datetime import date, timedelta


# 1. Afficher tous les emprunts
def afficher_emprunts():

    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    try:
        requete = """
            SELECT
                emprunt.id_emprunt,
                adherent.nom,
                adherent.prenom,
                livre.titre,
                emprunt.date_emprunt,
                emprunt.date_retour_prevue,
                emprunt.statut
            FROM emprunt
            JOIN adherent
                ON emprunt.id_adherent = adherent.id_adherent
            JOIN livre
                ON emprunt.id_livre = livre.id_livre
        """

        cursor.execute(requete)
        emprunts = cursor.fetchall()

        for emprunt in emprunts:
            print(emprunt)

    except Exception as error:
        print("Erreur :", error)

    finally:
        cursor.close()
        conn.close()


# 2. Ajouter un emprunt
def ajouter_emprunt(id_adherent, id_livre):

    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    try:
        conn.start_transaction()

        # Vérifier si l'adhérent existe
        cursor.execute(
            "SELECT id_adherent FROM adherent WHERE id_adherent = %s",
            (id_adherent,)
        )

        if cursor.fetchone() is None:
            print("Adhérent introuvable.")
            conn.rollback()
            return

        # Vérifier si le livre existe et s'il est disponible
        cursor.execute(
            "SELECT disponible FROM livre WHERE id_livre = %s FOR UPDATE",
            (id_livre,)
        )

        livre = cursor.fetchone()

        if livre is None:
            print("Livre introuvable.")
            conn.rollback()
            return

        if not livre[0]:
            print("Ce livre n'est pas disponible.")
            conn.rollback()
            return

        # Vérifier le nombre d'emprunts en cours
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM emprunt
            WHERE id_adherent = %s AND statut = 'En cours'
            """,
            (id_adherent,)
        )

        nombre_emprunts = cursor.fetchone()[0]

        if nombre_emprunts >= 3:
            print("L'adhérent a déjà 3 emprunts en cours.")
            conn.rollback()
            return

        # Calculer les dates
        date_emprunt = date.today()
        date_retour_prevue = date_emprunt + timedelta(days=14)

        # Ajouter l'emprunt
        cursor.execute(
            """
            INSERT INTO emprunt
            (id_adherent, id_livre, date_emprunt,
             date_retour_prevue, statut)
            VALUES (%s, %s, %s, %s, 'En cours')
            """,
            (id_adherent, id_livre, date_emprunt, date_retour_prevue)
        )

        # Rendre le livre indisponible
        cursor.execute(
            "UPDATE livre SET disponible = FALSE WHERE id_livre = %s",
            (id_livre,)
        )

        conn.commit()
        print("Emprunt ajouté avec succès !")

    except Exception as error:
        conn.rollback()
        print("Erreur :", error)

    finally:
        cursor.close()
        conn.close()


# 3. Retourner un livre
def retourner_livre(id_emprunt):

    conn = get_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    try:
        conn.start_transaction()

        cursor.execute(
            """
            SELECT id_livre, date_retour_prevue, statut
            FROM emprunt
            WHERE id_emprunt = %s
            FOR UPDATE
            """,
            (id_emprunt,)
        )

        emprunt = cursor.fetchone()

        if emprunt is None:
            print("Emprunt introuvable.")
            conn.rollback()
            return

        id_livre = emprunt[0]
        date_prevue = emprunt[1]
        statut = emprunt[2]

        if statut != "En cours":
            print("Cet emprunt est déjà terminé.")
            conn.rollback()
            return

        date_retour = date.today()

        # Calculer le retard éventuel
        retard = max(0, (date_retour - date_prevue).days)

        cursor.execute(
            """
            UPDATE emprunt
            SET date_retour_reelle = %s,
                statut = 'Terminé'
            WHERE id_emprunt = %s
            """,
            (date_retour, id_emprunt)
        )

        # Rendre le livre disponible
        cursor.execute(
            "UPDATE livre SET disponible = TRUE WHERE id_livre = %s",
            (id_livre,)
        )

        conn.commit()

        print("Livre retourné avec succès !")
        print("Nombre de jours de retard :", retard)

    except Exception as error:
        conn.rollback()
        print("Erreur :", error)

    finally:
        cursor.close()
        conn.close()


# 4. Test du programme
if __name__ == "__main__":

    ajouter_emprunt(1, 1)

    afficher_emprunts()
if __name__ == "__main__":

    # ajouter_emprunt(1, 1)

    retourner_livre(1)

    afficher_emprunts()
    
def obtenir_emprunts():

    conn = get_connection()

    if conn is None:
        return []

    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                e.id_emprunt,
                a.nom,
                a.prenom,
                l.titre,
                e.date_emprunt,
                e.date_retour_prevue,
                e.statut
            FROM emprunt e
            JOIN adherent a
                ON e.id_adherent = a.id_adherent
            JOIN livre l
                ON e.id_livre = l.id_livre
        """)

        emprunts = cursor.fetchall()
        return emprunts

    except Exception as error:
        print("Erreur :", error)
        return []

    finally:
        cursor.close()
        conn.close()