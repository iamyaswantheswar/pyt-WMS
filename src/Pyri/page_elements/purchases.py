import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
from datetime import datetime
from tkinter import messagebox

base_path = Path(__file__).parent.parent.parent.parent

class purchases_elements:
    def refresh_csv(self,frame,home):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        self.csv_data=[]
        with open(self.purchases_csv_filepath,"r",newline="")as file:
            self.reader=csv.reader(file)
            self.purchases_headings=next(self.reader)
            self.csv_data.append(self.purchases_headings)
            for row in self.reader:
                if row==[]:
                    continue
                elif row[-1]==self.current_date:
                    self.csv_data.append(row)
                
        with open(self.purchases_csv_filepath,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerows(self.csv_data)
        
        self.csv_data=purchases_elements.open_purchases_csv(self)
        purchases_elements.display_csv(self,frame,self.csv_data,0,1)
        self.tree.destroy()
    
    def purchases_ele(self,frame,home):
        frame.grid_columnconfigure(0,minsize=300)
        self.add_product_button=ui.Button(frame,text="Add new product",command = lambda : purchases_elements.add_product(self,home,frame),width=30,font=("Arial",10,"bold"))
        self.add_product_button.place(relx=0.02,rely=0.05)
        self.stock_existing_product_button=ui.Button(frame,text="Add stock ",command = lambda : purchases_elements.add_stock(self,home,frame),width=30,font=("Arial",10,"bold"))
        self.stock_existing_product_button.place(relx=0.02,rely=0.2)
        purchases_elements.refresh_csv(self,frame,home)
        self.csv_data=purchases_elements.open_purchases_csv(self)
        purchases_elements.display_csv(self,frame,self.csv_data,0,1)
        purchases_elements.refresh_csv(self,frame,home)


    def display_csv(self,frame,data,row,column,colspan=1):
        self.tree=ttk.Treeview(frame,columns=data[0],show="headings")
        self.tree.grid(row=row,column=column,columnspan=colspan,sticky="nsew",padx=(0,0),pady=(0,0))
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
        
#######################################################ADD STOCK CODE #########################################################################################
    def get_data_add_stock(self,frame,home,exsisting_stock,unit_price):
        self.uproduct_id=self.entry_uproduct_id.get()
        self.additional_product_quantity=int(self.entry_uproduct_quantity.get())
        self.product_final_quantity=self.additional_product_quantity + exsisting_stock
        self.product_final_stockvalue=self.product_final_quantity *  unit_price
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        self.data=[]
        with open(self.inventory_csv_filepath,"r",newline="")as file:
            self.reader=csv.reader(file)
            for row in self.reader:
                if row==[]:
                    continue
                elif row[0]==self.entry_uproduct_id.get():
                    d=row.copy()
                    d[2]=self.additional_product_quantity
                    d[4]=int(self.additional_product_quantity)*int(d[3])
                    row[2]=self.product_final_quantity
                    row[4]=self.product_final_stockvalue
                    self.data.append(row)
                else:
                    self.data.append(row)
        with open(self.inventory_csv_filepath,"w",newline="")as file:
            self.writer=csv.writer(file)
            self.writer.writerows(self.data)
            
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        
        with open(self.purchases_csv_filepath,"a+",newline="") as f:
            writer=csv.writer(f)
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            self.list_purchase=d[0:7]+[self.current_date]
            writer.writerow(self.list_purchase)
            
        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        with open(self.purchaseslog_filepath,"a+",newline="") as f:
            writer=csv.writer(f)
            self.list_purchase=d[0:7]+[self.current_date]
            writer.writerow(self.list_purchase)

        self.tree.destroy()
        self.csv_data=purchases_elements.open_purchases_csv(self)
        purchases_elements.display_csv(self,frame,self.csv_data,0,1)

            
        
                    
        
        




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
                self.reader=csv.reader(file)
                for i in self.reader:
                    if i==[]:
                        None
                    elif i[0]==self.entry_uproduct_id.get():
                        self.existing_stock=int(i[2])
                        self.unit_price=int(i[3])
                        purchases_elements.get_data_add_stock(self,frame,home,self.existing_stock,self.unit_price)
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
        self.add_stock_window.geometry("1000x600")
        
        self.label_uproduct_id = ui.Label(self.add_stock_window, text="Product ID",bg="white",font=('Arial',10))
        self.label_uproduct_id.place(relx=0.05,rely=0.05,anchor="w")
                
        self.entry_uproduct_id=ui.Entry(self.add_stock_window, width=40,bd=2,font=('Arial',13))
        self.entry_uproduct_id.place(relx=0.05, rely=0.1, anchor="w")
                
                
        self.label_uproduct_quantity = ui.Label(self.add_stock_window, text="Product Quantity",bg="white",font=('Arial',10))
        self.label_uproduct_quantity.place(relx=0.05,rely=0.35,anchor="w")

        self.entry_uproduct_quantity=ui.Entry(self.add_stock_window, width=40,bd=2,font=('Arial',13))
        self.entry_uproduct_quantity.place(relx=0.05, rely=0.4, anchor='w')
                                            

        self.confirm_button=ui.Button(self.add_stock_window,text="CONFIRM", command = lambda : purchases_elements.update_entry_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.95, anchor="center")
        





######################################################## ADD PRODUCT CODE#######################################################################################
        
    def entry_check(self,frame,home):
        
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        if  self.entry_product_id.get() != '':
            with open(self.inventory_csv_filepath,"r",newline="")as file:
                self.reader=csv.reader(file)
                for i in self.reader:
                    if i==[]:
                        None
                    elif i[0]==self.entry_product_id.get():
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
        self.product_name=self.entry_product_name.get()
        self.product_id=self.entry_product_id.get()
        self.product_quantity=self.entry_product_quantity.get()
        self.product_cost=self.entry_product_cost.get()
        self.product_stock_cost=int(self.product_quantity)*int(self.product_cost)
        self.product_exp=self.entry_product_exp.get()
        self.product_block=self.product_blocks.get()[-1]
        self.product_zone=self.product_zones.get()[-1]
        self.product_aisle=self.product_aisles.get()[-1]
        self.product_rack=self.product_racks.get()[-1]
        self.product_shelf=self.product_shelfs.get()[-1]
        self.product_location=self.product_block + self.product_zone + self.product_aisle + self.product_rack + self.product_shelf
        purchases_elements.write_data_purchases(self,frame,home,self.product_id,self.product_name,self.product_quantity,self.product_cost,self.product_stock_cost,self.product_location,self.product_exp)


    def write_data_purchases(self,frame,home,Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        with open(self.purchases_csv_filepath,"a+",newline="") as f:
            writer=csv.writer(f)
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            writer.writerow([Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate,self.current_date])
        self.purchaseslog_filepath=base_path / "data" / "database" / "stocklog" / "purchases_log.csv"
        with open(self.purchaseslog_filepath,"a+",newline="") as f:
            writer=csv.writer(f)
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            writer.writerow([Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate,self.current_date])
            self.add_product_window.destroy()
        self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        with open(self.inventory_csv_filepath,"a+",newline="")as f:
            writer=csv.writer(f)
            self.current_date=datetime.now().strftime("%d-%m-%Y")
            writer.writerow([Product_id,Product_name,Quantity,cost,Stockvalue,location,expirydate])
            
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
            print(self.entry_product_exp.get())
            #self.cal_window.grab_set()
            #self.cal_window.focus_set()
        ui.Button(self.cal_window,text="Select",command=lambda : enter_date(self)).pack(pady=5)
            
        
    def add_product(self,home,frame):
        self.add_product_window=ui.Toplevel(home)
        self.add_product_window.title("Add Product to Warehouse")
        self.add_product_window.configure(bg="white")
        self.add_product_window.geometry("1000x600")
        #self.add_product_window.grab_set()
        #self.add_product_window.focus_set()
        self.label_product_name = ui.Label(self.add_product_window, text="Product Name",bg="white",font=('Arial',10))
        self.label_product_name.place(relx=0.05,rely=0.05,anchor="w")
                
        self.entry_product_name=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_name.place(relx=0.05, rely=0.1, anchor="w")
                
        self.label_product_id = ui.Label(self.add_product_window, text="Product ID",bg="white",font=('Arial',10))
        self.label_product_id.place(relx=0.05,rely=0.2,anchor="w")

        self.entry_product_id=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_id.place(relx=0.05, rely=0.25, anchor='w')
                
        self.label_product_quantity = ui.Label(self.add_product_window, text="Product Quantity",bg="white",font=('Arial',10))
        self.label_product_quantity.place(relx=0.05,rely=0.35,anchor="w")

        self.entry_product_quantity=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_quantity.place(relx=0.05, rely=0.4, anchor='w')
                                            
        self.label_product_cost = ui.Label(self.add_product_window, text="Product Cost price",bg="white",font=('Arial',10))
        self.label_product_cost.place(relx=0.05,rely=0.5,anchor="w")

        self.entry_product_cost=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_cost.place(relx=0.05, rely=0.55, anchor='w')
                
        self.label_product_exp = ui.Label(self.add_product_window, text="Product Expiry date DD-MM-YYYY",bg="white",font=('Arial',10))
        self.label_product_exp.place(relx=0.05,rely=0.65,anchor="w")

        self.entry_product_exp=ui.Entry(self.add_product_window, width=40,bd=2,font=('Arial',13))
        self.entry_product_exp.place(relx=0.05, rely=0.7, anchor='w')
        
        
        self.cal_button=ui.Button(self.add_product_window,text="Choose date", command = lambda : purchases_elements.open_calendar(self,home),bg="white")
        self.cal_button.place(relx=0.5, rely=0.7, anchor='w')
        
        self.label_product_location=ui.Label(self.add_product_window,text="Select product location",bg="white",font=('Arial',11))
        self.label_product_location.place(relx=0.05,rely=0.8,anchor="w")

        self.product_location_blocks=["Block 1",'Block 2','Block 3',"Block 4"]
        self.product_blocks=ui.StringVar(value="Select Block")
        self.option_product_location_block=ui.OptionMenu(self.add_product_window,self.product_blocks,*self.product_location_blocks)
        self.option_product_location_block.place(relx=0.05,rely=0.85,anchor="w")
        self.option_product_location_block.configure(bg="white")

        self.product_location_zones=["Zone 1",'Zone 2','Zone 3',"Zone 4"] 
        self.product_zones=ui.StringVar(value="Select Zone")
        self.option_product_location_zone=ui.OptionMenu(self.add_product_window,self.product_zones,*self.product_location_zones)
        self.option_product_location_zone.place(relx=0.25,rely=0.85,anchor="w")
        self.option_product_location_zone.configure(bg="white")

        self.product_location_aisles=["Aisle 1",'Aisle 2','Aisle 3',"Aisle 4"] 
        self.product_aisles=ui.StringVar(value="Select Aisle")
        self.option_product_location_aisle=ui.OptionMenu(self.add_product_window,self.product_aisles,*self.product_location_aisles)
        self.option_product_location_aisle.place(relx=0.45,rely=0.85,anchor="w")
        self.option_product_location_aisle.configure(bg="white")

        self.product_location_racks=["Rack 1",'Rack 2','Rack 3',"Rack 4"] 
        self.product_racks=ui.StringVar(value="Select Rack")
        self.option_product_location_rack=ui.OptionMenu(self.add_product_window,self.product_racks,*self.product_location_racks)
        self.option_product_location_rack.place(relx=0.65,rely=0.85,anchor="w")
        self.option_product_location_rack.configure(bg="white")

        self.product_location_shelfs=["Shelf 1",'Shelf 2','Shelf 3',"Shelf 4"] 
        self.product_shelfs=ui.StringVar(value="Select Shelf")
        self.option_product_location_shelf=ui.OptionMenu(self.add_product_window,self.product_shelfs,*self.product_location_shelfs)
        self.option_product_location_shelf.place(relx=0.85,rely=0.85,anchor="w")
        self.option_product_location_shelf.configure(bg="white")

        self.confirm_button=ui.Button(self.add_product_window,text="CONFIRM", command = lambda : purchases_elements.entry_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
        self.confirm_button.place(relx=0.5, rely=0.95, anchor="center")


    
        #self.split_stock_button=ui.Button(self.add_product_window,text="Split stock",command = lambda :purchases_elements.split_stock(self,home))
        #self.split_stock_button.place(relx=0.05,rely=0.9,anchor="w")


    
                
            
            
        
                
