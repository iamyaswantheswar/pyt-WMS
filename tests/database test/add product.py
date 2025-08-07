import csv
from pathlib import Path

base_path = Path(__file__).parent.parent.parent

class Product:
    def add_product(self, sku, name, category, dimensions, weight):
        self.sku = sku
        self.name = name
        self.category = category
        self.dimensions = dimensions
        self.weight = weight
        data = [
            [
                self.sku,
                self.name,
                self.category,
                self.dimensions,
                self.weight,
            ]
        ]

        with open(base_path / "data" / "database"/ "products.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

add = Product()
add.add_product("123", "test", "test", "test", "test")