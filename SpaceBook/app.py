from flask import Flask
from flask_cors import CORS
from models.db import init_db
from controllers.user_controller import user_bp
from controllers.book_controller import book_bp

app = Flask(__name__)
CORS(app, supports_credentials=True)

# Inicializa o banco
init_db(app)

# Blueprints
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(book_bp, url_prefix='/api/books')

if __name__ == '__main__':
    app.run(debug=True)
