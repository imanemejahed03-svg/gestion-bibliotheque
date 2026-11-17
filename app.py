
from flask import Flask, render_template, request, redirect, url_for, flash



from services.livre_service import (
    obtenir_livres,
    ajouter_livre,
    modifier_livre,
    supprimer_livre
)

from services.adherent_service import (
    obtenir_adherents,
    ajouter_adherent,
    modifier_adherent,
    supprimer_adherent
)

from services.emprunt_service import (
    obtenir_emprunts,
    ajouter_emprunt,
    retourner_livre
)

app = Flask(__name__)

app.secret_key = "bibliotheque-cle-de-developpement"

# =========================
# PAGE D'ACCUEIL
# =========================


@app.route("/")
def accueil():

    # Récupérer les données depuis MySQL
    livres = obtenir_livres()
    adherents = obtenir_adherents()
    emprunts = obtenir_emprunts()

    # Calculer les statistiques
    total_livres = len(livres)

    total_adherents = len(adherents)

    emprunts_en_cours = sum(
        1 for emprunt in emprunts
        if emprunt[6] == "En cours"
    )

    livres_disponibles = sum(
        1 for livre in livres
        if livre[4]
    )

    # Envoyer les statistiques au template
    return render_template(
        "accueil.html",
        total_livres=total_livres,
        total_adherents=total_adherents,
        emprunts_en_cours=emprunts_en_cours,
        livres_disponibles=livres_disponibles
    )



# =========================
# GESTION DES LIVRES
# =========================

@app.route("/livres")
def liste_livres():
    livres = obtenir_livres()
    return render_template("livres.html", livres=livres)




@app.route("/ajouter-livre", methods=["GET", "POST"])
def ajouter_livre_page():

    if request.method == "POST":

        titre = request.form["titre"].strip()
        auteur = request.form["auteur"].strip()
        annee = request.form["annee_publication"].strip()

        if not titre or not auteur:
            flash("Le titre et l'auteur sont obligatoires.", "danger")

        elif annee and not annee.isdigit():
            flash("L'année doit contenir uniquement des chiffres.", "danger")

        else:
            annee = int(annee) if annee else None

            succes, message = ajouter_livre(
                titre, auteur, annee
            )

            flash(message, "success" if succes else "danger")

            if succes:
                return redirect(url_for("liste_livres"))

        return redirect(url_for("ajouter_livre_page"))

    return render_template("ajouter_livre.html")





@app.route("/modifier-livre/<int:id_livre>", methods=["GET", "POST"])
def modifier_livre_page(id_livre):

    if request.method == "POST":

        titre = request.form["titre"].strip()
        auteur = request.form["auteur"].strip()
        annee = request.form["annee_publication"].strip()

        if not titre or not auteur:
            flash("Le titre et l'auteur sont obligatoires.", "danger")

        elif annee and not annee.isdigit():
            flash("L'année doit contenir uniquement des chiffres.", "danger")

        else:
            annee = int(annee) if annee else None

            succes, message = modifier_livre(
                id_livre, titre, auteur, annee
            )

            flash(message, "success" if succes else "danger")

            if succes:
                return redirect(url_for("liste_livres"))

        return redirect(url_for(
            "modifier_livre_page",
            id_livre=id_livre
        ))

    livres = obtenir_livres()

    livre = next(
        (l for l in livres if l[0] == id_livre),
        None
    )

    if livre is None:
        flash("Livre introuvable.", "danger")
        return redirect(url_for("liste_livres"))

    return render_template("modifier_livre.html", livre=livre)




@app.route("/supprimer-livre/<int:id_livre>", methods=["POST"])
def supprimer_livre_page(id_livre):

    succes, message = supprimer_livre(id_livre)

    flash(message, "success" if succes else "danger")

    return redirect(url_for("liste_livres"))


# =========================
# GESTION DES ADHERENTS
# =========================

@app.route("/adherents")
def liste_adherents():
    adherents = obtenir_adherents()
    return render_template("adherents.html", adherents=adherents)


@app.route("/ajouter-adherent", methods=["GET", "POST"])
def ajouter_adherent_page():

    if request.method == "POST":

        nom = request.form["nom"].strip()
        prenom = request.form["prenom"].strip()
        email = request.form["email"].strip()
        telephone = request.form["telephone"].strip()

        if not nom or not prenom:
            flash("Le nom et le prénom sont obligatoires.", "danger")

        elif not email or "@" not in email:
            flash("Veuillez saisir une adresse email valide.", "danger")

        else:
            succes, message = ajouter_adherent(
                nom, prenom, email, telephone
            )

            flash(message, "success" if succes else "danger")

            if succes:
                return redirect(url_for("liste_adherents"))

    return render_template("ajouter_adherent.html")


# Modifier un adhérent

# Modifier un adhérent
@app.route("/modifier-adherent/<int:id_adherent>", methods=["GET", "POST"])
def modifier_adherent_page(id_adherent):

    if request.method == "POST":

        nom = request.form["nom"].strip()
        prenom = request.form["prenom"].strip()
        email = request.form["email"].strip()
        telephone = request.form["telephone"].strip()

        if not nom or not prenom:
            flash("Le nom et le prénom sont obligatoires.", "danger")

        elif not email or "@" not in email:
            flash("Veuillez saisir une adresse email valide.", "danger")

        else:
            succes, message = modifier_adherent(
                id_adherent,
                nom,
                prenom,
                email,
                telephone
            )

            flash(message, "success" if succes else "danger")

            if succes:
                return redirect(url_for("liste_adherents"))

        return redirect(url_for(
            "modifier_adherent_page",
            id_adherent=id_adherent
        ))

    adherents = obtenir_adherents()

    adherent = next(
        (a for a in adherents if a[0] == id_adherent),
        None
    )

    if adherent is None:
        flash("Adhérent introuvable.", "danger")
        return redirect(url_for("liste_adherents"))

    return render_template(
        "modifier_adherent.html",
        adherent=adherent
    )


# Supprimer un adhérent

# Supprimer un adhérent
@app.route("/supprimer-adherent/<int:id_adherent>", methods=["POST"])
def supprimer_adherent_page(id_adherent):

    succes, message = supprimer_adherent(id_adherent)

    flash(message, "success" if succes else "danger")

    return redirect(url_for("liste_adherents"))



# =========================
# GESTION DES EMPRUNTS
# =========================

@app.route("/emprunts")
def liste_emprunts():
    emprunts = obtenir_emprunts()
    return render_template("emprunts.html", emprunts=emprunts)


# Ajouter un emprunt
@app.route("/ajouter-emprunt", methods=["GET", "POST"])
def ajouter_emprunt_page():

    if request.method == "POST":

        id_adherent = int(request.form["id_adherent"])
        id_livre = int(request.form["id_livre"])

        ajouter_emprunt(id_adherent, id_livre)

        return redirect(url_for("liste_emprunts"))

    adherents = obtenir_adherents()
    livres = obtenir_livres()

    return render_template(
        "ajouter_emprunt.html",
        adherents=adherents,
        livres=livres
    )


# Retourner un livre
@app.route("/retourner-livre/<int:id_emprunt>", methods=["POST"])
def retourner_livre_page(id_emprunt):
    retourner_livre(id_emprunt)
    return redirect(url_for("liste_emprunts"))


# =========================
# DEMARRER LE SERVEUR
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)