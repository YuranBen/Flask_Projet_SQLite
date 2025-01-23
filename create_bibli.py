import sqlite3

def init_db():
    connection = sqlite3.connect('database.db')

    with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

    print("Base de données initialisée avec succès.")

if __name__ == "__main__":
    init_db()
    
connection.commit()
connection.close()
