# tests/factories.py

from factory import Factory, Faker
from yourapp.models import Product

class ProductFactory(Factory):
    class Meta:
        model = Product

    name = Faker('name')
    price = Faker('random_number', digits=2)
    # Add other fields as needed for your Product model
