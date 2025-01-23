from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)
# Configurez la base de données SQLite (vous pouvez utiliser PostgreSQL ou MySQL selon vos besoins)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle pour un livre
class Livre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100), nullable=False)
    auteur = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    date_publication = db.Column(db.String(10), nullable=False)
    exemplaires = db.Column(db.Integer, default=1)

# Créer la base de données si elle n'existe pas déjà
with app.app_context():
    db.create_all()

@app.route('/bookstore')
def index():
    livres = Livre.query.all()
    return render_template('index.html', livres=livres)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        genre = request.form['genre']
        date_publication = request.form['date_publication']
        exemplaires = request.form['exemplaires']

        nouveau_livre = Livre(titre=titre, auteur=auteur, genre=genre,
                              date_publication=date_publication, exemplaires=exemplaires)
        db.session.add(nouveau_livre)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_book.html')

@app.route('/search_books', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        query = request.form['query']
        livres = Livre.query.filter(Livre.titre.like(f'%{query}%') | Livre.auteur.like(f'%{query}%')).all()
        return render_template('index.html', livres=livres)

    return render_template('search_books.html')

if __name__ == "__main__":
    app.run(debug=True)
