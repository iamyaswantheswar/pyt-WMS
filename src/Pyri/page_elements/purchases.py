import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
base_path = Path(__file__).parent.parent.parent.parent
class purchases_elements:
    def purchases_ele(self,frame,home):
        frame.grid_columnconfigure(0,minsize=200)
        self.add_product_button=ui.Button(frame,text="Add product",command = lambda : purchases_elements.add_product(self,home))
        self.add_product_button.place(relx=0.04,rely=0.05)
        self.csv_data=purchases_elements.open_purchases_csv(self)
        purchases_elements.display_csv(self,frame,self.csv_data,0,1)
        
        
        
    def open_purchases_csv(self):
        self.purchases_csv_filepath= base_path / "data" / "database" / "purchases.csv"
        with open(self.purchases_csv_filepath,newline="")as f:
            self.reader=csv.reader(f)
            return list(self.reader)
        
        

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
            
        
    def add_product(self,home):
        self.add_product_window=ui.Toplevel(home)
        self.add_product_window.title("Add Product to Warehouse")
        self.add_product_window.configure(bg="white")
        self.add_product_window.geometry("400x600")
        #self.add_product_window.grab_set()
        #self.add_product_window.focus_set()
        self.label_product_name = ui.Label(self.add_product_window, text="Product Name",bg="white")
        self.label_product_name.place(relx=0,rely=0.05,anchor="w")
                
        self.entry_product_name=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_name.place(relx=0, rely=0.1, anchor="w")
                
        self.label_product_id = ui.Label(self.add_product_window, text="Product ID",bg="white")
        self.label_product_id.place(relx=0,rely=0.2,anchor="w")

        self.entry_product_id=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_id.place(relx=0, rely=0.25, anchor='w')
                
        self.label_product_quantity = ui.Label(self.add_product_window, text="Product Quantity",bg="white")
        self.label_product_quantity.place(relx=0,rely=0.35,anchor="center")

        self.entry_product_quantity=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_quantity.place(relx=0, rely=0.4, anchor='w')
                                            
        self.label_product_cost = ui.Label(self.add_product_window, text="Product Cost price",bg="white")
        self.label_product_cost.place(relx=0,rely=0.5,anchor="w")

        self.entry_product_cost=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_cost.place(relx=0, rely=0.55, anchor='w')
                
        self.label_product_exp = ui.Label(self.add_product_window, text="Product Expiry date DD-MM-YYYY",bg="white")
        self.label_product_exp.place(relx=0,rely=0.65,anchor="w")

        self.entry_product_exp=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_exp.place(relx=0, rely=0.7, anchor='w')
        
        
        self.cal_button=ui.Button(self.add_product_window,text="pickdate", command = lambda : purchases_elements.open_calendar(self,home))
        self.cal_button.place(relx=0, rely=0.8, anchor='w')
        
                
        self.label_product_category = ui.Label(self.add_product_window, text="Product Categeory")
        self.label_product_category.place(relx=0,rely=0.9,anchor="w")
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
                
            
            
        
                
