from datetime import datetime
import csv
import shutil
from pathlib import Path
base_path = Path(__file__).parent.parent.parent.parent

class SalesDataHandler:
    #sales str = Product id,Product name,Quantity,Unit Cost price,Unit Sale price,Final sale price,Sale value,Net profit,Sale Date,Sale id,Customer id
    def WriteSalerecord(self,productdata,saleprice,quantity,customerid,saleid):
        self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
        self.saleslog_filepath=base_path / "data" / "database" / "stocklog" / "sales_log.csv"
        with open(self.sales_csv_filepath,"a+",newline="") as f,open(self.saleslog_filepath,"a+",newline="") as logfile:
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            headers=["Product id","Product name","Sale quantity","Unit Cost price","Unit Sale price","Final sale price","Sale value","Net profit","Sale Date","Sale id","Customer id"]
            row={}
            row["Product id"] = productdata["Product id"]
            row['Product name'] = productdata["Product name"]
            row["Sale quantity"] = quantity
            row['Unit Cost price'] = productdata["Unit Cost price"]
            row['Unit Sale price'] = productdata["Unit Sale price"]
            row["Final sale price"]=saleprice
            row["Sale value"] =int(saleprice)*int(quantity)
            row['Net profit']=int(row["Sale value"])-(int(quantity)*int(row['Unit Cost price']))
            row['Sale Date']=self.current_date
            row['Sale id']=saleid
            row["Customer id"]=customerid
            self.writer1=csv.DictWriter(f,fieldnames=headers)
            self.writer1.writerow(row)
            self.writer2=csv.DictWriter(logfile,fieldnames=headers)
            self.writer2.writerow(row)

            
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.inventory_csv_filepath,"r",newline="")as file , open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                    if i["Product id"] == productdata["Product id"]:
                        i["Quantity"]= int(i["Quantity"])-int(quantity)
                        i["Stock value"]=int(i["Quantity"])*int(i["Unit Cost price"])
                        if i["Quantity"]==0:##code for demand can be added
                            self.writer.writerow(i)
                        else:
                            self.writer.writerow(i)
                    else:
                        self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.inventory_csv_filepath)


        
    def delete_sale(self,saleid,product_id):
        self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.sales_csv_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Sale id"]==saleid:
                    self.sale_qty=i["Sale quantity"]
                    self.unit_price=i["Unit Cost price"]
                    
                else:
                    self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.sales_csv_filepath)

            
        self.salelog_filepath=base_path / "data" / "database" / "stocklog" / "sales_log.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.salelog_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Sale id"]==saleid:
                    pass
                else:
                    self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.salelog_filepath)
            
                    
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.inventory_csv_filepath,"r",newline="")as file , open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                    if i["Product id"] == product_id:
                        i["Quantity"]= int(i["Quantity"])+int(self.sale_qty)
                        i["Stock value"]=int(i["Quantity"])*int(i["Unit Cost price"])
                        if i["Quantity"]==0:##code for demand can be added
                            self.writer.writerow(i)
                        else:
                            self.writer.writerow(i)
                        None
                    else:
                        self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.inventory_csv_filepath)











            
            
        
        
