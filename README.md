# Labyrinth Backend API (FastAPI)

## Objectif

Ce projet a pour but de créer une **API REST** avec **FastAPI** permettant de gérer le déplacement d’un joueur dans un **labyrinthe virtuel**.  
Elle permet :
- D’**initialiser une partie**.
- De **découvrir la carte du labyrinthe**.
- De **déplacer le joueur**.
- De **communiquer avec un backend distant** via des requêtes HTTP.

Ce projet constitue une base solide pour tout backend FastAPI containerisé avec **Docker** et **Docker Compose**.

---
## Prérequis

Avant de lancer le projet, assurez-vous d’avoir installé sur votre machine :
- **Python 3.11+**
- **Docker** et **Docker Compose**
- **Git**
---

## ⚙Fonctionnalités principales

| Endpoint | Méthode | Description |
|-----------|----------|-------------|
| `/` | `GET` | Message de bienvenue et liens vers la documentation |
| `/start` | `POST` | Lancer une nouvelle partie |
| `/map` | `GET` | Découvrir la carte du labyrinthe |
| `/move` | `POST` | Déplacer le joueur sur la carte |

---

## Étapes de lancement

### 1️- Cloner le dépôt
```
git clone https://github.com/soniarimamy/labyrinthe_backend.git
```

### 2️ - Se déplacer dans le dossier du projet
```
cd labyrinthe_backend
```

### 3️- Lancer l’application avec Docker
```
docker-compose up --build -d
```
Une fois le conteneur lancé, l’API sera accessible à l’adresse :
 http://127.0.0.1:8000

Documentation interactive :
- Swagger UI → http://127.0.0.1:8000/docs
- Redoc → http://127.0.0.1:8000/redoc

## Test des fonctionnalités avec curl
### 1. Démarrer une partie
```
curl -X POST http://127.0.0.1:8000/start \
-H "Content-Type: application/json" \
-d '{
  "player": "Rochel"
}'
```

### 2. Découvrir la carte
```
curl -X GET http://127.0.0.1:8000/map \
-H "accept: application/json"
```

###  3. Déplacer le joueur
```
curl -X POST http://127.0.0.1:8000/move \
-H "Content-Type: application/json" \
-d '{
  "position_x": 2,
  "position_y": 3
}'
```

### Exemple de réponse attendue :
```
{
  "status": "success",
  "msg": "player is moved successfully",
  "data": {
    "new_position": [2, 3],
    "message": "Player moved!"
  }
}
```

## Docker Hub
L’image Docker officielle du projet est disponible sur Docker Hub :
```
docker pull rochel05/labyrinth_backend_api:latest
```
Vous pouvez l’utiliser directement sans builder localement.

## Architecture du projet
```
labyrinthe_backend/
├── docker-compose.yml
├── Dockerfile
├── helpers/
│   ├── Game.py
│   └── __init__.py
├── ressources/
│   └── Game.py
├── routers/
│   └── Game.py
├── schemas/
│   └── Game.py
├── main.py
├── requirements.txt
├── LICENSE
├── player.txt
└── README.md
```

## Licence
Ce projet est distribué sous la licence MIT.
Vous êtes libre de l’utiliser, le modifier et le redistribuer, à condition de mentionner l’auteur original.

## Auteur
- Nom : Rochel Soniarimamy
- Email : rochel.soniarimamy@gmail.com
- Docker Hub : https://hub.docker.com/repositories/rochel05
- GitHub : https://github.com/soniarimamy/

## Contact
Pour toute question, suggestion ou contribution, contactez-moi :
- Email : rochel.soniarimamy@gmail.com
- Téléphone : +261 34 92 516 46
