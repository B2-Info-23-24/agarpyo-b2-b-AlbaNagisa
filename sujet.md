# Projet Python - Agarpyo

## Objectif

Vous êtes missionnés pour recréer le célèbre jeu Agar.io en Python en mode solo en utilisant la librairie Pygame.

## Fonctionnalités

Pour ce projet, vous devrez implémenter les fonctionnalités suivantes :

#### Le joueur

**Si contrôlé par les touches du clavier**, il ne se déplacera que si vous utilisez les touches du clavier.
**Si contrôlé par la souris**, il se déplacera dès le lancement de la partie et suivra la direction vers la souris.

Le joueur sera un rond qui aura les attributs suivants :

- **Score** : qui augmentera de 1 à chaque boule mangée.
- **Vitesse** : vitesse de déplacement commençant à 100 qui augmentera de 5 à chaque boule mangée jusqu'à une limite de 500 de vitesse.
- **Taille** : rayon du rond commençant à 40 et qui augmentera de 2 à chaque boule mangée jusqu'à une limite de 200 de rayon.

Une fois que le joueur atteint la bordure de la map il est automatiquement téléporté dans la même direction de l'autre côté de la map.

#### La nourriture (la boule)

**N** boules apparaîtront de manière aléatoire sur la map. Les boules doivent être sous forme de rond mais doivent se différencier par un certain attribut (par exemple : la couleur) des joueurs et doivent avoir la même taille chacune.
Une fois mangée, c'est-à-dire dès que la bordure du joueur touche la bordure de la boule, alors celle-ci disparaitra et fera apparaître une nouvelle de manière aléatoire sur la map.

#### Les pièges

En fonction de la difficulté, un nombre **N** de pièges (des ronds de couleur différente que le joueur et que la nourriture) apparaîtront de manière aléatoire avec une taille aléatoire entre **40** et **150** qui représentera le rayon du piège.

**Si la taille du joueur est inférieure à la taille du piège**, alors le joueur pourra se cacher en dessous du piège et rien ne se passera.
**Si la taille du joueur est supérieure à la taille du piège**, alors le joueur se verra diviser sa taille et sa vitesse par le numéro correspondant à la difficulté sélectionnée. Le **piège**, quant à lui, disparaîtra et un nouveau piège apparaîtra de manière aléatoire sur la map. Un joueur est au contact d'un piège si la bordure des deux entités se touchent.

#### Choix de difficultés

- Facile : **2**. `2 pièges et 5 boules apparaîtront`
- Normal : **3**. `3 pièges et 3 boules apparaîtront`
- Difficile : **4**. `4 pièges et 2 boules apparaîtront`

## Interface Utilisateur

#### Menu de jeu

- **"Play with keyboard"** : En cliquant sur la touche **P** ou **p** du clavier, vous pourrez contrôler le joueur avec les touches du clavier "Z,Q,S,D".
- **"Play with mouse"** : En cliquant sur la **souris**, vous pourrez contrôler la direction du joueur avec votre souris.
- **"Quit"** : En cliquant sur la touche **Q** ou **q** du clavier, l'application se verra arrêtée.

- Un **radiobutton** ou **liste déroulante** qui permettra de sélectionner une difficulté parmi les 3 difficultés suivantes : Facile, Normal, Difficile.

#### Jeu

- Taille d'écran : 1280x720
- Un chronomètre doit être affiché sur l'écran de jeu. Ce chronomètre commence à un temps configuré (minimum **60s**) et défilera chaque seconde (la décrémentation doit être visible en instantané). Lorsque ce chronomètre aura atteint **0s**, la partie sera terminée et un écran apparaîtra avec le score affiché et un bouton **"Retour au menu principal"** qui renverra vers le menu principal et remettra à zéro toute la partie.
- En pleine partie, le bouton **Escape** ou **Echap** permet de retourner au menu principal ce qui remettra à zéro toute la partie.
- Le score, la vitesse, la taille, et la difficulté choisie doivent apparaître sur l'écran de jeu du joueur et mis à jour continuellement si ces valeurs viennent à changer pendant la partie.

## Black Track (facultatif comptant comme un bonus à hauteur de maximum +2 points sur la note finale sur 20 à l'appréciation du correcteur)

#### Interface Utilisateur

Le menu du jeu doit comporter des boutons qui changent légèrement de couleur au passage de la souris dessus. Il ne doit plus être possible de lancer la partie ou quitter l'application avec une touche du clavier mais seulement en cliquant sur ces boutons.

#### Scoreboard & Gamify

- Le joueur pourra entrer un nom pour sa partie.
- Les scores des joueurs doivent être sauvegardès dans un fichier CSV qui comportera les colonnes suivantes : Nom du joueur, Taille du joueur, Vitesse du joueur, Difficulté choisie, Score
- Ces scores doivent pouvoir être consultables depuis le menu du jeu avec un bouton **"Top 10"** qui affichera seulement les **10 premiers** triés par ordre décroissant du score (meilleur score en haut, dernier score en bas). S'il n'y a pas 10 joueurs dans le fichier CSV, il doit seulement afficher les joueurs présents ainsi que leurs statistiques classés par ordre décroissant du score (meilleur score en haut, dernier score en bas).

#### Customisation

- Le joueur pourra avoir un menu d'options en plein jeu (ou même avant de lancer la partie) et pourra customiser l'interface. Il pourra alors choisir la couleur (ou le skin) du joueur, des pièges, et de la nourriture. Il pourra changer la couleur de fond du jeu.

- Un audio pourra être intégré au jeu.

- Impressionnez-moi avec votre imagination.

## Contraintes

- Vous devez utiliser la librairie Pygame pour réaliser l'application.
- Tous les standards intégrés à Python sont autorisés.
- Toute autre librairie de Python n'est pas autorisée. Si une question, ou une interrogation à ce sujet ou sur comment faire ==> voir avec Jean-Philippe CAETANO.
- L'utilisation de l'IA et tout autre outil faisant recours à l'IA est strictement interdite. La documentation à l'aide des IA n'est également pas autorisée. Toute utilisation des IA entraînera un 0.
- Le projet devra être rendu sur le github classroom accompagné d'un **read.me** bien renseigné. Veillez à bien tester votre **read.me**. Si un projet n'est pas lançable à l'aide du read.me, il sera compté comme non valable. Vous aurez donc 0. De plus, le correcteur n'apportera aucune modification à votre code et aux librairies et leurs version (Pas de correction d'erreur, pas de modification de l'environnement à l'initiative du correcteur).
- Aucun rendu ne sera toléré **après le dimanche 11 février 2024 à 23h59** (date et heure du dernier push du projet).
- Utilisation de Python de façon native. Pas de framework.
- Le projet devra être réalisé de façon individuelle.
- Un travail sur la gestion des versions de l’application est attendu (commits travaillés, gestion des branches). Une pénalité peut être appliquée en cas de non-respect conséquent des normes de nommage et de Gitflow.
- Les conventions de code en Python doivent être respectées.
- Vous devrez faire le plus possible utilisation de la Programmation Orienté Objet.

## Ressources

- [PEP 8 - Convention de code en Python](https://peps.python.org/pep-0008/)
- [Pygame - Documentation officielle](https://www.pygame.org/docs/)
- [Python - Documentation officielle](https://docs.python.org/3/) (attention à bien lire la version que vous utilisez)
