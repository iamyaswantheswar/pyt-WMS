
import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
import shutil
from datetime import datetime
from tkinter import messagebox
#from database.inventoryDH import Product,search_product_name
from src.Pyri.database.inventoryDH import Product,Inventory

base_path = Path(__file__).parent.parent.parent.parent
inventory_path = base_path / "data" / "database" / "inventory.csv"

class inventory_elements:

    def open_inventory_csv(self):
        self.inventory_csv_filepath = inventory_path

        with open(self.inventory_csv_filepath, newline="") as f:
            self.reader = csv.reader(f)
            return list(self.reader)

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


    def inventory_ele(self, frame, home):
        frame.grid_columnconfigure(0, minsize=250)
        '''
        self.add_product_button = ui.Button(frame, text="Add new vendor",
                                            command=lambda: purchases_elements.add_vendor(self, home, frame), width=25,
                                            font=("Arial", 10, "bold"))
        self.add_product_button.place(relx=0.02, rely=0.1)

        self.add_product_button = ui.Button(frame, text="Add new product",
                                            command=lambda: purchases_elements.add_product(self, home, frame), width=25,
                                            font=("Arial", 10, "bold"))
        self.add_product_button.place(relx=0.02, rely=0.26)

        self.stock_existing_product_button = ui.Button(frame, text="Add stock ",
                                                       command=lambda: purchases_elements.add_stock(self, home, frame),
                                                       width=25, font=("Arial", 10, "bold"))
        self.stock_existing_product_button.place(relx=0.02, rely=0.42)

        self.modify_purchase_button = ui.Button(frame, text="Modify Purchase ",
                                                command=lambda: purchases_elements.modify_purchase(self, home, frame),
                                                width=25, font=("Arial", 10, "bold"))
        self.modify_purchase_button.place(relx=0.02, rely=0.58)

        self.delete_purchase_button = ui.Button(frame, text="Delete Purchase ",
                                                command=lambda: purchases_elements.delete_purchase(self, home, frame),
                                                width=25, font=("Arial", 10, "bold"))
        self.delete_purchase_button.place(relx=0.02, rely=0.74)

        self.view_history_button = ui.Button(frame, text="View Purchase history ",
                                             command=lambda: purchases_elements.view_purchase_history(self, home),
                                             width=25, font=("Arial", 10, "bold"))
        self.view_history_button.place(relx=0.02, rely=0.9)
        '''
        #inventory_elements.refresh_csv(self, frame, home)
        self.csv_data = Inventory.open_inventory_csv(self)
        inventory_elements.display_csv(self, frame, self.csv_data,0,1)
