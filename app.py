from flask import Flask, render_template
from datetime import date
from db_defs import get_engine, create_db, get_session, Notiz
from Note import *

app = Flask(__name__)

engine = get_engine()         # Datenbank-Engine erstellen (Datei Database.db)
create_db(engine)             # Tabellen erstellen, falls nicht vorhanden
session = get_session(engine) #
app.register_blueprint(note_api)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Läuft standardmäßig auf localhost:5000