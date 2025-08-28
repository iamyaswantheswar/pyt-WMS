# This file contains the entities used in the database.
# And also the functions for the entities
# It will be imported by other files in the database.
import csv
import shutil
import datetime
import os
from pathlib import Path

base_path = Path(__file__).parent.parent.parent

def generate_location_id( block, zone, aisle, rack, shelf):
    location_id = f"{block}-{zone}-{aisle}-{rack}-{shelf}"
    return location_id

class Product:

    def __init__(self, id, name = '', category = [], price = 0, dimensions = '', weight = 0, quantity_in_stock = 0, locations = [], new = False):
        self.id = id
        self.name = name
        self.category = category
        self.dimensions = dimensions
        self.weight = weight
        self.quantity_in_stock = quantity_in_stock
        self.price = price
        self.locations = locations

        with open(base_path / 'data' / 'database' / 'purchases.csv', mode = 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                if row["id"] == self.id:
                    self.id = row["id"]
                    self.name = row["name"]
                    self.category = row["category"]
                    self.dimensions = row["dimensions"]
                    self.weight = row["weight"]
                    self.quantity_in_stock = row["quantity_in_stock"]
                    self.price = row["price"]
                    self.locations = row["locations"]

        if new:
            self.new_product()

    def backup_csv(self):
        file_path = base_path / "data" / "database" / "products.csv"
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{file_path.stem}_{timestamp}.csv"
        shutil.copy2(file_path, f"{file_path.parent}/history/products/{backup_name}")

    def new_product(self):
        data = [
            [
                self.id,
                self.name,
                self.category,
                self.dimensions,
                self.weight,
                self.quantity_in_stock,
                self.price,
                self.locations
            ]
        ]

        self.backup_csv()

        with open(base_path / "data" / "database" / "products.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def update_quantity(self, quantity, WriteToCSV = False):
        self.quantity_in_stock += quantity
        if WriteToCSV:
            self.write_to_csv()

    def update_price(self, price, WriteToCSV = False):
        self.price = price
        if WriteToCSV:
            self.write_to_csv()

    def generate_stock_id(self,loc):
        return f"{self.id}@{loc}"

    def update_location(self, location, WriteToCSV = False):
        self.locations = location
        if WriteToCSV:
            self.write_to_csv()

    def write_to_csv(self):
        self.backup_csv()
        with open(base_path / "data" / "database" / "products.csv", mode = 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                if row["id"] == self.id:
                    row["id"] = self.id
                    row["name"] = self.name
                    row["category"] = self.category
                    row["dimensions"] = self.dimensions
                    row["weight"] = self.weight
                    row["quantity_in_stock"] = self.quantity_in_stock
                    row["price"] = self.price
                    row["locations"] = self.locations
                    with open(base_path / "data" / "database" / "products.csv", mode = 'w', newline='') as file2:
                        writer = csv.DictWriter(file2, fieldnames = ["id", "name", "category", "dimensions", "weight", "quantity_in_stock", "price", "locations"])
                        writer.writeheader()
                        writer.writerows(rows)

class Stock:

    def __init__(self, stock_id, location, product, quantity, expiry):
        self.stock_id = stock_id
        self.product = product
        self.location = location
        self.quantity = quantity
        self.expiry = expiry

    def backup_csv(self):
        file_path = base_path / "data" / "database" / "stock.csv"
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{file_path.stem}_{timestamp}.csv"
        shutil.copy2(file_path, f"{file_path.parent}/history/stock/{backup_name}")

    def increase_stock(self, quantity, WriteToCSV = False):
        try:
            if quantity < 0:
                raise ValueError
            else:
                self.quantity += quantity
                if WriteToCSV:
                    self.write_to_csv()
                    self.product.update_quantity(quantity, WriteToCSV = WriteToCSV)
        except ValueError:
            raise ValueError("Quantity must be a positive integer")

    def decrease_stock(self, quantity, WriteToCSV = False):
        try:
            if quantity < 0:
                raise ValueError
            else:
                self.quantity -= quantity
                if WriteToCSV:
                    self.write_to_csv()
                    self.product.update_quantity(-quantity, WriteToCSV = WriteToCSV)
        except ValueError:
            raise ValueError("Quantity must be a positive integer")

    def write_to_csv(self):
        self.backup_csv()
        with open(base_path / "data" / "database" / "stock.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                if row["stock_id"] == self.stock_id:
                    row["stock_id"] = self.stock_id
                    row["location"] = self.location
                    row["product"] = self.product
                    row["quantity"] = self.quantity
                    row["expiry"] = self.expiry
                    with open(base_path / "data" / "database" / "stock.csv", mode = 'w', newline='') as file2:
                        writer = csv.DictWriter(file2, fieldnames = ["stock_id", "location", "product", "quantity", "expiry"])
                        writer.writeheader()
                        writer.writerows(rows)




        



    
