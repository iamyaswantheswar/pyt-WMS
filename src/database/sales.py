import datetime as dt
import csv
import shutil
from pathlib import Path

base_path = Path(__file__).parent.parent.parent

class Sale:
    def __init__(self, stock_id, quantity, status, date ='today'):
        self.sale_id = self.generate_sale_id()
        self.stock_id = stock_id
        self.quantity = quantity
        self.date = date
        self.status = status

        if date == 'today':
            self.date = dt.datetime.now().strftime('%Y-%m-%d')
        '''    
        with open(base_path / 'data' / 'database' / 'sales.csv', mode = 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                if row['sale_id'] == self.sale_id:
                    self.sale_id = row['id']
                    self.stock_id = row['stock_id']
                    self.quantity = row['quantity']
                    self.date = row['date']
                    self.status = row['status'] '''

    def generate_sale_id(self):
        return f"{self.stock_id}@{self.date}"

    def write_to_csv(self):
        self.backup_csv()
        with open(base_path / "data" / "database" / "sales.csv", mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                if row["sale_id"] == self.sale_id:
                    row["sale_id"] = self.id
                    row["stock_id"] = self.stock_id
                    row["quantity"] = self.quantity
                    row["status"] = self.status
                    row["date"] = self.date
                    with open(base_path / "data" / "database" / "sales.csv", mode='w', newline='') as file2:
                        writer = csv.DictWriter(file2, fieldnames=["sale_id", "stock_id", "quantity", "status", "date"])
                        writer.writeheader()
                        writer.writerows(rows)

    def backup_csv(self):
        file_path = base_path / "data" / "database" / "sales.csv"
        timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{file_path.stem}_{timestamp}.csv"
        shutil.copy2(file_path, f"{file_path.parent}/history/sales/{backup_name}")




