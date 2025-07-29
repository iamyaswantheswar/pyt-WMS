# This file contains the entities used in the database.
# And also the functions for the entities
# It will be imported by other files in the database.


class Product:
    sku: str
    name: str
    category: str
    dimensions: str
    weight: float

class Location:
    block: int
    zone: int
    aisle: int
    rack: int
    shelf: int

class Inventory:
    product: Product
    location: Location
    quantity: int


