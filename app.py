from flask import Flask, render_template
from datetime import date
from db_defs import get_engine, create_db, get_session, Notiz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)  # Läuft standardmäßig auf localhost:5000