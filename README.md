# 🤔 Vos README.md
## A la racine du projet : pour l'administrateur
- **Titre** du jeu
- **Description** courte du jeu
- **🎯 Contexte & cahier des charges** : développé dans le cadre d'une formation, pour un formateur pour monter en compétence en Python ...
- **🎲 Règles** du jeu : maquette, déroulé d'une partie, conditions de victoire
- **🎮 Use cases**:
    - pour l'administrateur : expliquer ce que peut/doit faire un administrateur qui souhaite lancer/administrer une arène de jeu avec des apprenants
    - pour le joueur : renvoyer vers README API
- **🖧 Architecture matériel** (optionnel, peut être décrit avec le diagramme de séquence) : schéma overview présentant les machines et protocoles (serveurs, clients, broker) avec texte expliquant le choix des technologies
- **📞 Diagramme de séquence**: expliquer le déroulé d'une partie, les principales étapes à faire dans l'ordre et qui/quoi/comment, les couches s'échangent quelles données pour qui/pour quoi
- **✅ Pré-requis**
    - matériel et logiciel requis pour executer votre projet, pour l'administrateur
    - pour les apprenants rediriger vers README API
- **⚙️ Installation** : step by step (commandes à executer par l'administrateur, paquets à installer ...)
- **🧪 Tests**:
    - définition du plan de test ce qu'on attend quand on fait quoi
    - step by step pour lancer les tests
- **🛣️ Roadmap**
- **🧑‍💻 Auteur**
- **⚖️ License**

## Dans le dossier API : pour les joueurs
- **Titre** du jeu
- **Description** courte du projet
- **🎲 Règles du jeu** : maquette, déroulé d'une partie, conditions de victoire
- **🎮 Use cases**: actions possibles du joueur via l'API
- **✅ Pré-requis** : matériel et logiciel requis pour executer votre projet
- **⚙️ Installation** : step by step (commandes à executer, paquets à installer ...)
- **🧑‍💻 Auteur**
- **⚖️ License**


# 📂 Arborescence projet Github
- votrejeu
    - doc
        - *.svg
    - src
        - api
            - j2l           -> *lib jusdeliens à récupérer sur tutos.jusdeliens.com*
            - votrejeu.py   -> *interface API de votre jeu côté client*
            - readme.md     -> *explique au joueur les actions possibles de l'api*
        - server
            - main.py       -> *logique backend implémentant les règles du jeu*
        - gui
            - ...
    - tests
        - api
            - test_votrejeu.py
        - server
            - test_main.py
        - gui
            - ...
    - readme.md             -> *inclus diagramme de conception du dossier doc*
