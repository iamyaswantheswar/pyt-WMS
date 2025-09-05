import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
import shutil
from datetime import datetime
from tkinter import messagebox
from database.VendorDH import VendorDataHandler
from database.DemandDH import DemandDataHandler

base_path = Path(__file__).parent.parent.parent.parent
class demand_elements:
        def demand_ele(self,frame,home):
                frame.grid_rowconfigure(0,minsize=70)
                self.create_demand_button=ui.Button(frame,text="Create Demand",command = lambda : demand_elements.create_demand(self,frame,home),width=35,font=("Arial",10,"bold"))
                self.create_demand_button.place(relx=0.15,rely=0.05,anchor="center")

                self.modify_demand_button=ui.Button(frame,text="Modify Demand ",command = lambda : demand_elements.modify_demand(self,frame,home),width=35,font=("Arial",10,"bold"))
                self.modify_demand_button.place(relx=0.5,rely=0.05,anchor="center")
                
                self.delete_demand_button=ui.Button(frame,text="Delete Demand ",command = lambda : demand_elements.delete_demand(self,frame,home),width=35,font=("Arial",10,"bold"))
                self.delete_demand_button.place(relx=0.85,rely=0.05,anchor="center")

                self.csv_data=demand_elements.open_demand_csv(self)
                demand_elements.display_csv(self,frame,self.csv_data,1,1)
        
        
        


        def display_csv(self,frame,data,row,column,colspan=1):
                self.style=ttk.Style()
                self.style.theme_use("default")
                self.tree=ttk.Treeview(frame,columns=data[0],show="headings")
                self.tree.grid(row=row,column=column,columnspan=colspan,sticky="nsew",padx=(0,0),pady=(0,0))
                self.hbar=ttk.Scrollbar(frame,orient="horizontal",command=self.tree.xview)
                self.vbar=ttk.Scrollbar(frame,orient="vertical",command=self.tree.yview)
                self.tree.configure(xscrollcommand=self.hbar.set,yscrollcommand=self.vbar.set)
                self.hbar.grid(row=2,column=1,sticky="ew")
                self.vbar.grid(row=1,column=2,sticky="ns")
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


        def open_demand_csv(self):
                self.demand_csv_filepath= base_path / "data" / "database" / "demand.csv"
                
                with open(self.demand_csv_filepath,newline="")as f:
                    self.reader=csv.reader(f)
                    return list(self.reader)

