# type: ignore
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Box(db.Model):
    __tablename__ = 'box'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

class BoxImage(db.Model):
    __tablename__ = 'box_image'

    box_id = db.Column(db.Integer, db.ForeignKey('box.id'), primary_key=True, nullable=False)
    path = db.Column(db.Text, primary_key=True, nullable=False)
    box = db.relationship('Box', backref=db.backref('images', lazy=False))
