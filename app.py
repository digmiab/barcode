from flask import Flask, request, render_template
from extensions import db
from models import Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables(app):
    with app.app_context():
        db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    product = None
    if request.method == 'POST':
        barcode = request.form.get('barcode').strip()
        print(f"Processed Barcode: '{barcode}'")  
        try:
            product = Product.query.filter_by(barcode=barcode).first()
            print(product)  
        except Exception as e:
            print(f"Error during query: {e}")
        
        if product:
            print("Product Name:", product.product_name)  
            print("Image_path:", product.image_path)  
        else:
            print("No product found with the given barcode.")
    return render_template('index.html', product=product)

if __name__ == '__main__':
    create_tables(app)  
    app.run(debug=True)  # Set debug=True for development to automatically apply changes and provide detailed errors
