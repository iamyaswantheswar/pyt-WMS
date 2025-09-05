import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
import shutil
from datetime import datetime
from tkinter import messagebox
from database.SalesDH import SalesDataHandler
from database.CustomerDH import CustomerDataHandler


base_path = Path(__file__).parent.parent.parent.parent
class sales_elements:
        def sales_ele(self,frame,home):
                frame.grid_columnconfigure(0,minsize=250)
                self.new_sale_button=ui.Button(frame,text="Add customer",command = lambda : sales_elements.add_customer(self,frame,home),width=25,font=("Arial",10,"bold"))
                self.new_sale_button.place(relx=0.02,rely=0.05)
                
                self.sale_new_cus_button=ui.Button(frame,text="New Sale",command = lambda : sales_elements.new_sale(self,frame,home),width=25,font=("Arial",10,"bold"))
                self.sale_new_cus_button.place(relx=0.02,rely=0.25)
                
                self.modify_sale_button=ui.Button(frame,text="Modify sale ",command = lambda : sales_elements.modify_sale(self,frame,home),width=25,font=("Arial",10,"bold"))
                self.modify_sale_button.place(relx=0.02,rely=0.45)
                
                self.delete_sale_button=ui.Button(frame,text="Delete sale ",command = lambda : None,width=25,font=("Arial",10,"bold"))
                self.delete_sale_button.place(relx=0.02,rely=0.65)
                
                
                self.view_history_button=ui.Button(frame,text="View sales history ",command = lambda : None ,width=25,font=("Arial",10,"bold"))
                self.view_history_button.place(relx=0.02,rely=0.85)

                sales_elements.refresh_csv(self,frame,home)
                self.csv_data=sales_elements.open_sales_csv(self)
                sales_elements.display_csv(self,frame,self.csv_data,0,1)
                
        def refresh_csv(self,frame,home):
                self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
                self.current_date=datetime.now().strftime("%d-%m-%Y")
                self.temp_csv_filepath=base_path / "data" / "database" / "temp.csv"
                with open(self.sales_csv_filepath,"r",newline="")as file,open(self.temp_csv_filepath,"w",newline="")as temp:
                    self.reader=csv.DictReader(file)
                    headers=self.reader.fieldnames
                    self.writer=csv.DictWriter(temp,fieldnames=headers)
                    self.writer.writeheader()
                    for row in self.reader:
                        if row["Sale Date"]==self.current_date:
                            self.writer.writerow(row)
                shutil.move(self.temp_csv_filepath,self.sales_csv_filepath)
                
                
                self.csv_data=sales_elements.open_sales_csv(self)
                sales_elements.display_csv(self,frame,self.csv_data,0,1)
                self.tree.destroy()
                


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


        def open_sales_csv(self):
                self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
                with open(self.sales_csv_filepath,newline="")as f:
                    self.reader=csv.reader(f)
                    return list(self.reader)
################################################################### ADD CUSTOMER###########################

        def add_customer(self,frame,home):
                self.add_customer_window=ui.Toplevel(home)
                self.add_customer_window.title("Add Customer")
                self.add_customer_window.configure(bg="white")
                self.add_customer_window.geometry("500x200")
                
                self.label_customer_id = ui.Label(self.add_customer_window, text="Customer ID",bg="white",font=('Arial',10))
                self.label_customer_id.place(relx=0.05,rely=0.05,anchor="w")
                        
                self.entry_customer_id=ui.Entry(self.add_customer_window, width=40,bd=2,font=('Arial',13))
                self.entry_customer_id.place(relx=0.05, rely=0.2, anchor="w")
                        
                        
                self.label_customer_name = ui.Label(self.add_customer_window, text="Customer Name",bg="white",font=('Arial',10))
                self.label_customer_name.place(relx=0.05,rely=0.45,anchor="w")

                self.entry_customer_name=ui.Entry(self.add_customer_window, width=40,bd=2,font=('Arial',13))
                self.entry_customer_name.place(relx=0.05, rely=0.6, anchor='w')
                                                    

                self.confirm_button=ui.Button(self.add_customer_window,text="CONFIRM", command = lambda : sales_elements.customer_data_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.85, anchor="center")
                
        def customer_data_check(self,frame,home):
                self.customer_csv_filepath= base_path / "data" / "database" / "customer.csv"
                if self.entry_customer_id.get()=="" or self.entry_customer_name.get()=="":
                    messagebox.showerror("Invalid Entry","Empty entries are not accepted")
                    self.add_customer_window.destroy()
                    sales_elements.add_customer(self,frame,home)
                    
                else:
                    with open(self.customer_csv_filepath,"r",newline="") as file:
                        self.reader=csv.DictReader(file)
                        for i in self.reader:
                            if i["Customer id"]==self.entry_customer_id.get():
                                messagebox.showerror("Customer exists","Customer id already present in database")
                                self.add_customer_window.destroy()
                                sales_elements.add_customer(self,frame,home)
                                break
                        else:
                            CustomerDataHandler.add_customer(self,self.entry_customer_id.get(),self.entry_customer_name.get())
                            self.add_customer_window.destroy()


