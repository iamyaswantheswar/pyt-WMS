import csv
import datetime
from datetime import datetime
from pathlib import Path

base_path = Path(__file__).parent.parent.parent.parent

inventory_path = base_path / 'data' / 'database' / 'inventory.csv'

temp_inventory_path = base_path / 'data' / 'database' / 'temp_memory'

display_csv_path = temp_inventory_path / 'display_inventory.csv'


def generate_location_id(block, zone, aisle, rack, shelf):
    location_id = f"{block}{zone}{aisle}{rack}{shelf}"
    return location_id

class Inventory:

    def search_product_name(self, query, by_what):
        output = None
        if by_what == "Product Name":
            by = "Product name"
        if by_what == "Product ID":
            by = "Product id"
        if by_what == "Vendor ID":
            by = "Vendor id"
        with open(display_csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            to_write = []
            for row in reader:
                if str(query).lower() in row[by].lower():
                    to_write.append(row)
            if to_write == []:
                output = False
            with open(display_csv_path, mode='w', newline='') as search_file:
                writer = csv.DictWriter(search_file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(to_write)
        if not output:
            return False
        else:
            with open(display_csv_path, mode='r', newline='') as search_file:
                reader = csv.reader(search_file)
                return list(reader)

    #Opens the inventory csv file and copies it to display_inventory.csv (this is the csv that is displayed in the inventory window)
    def open_inventory_csv(self):
        with open(inventory_path, mode='r', newline='') as file, open(display_csv_path, mode='w', newline='') as display_file:
            reader = csv.DictReader(file)
            writer = csv.DictWriter(display_file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(reader)
        with open(display_csv_path, newline="") as f:
            reader = csv.reader(f)
            return list(reader)

    def filter_inventory_location(self,block,zone,aisle,rack,shelf):
        location_id = generate_location_id(block,zone,aisle,rack,shelf)

        with open(display_csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            to_write = []
            for row in rows:
                location_str = str(row["Location"])
                index = 0
                for char in location_id:
                    if char.isdigit():
                        index += 1
                        continue
                    else:
                        break
                if row["Location"][:index] == location_id[:index]:
                    to_write.append(row)
            with open(display_csv_path, mode='w', newline='') as filter_file:
                writer = csv.DictWriter(filter_file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(to_write)

        with open(display_csv_path, mode='r', newline='') as filter_file:
            reader = csv.reader(filter_file)
            return list(reader)

    def filter_inventory_expiry_date(self, start_date, end_date):
        start = datetime.strptime(start_date, "%d-%m-%Y")
        end = datetime.strptime(end_date, "%d-%m-%Y")

        with open(display_csv_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            filtered = []
            for row in rows:
                if start <= datetime.strptime(row['Expiry Date'], "%d-%m-%Y") <= end:
                    filtered.append(row)
            with open(display_csv_path, mode='w', newline='') as filter_file:
                writer = csv.DictWriter(filter_file, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(filtered)
        with open(display_csv_path, mode='r', newline='') as filter_file:
            reader = csv.reader(filter_file)
            return list(reader)

    def sort_inventory(self, sort_by, sort_type):
        if sort_by == "Expiry Date":
            with open(display_csv_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                if sort_type == "Ascending":
                    sort_type_bool = False
                else:
                    sort_type_bool = True
                sorted_rows = sorted(rows, key=lambda x: datetime.strptime(x['Expiry Date'], "%d-%m-%Y"), reverse=sort_type_bool)
                with open(display_csv_path, mode='w', newline='') as sort_file:
                    writer = csv.DictWriter(sort_file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(sorted_rows)

        else:
            with open(display_csv_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                if sort_type == "Ascending":
                    sort_type_bool = False
                else:
                    sort_type_bool = True
                if sort_by == "Product Name":
                    sort_by = "Product name"
                sorted_rows = sorted(rows, key=lambda x: x[sort_by], reverse=sort_type_bool)
                with open(display_csv_path, mode='w', newline='') as sort_file:
                    writer = csv.DictWriter(sort_file, fieldnames=reader.fieldnames)
                    writer.writeheader()
                    writer.writerows(sorted_rows)

        with open(display_csv_path, mode='r', newline='') as sort_file:
            reader = csv.reader(sort_file)
            return list(reader)


