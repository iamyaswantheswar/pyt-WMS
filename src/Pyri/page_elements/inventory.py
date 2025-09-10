import tkinter as ui
from pathlib import Path
from tkinter import ttk
import csv
from database.inventoryDH import  Inventory

base_path = Path(__file__).parent.parent.parent.parent
inventory_path = base_path / "data" / "database" / "inventory.csv"
filter_usage_location = False
filter_usage_expiry = False

class inventory_elements:

    def open_inventory_csv(self):
        self.inventory_csv_filepath = inventory_path

        with open(self.inventory_csv_filepath, newline="") as f:
            self.reader = csv.reader(f)
            return list(self.reader)

    def display_csv(self, frame, data, row, column, colspan=1):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.tree = ttk.Treeview(frame, columns=data[0], show="headings")
        self.tree.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=(0, 0), pady=(0, 0))
        self.hbar = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.vbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
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
        frame.grid_rowconfigure(row, weight=1)
        frame.grid_columnconfigure(column, weight=1)
        return self.tree

    def inventory_ele(self, frame, home):
        frame.grid_columnconfigure(0, minsize=250)

        self.search_button = ui.Button(frame, text="Search",
                                       command=lambda: inventory_elements.search_product_window(self, home, frame),
                                       width=25,
                                       font=("Arial", 10, "bold"))
        self.search_button.place(relx=0.02, rely=0.1)

        self.filter_location_button = ui.Button(frame, text="Filter by Location",
                                       command=lambda: inventory_elements.filter_by_location_window(self, frame, home),
                                       width=25,
                                       font=("Arial", 10, "bold"))
        self.filter_location_button.place(relx=0.02, rely=0.4)

        self.csv_data = Inventory.open_inventory_csv(self)
        inventory_elements.display_csv(self, frame, self.csv_data, 0, 1)

    #################################### Search ###########################################

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
        self.drop_down_box.set('Product Name')
        self.drop_down_box.place(relx=0.5, rely=0.5, anchor='w')

        self.confirm_button = ui.Button(self.view_search_window, text="CONFIRM",
                                        command=lambda: inventory_elements.view_search_result(self, home, frame,
                                                                                              self.search_entry_box.get(),
                                                                                              self.drop_down_box.get()),
                                        bg="white", width=25, font=("Arial", 10, "bold"))
        self.confirm_button.place(relx=0.5, rely=0.8, anchor="center")

    def view_search_result(self, home, frame, query, by_what):
        self.view_search_window.destroy()
        self.search_result_window = ui.Toplevel(home)
        self.search_result_window.title(f"Search results for '{query}'")
        self.search_result_window.configure(bg="white")

        self.result_data = Inventory.search_product_name(self, query, by_what)

        inventory_elements.display_search_result(self, self.search_result_window, self.result_data, 0, 0)

    def display_search_result(self, window, data, row, column, colspan=2):
        self.tree = ttk.Treeview(window, columns=data[0], show="headings")
        self.tree.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=(0, 0), pady=(0, 0))

        self.hbar_search = ttk.Scrollbar(window, orient="horizontal", command=self.tree.xview)
        self.vbar_search = ttk.Scrollbar(window, orient="vertical", command=self.tree.yview)

        self.tree.configure(xscrollcommand=self.hbar_search.set, yscrollcommand=self.vbar_search.set)

        self.hbar_search.grid(row=1, column=0, columnspan=colspan, sticky="ew")
        self.vbar_search.grid(row=0, column=colspan, sticky="ns")

        # Configure grid weights
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # configure coloumns
        for col in data[0]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=120)
            # inserting rows
        for row_data in data[1:]:
            self.tree.insert("", "end", values=row_data)
        return self.tree

    ################################## Filter ######################################

    def filter_by_location_window(self, frame, home):
        self.view_filter_by_location_window = ui.Toplevel(home)
        self.view_filter_by_location_window.title("Filter Inventory by Location")
        self.view_filter_by_location_window.configure(bg="white")
        self.view_filter_by_location_window.geometry("800x150")

        self.product_location_blocks = ["Block 1", 'Block 2', 'Block 3', "Block 4"]
        self.product_blocks = ui.StringVar(value="Select Block")
        self.option_product_location_block = ui.OptionMenu(self.view_filter_by_location_window, self.product_blocks,
                                                           *self.product_location_blocks)
        self.option_product_location_block.place(relx=0.05, rely=0.39, anchor="w")
        self.option_product_location_block.configure(bg="white")

        self.product_location_zones = ["Zone 1", 'Zone 2', 'Zone 3', "Zone 4"]
        self.product_zones = ui.StringVar(value="Select Zone")
        self.option_product_location_zone = ui.OptionMenu(self.view_filter_by_location_window, self.product_zones,
                                                          *self.product_location_zones)
        self.option_product_location_zone.place(relx=0.22, rely=0.39, anchor="w")
        self.option_product_location_zone.configure(bg="white")

        self.product_location_aisles = ["Aisle 1", 'Aisle 2', 'Aisle 3', "Aisle 4"]
        self.product_aisles = ui.StringVar(value="Select Aisle")
        self.option_product_location_aisle = ui.OptionMenu(self.view_filter_by_location_window, self.product_aisles,
                                                           *self.product_location_aisles)
        self.option_product_location_aisle.place(relx=0.42, rely=0.39, anchor="w")
        self.option_product_location_aisle.configure(bg="white")

        self.product_location_racks = ["Rack 1", 'Rack 2', 'Rack 3', "Rack 4"]
        self.product_racks = ui.StringVar(value="Select Rack")
        self.option_product_location_rack = ui.OptionMenu(self.view_filter_by_location_window, self.product_racks,
                                                          *self.product_location_racks)
        self.option_product_location_rack.place(relx=0.62, rely=0.39, anchor="w")
        self.option_product_location_rack.configure(bg="white")

        self.product_location_shelfs = ["Shelf 1", 'Shelf 2', 'Shelf 3', "Shelf 4"]
        self.product_shelfs = ui.StringVar(value="Select Shelf")
        self.option_product_location_shelf = ui.OptionMenu(self.view_filter_by_location_window, self.product_shelfs,
                                                           *self.product_location_shelfs)
        self.option_product_location_shelf.place(relx=0.82, rely=0.39, anchor="w")
        self.option_product_location_shelf.configure(bg="white")

        self.confirm_button = ui.Button(self.view_filter_by_location_window, text="CONFIRM",
                                        command=lambda: inventory_elements.filter_by_location_result_window(self, frame,
                                                                                                            home),
                                        bg="white",
                                        width=25, font=("Arial", 10, "bold"))
        self.confirm_button.place(relx=0.5, rely=0.95, anchor="center")

    def filter_by_location_result_window(self, frame, home):
        self.view_filter_by_location_window.destroy()
        self.product_block = self.product_blocks.get()[-1]
        self.product_zone = self.product_zones.get()[-1]
        self.product_aisle = self.product_aisles.get()[-1]
        self.product_rack = self.product_racks.get()[-1]
        self.product_shelf = self.product_shelfs.get()[-1]
        self.product_location = self.product_block + self.product_zone + self.product_aisle + self.product_rack + self.product_shelf
        self.csv_data = Inventory.filter_inventory_location(self,self.product_block,self.product_zone,self.product_aisle,self.product_rack,self.product_shelf,filter_usage=filter_usage_location)
        self.tree.destroy()
        inventory_elements.display_csv(self, frame, self.csv_data, 0, 1)
        filter_usage_location = True
