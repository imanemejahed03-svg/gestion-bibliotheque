
class Adherent:

    # Constructeur
    def __init__(self, id_adherent, nom, prenom, email, telephone):

        self.id_adherent = id_adherent
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone

    # Afficher les informations de l'adhérent
    def afficher_informations(self):

        print("------ Informations de l'adhérent ------")
        print("ID :", self.id_adherent)
        print("Nom :", self.nom)
        print("Prénom :", self.prenom)
        print("Email :", self.email)
        print("Téléphone :", self.telephone)

    # Modifier l'adresse email
    def modifier_email(self, nouvel_email):

        self.email = nouvel_email
        print("Adresse email modifiée avec succès.")


# Création de deux adhérents
adherent1 = Adherent(
    1,
    "Mejahed",
    "Imane",
    "imane@gmail.com",
    "0612345678"
)

adherent2 = Adherent(
    2,
    "Alami",
    "Sara",
    "sara@gmail.com",
    "0623456789"
)


# Tester les méthodes
adherent1.afficher_informations()

print("\nModification de l'email :")
adherent1.modifier_email("imane.pro@gmail.com")

adherent1.afficher_informations()
