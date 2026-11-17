# Gestion de Bibliothèque

Application web de gestion d'une bibliothèque développée avec **Python, Flask et MariaDB**, conteneurisée avec **Docker et Docker Compose**.

## Présentation du projet

Ce projet consiste à développer une application web permettant de gérer les activités principales d'une bibliothèque à travers une interface simple et intuitive.

L'application permet de gérer les livres, les adhérents et les emprunts.

## Fonctionnalités

- **Gestion des livres :** ajout, consultation, modification et suppression.
- **Gestion des adhérents :** ajout, consultation, modification et suppression.
- **Gestion des emprunts :** création et suivi des emprunts.
- **Gestion de la base de données :** stockage des informations avec MariaDB.
- **Interface web :** navigation simple et organisée.

## Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python 3.13 | Langage de programmation |
| Flask | Framework web |
| MariaDB | Base de données |
| MySQL Connector | Connexion à la base de données |
| HTML / CSS / JavaScript | Interface utilisateur |
| Docker | Conteneurisation |
| Docker Compose | Orchestration des services |
| Git / GitHub | Gestion de versions |

## Architecture du projet

```text
gestion_bibliotheque/
│
├── database/
│   ├── __init__.py
│   └── connection.py
│
├── models/
│   ├── __init__.py
│   ├── livre.py
│   ├── adherent.py
│   └── emprunt.py
│
├── services/
│   ├── __init__.py
│   ├── livre_service.py
│   ├── adherent_service.py
│   └── emprunt_service.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│
├── test/
│
├── app.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── .env.example
```

## Installation et lancement

### 1. Cloner le projet

```bash
git clone https://github.com/imanemejahed03-svg/gestion-bibliotheque.git
cd gestion-bibliotheque
```

### 2. Configurer les variables d'environnement

Créer un fichier `.env` à partir de `.env.example` et renseigner les informations de connexion :

```env
MARIADB_ROOT_PASSWORD=your_root_password
MARIADB_DATABASE=gestion_bibliotheque
MARIADB_USER=library_user
MARIADB_PASSWORD=your_password
```

### 3. Construire et démarrer les conteneurs

```bash
docker compose build
docker compose up -d
```

### 4. Vérifier les conteneurs

```bash
docker compose ps
```

### 5. Accéder à l'application

Ouvrir le navigateur à l'adresse :

http://localhost:5000

## Configuration Docker

Le projet utilise deux services :

- **db :** conteneur MariaDB 10.4.32.
- **app :** conteneur Python exécutant l'application Flask.

Un volume Docker nommé `bibliotheque_data` assure la persistance des données de la base de données.

## Commandes Docker utiles

```bash
# Afficher les conteneurs
docker compose ps

# Consulter les logs
docker compose logs

# Consulter les logs de l'application
docker compose logs app

# Arrêter les conteneurs
docker compose stop

# Redémarrer les conteneurs
docker compose start
```

## Auteur

**Imane Mejahed**

Projet académique – Gestion de Bibliothèque.

---

*Développé avec Python, Flask, MariaDB et Docker.*