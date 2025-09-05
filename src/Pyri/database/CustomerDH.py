import datetime as dt
import csv
import shutil
import ast
from pathlib import Path


##ast.literal_eval(data)
base_path = Path(__file__).parent.parent.parent.parent
class CustomerDataHandler:
    def GetCustomerIds(self):
        self.customer_csv_filepath= base_path / "data" / "database" / "customer.csv"
        with open(self.customer_csv_filepath,"r",newline="") as file:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.customerid_list=[]
            for i in self.reader:
                self.id_name=i["Customer id"]+" "+i["Customer name"]
                self.customerid_list.append(self.id_name)
            return self.customerid_list

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
    def add_sale(self,customerid,salevalue,saleid):
        self.customer_csv_filepath= base_path / "data" / "database" / "customer.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.customer_csv_filepath,"r",newline="") as file,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Customer id"]==customerid:
                    self.purchases_data=ast.literal_eval(i["Sale ids"])
                    self.purchases_data.append(saleid)
                    i["Sale ids"]=self.purchases_data
                    i["Stock Value"]=int(i["Stock Value"])+int(salevalue)
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.customer_csv_filepath)



            
    def delete_sale(self,customerid,saleid,oldsprice,oldqty):
        self.customer_csv_filepath= base_path / "data" / "database" / "customer.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.customer_csv_filepath,"r",newline="") as file,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Customer id"]==customerid:
                    self.sales_data=ast.literal_eval(i["Sale ids"])
                    self.sales_data.remove(saleid)
                    i["Sale ids"]=self.sales_data
                    i["Stock Value"]=int(i["Stock Value"])-(int(oldsprice)*int(oldqty))
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
        shutil.move(self.temp_csv_filepath,self.customer_csv_filepath)















        
