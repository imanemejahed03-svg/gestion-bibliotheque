
class Livre:

    # 1. Constructeur : initialisation des attributs
    def __init__(self, id_livre, titre, auteur, annee_publication, disponible=True):

        self.id_livre = id_livre
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.disponible = disponible

    # 2. Méthode pour afficher les informations du livre
    def afficher_informations(self):

        print("------ Informations du livre ------")
        print("Identifiant :", self.id_livre)
        print("Titre :", self.titre)
        print("Auteur :", self.auteur)
        print("Année de publication :", self.annee_publication)

        if self.disponible:
            print("Disponibilité : Disponible")
        else:
            print("Disponibilité : Emprunté")

    # 3. Méthode pour emprunter un livre
    def emprunter(self):

        if self.disponible == True:
            self.disponible = False
            print("Le livre", self.titre, "a été emprunté avec succès.")
        else:
            print("Impossible d'emprunter", self.titre, ": le livre est déjà emprunté.")

    # 4. Méthode pour retourner un livre
    def retourner(self):

        if self.disponible == False:
            self.disponible = True
            print("Le livre", self.titre, "a été retourné avec succès.")
        else:
            print("Le livre", self.titre, "est déjà disponible.")


# -----------------------------------------
# Création de deux objets de la classe Livre
# -----------------------------------------

livre1 = Livre(1, "Le Petit Prince", "Antoine de Saint-Exupéry", 1943)

livre2 = Livre(2, "L'Etranger", "Albert Camus", 1942)


# -----------------------------------------
# Test des méthodes
# -----------------------------------------

# Afficher les informations des deux livres
print("\n===== LIVRE 1 =====")
livre1.afficher_informations()

print("\n===== LIVRE 2 =====")
livre2.afficher_informations()


# Emprunter le premier livre
print("\n===== TEST EMPRUNT =====")
livre1.emprunter()

# Essayer de l'emprunter une deuxième fois
livre1.emprunter()


# Retourner le premier livre
print("\n===== TEST RETOUR =====")
livre1.retourner()


# Afficher les informations après les opérations
print("\n===== ETAT FINAL =====")
livre1.afficher_informations()
