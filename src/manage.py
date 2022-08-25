from flask.cli import FlaskGroup
from flask import current_app as app
from project import db
# from project.models import User

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.session.drop_all()
    db.session.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
