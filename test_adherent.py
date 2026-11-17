from services.adherent_service import ajouter_adherent

resultat = ajouter_adherent(
    "Test",
    "Utilisateur",
    "test.projet@gmail.com",
    "0600000000"
)

print(resultat)
