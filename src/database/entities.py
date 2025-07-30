# This file contains the entities used in the database.
# And also the functions for the entities
# It will be imported by other files in the database.


class Product:

    def __init__(self, sku, name, category, dimensions, weight):
        self.sku = sku
        self.name = name
        self.category = category
        self.dimensions = dimensions
        self.weight = weight

class Location:

    def __init__(self, block, zone, aisle, rack, shelf):
        self.block = block
        self.zone = zone
        self.aisle = aisle
        self.rack = rack
        self.shelf = shelf

class Inventory:
    product: Product
    location: Location
    quantity: int
    expiry: str

    def __init__(self, product, location, quantity, expiry):
        self.product = product
        self.location = location
        self.quantity = quantity
        self.expiry = expiry



    
