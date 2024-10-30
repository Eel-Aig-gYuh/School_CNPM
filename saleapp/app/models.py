from sqlalchemy import Column, Integer, String
from flask import SQLAlchemy
from app import app, db


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    produts = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
