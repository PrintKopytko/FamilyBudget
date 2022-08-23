from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)


def create_app():
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@postgres_db:5432/familybudget'

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
