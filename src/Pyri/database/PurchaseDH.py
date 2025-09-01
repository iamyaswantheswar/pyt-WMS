from datetime import datetime
import csv
import shutil
from pathlib import Path
base_path = Path(__file__).parent.parent.parent.parent
class PurchasesDataHandler:
    def Writenewproductdata(self,Product_id,Product_name,Quantity,cost,saleprice,Stockvalue,location,expirydate,purchaseid,vendorid):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        with open(self.purchases_csv_filepath,"a+",newline="") as f,open(self.purchaseslog_filepath,"a+",newline="") as logfile:
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            headers=["Product id","Product name","Quantity","Unit Cost price","Unit Sale price","Stock value","Location","Expiry Date","Purchase Date","Purchase id","Vendor id"]
            row={}
            row["Product id"] = Product_id
            row['Product name'] = Product_name
            row["Quantity"] = Quantity
            row['Unit Cost price'] = cost
            row['Unit Sale price'] = saleprice
            row['Stock value'] =Stockvalue
            row['Location']=location
            row['Expiry Date']=expirydate
            row['Purchase Date']=self.current_date
            row['Purchase id']=purchaseid
            row["Vendor id"]=vendorid
            self.writer1=csv.DictWriter(f,fieldnames=headers)
            self.writer1.writerow(row)
            self.writer2=csv.DictWriter(logfile,fieldnames=headers)
            self.writer2.writerow(row)
            self.add_product_window.destroy()
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        with open(self.inventory_csv_filepath,"a+",newline="")as f:
            headers=["Product id","Product name","Quantity","Unit Cost price","Unit Sale price","Stock value",'Location',"Expiry Date","Vendor id"]
            row={}
            row["Product id"] = Product_id
            row['Product name'] = Product_name
            row["Quantity"] = Quantity
            row['Unit Cost price'] = cost
            row['Unit Sale price']=saleprice
            row['Stock value'] =Stockvalue
            row['Location']=location
            row['Expiry Date']=expirydate
            row['Vendor id']=vendorid
            self.writer=csv.DictWriter(f,fieldnames=headers)
            self.writer.writerow(row)
#Product id,Product name,Quantity,Unit Cost price,Unit Sale price,Stock value,Location,Expiry Date,Vendor id

    def Updateproductstock(self,productid,exsisting_stock,unit_price,new_stock,totalstock,totalvalue):
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        self.data=[]
        with open(self.inventory_csv_filepath,"r",newline="")as file , open(self.temp_csv_filepath,"w",newline="")as temp:

            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                    if i["Product id"] == productid:
                        self.uproduct_data=i
                        i["Quantity"]=totalstock
                        i["Stock value"]=totalvalue
                        self.writer.writerow(i)
                    else:
                        self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.inventory_csv_filepath)

            
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        with open(self.purchases_csv_filepath,"a+",newline="") as f,open(self.purchaseslog_filepath,"a+",newline="") as logfile:
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            self.current_date_time=datetime.now().strftime("%d%m%Y%H%M")
            self.product_purchase_id=productid+str(new_stock)+self.current_date_time
            headers=["Product id","Product name","Quantity","Unit Cost price","Unit Sale price","Stock value","Location","Expiry Date","Purchase Date","Purchase id","Vendor id"]
            row={}
            row["Product id"] = productid
            row['Product name'] = self.uproduct_data["Product name"]
            row["Quantity"] = new_stock
            row['Unit Cost price'] = self.uproduct_data["Unit Cost price"]
            row['Unit Sale price'] = self.uproduct_data["Unit Sale price"]
            row['Stock value'] =int(new_stock)*int(self.uproduct_data["Unit Cost price"])
            row['Location']=self.uproduct_data["Location"]
            row['Expiry Date']=self.uproduct_data["Expiry Date"]
            row['Purchase Date']=self.current_date
            row['Purchase id']=self.product_purchase_id
            row["Vendor id"]=self.uproduct_data["Vendor id"]
            self.writer1=csv.DictWriter(f,fieldnames=headers)
            self.writer1.writerow(row)
            self.writer2=csv.DictWriter(logfile,fieldnames=headers)
            self.writer2.writerow(row)

    def modify_quantity(self,purchaseid,mquantity,product_id):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.purchases_csv_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Purchase id"]==purchaseid:
                    self.wrong_qty=int(i['Quantity'])
                    i['Quantity']=mquantity
                    i["Stock value"]= int(mquantity)*int(i['Unit Cost price'])
                    self.updated_product_data=i
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.purchases_csv_filepath)

            
        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.purchaseslog_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Purchase id"]==purchaseid:
                    self.wrong_qty=int(i['Quantity'])
                    i['Quantity']=mquantity
                    i["Stock value"]= int(mquantity)*int(i['Unit Cost price'])
                    self.updated_product_data=i
                    self.writer.writerow(i)
                else:
                    self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.purchaseslog_filepath)
            
                    
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.inventory_csv_filepath,"r",newline="")as file , open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                    if i["Product id"] == product_id:
                        i["Quantity"]= (int(i["Quantity"])-self.wrong_qty)+int(mquantity)
                        i["Stock value"]=int(i["Quantity"])*int(i["Unit Cost price"])
                        if i["Quantity"]==0:##code for demand can be added
                            None
                        else:
                            self.writer.writerow(i)
                    else:
                        self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.inventory_csv_filepath)
        
    def delete_purchase(self,purchaseid,product_id):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.purchases_csv_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Purchase id"]==purchaseid:
                    self.removed_qty=i["Quantity"]
                    self.unit_price=i["Unit Cost price"]
                    
                else:
                    self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.purchases_csv_filepath)

            
        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        self.temp_csv_filepath= base_path / "data" / "database" / "temp.csv"
        with open(self.purchaseslog_filepath,"r",newline="") as f,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(f)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                if i["Purchase id"]==purchaseid:
                    pass
                else:
                    self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.purchaseslog_filepath)
            
                    
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.inventory_csv_filepath,"r",newline="")as file , open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for i in self.reader:
                    if i["Product id"] == product_id:
                        i["Quantity"]= int(i["Quantity"])-int(self.removed_qty)
                        i["Stock value"]=int(i["Quantity"])*int(i["Unit Cost price"])
                        if i["Quantity"]==0:##code for demand can be added
                            None
                        else:
                            self.writer.writerow(i)
                        None
                    else:
                        self.writer.writerow(i)
            shutil.move(self.temp_csv_filepath,self.inventory_csv_filepath)
        
            
        
        
        

    
