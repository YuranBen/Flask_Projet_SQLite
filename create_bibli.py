import sqlite3

# Connexion à la base de données (elle sera créée si elle n'existe pas)
conn = sqlite3.connect('bibliotheque.db')
cursor = conn.cursor()

# Création des tables
cursor.execute('''
DROP TABLE IF EXISTS livres;
CREATE TABLE livres (
    id_livres INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Titre TEXT NOT NULL,
    Auteur TEXT NOT NULL,
    Année TEXT NOT NULL,
    Quantite INTEGER NOT NULL
);


DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Nom TEXT NOT NULL,
    Prenom TEXT NOT NULL,
    Mdp TEXT NOT NULL,
    Mail TEXT NOT NULL,
    Roles TEXT NOT NULL
);

DROP TABLE IF EXISTS emprunts;
CREATE TABLE emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER NOT NULL,
    id_livres INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Date_emprunt TEXT NOT NULL,
    Date_rendu TEXT NOT NULL,
    Statut TEXT NOT NULL,
    FOREIGN KEY (id_livres) REFERENCES livres(id_livres),
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);
''')

# Fonction pour insérer un livre
def ajouter_livre(titre, auteur, annee, quantite):
    cursor.execute("""
    INSERT INTO livres (Titre, Auteur, Année, Quantité)
    VALUES (?, ?, ?, ?);
    """, (titre, auteur, annee, quantite))
    conn.commit()

# Fonction pour ajouter un utilisateur
def ajouter_utilisateur(nom, prenom, mdp, mail, roles):
    cursor.execute("""
    INSERT INTO users (Nom, Prenom, Mdp, Mail, Roles)
    VALUES (?, ?, ?, ?, ?);
    """, (nom, prenom, mdp, mail, roles))
    conn.commit()

# Fonction pour enregistrer un emprunt
def enregistrer_emprunt(id_user, id_livres, date_emprunt, date_rendu, statut):
    cursor.execute("""
    INSERT INTO emprunts (id_user, id_livres, Date_emprunt, Date_rendu, Statut)
    VALUES (?, ?, ?, ?, ?);
    """, (id_user, id_livres, date_emprunt, date_rendu, statut))
    conn.commit()

# Exemple d'ajout de livres et d'utilisateurs
ajouter_livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "1954", 5)
ajouter_utilisateur("Dupont", "Jean", "password123", "jean.dupont@mail.com", "admin")

# Exemple d'ajout d'un emprunt
enregistrer_emprunt(1, 1, "2025-01-23", "2025-02-23", "emprunté")

# Affichage des livres pour vérifier
cursor.execute("SELECT * FROM livres;")
livres = cursor.fetchall()
for livre in livres:
    print(livre)

# Fermer la connexion
conn.close()

