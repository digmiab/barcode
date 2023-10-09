from extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(50), unique=True, nullable=False)
    image_path = db.Column(db.String(200), nullable=False)
    info_text = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    product_name = db.Column(db.String, nullable=True)
