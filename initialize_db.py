from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, Sequence('product_id_seq'), primary_key=True)
    barcode = Column(String(50), unique=True, nullable=False)
    image_path = Column(String(255), nullable=True)

DATABASE_URL = 'postgresql://qemyaybxfcyrku:092be4797a5824a0f069f8fb98ff7ed47ea0b433c051228f8e41a31ca5b9bc93@ec2-99-80-190-165.eu-west-1.compute.amazonaws.com:5432/d9vajhkjedec12'
engine = create_engine(DATABASE_URL)

# Create the tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example: Insert a sample product into the database
sample_product = Product(barcode='050151578451', image_path='https://th.bing.com/th?id=ORMS.21147cfe368718e7b97801b0d40b6740&pid=Wdp&w=300&h=156&qlt=90&c=1&rs=1&dpr=1&p=0')
session.add(sample_product)
session.commit()

print("Database initialized and sample product added.")
