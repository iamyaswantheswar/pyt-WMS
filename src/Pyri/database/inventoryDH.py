import csv
import shutil
import datetime
from pathlib import Path

from src.Pyri.page_elements.inventory import inventory_elements

base_path = Path(__file__).parent.parent.parent.parent

inventory_path = base_path / 'data' / 'database' / 'inventory.csv'

def generate_location_id(block, zone, aisle, rack, shelf):
    location_id = f"{block}-{zone}-{aisle}-{rack}-{shelf}"
    return location_id

def search_product_name(query):
    with open(base_path / 'data' / 'database' / 'purchases.csv', mode='r', newline='') as file, open(base_path / 'data' / 'database' / 'temp_memory' / 'search.csv', mode='a', newline='') as search_file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(search_file, fieldnames=fieldnames)
        for row in reader:
            if query.lower() in row["Product name"].lower():
                writer.writerow(row)
    return None

class Product:

    def __init__(self, product_id, product_name='', quantity=0, unit_cost_price=0, unit_sale_price=0, stock_value=0,
                 location='', expiry_date='', new=False):
        # give only product_id if you want to fetch the product details from the database
        # give all the details if you want to create a new product and set new = True
        self.product_id = product_id
        self.inventory_path = inventory_path
        if not new:
            with open(self.inventory_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["id"] == self.product_id:
                        self.product_id = row["Product id"]
                        self.product_name = row["Product name"]
                        self.quantity = int(row["Quantity"])
                        self.u_cost_price = float(row["Unit Cost price"])
                        self.u_sale_price = float(row["Unit Sale price"])
                        self.stock_value = float(row["Stock value"])
                        self.location = row["Location"]
                        self.expiry_date = row["Expiry Date"]
                        break

        elif new:
            self.new_product(product_id, product_name, quantity, unit_cost_price, unit_sale_price, stock_value,
                             location, expiry_date)

        else:
            raise ValueError(f"Purchase with ID {self.product_id} not found.")

    def backup_csv(self):
        # backup the products.csv file to history folder with timestamp in the name
        file_path = self.inventory_path
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{file_path.stem}_{timestamp}.csv"
        shutil.copy2(file_path, f"{file_path.parent}/history/products/{backup_name}")

    def new_product(self, product_id, product_name, quantity, unit_cost_price, unit_sale_price, stock_value,
                             location, expiry_date):

        def error_check():
            try:
                if int(quantity) < 0:
                    raise ValueError("Quantity cannot be negative")
                if float(unit_cost_price) < 0:
                    raise ValueError("Unit cost price cannot be negative")
                if float(unit_sale_price) < 0:
                    raise ValueError("Unit sale price cannot be negative")
                if float(stock_value) < 0:
                    raise ValueError("Stock value cannot be negative")
            except ValueError as e:
                raise ValueError(e)

        error_check()

        data = [
            [
             product_id,
             product_name,
             quantity,
             unit_cost_price,
             unit_sale_price,
             stock_value,
             location,
             expiry_date
            ]
        ]

        self.backup_csv()

        with open(self.inventory_path, 'a', newline='') as file:
            writer = csv.DictWriter(file)
            writer.writerows(data)

    def update_quantity(self, quantity, WriteToCSV=False):
        self.quantity_in_stock += quantity
        if WriteToCSV:
            self.write_to_csv()

    def update_price(self, price, WriteToCSV=False):
        self.price = price
        if WriteToCSV:
            self.write_to_csv()

    '''
    def generate_stock_id(self, loc):
        return f"{self.id}@{loc}"
    '''

    def update_location(self, location, WriteToCSV=False):
        self.locations = location
        if WriteToCSV:
            self.write_to_csv()

    def write_to_csv(self):
        self.backup_csv()
        with open(self.inventory_path, mode='r', newline='') as file:
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
                    with open(self.inventory_path, mode='w', newline='') as file2:
                        writer = csv.DictWriter(file2, fieldnames=["id", "name", "category", "dimensions", "weight",
                                                                   "quantity_in_stock", "price", "locations"])
                        writer.writeheader()
                        writer.writerows(rows)



'''
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

    def increase_stock(self, quantity, WriteToCSV=False):
        try:
            if quantity < 0:
                raise ValueError
            else:
                self.quantity += quantity
                if WriteToCSV:
                    self.write_to_csv()
                    self.product.update_quantity(quantity, WriteToCSV=WriteToCSV)
        except ValueError:
            raise ValueError("Quantity must be a positive integer")

    def decrease_stock(self, quantity, WriteToCSV=False):
        try:
            if quantity < 0:
                raise ValueError
            else:
                self.quantity -= quantity
                if WriteToCSV:
                    self.write_to_csv()
                    self.product.update_quantity(-quantity, WriteToCSV=WriteToCSV)
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
                    with open(base_path / "data" / "database" / "stock.csv", mode='w', newline='') as file2:
                        writer = csv.DictWriter(file2,
                                                fieldnames=["stock_id", "location", "product", "quantity", "expiry"])
                        writer.writeheader()
                        writer.writerows(rows)
'''