############################################################ Create demand #########################################
        def  create_demand(self,frame,home):
                self.create_demand_window=ui.Toplevel(home)
                self.create_demand_window.title("Add Product to Warehouse")
                self.create_demand_window.configure(bg="white")
                self.create_demand_window.geometry("500x500")
                
                
                self.label_product_name = ui.Label(self.create_demand_window, text="Product Name",bg="white",font=('Arial',10))
                self.label_product_name.place(relx=0.05,rely=0.02,anchor="w")
                        
                self.entry_product_name=ui.Entry(self.create_demand_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_name.place(relx=0.05, rely=0.052, anchor="w")
                        
                self.label_product_id = ui.Label(self.create_demand_window, text="Product ID",bg="white",font=('Arial',10))
                self.label_product_id.place(relx=0.05,rely=0.12,anchor="w")

                self.entry_product_id=ui.Entry(self.create_demand_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_id.place(relx=0.05, rely=0.152, anchor='w')
                        
                self.label_product_quantity = ui.Label(self.create_demand_window, text="Product Quantity",bg="white",font=('Arial',10))
                self.label_product_quantity.place(relx=0.05,rely=0.22,anchor="w")

                self.entry_product_quantity=ui.Entry(self.create_demand_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_quantity.place(relx=0.05, rely=0.252, anchor='w')

                self.label_product_vendor=ui.Label(self.create_demand_window,text="Select Vendor id",bg="white",font=('Arial',11))
                self.label_product_vendor.place(relx=0.05,rely=0.62,anchor="w")

                self.vendor_list= VendorDataHandler.GetVendorIds(self)
                self.product_vendorid=ui.StringVar(value="Select Vendor")
                self.option_product_vendorid=ui.OptionMenu(self.create_demand_window,self.product_vendorid,*self.vendor_list)
                self.option_product_vendorid.place(relx=0.05,rely=0.67,anchor="w")
                self.option_product_vendorid.configure(bg="white")

                self.confirm_button=ui.Button(self.create_demand_window,text="CONFIRM", command = lambda : demand_elements.entry_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.9, anchor="center")

        def entry_check(self,frame,home):
                self.inventory_csv_filepath= base_path / "data" / "database" / "inventory.csv"
                if  self.entry_product_id.get() != '':
                    with open(self.inventory_csv_filepath,"r",newline="")as file:
                        self.reader=csv.DictReader(file)
                        for i in self.reader:
                            if i==[]:
                                None
                            elif i["Product id"]==self.entry_product_id.get():
                                self.response1 = messagebox.askyesno("Product Info Exists","Product with Product_ID:" + self.entry_product_id.get() + "\n"+ "Info alredy exists do yow want to use it ?"+"\n"+"Click No to retry")
                                if self.response1==True:
                                        self.create_demand_window.destroy()
                                        self.demand_data=i
                                        try:
                                                q=int(self.entry_product_quantity.get())
                                        except:
                                                messagebox.showerror("INVALID DATA","Please enter valid quantity")
                                                self.create_demand_window.destroy()
                                                demand_elements.create_demand(self,frame,home)
                                                return
                                        self.demand_data["Quantity"]=self.entry_product_quantity.get()
                                        DemandDataHandler.WriteDemandrecord(self,self.demand_data)#backend
                                        self.tree.destroy()
                                        self.csv_data=demand_elements.open_demand_csv(self)
                                        demand_elements.display_csv(self,frame,self.csv_data,1,1)
                                else:
                                        self.create_demand_window.destroy()
                                        demand_elements.create_demand(self,frame,home)   
                else:
                        messagebox.showerror("Empty id","Product id  can't be empty.")
                        self.create_demand_window.destroy()
                        demand_elements.create_demand(self,frame,home)
                        return None

                self.entry_errors=[]
                if self.entry_product_name.get()=="":
                    self.entry_errors.append("Product name")
                try:
                    q=int(self.entry_product_quantity.get())
                except:
                    self.entry_errors.append("Product quantity")

                if self.product_vendorid.get() == "Select Vendor":
                    self.entry_errors.append("Product vendor")
                    
                    
                if self.entry_errors==[]:
                    self.demand_data={}
                    self.demand_data["Product id"]=self.entry_product_id.get()
                    self.demand_data["Product name"]=self.entry_product_name.get()
                    self.demand_data["Quantity"]=self.entry_product_quantity.get()
                    self.demand_data["Vendor id"]=self.product_vendorid.get().split()[0]
                    DemandDataHandler.WriteDemandrecord(self,self.demand_data)
                    self.create_demand_window.destroy()
                    self.tree.destroy()
                    self.csv_data=demand_elements.open_demand_csv(self)
                    demand_elements.display_csv(self,frame,self.csv_data,1,1)
                    
                    
                else:
                    s=""
                    for i in self.entry_errors:
                        s=s+"\n"+"  "+i
                    messagebox.showerror("INVALID DATA ENTRY","Following entries are invalid "+"\n"+ s+"\n\n"+"Please enter valid data types")
                    self.create_demand_window.destroy()
                    demand_elements.create_demand(self,frame,home)
                    
                    self.entry_errors=[]
            
            
################################################## modify demand #######################
        def modify_demand(self,frame,home):
                self.modify_demand_window=ui.Toplevel(home)
                self.modify_demand_window.title("Modify demand")
                self.modify_demand_window.configure(bg="white")
                self.modify_demand_window.geometry("500x500")
                
                        
                self.label_product_id = ui.Label(self.modify_demand_window, text="Product ID",bg="white",font=('Arial',10))
                self.label_product_id.place(relx=0.05,rely=0.12,anchor="w")

                self.entry_product_id=ui.Entry(self.modify_demand_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_id.place(relx=0.05, rely=0.152, anchor='w')
                        
                self.label_product_quantity = ui.Label(self.modify_demand_window, text="Total Demand Quantity",bg="white",font=('Arial',10))
                self.label_product_quantity.place(relx=0.05,rely=0.22,anchor="w")

                self.entry_product_quantity=ui.Entry(self.modify_demand_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_quantity.place(relx=0.05, rely=0.252, anchor='w')

                self.confirm_button=ui.Button(self.modify_demand_window,text="CONFIRM", command = lambda : demand_elements.modify_data_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.85, anchor="center")
                
        def modify_data_check(self,frame,home):
                try:
                        q=int(self.entry_product_quantity.get())
                except:
                        messagebox.showerror("INVALID DATA","Please enter valid quantity")
                        self.modify_demand_window.destroy()
                        demand_elements.modify_demand(self,frame,home)
                        return        
                if self.entry_product_id.get()!="":
                        self.demand_csv_filepath= base_path / "data" / "database" / "demand.csv"
                        with open(self.demand_csv_filepath,"r",newline="") as f:
                                self.reader=csv.DictReader(f)
                                for i in self.reader:
                                        if i["Product id"]==self.entry_product_id.get():
                                                f.close()
                                                DemandDataHandler.modify_demand(self,i["Product id"],self.entry_product_quantity.get())
                                                self.modify_demand_window.destroy()
                                                self.tree.destroy()
                                                self.csv_data=demand_elements.open_demand_csv(self)
                                                demand_elements.display_csv(self,frame,self.csv_data,1,1)
                                                break
                                else:
                                        self.response=messagebox.askyesno("Not Found","Product not found do you want to raise demand ?")
                                        if self.response==True:
                                                self.modify_demand_window.destroy()
                                                demand_elements.create_demand(self,frame,home)
                                        else:
                                                self.modify_demand_window.destroy()

###################################################### Delete demand ######################################
        def delete_demand(self,frame,home):
                self.delete_demand_window=ui.Toplevel(home)
                self.delete_demand_window.title("Modify demand")
                self.delete_demand_window.configure(bg="white")
                self.delete_demand_window.geometry("500x500")
                
                        
                self.label_product_id = ui.Label(self.delete_demand_window, text="Product ID",bg="white",font=('Arial',10))
                self.label_product_id.place(relx=0.05,rely=0.12,anchor="w")

                self.entry_product_id=ui.Entry(self.delete_demand_window, width=40,bd=2,font=('Arial',13))
                self.entry_product_id.place(relx=0.05, rely=0.152, anchor='w')
                        

                self.confirm_button=ui.Button(self.delete_demand_window,text="CONFIRM", command = lambda : demand_elements.delete_data_check(self,frame,home),bg="white",width= 25,font=("Arial",10,"bold"))
                self.confirm_button.place(relx=0.5, rely=0.85, anchor="center")
                
        def delete_data_check(self,frame,home):      
                if self.entry_product_id.get()!="":
                        self.demand_csv_filepath= base_path / "data" / "database" / "demand.csv"
                        with open(self.demand_csv_filepath,"r",newline="") as f:
                                self.reader=csv.DictReader(f)
                                for i in self.reader:
                                        if i["Product id"]==self.entry_product_id.get():
                                                f.close()
                                                self.response=messagebox.askyesno("Warning","Do you want to completly delete this demand?")
                                                if self.response==True:
                                                        self.delete_demand_window.destroy()
                                                        DemandDataHandler.delete_demand(self,i["Product id"])
                                                        self.tree.destroy()
                                                        self.csv_data=demand_elements.open_demand_csv(self)
                                                        demand_elements.display_csv(self,frame,self.csv_data,1,1)
                                                
                                                else:
                                                        self.delete_demand_window.destroy()
                                                
                                                break
                                else:
                                        self.response=messagebox.askyesno("Not Found","Demand not found to delete Do you want to retry ?")
                                        if self.response==True:
                                                self.delete_demand_window.destroy()
                                                demand_elements.delete_demand(self,frame,home)
                                        else:
                                                self.delete_demand_window.destroy()









                                                
