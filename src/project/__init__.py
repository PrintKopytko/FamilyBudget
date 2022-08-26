from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@postgres_db:5432/familybudget'

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from src.project.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from src.project.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from src.project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.app_context().push()

    # If db was not created, create it from model
    if not db.engine.table_names():
        db.create_all()
        db.session.commit()
    return app
