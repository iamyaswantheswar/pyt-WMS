import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
import shutil
from datetime import datetime
from tkinter import messagebox
from database.PurchaseDH import PurchasesDataHandler
from database.VendorDH import VendorDataHandler



base_path = Path(__file__).parent.parent.parent.parent

class purchases_elements:
    def refresh_csv(self,frame,home):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
        with open(self.purchases_csv_filepath,"r",newline="")as file,open(self.temp_csv_filepath,"w",newline="")as temp:
            self.reader=csv.DictReader(file)
            headers=self.reader.fieldnames
            self.writer=csv.DictWriter(temp,fieldnames=headers)
            self.writer.writeheader()
            for row in self.reader:
                if row["Purchase Date"]==self.current_date:
                    self.writer.writerow(row)
        shutil.move(self.temp_csv_filepath,self.purchases_csv_filepath)

        
        self.csv_data=purchases_elements.open_purchases_csv(self)
        purchases_elements.display_csv(self,frame,self.csv_data,0,1)
        self.tree.destroy()
    
    def purchases_ele(self,frame,home):
        frame.grid_columnconfigure(0,minsize=250)
        self.add_product_button=ui.Button(frame,text="Add new vendor",command = lambda : purchases_elements.add_vendor(self,home,frame),width=25,font=("Arial",10,"bold"))
        self.add_product_button.place(relx=0.02,rely=0.1)
        
        self.add_product_button=ui.Button(frame,text="Add new product",command = lambda : purchases_elements.add_product(self,home,frame),width=25,font=("Arial",10,"bold"))
        self.add_product_button.place(relx=0.02,rely=0.26)
        
        self.stock_existing_product_button=ui.Button(frame,text="Add stock ",command = lambda : purchases_elements.add_stock(self,home,frame),width=25,font=("Arial",10,"bold"))
        self.stock_existing_product_button.place(relx=0.02,rely=0.42)
        
        self.modify_purchase_button=ui.Button(frame,text="Modify Purchase ",command = lambda : purchases_elements.modify_purchase(self,home,frame),width=25,font=("Arial",10,"bold"))
        self.modify_purchase_button.place(relx=0.02,rely=0.58)
        
        self.delete_purchase_button=ui.Button(frame,text="Delete Purchase ",command = lambda : purchases_elements.delete_purchase(self,home,frame),width=25,font=("Arial",10,"bold"))
        self.delete_purchase_button.place(relx=0.02,rely=0.74)
        
        
        self.view_history_button=ui.Button(frame,text="View Purchase history ",command = lambda : purchases_elements.view_purchase_history(self,home),width=25,font=("Arial",10,"bold"))
        self.view_history_button.place(relx=0.02,rely=0.9)

        
        
        purchases_elements.refresh_csv(self,frame,home)
        self.csv_data=purchases_elements.open_purchases_csv(self)
        purchases_elements.display_csv(self,frame,self.csv_data,0,1)
        
        
        


    def display_csv(self,frame,data,row,column,colspan=1):
        self.style=ttk.Style()
        self.style.theme_use("clam")
        self.tree=ttk.Treeview(frame,columns=data[0],show="headings")
        self.tree.grid(row=row,column=column,columnspan=colspan,sticky="nsew",padx=(0,0),pady=(0,0))
        self.hbar=ttk.Scrollbar(frame,orient="horizontal",command=self.tree.xview)
        self.vbar=ttk.Scrollbar(frame,orient="vertical",command=self.tree.yview)
        self.tree.configure(xscrollcommand=self.hbar.set,yscrollcommand=self.vbar.set)
        self.hbar.grid(row=1,column=1,sticky="ew")
        self.vbar.grid(row=0,column=2,sticky="ns")
            #configure coloumns
        for col in data[0]:
            self.tree.heading(col,text=col)
            self.tree.column(col,anchor="center",width=120)
            #inserting rows
        for row_data in data[1:]:
            self.tree.insert("","end",values=row_data)
        frame.grid_rowconfigure(row,weight=1)
        frame.grid_columnconfigure(column,weight=1)
        return self.tree


    def open_purchases_csv(self):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        
        with open(self.purchases_csv_filepath,newline="")as f:
            self.reader=csv.reader(f)
            return list(self.reader)



