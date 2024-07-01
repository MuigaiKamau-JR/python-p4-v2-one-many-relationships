# server/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hire_date = db.Column(db.Date)

    # One-to-Many relationship with Review
    reviews = db.relationship("Review", backref="employee", lazy=True, cascade="all, delete-orphan")

    # One-to-One relationship with Onboarding
    onboarding = db.relationship("Onboarding", uselist=False, backref="employee", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}, {self.hire_date}>"

class Onboarding(db.Model):
    __tablename__ = "onboardings"

    id = db.Column(db.Integer, primary_key=True)
    orientation = db.Column(db.DateTime)
    forms_complete = db.Column(db.Boolean, default=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), unique=True, nullable=False)

    def __repr__(self):
        return f"<Onboarding {self.id}, {self.orientation}, {self.forms_complete}>"

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    summary = db.Column(db.String)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)

    def __repr__(self):
        return f"<Review {self.id}, {self.year}, {self.summary}>"
