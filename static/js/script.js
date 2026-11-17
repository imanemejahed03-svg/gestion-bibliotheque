
document.addEventListener("DOMContentLoaded", function () {

    // =====================================
    // 1. ANIMATION DES CARTES
    // =====================================

    const cards = document.querySelectorAll(
        ".stat-card, .action-card"
    );

    cards.forEach((card, index) => {

        card.animate(
            [
                {
                    opacity: 0,
                    transform: "translateY(15px)"
                },
                {
                    opacity: 1,
                    transform: "translateY(0)"
                }
            ],
            {
                duration: 500,
                delay: index * 100,
                easing: "ease-out",
                fill: "both"
            }
        );

    });


    // =====================================
    // 2. DISPARITION AUTOMATIQUE DES MESSAGES
    // =====================================

    const messages = document.querySelectorAll(".message");

    messages.forEach((message) => {

        setTimeout(() => {

            const animation = message.animate(
                [
                    { opacity: 1, transform: "translateY(0)" },
                    { opacity: 0, transform: "translateY(-10px)" }
                ],
                {
                    duration: 400,
                    easing: "ease-in",
                    fill: "forwards"
                }
            );

            animation.onfinish = () => message.remove();

        }, 4000);

    });


    // =====================================
    // 3. CONFIRMATION DE SUPPRESSION
    // =====================================

    document.addEventListener("click", function (event) {

        const deleteLink = event.target.closest(
            'a[href*="supprimer"]'
        );

        if (!deleteLink) return;

        const confirmation = confirm(
            "Voulez-vous vraiment supprimer cet élément ?"
        );

        if (!confirmation) {
            event.preventDefault();
        }

    });


    // =====================================
    // 4. CONFIRMATION DES FORMULAIRES
    // =====================================

    const forms = document.querySelectorAll("form[data-confirm]");

    forms.forEach((form) => {

        form.addEventListener("submit", function (event) {

            const confirmation = confirm(
                form.dataset.confirm
            );

            if (!confirmation) {
                event.preventDefault();
            }

        });

    });


    // =====================================
    // 5. RECHERCHE INSTANTANEE DES LIVRES
    // =====================================

    const searchLivres = document.getElementById("searchLivres");

    if (searchLivres) {

        searchLivres.addEventListener("input", function () {

            const recherche = this.value.toLowerCase().trim();

            const lignes = document.querySelectorAll(
                "table tbody tr"
            );

            lignes.forEach((ligne) => {

                const contenu = ligne.textContent.toLowerCase();

                ligne.style.display =
                    contenu.includes(recherche) ? "" : "none";

            });

        });

    }


    // =====================================
    // 6. EFFET SUR LES LIENS DE NAVIGATION
    // =====================================

    const links = document.querySelectorAll(".nav-link");

    links.forEach((link) => {

        link.addEventListener("mouseenter", function () {
            this.style.transition = "all 0.25s ease";
        });

    });

});

    // =====================================
    // 7. RECHERCHE INSTANTANEE DES ADHERENTS
    // =====================================

    const searchAdherents = document.getElementById("searchAdherents");

    if (searchAdherents) {

        searchAdherents.addEventListener("input", function () {

            const recherche = this.value.toLowerCase().trim();

            const lignes = document.querySelectorAll(
                "#adherentsTable tbody tr.adherent-row"
            );

            const messageVide = document.getElementById(
                "noAdherentResult"
            );

            let resultatTrouve = false;

            lignes.forEach((ligne) => {

                const contenu = Array.from(ligne.cells)
                    .slice(0, -1)
                    .map(cellule => cellule.textContent)
                    .join(" ")
                    .toLowerCase();

                if (contenu.includes(recherche)) {

                    ligne.style.display = "";
                    resultatTrouve = true;

                } else {

                    ligne.style.display = "none";

                }

            });

            if (messageVide) {
                messageVide.style.display =
                    resultatTrouve ? "none" : "";
            }

        });

    }


    // =====================================
    // 8. RECHERCHE INSTANTANEE DES EMPRUNTS
    // =====================================

    const searchEmprunts = document.getElementById("searchEmprunts");

    if (searchEmprunts) {

        searchEmprunts.addEventListener("input", function () {

            const recherche = this.value.toLowerCase().trim();

            const lignes = document.querySelectorAll(
                "#empruntsTable tbody tr.emprunt-row"
            );

            const messageVide = document.getElementById(
                "noEmpruntResult"
            );

            let resultatTrouve = false;

            lignes.forEach((ligne) => {

                const contenu = Array.from(ligne.cells)
                    .slice(0, -1)
                    .map(cellule => cellule.textContent)
                    .join(" ")
                    .toLowerCase();

                if (contenu.includes(recherche)) {

                    ligne.style.display = "";
                    resultatTrouve = true;

                } else {

                    ligne.style.display = "none";

                }

            });

            if (messageVide) {
                messageVide.style.display =
                    resultatTrouve ? "none" : "";
            }

        });

    }

// Validation du formulaire adhérent

const formAdherent = document.getElementById("formAdherent");

if (formAdherent) {

    formAdherent.addEventListener("submit", function(event) {

        let valide = true;

        const nom = document.getElementById("nom");
        const prenom = document.getElementById("prenom");
        const email = document.getElementById("email");

        document.querySelectorAll(".field-error").forEach(function(error) {
            error.textContent = "";
        });

        if (nom.value.trim() === "") {
            document.getElementById("nomError").textContent =
                "Le nom est obligatoire.";
            valide = false;
        }

        if (prenom.value.trim() === "") {
            document.getElementById("prenomError").textContent =
                "Le prénom est obligatoire.";
            valide = false;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailRegex.test(email.value.trim())) {
            document.getElementById("emailError").textContent =
                "Veuillez saisir une adresse email valide.";
            valide = false;
        }

        if (!valide) {
            event.preventDefault();
        }

    });

}

const formLivre = document.getElementById("formLivre");

if (formLivre) {

    formLivre.addEventListener("submit", function(event) {

        let valide = true;

        const titre = document.getElementById("titre");
        const auteur = document.getElementById("auteur");
        const annee = document.getElementById("annee_publication");

        document.querySelectorAll(".field-error").forEach(error => {
            error.textContent = "";
        });

        if (titre.value.trim() === "") {
            document.getElementById("titreError").textContent =
                "Le titre est obligatoire.";
            valide = false;
        }

        if (auteur.value.trim() === "") {
            document.getElementById("auteurError").textContent =
                "Le nom de l'auteur est obligatoire.";
            valide = false;
        }

        if (annee.value !== "") {
            const anneeActuelle = new Date().getFullYear();

            if (Number(annee.value) < 1 ||
                Number(annee.value) > anneeActuelle) {

                document.getElementById("anneeError").textContent =
                    "Veuillez saisir une année valide.";

                valide = false;
            }
        }

        if (!valide) {
            event.preventDefault();
        }

    });

}