#######################################################Add Vendor Code #####################################################################################
    def add_vendor(self,home,frame):
        self.add_vendor_window=ui.Toplevel(home)
        self.add_vendor_window.title("Add Vendor")
        self.add_vendor_window.configure(bg="white")
        self.add_vendor_window.geometry("500x200")
        
        self.label_vendor_id = ui.Label(self.add_vendor_window, text="Vendor ID",bg="white",font=('Arial',10))
        self.label_vendor_id.place(relx=0.05,rely=0.05,anchor="w")
                
        self.entry_vendor_id=ui.Entry(self.add_vendor_window, width=40,bd=2,font=('Arial',13))
        self.entry_vendor_id.place(relx=0.05, rely=0.2, anchor="w")
                
                
        self.label_vendor_name = ui.Label(self.add_vendor_window, text="Vendor Name",bg="white",font=('Arial',10))
        self.label_vendor_name.place(relx=0.05,rely=0.45,anchor="w")

        self.entry_vendor_name=ui.Entry(self.add_vendor_window, width=40,bd=2,font=('Arial',13))
        self.entry_vendor_name.place(relx=0.05, rely=0.6, anchor='w')
                                            

        self.confirm_button=ui.Button(self.add_vendor_window,text="CONFIRM", command = lambda : purchases_elements.vendor_data_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.85, anchor="center")
        
    def vendor_data_check(self,frame,home):
        self.vendor_csv_filepath= base_path / "data" / "database" / "vendor.csv"
        if self.entry_vendor_id.get()=="" or self.entry_vendor_name.get()=="":
            messagebox.showerror("Invalid Entry","Empty entries are not accepted")
            self.add_vendor_window.destroy()
            purchases_elements.add_vendor(self,home,frame)
        else:
            with open(self.vendor_csv_filepath,"r",newline="") as file:
                self.reader=csv.DictReader(file)
                for i in self.reader:
                    if i["Vendor id"]==self.entry_vendor_id.get():
                        messagebox.showerror("Vendor exists","Vendor id already present in database")
                        self.add_vendor_window.destroy()
                        purchases_elements.add_vendor(self,home,frame)
                        break
                else:
                    VendorDataHandler.add_vendor(self,self.entry_vendor_id.get(),self.entry_vendor_name.get())
                    self.add_vendor_window.destroy()
            
            
        
#######################################################ADD STOCK CODE #######################################################################################

    def update_entry_check(self,frame,home):
        try:
            q=int(self.entry_uproduct_quantity.get())
        except:
            messagebox.showerror("Invalid quantity","Enter valid quantity ")
            self.add_stock_window.destroy()
            purchases_elements.add_stock(self,home,frame)
            return None
            
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        if  self.entry_uproduct_id.get() != '':
            
            
            with open(self.inventory_csv_filepath,"r",newline="")as file:
                self.reader=csv.DictReader(file)
                for i in self.reader:
                    if i["Product id"]==self.entry_uproduct_id.get():
                        self.product_vendor=i["Vendor id"]
                        self.existing_stock=int(i["Quantity"])
                        self.unit_price=int(i["Unit Cost price"])
                        self.uproduct_id=self.entry_uproduct_id.get()
                        self.additional_product_quantity=int(self.entry_uproduct_quantity.get())
                        self.purchase_value=self.unit_price*self.additional_product_quantity
                        self.product_final_quantity=self.additional_product_quantity + self.existing_stock
                        self.product_final_stockvalue=self.product_final_quantity * self.unit_price
                        #going to backend to write data
                        PurchasesDataHandler.Updateproductstock(self,self.uproduct_id,self.existing_stock,self.unit_price,self.additional_product_quantity,self.product_final_quantity,self.product_final_stockvalue)
                        VendorDataHandler.add_purchase(self,self.product_vendor,self.purchase_value,self.product_purchase_id)

                        self.tree.destroy()
                        self.csv_data=purchases_elements.open_purchases_csv(self)
                        purchases_elements.display_csv(self,frame,self.csv_data,0,1)
                        self.add_stock_window.destroy()
                        break
                    
                else:
                    self.response = messagebox.askyesno("Product Not found","Product with Product_ID:" + self.entry_uproduct_id.get() + "\n"+ "Not found Do you want to add this product ?"+"\n"+"Click No to retry")
                    if self.response==True:
                        self.add_stock_window.destroy()
                        purchases_elements.add_product(self,home,frame)
                    else:
                        self.add_stock_window.destroy()
                        
                        purchases_elements.add_stock(self,home,frame)
        else:
            messagebox.showerror("Empty id","Product id  can't be empty.")
            self.add_stock_window.destroy()
            purchases_elements.add_stock(self,home,frame)
            
    def add_stock(self,home,frame):
        self.add_stock_window=ui.Toplevel(home)
        self.add_stock_window.title("Add Stock to inventory")
        self.add_stock_window.configure(bg="white")
        self.add_stock_window.geometry("500x250")
        
        self.label_uproduct_id = ui.Label(self.add_stock_window, text="Product ID",bg="white",font=('Arial',10))
        self.label_uproduct_id.place(relx=0.05,rely=0.1,anchor="w")
                
        self.entry_uproduct_id=ui.Entry(self.add_stock_window, width=40,bd=2,font=('Arial',13))
        self.entry_uproduct_id.place(relx=0.05, rely=0.25, anchor="w")
                
                
        self.label_uproduct_quantity = ui.Label(self.add_stock_window, text="Product Quantity",bg="white",font=('Arial',10))
        self.label_uproduct_quantity.place(relx=0.05,rely=0.45,anchor="w")

        self.entry_uproduct_quantity=ui.Entry(self.add_stock_window, width=40,bd=2,font=('Arial',13))
        self.entry_uproduct_quantity.place(relx=0.05, rely=0.6, anchor='w')
                                            

        self.confirm_button=ui.Button(self.add_stock_window,text="CONFIRM", command = lambda : purchases_elements.update_entry_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.9, anchor="center")
        





