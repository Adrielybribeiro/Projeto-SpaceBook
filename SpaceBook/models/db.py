import mysql.connector
from flask import g
from config import DB_CONFIG

def init_db(app):
    @app.before_request
    def before_request():
        g.db = mysql.connector.connect(**DB_CONFIG)
        g.cursor = g.db.cursor()

    @app.teardown_request
    def teardown_request(exception):
        db = getattr(g, 'db', None)
        if db is not None:
            db.close()
