# database_setup.py

from flask import Flask
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db.init_app(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(50), unique=True, nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    info_text = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