######################################################## ADD PRODUCT CODE#######################################################################################
        
    def entry_check(self,frame,home):
        ##Product id,Product name,Quantity,Unit Cost price,Unit Sale price,Stock value,Location,Expiry Date,Purchase Date,Purchase id,Vendor id
        
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        if  self.entry_product_id.get() != '':
            with open(self.inventory_csv_filepath,"r",newline="")as file:
                self.reader=csv.DictReader(file)
                for i in self.reader:
                    if i==[]:
                        None
                    elif i["Product id"]==self.entry_product_id.get():
                        self.response1 = messagebox.askyesno("Product Exists","Product with Product_ID:" + self.entry_product_id.get() + "\n"+ "Already exists in inventory Do want to update stock ?"+"\n"+"Click No to retry")
                        if self.response1==True:
                            self.add_product_window.destroy()
                            purchases_elements.add_stock(self,home,frame)
                        else:
                            self.add_product_window.destroy()
                            purchases_elements.add_product(self,home,frame)
                        return None
        else:
            messagebox.showerror("Empty id","Product id  can't be empty.")
            self.add_product_window.destroy()
            purchases_elements.add_product(self,home,frame)
            return None

        self.entry_errors=[]
        if self.entry_product_name.get()=="":
            self.entry_errors.append("Product name")
        try:
            q=int(self.entry_product_quantity.get())
        except:
            self.entry_errors.append("Product quantity")
            
        try:
            q=int(self.entry_product_cost.get())
            
        except:
            self.entry_errors.append("Product cost")

        try:
            q=int(self.entry_product_saleprice.get())
            
        except:
            self.entry_errors.append("Product saleprice")
            
        try:
            datetime.strptime(self.entry_product_exp.get(),"%d-%m-%Y")
        except:
            self.entry_errors.append("Product exp")
            
        try:
            q=int(self.product_blocks.get()[-1])
        except:
            self.entry_errors.append("Product block")
            
        try:
            q=int(self.product_zones.get()[-1])
        except:
            self.entry_errors.append("Product zone")
            
        try:
            q=int(self.product_aisles.get()[-1])
        except:
            self.entry_errors.append("Product aisle")
        try:
            q=int(self.product_racks.get()[-1])
        except:
            self.entry_errors.append("Product rack")
            
        try:
            q=int(self.product_shelfs.get()[-1])
        except:
            self.entry_errors.append("Product shelf")
            
        if self.product_vendorid.get() == "Select Vendor":
            self.entry_errors.append("Product vendor")
            
            
            
        if self.entry_errors==[]:
            purchases_elements.get_data_add_product(self,frame,home)
        else:
            s=""
            for i in self.entry_errors:
                s=s+"\n"+"  "+i
            messagebox.showerror("INVALID DATA ENTRY","Following entries are invalid "+"\n"+ s+"\n\n"+"Please enter valid data types")
            self.add_product_window.destroy()
            purchases_elements.add_product(self,home,frame)
            self.entry_errors=[]
            
            
            
        
    
    def get_data_add_product(self,frame,home):
        self.current_date=datetime.now().strftime("%d%m%Y%H%M")

        self.product_name=self.entry_product_name.get()
        self.product_id=self.entry_product_id.get()
        self.product_quantity=self.entry_product_quantity.get()
        self.product_cost=self.entry_product_cost.get()
        self.product_saleprice=self.entry_product_saleprice.get()
        self.product_stock_cost=int(self.product_quantity)*int(self.product_cost)
        self.product_exp=self.entry_product_exp.get()
        self.product_vendor=self.product_vendorid.get().split()[0]
        self.product_block=self.product_blocks.get()[-1]
        self.product_zone=self.product_zones.get()[-1]
        self.product_aisle=self.product_aisles.get()[-1]
        self.product_rack=self.product_racks.get()[-1]
        self.product_shelf=self.product_shelfs.get()[-1]
        self.product_location=self.product_block + self.product_zone + self.product_aisle + self.product_rack + self.product_shelf
        self.product_purchase_id=self.product_id+str(self.product_quantity)+self.current_date
        #going to backend to write data
        PurchasesDataHandler.Writenewproductdata(self,self.product_id,self.product_name,self.product_quantity,self.product_cost,self.product_saleprice,self.product_stock_cost,self.product_location,self.product_exp,self.product_purchase_id,self.product_vendor)
        VendorDataHandler.add_purchase(self,self.product_vendor,self.product_stock_cost,self.product_purchase_id)

        self.tree.destroy()
        self.csv_data=purchases_elements.open_purchases_csv(self)
        purchases_elements.display_csv(self,frame,self.csv_data,0,1)

    def open_calendar(self,home):
        self.cal_window=ui.Toplevel(home)
        self.cal_window.title("Select Date")
        self.cal_window.geometry("300x300")
        self.cal = Calendar(self.cal_window,selectmode="day",date_pattern="dd-mm-yyyy")
        self.cal.pack()
        def enter_date(self):
            self.entry_product_exp.delete(0,ui.END)
            self.entry_product_exp.insert(0,self.cal.get_date())
            self.cal_window.destroy()
            #self.cal_window.grab_set()
            #self.cal_window.focus_set()
        ui.Button(self.cal_window,text="Select",command=lambda : enter_date(self)).pack(pady=5)
            
        
    def add_product(self,home,frame):
        self.add_product_window=ui.Toplevel(home)
        self.add_product_window.title("Add Product to Warehouse")
        self.add_product_window.configure(bg="white")
        self.add_product_window.geometry("900x650")
        #self.add_product_window.grab_set()
        #self.add_product_window.focus_set()
        self.label_product_name = ui.Label(self.add_product_window, text="Product Name",bg="white",font=('Arial',10))
        self.label_product_name.place(relx=0.05,rely=0.02,anchor="w")
                
        self.entry_product_name=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_name.place(relx=0.05, rely=0.052, anchor="w")
                
        self.label_product_id = ui.Label(self.add_product_window, text="Product ID",bg="white",font=('Arial',10))
        self.label_product_id.place(relx=0.05,rely=0.12,anchor="w")

        self.entry_product_id=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_id.place(relx=0.05, rely=0.152, anchor='w')
                
        self.label_product_quantity = ui.Label(self.add_product_window, text="Product Quantity",bg="white",font=('Arial',10))
        self.label_product_quantity.place(relx=0.05,rely=0.22,anchor="w")

        self.entry_product_quantity=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_quantity.place(relx=0.05, rely=0.252, anchor='w')
                                            
        self.label_product_cost = ui.Label(self.add_product_window, text="Product Cost price",bg="white",font=('Arial',10))
        self.label_product_cost.place(relx=0.05,rely=0.32,anchor="w")

        self.entry_product_cost=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_cost.place(relx=0.05, rely=0.352, anchor='w')

        self.label_product_saleprice = ui.Label(self.add_product_window, text="Product Sale price",bg="white",font=('Arial',10))
        self.label_product_saleprice.place(relx=0.05,rely=0.42,anchor="w")

        self.entry_product_saleprice=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_saleprice.place(relx=0.05, rely=0.452, anchor='w')
                
        self.label_product_exp = ui.Label(self.add_product_window, text="Product Expiry date DD-MM-YYYY",bg="white",font=('Arial',10))
        self.label_product_exp.place(relx=0.05,rely=0.52,anchor="w")

        self.entry_product_exp=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_exp.place(relx=0.05, rely=0.552, anchor='w')
        
        
        self.cal_button=ui.Button(self.add_product_window,text="Choose date", command = lambda : purchases_elements.open_calendar(self,home),bg="white")
        self.cal_button.place(relx=0.55, rely=0.552, anchor='w')

        self.label_product_vendor=ui.Label(self.add_product_window,text="Select Vendor id",bg="white",font=('Arial',11))
        self.label_product_vendor.place(relx=0.05,rely=0.62,anchor="w")

        self.vendor_list= VendorDataHandler.GetVendorIds(self)
        self.product_vendorid=ui.StringVar(value="Select Vendor")
        self.option_product_vendorid=ui.OptionMenu(self.add_product_window,self.product_vendorid,*self.vendor_list)
        self.option_product_vendorid.place(relx=0.05,rely=0.67,anchor="w")
        self.option_product_vendorid.configure(bg="white")
        
        self.label_product_location=ui.Label(self.add_product_window,text="Select product location",bg="white",font=('Arial',11))
        self.label_product_location.place(relx=0.05,rely=0.74,anchor="w")

        self.product_location_blocks=["Block 1",'Block 2','Block 3',"Block 4"]
        self.product_blocks=ui.StringVar(value="Select Block")
        self.option_product_location_block=ui.OptionMenu(self.add_product_window,self.product_blocks,*self.product_location_blocks)
        self.option_product_location_block.place(relx=0.05,rely=0.79,anchor="w")
        self.option_product_location_block.configure(bg="white")

        self.product_location_zones=["Zone 1",'Zone 2','Zone 3',"Zone 4"] 
        self.product_zones=ui.StringVar(value="Select Zone")
        self.option_product_location_zone=ui.OptionMenu(self.add_product_window,self.product_zones,*self.product_location_zones)
        self.option_product_location_zone.place(relx=0.22,rely=0.79,anchor="w")
        self.option_product_location_zone.configure(bg="white")

        self.product_location_aisles=["Aisle 1",'Aisle 2','Aisle 3',"Aisle 4"] 
        self.product_aisles=ui.StringVar(value="Select Aisle")
        self.option_product_location_aisle=ui.OptionMenu(self.add_product_window,self.product_aisles,*self.product_location_aisles)
        self.option_product_location_aisle.place(relx=0.42,rely=0.79,anchor="w")
        self.option_product_location_aisle.configure(bg="white")

        self.product_location_racks=["Rack 1",'Rack 2','Rack 3',"Rack 4"] 
        self.product_racks=ui.StringVar(value="Select Rack")
        self.option_product_location_rack=ui.OptionMenu(self.add_product_window,self.product_racks,*self.product_location_racks)
        self.option_product_location_rack.place(relx=0.62,rely=0.79,anchor="w")
        self.option_product_location_rack.configure(bg="white")

        self.product_location_shelfs=["Shelf 1",'Shelf 2','Shelf 3',"Shelf 4"] 
        self.product_shelfs=ui.StringVar(value="Select Shelf")
        self.option_product_location_shelf=ui.OptionMenu(self.add_product_window,self.product_shelfs,*self.product_location_shelfs)
        self.option_product_location_shelf.place(relx=0.82,rely=0.79,anchor="w")
        self.option_product_location_shelf.configure(bg="white")

        self.confirm_button=ui.Button(self.add_product_window,text="CONFIRM", command = lambda : purchases_elements.entry_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.9, anchor="center")


    
        #self.split_stock_button=ui.Button(self.add_product_window,text="Split stock",command = lambda :purchases_elements.split_stock(self,home))
        #self.split_stock_button.place(relx=0.05,rely=0.9,anchor="w")


