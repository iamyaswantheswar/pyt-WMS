from datetime import datetime
import csv
import shutil
from pathlib import Path
base_path = Path(__file__).parent.parent.parent.parent
class PurchasesDataHandler:
    def Writenewproductdata(self,Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate,purchaseid):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        with open(self.purchases_csv_filepath,"a+",newline="") as f:
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            headers=['Product id','Product name','Quantity','Unit price','Stock value','Location','Expiry Date',"Purchase Date","Purchase Id"]
            row={}
            row["Product id"] = Product_id
            row['Product name'] = Product_name
            row["Quantity"] = Quantity
            row['Unit price'] = cost
            row['Stock value'] =Stockvalue
            row['Location']=location
            row['Expiry Date']=expirydate
            row['Purchase Date']=self.current_date
            row['Purchase Id']=purchaseid
            self.writer=csv.DictWriter(f,fieldnames=headers)
            self.writer.writerow(row)
            

        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        with open(self.purchaseslog_filepath,"a+",newline="") as f:
            headers=['Product id','Product name','Quantity','Unit price','Stock value','Location','Expiry Date',"Purchase Date","Purchase Id"]
            row={}
            row["Product id"] = Product_id
            row['Product name'] = Product_name
            row["Quantity"] = Quantity
            row['Unit price'] = cost
            row['Stock value'] =Stockvalue
            row['Location']=location
            row['Expiry Date']=expirydate
            row['Purchase Date']=self.current_date
            row['Purchase Id']=purchaseid
            self.writer=csv.DictWriter(f,fieldnames=headers)
            self.writer.writerow(row)
            self.add_product_window.destroy()
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        with open(self.inventory_csv_filepath,"a+",newline="")as f:
            headers=['Product id','Product name','Quantity','Unit price','Stock value','Location','Expiry Date']
            row={}
            row["Product id"] = Product_id
            row['Product name'] = Product_name
            row["Quantity"] = Quantity
            row['Unit price'] = cost
            row['Stock value'] =Stockvalue
            row['Location']=location
            row['Expiry Date']=expirydate
            self.writer=csv.DictWriter(f,fieldnames=headers)
            self.writer.writerow(row)
#Product id,Product name,Quantity,Unit price,Stock value,Location,Expiry Date
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
        
        with open(self.purchases_csv_filepath,"a+",newline="") as f:
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            self.current_date_time=datetime.now().strftime("%d%m%Y%H%M")
            self.product_purchase_id=productid+str(new_stock)+self.current_date_time
            headers=['Product id','Product name','Quantity','Unit price','Stock value','Location','Expiry Date',"Purchase Date","Purchase Id"]
            row={}
            row["Product id"] = productid
            row['Product name'] = self.uproduct_data["Product name"]
            row["Quantity"] = new_stock
            row['Unit price'] = self.uproduct_data["Unit price"]
            row['Stock value'] =int(new_stock)*int(self.uproduct_data["Unit price"])
            row['Location']=self.uproduct_data["Location"]
            row['Expiry Date']=self.uproduct_data["Expiry Date"]
            row['Purchase Date']=self.current_date
            row['Purchase Id']=self.product_purchase_id
            self.writer=csv.DictWriter(f,fieldnames=headers)
            self.writer.writerow(row)
            
        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        with open(self.purchaseslog_filepath,"a+",newline="") as f:
            headers=['Product id','Product name','Quantity','Unit price','Stock value','Location','Expiry Date',"Purchase Date","Purchase Id"]
            row={}
            row["Product id"] = productid
            row['Product name'] = self.uproduct_data["Product name"]
            row["Quantity"] = new_stock
            row['Unit price'] = self.uproduct_data["Unit price"]
            row['Stock value'] =int(new_stock)*int(self.uproduct_data["Unit price"])
            row['Location']=self.uproduct_data["Location"]
            row['Expiry Date']=self.uproduct_data["Expiry Date"]
            row['Purchase Date']=self.current_date
            row['Purchase Id']=self.product_purchase_id
            self.writer=csv.DictWriter(f,fieldnames=headers)
            self.writer.writerow(row)

    
