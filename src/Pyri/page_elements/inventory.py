
import tkinter as ui
from pathlib import Path
from tkinter import ttk
import csv
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

        self.search_button = ui.Button(frame, text="Search",
                                       command=lambda: inventory_elements.search_product_window(self, home, frame), width=25,
                                       font=("Arial", 10, "bold"))
        self.search_button.place(relx=0.02, rely=0.1)
        self.csv_data = Inventory.open_inventory_csv(self)
        inventory_elements.display_csv(self, frame, self.csv_data,0,1)

    def search_product_window(self, frame, home):
        self.view_search_window = ui.Toplevel(home)
        self.view_search_window.title("Search Product")
        self.view_search_window.configure(bg="white")
        self.view_search_window.geometry("800x150")

        self.view_search = ui.Label(self.view_search_window, text="Enter search query", bg="white",
                                    font=('Arial', 10))
        self.view_search.place(relx=0.05, rely=0.2, anchor="w")

        self.search_entry_box = ui.Entry(self.view_search_window, width=30, bd=2, font=('Arial', 13))
        self.search_entry_box.place(relx=0.03, rely=0.5, anchor='w')

        self.drop_down_box = ttk.Combobox(self.view_search_window, width=27, font=('Arial', 13), state='readonly')
        self.drop_down_box['values'] = ('Product Name', 'Product ID', 'Vendor ID')
        self.drop_down_box.place(relx=0.5, rely=0.5, anchor='w')

        self.confirm_button = ui.Button(self.view_search_window, text="CONFIRM",
                                        command=lambda: inventory_elements.view_search_result(self,home,frame,self.search_entry_box.get(),self.drop_down_box.get()),
                                        bg="white", width=25, font=("Arial", 10, "bold"))
        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")

    def view_search_result(self,home,frame,query,by_what):
        self.view_search_window.destroy()
        self.search_result_window = ui.Toplevel(home)
        self.search_result_window.title(f"Search results for '{query}'")
        self.search_result_window.configure(bg="white")

        self.result_data = Inventory.search_product_name(self, query, by_what)

        inventory_elements.display_search_result(self, self.search_result_window, self.result_data, 0, 0)

    def display_search_result(self, window, data, row, column, colspan=2):
        self.tree = ttk.Treeview(window, columns=data[0], show="headings")
        self.tree.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=(0, 0), pady=(0, 0))
        #self.hbar = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        #self.vbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.hbar.grid(row=1, column=1, sticky="ew")
        self.vbar.grid(row=0, column=2, sticky="ns")
        # configure coloumns
        for col in data[0]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=120)
            # inserting rows
        for row_data in data[1:]:
            self.tree.insert("", "end", values=row_data)
        return self.tree