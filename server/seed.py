#!/usr/bin/env python3
# server/seed.py

import datetime
from app import app, db
from models import Employee, Review, Onboarding

with app.app_context():
    # Delete all rows in tables
    Employee.query.delete()
    Review.query.delete()
    Onboarding.query.delete()

    # Add model instances to database
    uri = Employee(name="Uri Lee", hire_date=datetime.datetime(2022, 5, 17))
    tristan = Employee(name="Tristan Tal", hire_date=datetime.datetime(2020, 1, 30))

    # One-to-Many relationship
    uri.reviews = [
        Review(year=2023, summary="Great web developer!"),
    ]

    tristan.reviews = [
        Review(year=2021, summary="Good coding skills, often late to work"),
        Review(year=2022, summary="Strong coding skills, takes long lunches"),
        Review(year=2023, summary="Awesome coding skills, dedicated worker"),
    ]

    # One-to-One relationship
    uri.onboarding = Onboarding(orientation=datetime.datetime(2023, 3, 27))
    tristan.onboarding = Onboarding(
        orientation=datetime.datetime(2020, 1, 20, 14, 30), forms_complete=True
    )

    db.session.add_all([uri, tristan])
    db.session.commit()
