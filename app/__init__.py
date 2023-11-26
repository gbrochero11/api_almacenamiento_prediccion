from app.config import DATABASE_CONNECTION_URI
from flask import Flask, jsonify
from flask_cors import CORS
from app.utils.db import db

app = Flask(__name__)
CORS(app,  origins="*", supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
# Configurando app
app.secret_key = 'secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db.init_app(app)
with app.app_context():
    db.create_all()

# Configurando/registrando rutas
from app.routes import usuarios_routes, datos_routes
app.register_blueprint(usuarios_routes.usuarios_blueprint)
app.register_blueprint(datos_routes.datos_blueprint)
