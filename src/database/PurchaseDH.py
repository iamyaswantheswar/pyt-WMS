base_path = Path(__file__).parent.parent.parent
import datetime
import csv
import shutil
from pathlib import Path
class PurchasesDataHandler:
    def write_data_purchases(self,Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate,purchaseid):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        with open(self.purchases_csv_filepath,"a+",newline="") as f:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            for row in rows:
                row["Product id"] = Product_id
                row['Product name'] = Product_name
                row["Quantity"] = Quantity
                row['Unit price'] = cost
                row[]

        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        with open(self.purchaseslog_filepath,"a+",newline="") as f:
            writer=csv.writer(f)
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            writer.writerow([Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate,self.current_date,purchaseid])
            self.add_product_window.destroy()
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        with open(self.inventory_csv_filepath,"a+",newline="")as f:
            writer=csv.writer(f)
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            writer.writerow([Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate])