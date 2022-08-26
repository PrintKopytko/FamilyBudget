from src.project import db
from flask_login import UserMixin

association_table = db.Table(
    "association",
    db.Model.metadata,
    db.Column("user_id", db.ForeignKey("user.id"), primary_key=True),
    db.Column("budget_id", db.ForeignKey("budget.id"), primary_key=True),
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    owned_budget = db.relationship("Budget", back_populates="user", uselist=False)
    shared_budgets = db.relationship(
        "Budget", secondary=association_table, back_populates="users_with_access"
    )


class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    owner = db.Column(db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", back_populates="owned_budget")
    users_with_access = db.relationship(
        "User", secondary=association_table, back_populates="shared_budgets"
    )
