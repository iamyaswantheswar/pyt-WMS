from datetime import datetime
import csv
import shutil
from pathlib import Path
base_path = Path(__file__).parent.parent.parent.parent

class DemandDataHandler:
    
    def WriteDemandrecord(self,data):
        self.demand_csv_filepath= base_path / "data" / "database" / "demand.csv"
        with open(self.demand_csv_filepath,"a+",newline="") as f:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            f.seek(0)
            for i in self.reader:
                if i["Product id"] == data["Product id"]:
                    i["Quantity"]=int(i["Quantity"])+int(data["Quantity"])
                    DemandDataHandler.modify_demand(self,data["Product id"],i["Quantity"])
                    return
                
            f.seek(0,2)
            headers=["Product id","Product name","Quantity","Vendor id"]
            row={}
            row["Product id"] = data["Product id"]
            row['Product name'] = data["Product name"]
            row["Quantity"] = data["Quantity"]
            row["Vendor id"]=data["Vendor id"]
            self.writer=csv.DictWriter(f,fieldnames=headers)
            self.writer.writerow(row)


        
    def delete_demand(self,product_id):
        self.demand_csv_filepath= base_path / "data" / "database" / "demand.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.demand_csv_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Product id"]==product_id:
                    pass
                else:
                    self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.demand_csv_filepath)

    
    def modify_demand(self,product_id,quantity):
        self.demand_csv_filepath= base_path / "data" / "database" / "demand.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.demand_csv_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Product id"]==product_id:
                    i["Quantity"]=quantity
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.demand_csv_filepath)
        











            
            
        
        
