from flask import Flask
from flask_migrate import Migrate

from packrat0.models import db
from packrat0.routes import api_blueprint

app = Flask(__name__)
app.config.from_pyfile('secrets.py')

app.register_blueprint(api_blueprint)
db.init_app(app)

migrate = Migrate(app, db)
