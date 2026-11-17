
from datetime import date, timedelta


class Emprunt:

    # Constructeur
    def __init__(self, id_emprunt, adherent, livre):

        self.id_emprunt = id_emprunt

        # Association avec les objets Adherent et Livre
        self.adherent = adherent
        self.livre = livre

        # Date actuelle
        self.date_emprunt = date.today()

        # Retour prévu après 14 jours
        self.date_retour_prevue = self.date_emprunt + timedelta(days=14)

        # Date réelle initialement vide
        self.date_retour_reelle = None

        self.statut = "En cours"

    # Afficher les informations de l'emprunt
    def afficher_emprunt(self):

        print("------ Informations de l'emprunt ------")

        print("ID emprunt :", self.id_emprunt)

        print("Adhérent :", self.adherent.prenom, self.adherent.nom)

        print("Livre :", self.livre.titre)

        print("Date emprunt :", self.date_emprunt)

        print("Date retour prévue :", self.date_retour_prevue)

        print("Statut :", self.statut)

    # Effectuer le retour du livre
    def retourner_livre(self):

        if self.statut == "En cours":

            self.date_retour_reelle = date.today()

            self.statut = "Terminé"

            self.livre.retourner()

            print("Emprunt terminé avec succès.")

        else:
            print("Ce livre a déjà été retourné.")


# Importer les classes
from livre import Livre
from adherent import Adherent


# Créer un livre
livre1 = Livre(
    1,
    "Le Petit Prince",
    "Antoine de Saint-Exupéry",
    1943
)

# Créer un adhérent
adherent1 = Adherent(
    1,
    "Alami",
    "Sara",
    "sara@gmail.com",
    "0623456789"
)

# Emprunter le livre
livre1.emprunter()

# Créer un objet Emprunt
emprunt1 = Emprunt(1, adherent1, livre1)

# Afficher les informations
emprunt1.afficher_emprunt()

# Retourner le livre
print("\n--- Retour du livre ---")

emprunt1.retourner_livre()

# Vérifier les informations du livre
livre1.afficher_informations()