##################################################### New Sale #############################################################
                
        def new_sale(self,frame,home):
                self.new_sale_window=ui.Toplevel(home)
                self.new_sale_window.title("New Sale")
                self.new_sale_window.configure(bg="white")
                self.new_sale_window.geometry("500x120")
                        
                self.label_product_id = ui.Label(self.new_sale_window, text="Enter Product ID",bg="white",font=('Arial',10))
                self.label_product_id.place(relx=0.05,rely=0.2,anchor="w")

                self.entry_product_id=ui.Entry(self.new_sale_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_id.place(relx=0.05, rely=0.4, anchor='w')
                        
                self.confirm_button=ui.Button(self.new_sale_window,text="CONFIRM", command = lambda : sales_elements.get_product_data(self,frame,home,self.entry_product_id.get()) ,bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")


        def get_product_data(self,frame,home,productid):
                if productid=="":
                        messagebox.showerror("Empty Product ID","Product id cant be empty")
                        self.new_sale_window.destroy()
                        sales_elements.new_sale(self,frame,home)
                else:
                        self_inventory_csv_path=base_path / "data" / "database" / "inventory.csv"
                        with open(self_inventory_csv_path,"r",newline="") as file:
                                self.reader=csv.DictReader(file)
                                headers=self.reader.fieldnames
                                self.product_data={}
                                for i in self.reader:
                                        if i["Product id"] == productid:
                                                if int(i["Quantity"]) == 0:
                                                        self.response = messagebox.askyesno("Low Quantity","Stock unavailable \n Do you wan to raise a demand ?")
                                                        if self.response == True :
                                                                pass #raise demand code
                                                        else:
                                                                messagebox.showerror("Low Quantity","Can't proceed with sale")
                                                                self.new_sale_window.destroy()
                                                                return
                                                        
                                                self.product_data=i
                        if self.product_data=={}:
                                messagebox.showerror("Invalid Product ID","Product not found")
                                self.new_sale_window.destroy()
                                sales_elements.new_sale(self,frame,home)
                        else:
                                self.new_sale_window.destroy()
                                sales_elements.new_sale_detail_window(self,frame,home,self.product_data)

        def new_sale_detail_window(self,frame,home,productdata):
                # inventory str = Product id,Product name,Quantity,Unit Cost price,Unit Sale price,Stock value,Location,Expiry Date,Vendor id
                self.new_sale_data_window=ui.Toplevel(home)
                self.new_sale_data_window.title("New sale")
                self.new_sale_data_window.configure(bg="white")
                self.new_sale_data_window.geometry("900x650")
                #self.new_sale_data_window.grab_set()
                #self.new_sale_data_window.focus_set()
                self.label_product_name = ui.Label(self.new_sale_data_window, text="Product Name",bg="white",font=('Arial',10))
                self.label_product_name.place(relx=0.05,rely=0.02,anchor="w")
                
                        
                self.entry_product_name=ui.Entry(self.new_sale_data_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_name.place(relx=0.05, rely=0.052, anchor="w")
                self.entry_product_name.insert(0,productdata["Product name"])
                self.entry_product_name.config(state="readonly")
                        
                self.label_product_id = ui.Label(self.new_sale_data_window, text="Product ID",bg="white",font=('Arial',10))
                self.label_product_id.place(relx=0.05,rely=0.12,anchor="w")

                self.entry_product_id=ui.Entry(self.new_sale_data_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_id.place(relx=0.05, rely=0.152, anchor='w')
                self.entry_product_id.insert(0,productdata["Product id"])
                self.entry_product_id.config(state="readonly")

                self.label_product_cost = ui.Label(self.new_sale_data_window, text="Product Cost price",bg="white",font=('Arial',10))
                self.label_product_cost.place(relx=0.05,rely=0.22,anchor="w")

                self.entry_product_cost=ui.Entry(self.new_sale_data_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_cost.place(relx=0.05, rely=0.252, anchor='w')
                self.entry_product_cost.insert(0,productdata["Unit Cost price"])
                self.entry_product_cost.config(state="readonly")
                

                self.label_product_saleprice = ui.Label(self.new_sale_data_window, text="Product sale price",bg="white",font=('Arial',10))
                self.label_product_saleprice.place(relx=0.05,rely=0.32,anchor="w")

                self.entry_product_saleprice=ui.Entry(self.new_sale_data_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_saleprice.place(relx=0.05, rely=0.352, anchor='w')
                self.entry_product_saleprice.insert(0,productdata["Unit Sale price"])
                self.entry_product_saleprice.config(state="readonly")

                self.label_product_fsaleprice = ui.Label(self.new_sale_data_window, text="Price after discount",bg="white",font=('Arial',10))
                self.label_product_fsaleprice.place(relx=0.05,rely=0.42,anchor="w")

                self.entry_product_fsaleprice=ui.Entry(self.new_sale_data_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_fsaleprice.place(relx=0.05, rely=0.452, anchor='w')
                
                        
                self.label_product_quantity = ui.Label(self.new_sale_data_window, text="Product Quantity",bg="white",font=('Arial',10))
                self.label_product_quantity.place(relx=0.05,rely=0.52,anchor="w")

                self.entry_product_sale_quantity=ui.Entry(self.new_sale_data_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_sale_quantity.place(relx=0.05, rely=0.552, anchor='w')
                                                    
                self.customer_list= CustomerDataHandler.GetCustomerIds(self)
                self.product_customerid=ui.StringVar(value="Select Customer")
                self.option_product_customerid=ui.OptionMenu(self.new_sale_data_window,self.product_customerid,*self.customer_list)
                self.option_product_customerid.place(relx=0.05,rely=0.67,anchor="w")
                self.option_product_customerid.configure(bg="white")

                self.confirm_button=ui.Button(self.new_sale_data_window,text="CONFIRM", command = lambda : sales_elements.entry_check(self,frame,home,productdata),bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.9, anchor="center")
                

        def entry_check(self,frame,home,productdata):
                #Product id,Product name,Quantity,Unit Cost price,Unit Sale price,Final sale price,Stock value,Net profit,Sale Date,Sale id,Customer id
                self.errors=[]
                if self.entry_product_fsaleprice.get()!="":
                        try:
                                self.sale_price=int(self.entry_product_fsaleprice.get())
                        except:
                                self.errors.append("Sale price")
                else:
                     self.sale_price=product["Unit Sale price"]
                     
                if self.entry_product_sale_quantity.get()=="":
                        self.errors.append("Sale quantity")
                else:
                        try:
                                self.sale_quantity=int(self.entry_product_sale_quantity.get())
                        except:
                                self.errors.append("Sale quantity")

                if self.product_customerid.get()== "Select Customer":
                        self.errors.append("Customer id")
                else:
                        self.sale_customer_id=self.product_customerid.get().split()[0]

                self.demand_quantity=0                
                if int(self.entry_product_sale_quantity.get()) > int(productdata["Quantity"]):
                        self.response = messagebox.askyesno("Low Quantity",f"Inventory has only {productdata["Quantity"]} Do you want to raise demand for remaing quantity ? \n Choose no to continue sale with maximum available quantity without raising demand ")
                        if self.response==True:
                                self.demand_quantity=int(self.entry_product_sale_quantity.get())-int(productdata["Quantity"])
                                self.sale_quantity=productdata["Quantity"]
                        else:
                                self.sale_quantity=productdata["Quantity"]
                        
                                                                     
                
                if self.errors==[]:
                        self.current_date=datetime.now().strftime("%d%m%Y%H%M%S")
                        self.sale_id="S" + productdata["Product id"]+str(self.sale_quantity)+self.current_date
                        SalesDataHandler.WriteSalerecord(self,productdata,self.sale_price,self.sale_quantity,self.sale_customer_id,self.sale_id)
                        self.sale_value=int(self.sale_price)*int(self.sale_quantity)
                        CustomerDataHandler.add_sale(self,self.sale_customer_id,self.sale_value,self.sale_id)
                        self.new_sale_data_window.destroy()
                        self.tree.destroy()
                        self.csv_data=sales_elements.open_sales_csv(self)
                        sales_elements.display_csv(self,frame,self.csv_data,0,1)
                        if self.demand_quantity!=0:
                                pass #code for demand
                else:
                        s=""
                        for i in self.errors:
                                s=s+"\n"+"  "+i
                        messagebox.showerror("INVALID DATA ENTRY","Following entries are invalid "+"\n"+ s+"\n\n"+"Please enter valid data types")
                        self.new_sale_data_window.destroy()
                        sales_elements.new_sale_detail_window(self,frame,home,self.product_data)
                        
                        
############################################# Modify sale ############################################################
        def modify_sale(self,frame,home):
                self.modify_sale_window=ui.Toplevel(home)
                self.modify_sale_window.title("Modify Sale")
                self.modify_sale_window.configure(bg="white")
                self.modify_sale_window.geometry("500x150")
                
                        
                self.label_mproduct_id = ui.Label(self.modify_sale_window, text="Product ID",bg="white",font=('Arial',10))
                self.label_mproduct_id.place(relx=0.05,rely=0.2,anchor="w")

                self.entry_mproduct_id=ui.Entry(self.modify_sale_window, width=40,bd=2,font=('Arial',13))
                self.entry_mproduct_id.place(relx=0.05, rely=0.5, anchor='w')

                self.confirm_button=ui.Button(self.modify_sale_window,text="CONFIRM", command = lambda : sales_elements.get_sale_ids(self,home,frame,self.entry_mproduct_id.get()),bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")

    
        
        def get_sale_ids(self,home,frame,product_id):
                if product_id == "":
                        messagebox.showerror("Empty id","Product id  can't be empty.")
                        self.modify_sale_window.destroy()
                        sales_elements.modify_sale(self,frame,home)
                else:
                        self.modify_sale_window.destroy()
                        self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
                        with open(self.sales_csv_filepath,"r",newline="")as file:
                                self.reader=csv.DictReader(file)
                                self.sale_ids=[]
                                for i in self.reader:
                                        if i["Product id"] == product_id:
                                                self.sale_ids.append(i["Sale id"])
                                if self.sale_ids==[]:
                                        messagebox.showerror("Invalid id","Product id doesnt exist")
                                        self.modify_sale_window.destroy()
                                        sales_elements.modify_sale(self,home,frame)
                                else:
                                        self.modify_sale_window.destroy()
                                        sales_elements.modify_sale_choose_saleid(self,home,frame,self.sale_ids,product_id)
                    
        def modify_sale_choose_saleid(self,home,frame,saleids,product_id):
                self.modify_ids_window=ui.Toplevel(home)
                self.modify_ids_window.title("Choose sale id to modify")
                self.modify_ids_window.configure(bg="white")
                self.modify_ids_window.geometry("500x200")
                
                self.label_msale_ids= ui.Label(self.modify_ids_window, text="Choose sale id",bg="white",font=('Arial',10))
                self.label_msale_ids.place(relx=0.05,rely=0.2,anchor="w")
                
                self.sale_ids=saleids
                self.product_sale_ids=ui.StringVar(value="Select Sale id")
                self.option_product_sale_ids=ui.OptionMenu(self.modify_ids_window,self.product_sale_ids,*self.sale_ids)
                self.option_product_sale_ids.place(relx=0.05,rely=0.4,anchor="w")
                self.option_product_sale_ids.configure(bg="white")

                
                self.confirm_button=ui.Button(self.modify_ids_window,text="CONFIRM", command = lambda : sales_elements.modify_saledata_window(self,home,frame,self.product_sale_ids.get(),product_id),bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")
         
        def modify_saledata_window(self,home,frame,saleid,product_id):
                if saleid=="Select Sale id":
                        messagebox.showerror("Invalid selection","Please select Sale ID before pressing Confirm")
                        self.modify_ids_window.destroy()
                        sales_elements.get_sale_ids(self,home,frame,product_id)
                else:
                        self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
                        with open(self.sales_csv_filepath,"r",newline="")as file:
                                self.reader=csv.DictReader(file)
                                for i in self.reader:
                                        if i["Sale id"] == saleid:
                                                self.old_saleprice=i["Final sale price"]
                                                self.customer_id=i["Customer id"]
                                                self.old_qty=i["Sale quantity"]

                                        
                        
                        self.modify_ids_window.destroy()
                        self.msale_window=ui.Toplevel(home)
                        self.msale_window.title("Modify Sale")
                        self.msale_window.configure(bg="white")
                        self.msale_window.geometry("500x300")
                        
                        self.label_msale_fsaleprice = ui.Label(self.msale_window, text="New Sale Price",bg="white",font=('Arial',10))
                        self.label_msale_fsaleprice.place(relx=0.05,rely=0.25,anchor="w")

                        self.entry_msale_fsaleprice=ui.Entry(self.msale_window, width=40,bd=2,font=('Arial',13))
                        self.entry_msale_fsaleprice.place(relx=0.05, rely=0.35, anchor='w')

                        self.label_msale_quantity = ui.Label(self.msale_window, text="New Sale Quantity",bg="white",font=('Arial',10))
                        self.label_msale_quantity.place(relx=0.05,rely=0.55,anchor="w")

                        self.entry_msale_quantity=ui.Entry(self.msale_window, width=40,bd=2,font=('Arial',13))
                        self.entry_msale_quantity.place(relx=0.05, rely=0.65, anchor='w')
                    
                    
                        self.confirm_button=ui.Button(self.msale_window,text="CONFIRM", command = lambda : sales_elements.write_mdata(self,home,frame,saleid,product_id,self.customer_id,self.old_qty,self.entry_msale_quantity.get(),self.old_saleprice,self.entry_msale_fsaleprice.get()),bg="white",width= 25,font=("Arial",10,"bold"))
                        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")
                    
            
        def write_mdata(self,home,frame,saleid,product_id,customerid,oldqty,newqty,oldsprice,newsprice):
                if newqty == "":
                    messagebox.showerror("Empty entry","New quantity cant be empty")
                else:
                        try:
                                q=int(newqty)
                        except:
                                messagebox.showerror("Invalid entry","Invalid data x type")
                                self.msale_window.destroy()
                                sales_elements.modify_saledata_window(self,home,frame,saleid,product_id)
                                return
                if newsprice == "":
                        newsprice=oldsprice
                else:
                        try:
                                q=int(newsprice)
                        except:
                                messagebox.showerror("Invalid entry","Invalid data type")
                                self.msale_window.destroy()
                                sales_elements.modify_saledata_window(self,home,frame,saleid,product_id)
                                return
                if int(newqty) == 0:
                        self.response = messagebox.askyesno("Warning","Do you really  want to delete this sale transation")
                        if self.response==True:
                                #goes to backend
                                SalesDataHandler.delete_sale(self,saleid,product_id)
                                CustomerDataHandler.delete_sale(self,customerid,saleid,oldsprice,oldqty)
                                self.msale_window.destroy()
                                self.tree.destroy()
                                self.csv_data=sales_elements.open_sales_csv(self)
                                sales_elements.display_csv(self,frame,self.csv_data,0,1)
                        else:
                                self.msale_window.destroy()
                                sales_elements.modify_saledata_window(self,home,frame,saleid,product_id)
                else:
                        self_inventory_csv_path=base_path / "data" / "database" / "inventory.csv"
                        with open(self_inventory_csv_path,"r",newline="") as file:
                                self.reader=csv.DictReader(file)
                                headers=self.reader.fieldnames
                                self.product_data={}
                                for i in self.reader:
                                        if i["Product id"] == product_id:
                                                self.product_data=i
                        SalesDataHandler.delete_sale(self,saleid,product_id)
                        CustomerDataHandler.delete_sale(self,customerid,saleid,oldsprice,oldqty)
                        
                        SalesDataHandler.WriteSalerecord(self,self.product_data,newsprice,newqty,customerid,saleid)
                        self.sale_value=int(newsprice)*int(newqty)
                        CustomerDataHandler.add_sale(self,customerid,self.sale_value,saleid) 
                        self.tree.destroy()
                        self.csv_data=sales_elements.open_sales_csv(self)
                        sales_elements.display_csv(self,frame,self.csv_data,0,1)
                        self.msale_window.destroy()
                        




















                



