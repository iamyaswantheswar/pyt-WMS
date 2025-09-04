import datetime as dt
import csv
import shutil
import ast
from pathlib import Path


##ast.literal_eval(data)
base_path = Path(__file__).parent.parent.parent.parent
class CustomerDataHandler:
    def GetVendorIds(self):
        self.Vendor_csv_filepath= base_path / "data" / "database" / "vendor.csv"
        with open(self.Vendor_csv_filepath,"r",newline="") as file:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.vendorid_list=[]
            for i in self.reader:
                self.id_name=i["Vendor id"]+" "+i["Vendor name"]
                self.vendorid_list.append(self.id_name)
            return self.vendorid_list

    def add_customer(self,customerid,customername):
        self.customer_csv_filepath= base_path / "data" / "database" / "customer.csv"
        with open(self.customer_csv_filepath,"a+",newline="") as file:
            headers=["Customer id","Customer name","Stock Value","Sale ids"]
            self.writer=csv.DictWriter(file,fieldnames=headers)
            data={}
            data["Customer id"]=customerid
            data["Customer name"]=customername
            data["Stock Value"]=0
            data["Sale ids"]=[]
            self.writer.writerow(data)
    def add_purchase(self,vendorid,stockvalue,purchaseid):
        self.Vendor_csv_filepath= base_path / "data" / "database" / "vendor.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.Vendor_csv_filepath,"r",newline="") as file,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Vendor id"]==vendorid:
                    self.purchases_data=ast.literal_eval(i["Purchase ids"])
                    self.purchases_data.append(purchaseid)
                    i["Purchase ids"]=self.purchases_data
                    i["Stock Value"]=int(i["Stock Value"])+int(stockvalue)
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.Vendor_csv_filepath)


    def modify_purchase(self,mquantity,vendorid,unitprice,wrongqty):
        self.Vendor_csv_filepath= base_path / "data" / "database" / "vendor.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.Vendor_csv_filepath,"r",newline="") as file,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Vendor id"]==vendorid:
                    self.wrong_stock_value=int(unitprice)*int(wrongqty)
                    self.new_stock_value=int(unitprice)*int(mquantity)
                    i["Stock Value"]=(int(i["Stock Value"])-int(self.wrong_stock_value))+self.new_stock_value
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.Vendor_csv_filepath)
    def delete_purchase(self,vendorid,purchaseid,unitprice,previousqty):
        self.Vendor_csv_filepath= base_path / "data" / "database" / "vendor.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.Vendor_csv_filepath,"r",newline="") as file,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Vendor id"]==vendorid:
                    self.purchases_data=ast.literal_eval(i["Purchase ids"])
                    self.purchases_data.remove(purchaseid)
                    i["Purchase ids"]=self.purchases_data
                    i["Stock Value"]=int(i["Stock Value"])-(int(unitprice)*int(previousqty))
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.Vendor_csv_filepath)















        
