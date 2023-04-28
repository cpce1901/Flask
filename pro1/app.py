from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import *

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

# Importar los modelos de las aplicaciones
from apps.usuarios.models import User
from apps.api_lectura.models import Medidas, Equipo, Sensor


# Registro de las aplicaciones
from apps.usuarios.routes import usuarios_bp
from apps.sensores.routes import sensores_bp
from apps.dashboard.routes import dashboard_bp
from apps.reportes.routes import reportes_bp
from apps.api_lectura.routes import api_bp


app.register_blueprint(usuarios_bp)
app.register_blueprint(sensores_bp)
app.register_blueprint(reportes_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(api_bp)

