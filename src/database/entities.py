# This file contains the entities used in the database.
# And also the functions for the entities
# It will be imported by other files in the database.
import csv
from pathlib import Path

base_path = Path(__file__).parent.parent.parent

class Product:

    def __init__(self, sku, name, category, dimensions, weight):
        self.sku = sku
        self.name = name
        self.category = category
        self.dimensions = dimensions
        self.weight = weight

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

        with open(base_path / "data" / "database" / "products.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


class Location:

    def __init__(self, block, zone, aisle, rack, shelf):
        self.block = block
        self.zone = zone
        self.aisle = aisle
        self.rack = rack
        self.shelf = shelf

    def add_location(self, block, zone, aisle, rack, shelf):
        self.block = block
        self.zone = zone
        self.aisle = aisle
        self.rack = rack
        self.shelf = shelf
        data = [
            [
                self.block,
                self.zone,
                self.aisle,
                self.rack,
                self.shelf,
            ]
        ]

        with open(base_path / "data" / "database" / "locations.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

class Inventory:

    def __init__(self, product, location, quantity, expiry):
        self.product = product
        self.location = location
        self.quantity = quantity
        self.expiry = expiry

    def add_stock(self, quantity):
        try:
            if quantity < 0:
                raise ValueError
            else:
                self.quantity += quantity
        except ValueError:
            raise ValueError("Quantity must be an integer")

        



    