#################################################################################### Modify Purchase #######################################################

    def modify_purchase(self,home,frame):
        self.modify_purchase_window=ui.Toplevel(home)
        self.modify_purchase_window.title("Modify purchase")
        self.modify_purchase_window.configure(bg="white")
        self.modify_purchase_window.geometry("500x150")
        
                
        self.label_mproduct_id = ui.Label(self.modify_purchase_window, text="Product ID",bg="white",font=('Arial',10))
        self.label_mproduct_id.place(relx=0.05,rely=0.2,anchor="w")

        self.entry_mproduct_id=ui.Entry(self.modify_purchase_window, width=40,bd=2,font=('Arial',13))
        self.entry_mproduct_id.place(relx=0.05, rely=0.5, anchor='w')

        self.confirm_button=ui.Button(self.modify_purchase_window,text="CONFIRM", command = lambda : purchases_elements.get_purchase_ids(self,home,frame,self.entry_mproduct_id.get()),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")

    
        
    def get_purchase_ids(self,home,frame,product_id):
        if product_id == "":
            messagebox.showerror("Empty id","Product id  can't be empty.")
            self.modify_purchase_window.destroy()
            purchases_elements.modify_purchase(self,home,frame)
        else:
            self.modify_purchase_window.destroy()
            self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
            with open(self.purchases_csv_filepath,"r",newline="")as file:
                self.reader=csv.DictReader(file)
                self.purchase_ids=[]
                for i in self.reader:
                    if i["Product id"] == product_id:
                        self.purchase_ids.append(i["Purchase id"])
                        self.vendor_id=i["Vendor id"]
                        self.unit_price=i['Unit Cost price']
                if self.purchase_ids==[]:
                    messagebox.showerror("Invalid id","Product id doesnt exist")
                    self.modify_purchase_window.destroy()
                    purchases_elements.modify_purchase(self,home,frame)
                else:
                    self.modify_purchase_window.destroy()
                    purchases_elements.modify_purchase_choose_pruchaseid(self,home,frame,self.purchase_ids,product_id,self.vendor_id,self.unit_price)
                    
    def modify_purchase_choose_pruchaseid(self,home,frame,purchaseids,product_id,vendorid,unitprice):
        self.modify_ids_window=ui.Toplevel(home)
        self.modify_ids_window.title("Choose purchase id to modify")
        self.modify_ids_window.configure(bg="white")
        self.modify_ids_window.geometry("500x200")
        
        self.label_mproduct_ids= ui.Label(self.modify_ids_window, text="Choose Purchase id",bg="white",font=('Arial',10))
        self.label_mproduct_ids.place(relx=0.05,rely=0.2,anchor="w")
        
        self.purchases_ids=purchaseids
        self.product_purchase_ids=ui.StringVar(value="Select Purchaseid")
        self.option_product_purchase_ids=ui.OptionMenu(self.modify_ids_window,self.product_purchase_ids,*self.purchases_ids)
        self.option_product_purchase_ids.place(relx=0.05,rely=0.4,anchor="w")
        self.option_product_purchase_ids.configure(bg="white")

        
        self.confirm_button=ui.Button(self.modify_ids_window,text="CONFIRM", command = lambda : purchases_elements.modify_purchasedata_window(self,home,frame,self.product_purchase_ids.get(),product_id,vendorid,unitprice),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")
 
    def modify_purchasedata_window(self,home,frame,purchaseid,product_id,vendorid,unitprice):
        if purchaseid=="Select Purchaseid":
            messagebox.showerror("Invalid selection","Please select Purchase ID before pressing Confirm")
            self.modify_ids_window.destroy()
            purchases_elements.get_purchase_ids(self,home,frame,product_id)
        else:
            self.modify_ids_window.destroy()
            self.mproduct_window=ui.Toplevel(home)
            self.mproduct_window.title("Modify Quantity")
            self.mproduct_window.configure(bg="white")
            self.mproduct_window.geometry("500x200")
                    
            self.label_mproduct_quantity = ui.Label(self.mproduct_window, text="New Product Quantity",bg="white",font=('Arial',10))
            self.label_mproduct_quantity.place(relx=0.05,rely=0.35,anchor="w")

            self.entry_mproduct_quantity=ui.Entry(self.mproduct_window, width=40,bd=2,font=('Arial',13))
            self.entry_mproduct_quantity.place(relx=0.05, rely=0.45, anchor='w')
            
            
            self.confirm_button=ui.Button(self.mproduct_window,text="CONFIRM", command = lambda : purchases_elements.write_mdata(self,home,frame,purchaseid,self.entry_mproduct_quantity.get(),product_id,vendorid,unitprice),bg="white",width= 25,font=("Arial",10,"bold"))
            self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")
            
            
    def write_mdata(self,home,frame,purchaseid,mquantity,product_id,vendorid,unitprice):
        if mquantity == "":
            messagebox.showerror("Empty entry","New quantity cant be empty")
        else:
            try:
                q=int(mquantity)
            except:
                messagebox.showerror("Invalid entry","Invalid data type")
                self.mproduct_window.destroy()
                purchases_elements.modify_purchasedata_window(self,home,purchaseid)
                return
            if int(mquantity) == 0:
                self.response = messagebox.askyesno("Warning","Do you really  want to delete this purchase transation")
                if self.response==True:
                    #goes to backend
                    PurchasesDataHandler.delete_purchase(self,purchaseid,product_id)
                    VendorDataHandler.delete_purchase(self,vendorid,purchaseid,unitprice,self.removed_qty) #self.removed_qty comes from PurchasesDataHandler.delete_purchase()
                    self.tree.destroy()
                    self.csv_data=purchases_elements.open_purchases_csv(self)
                    purchases_elements.display_csv(self,frame,self.csv_data,0,1)
                    self.mproduct_window.destroy()
            else:
                #goes to backend
                PurchasesDataHandler.modify_quantity(self,purchaseid,mquantity,product_id)
                VendorDataHandler.modify_purchase(self,mquantity,vendorid,unitprice,self.wrong_qty)#self.wrongqty is from PurchasesDataHandler.modify_quantity
                self.tree.destroy()
                self.csv_data=purchases_elements.open_purchases_csv(self)
                purchases_elements.display_csv(self,frame,self.csv_data,0,1)
                self.mproduct_window.destroy()
######################################################## Delete Purchase ###################################################################
    def delete_purchase(self,home,frame):
        self.delete_purchase_window=ui.Toplevel(home)
        self.delete_purchase_window.title("Delete Purchase Record")
        self.delete_purchase_window.configure(bg="white")
        self.delete_purchase_window.geometry("700x150")

        self.label_dproduct_id = ui.Label(self.delete_purchase_window, text="Product ID",bg="white",font=('Arial',10))
        self.label_dproduct_id.place(relx=0.05,rely=0.2,anchor="w")

        self.entry_dproduct_id=ui.Entry(self.delete_purchase_window, width=40,bd=2,font=('Arial',13))
        self.entry_dproduct_id.place(relx=0.05, rely=0.5, anchor='w')

        self.confirm_button=ui.Button(self.delete_purchase_window,text="CONFIRM", command = lambda : purchases_elements.get_dpurchase_ids(self,home,frame,self.entry_dproduct_id.get()),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")
    def get_dpurchase_ids(self,home,frame,product_id):
        if product_id == "":
            messagebox.showerror("Empty id","Product id  can't be empty.")
            self.delete_purchase_window.destroy()
            purchases_elements.delete_purchase(self,home,frame)
        else:
            self.delete_purchase_window.destroy()
            self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
            with open(self.purchases_csv_filepath,"r",newline="")as file:
                self.reader=csv.DictReader(file)
                self.purchase_ids=[]
                for i in self.reader:
                    if i["Product id"] == product_id:
                        self.vendor_id=i["Vendor id"]
                        self.unit_price=i["Unit Cost price"]
                        self.purchase_ids.append(i["Purchase id"])
                        
                if self.purchase_ids==[]:
                    messagebox.showerror("Invalid id","Product id doesnt exist")
                    self.delete_purchase_window.destroy()
                    purchases_elements.delete_purchase(self,home,frame)
                else:
                    self.delete_purchase_window.destroy()
                    purchases_elements.delete_purchase_choose_pruchaseid(self,home,frame,self.purchase_ids,product_id,self.vendor_id,self.unit_price)
                    
    def delete_purchase_choose_pruchaseid(self,home,frame,purchaseids,product_id,vendorid,unitprice):
        self.delete_ids_window=ui.Toplevel(home)
        self.delete_ids_window.title("Choose purchase id to delete")
        self.delete_ids_window.configure(bg="white")
        self.delete_ids_window.geometry("500x200")
        
        self.label_mproduct_ids= ui.Label(self.delete_ids_window, text="Choose Purchase id",bg="white",font=('Arial',10))
        self.label_mproduct_ids.place(relx=0.05,rely=0.2,anchor="w")
        
        self.purchases_ids=purchaseids
        self.product_purchase_ids=ui.StringVar(value="Select Purchaseid")
        self.option_product_purchase_ids=ui.OptionMenu(self.delete_ids_window,self.product_purchase_ids,*self.purchases_ids)
        self.option_product_purchase_ids.place(relx=0.05,rely=0.4,anchor="w")
        self.option_product_purchase_ids.configure(bg="white")

        
        self.confirm_button=ui.Button(self.delete_ids_window,text="CONFIRM", command = lambda : purchases_elements.confirm_purchase_data_deletion(self,home,frame,self.product_purchase_ids.get(),product_id,vendorid,unitprice),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")
        
    def confirm_purchase_data_deletion(self,home,frame,purchaseid,product_id,vendorid,unitprice):
        if purchaseid=="Select Purchaseid":
            messagebox.showerror("Invalid selection","Please select Purchase ID before pressing Confirm")
            self.delete_ids_window.destroy()
            purchases_elements.get_dpurchase_ids(self,home,frame,product_id)
            return
        self.response = messagebox.askyesno("Warning","Do you really  want to delete this purchase transation")
        if self.response==True:
            self.delete_ids_window.destroy()
            #goes to backend
            PurchasesDataHandler.delete_purchase(self,purchaseid,product_id)
            VendorDataHandler.delete_purchase(self,vendorid,purchaseid,unitprice,self.removed_qty) #self.removed_qty comes from PurchasesDataHandler.delete_purchase()
            self.tree.destroy()
            self.csv_data=purchases_elements.open_purchases_csv(self)
            purchases_elements.display_csv(self,frame,self.csv_data,0,1)
            self.delete_ids_window.destroy()
            
        else:
            self.delete_ids_window.destroy()
                        

        
        


                

########################################################## View Purchase History ############################################################
    def view_purchase_history(self,home):
        self.view_purchase_history_window=ui.Toplevel(home)
        self.view_purchase_history_window.title("Purchase History")
        self.view_purchase_history_window.configure(bg="white")
        self.view_purchase_history_window.geometry("700x150")
                                                
        self.view_history_date = ui.Label(self.view_purchase_history_window, text="Enter date [DD-MM-YYYY}",bg="white",font=('Arial',10))
        self.view_history_date.place(relx=0.05,rely=0.2,anchor="w")

        self.entry_view_history_date=ui.Entry(self.view_purchase_history_window, width=30,bd=2,font=('Arial',13))
        self.entry_view_history_date.place(relx=0.05, rely=0.5, anchor='w')
        
        
        self.cal_history_button=ui.Button(self.view_purchase_history_window,text="Choose date", command = lambda : purchases_elements.open_history_calendar(self,home),bg="white")
        self.cal_history_button.place(relx=0.5, rely=0.5, anchor='w')
        
        self.confirm_button=ui.Button(self.view_purchase_history_window,text="CONFIRM", command = lambda : purchases_elements.verify_entry(self,home,self.entry_view_history_date.get()),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")

    def open_history_calendar(self,home):
        self.cal_window=ui.Toplevel(home)
        self.cal_window.title("Select Date")
        self.cal_window.geometry("300x300")
        self.cal = Calendar(self.cal_window,selectmode="day",date_pattern="dd-mm-yyyy")
        self.cal.pack()
        def enter_date(self):
            self.entry_view_history_date.delete(0,ui.END)
            self.entry_view_history_date.insert(0,self.cal.get_date())
            self.cal_window.destroy()
        ui.Button(self.cal_window,text="Select",command=lambda : enter_date(self)).pack(pady=5)

    def verify_entry(self,home,date):
        try:
            datetime.strptime(date,"%d-%m-%Y")
        except:
            messagebox.showerror("Invalid Entry","Enter date in given format")
            self.view_purchase_history_window.destroy()
            purchases_elements.view_purchase_history(self,home)
            return
        purchases_elements.purchase_history_window(self,home,date)
            
            

    def purchase_history_window(self,home,date):
        self.view_purchase_history_window.destroy()
        self.purchase_history_window=ui.Toplevel(home)
        self.purchase_history_window.title(f"Purchases on {date}")
        self.purchase_history_window.configure(bg="white")

        self.csv_data=purchases_elements.open_purchases_history_csv(self)
        purchases_elements.display_history_csv(self,self.purchase_history_window,self.csv_data,date,0,0)

    def open_purchases_history_csv(self):
        self.purchaseslog_csv_filepath= base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        
        with open(self.purchaseslog_csv_filepath,newline="")as f:
            self.reader=csv.reader(f)
            return list(self.reader)


    def display_history_csv(self,window,data,date,row,column,colspan=2):
        self.tree=ttk.Treeview(window,columns=data[0],show="headings")
        self.tree.grid(row=row,column=column,columnspan=colspan,sticky="nsew",padx=(0,0),pady=(0,0))
            #configure coloumns
        for col in data[0]:
            self.tree.heading(col,text=col)
            self.tree.column(col,anchor="center",width=120)
            #inserting rows
        for row_data in data[1:]:
            self.entry_count=0
            if row_data==[]:
                continue
            if row_data[-3]==date:
                self.tree.insert("","end",values=row_data)
                self.entry_count+=1
        if self.entry_count==0:
            self.tree.destroy()
            self.purchase_history_window.geometry("900x300")
            self.lable_no_purchase_history=ui.Label(window,text="No Purchase records on this date",bg="white",font=('Arial',20,"bold"))
            self.lable_no_purchase_history.place(relx=0.5,rely=0.5,anchor="center")
        return self.tree


    
            













            
        
                
