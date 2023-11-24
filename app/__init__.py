from app.config import DATABASE_CONNECTION_URI
from flask import Flask, jsonify

app = Flask(__name__)

# Configurando app
app.secret_key = 'secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Configurando/registrando rutas
from app.routes import usuarios_routes
app.register_blueprint(usuarios_routes.usuarios_blueprint)
