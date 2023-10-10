# populate_db.py

import csv
from database_setup import app, db, Product

def populate_from_csv(csv_path):
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            barcode, image_path, info_text, price = row
            product = product(barcode=barcode, image_path=image_path, info_text=info_text, price=float(price))
            db.session.add(product)

        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        populate_from_csv('products.csv')
