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
        
    '''#def split_stock(self,home):
        def get_locations_qty(self):
            self.no_of_locations=self.entry_locations_query.get()
            self.locations_query.destroy()
            self.multiple_location_page=ui.Toplevel(home)
            self.multiple_location_page.title("Add locations")
            self.multiple_location_page.configure(bg="white")
            self.location_variables={}
            self.lable_place_y_variable=0
            for i in range(0,int(self.no_of_locations)):
                self.location_variables[i]=ui.Label(self.multiple_location_page,text=f"Location {i+1}")
                self.location_variables[i].place(relx=0.1,rely=self.lable_place_y_variable)
                self.lable_place_y_variable+=0.05'





        self.locations_query=ui.Toplevel(home)
        self.locations_query.title("Location splitter")
        self.locations_query.configure(bg="white")
        self.locations_query.geometry("150x100")
        self.lable_locations_query=ui.Label(self.locations_query,text="Enter the no of locations to split the stock")
        self.lable_locations_query.grid(row=0,column=1)
        self.entry_locations_query=ui.Entry(self.locations_query,width=30)
        self.entry_locations_query.grid(row=1,column=1)
        self.button_locations_query=ui.Button(self.locations_query,text="Enter",command= lambda :get_locations_qty(self))
        self.button_locations_query.grid(row=2,column=1)'''


        
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
        self.label_product_name.place(relx=0.05,rely=0.05,anchor="w")
                
        self.entry_product_name=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_name.place(relx=0.05, rely=0.1, anchor="w")
                
        self.label_product_id = ui.Label(self.add_product_window, text="Product ID",bg="white")
        self.label_product_id.place(relx=0.05,rely=0.2,anchor="w")

        self.entry_product_id=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_id.place(relx=0.05, rely=0.25, anchor='w')
                
        self.label_product_quantity = ui.Label(self.add_product_window, text="Product Quantity",bg="white")
        self.label_product_quantity.place(relx=0.05,rely=0.35,anchor="w")

        self.entry_product_quantity=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_quantity.place(relx=0.05, rely=0.4, anchor='w')
                                            
        self.label_product_cost = ui.Label(self.add_product_window, text="Product Cost price",bg="white")
        self.label_product_cost.place(relx=0.05,rely=0.5,anchor="w")

        self.entry_product_cost=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_cost.place(relx=0.05, rely=0.55, anchor='w')
                
        self.label_product_exp = ui.Label(self.add_product_window, text="Product Expiry date DD-MM-YYYY",bg="white")
        self.label_product_exp.place(relx=0.05,rely=0.65,anchor="w")

        self.entry_product_exp=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_exp.place(relx=0.05, rely=0.7, anchor='w')
        
        
        self.cal_button=ui.Button(self.add_product_window,text="pickdate", command = lambda : purchases_elements.open_calendar(self,home))
        self.cal_button.place(relx=0.45, rely=0.7, anchor='w')
        
        self.label_product_location=ui.Label(self.add_product_window,text="Product location")
        self.label_product_location.place(relx=0.05,rely=0.75,anchor="w")

        self.product_location_blocks=["Block 1",'Block 2','Block 3',"Block 4"]
        self.product_block=ui.StringVar(value="Select Block")
        self.option_product_location_block=ui.OptionMenu(self.add_product_window,self.product_block,*self.product_location_blocks)
        self.option_product_location_block.place(relx=0.05,rely=0.8)

        self.product_location_zones=["Zone 1",'Zone 2','Zone 3',"Zone 4"] 
        self.product_zone=ui.StringVar(value="Select Zone")
        self.option_product_location_zone=ui.OptionMenu(self.add_product_window,self.product_zone,*self.product_location_zones)
        self.option_product_location_zone.place(relx=0.2,rely=0.8)

        self.product_location_aisles=["Aisle 1",'Aisle 2','Aisle 3',"Aisle 4"] 
        self.product_aisle=ui.StringVar(value="Select Aisle")
        self.option_product_location_aisle=ui.OptionMenu(self.add_product_window,self.product_aisle,*self.product_location_aisles)
        self.option_product_location_aisle.place(relx=0.4,rely=0.8)

        self.product_location_racks=["Rack 1",'Rack 2','Rack 3',"Rack 4"] 
        self.product_rack=ui.StringVar(value="Select Rack")
        self.option_product_location_rack=ui.OptionMenu(self.add_product_window,self.product_rack,*self.product_location_racks)
        self.option_product_location_rack.place(relx=0.6,rely=0.8)

        self.product_location_shelfs=["Shelf 1",'Shelf 2','Shelf 3',"Shelf 4"] 
        self.product_shelf=ui.StringVar(value="Select Shelf")
        self.option_product_location_shelf=ui.OptionMenu(self.add_product_window,self.product_shelf,*self.product_location_shelfs)
        self.option_product_location_shelf.place(relx=0.8,rely=0.8)


    
        #self.split_stock_button=ui.Button(self.add_product_window,text="Split stock",command = lambda :purchases_elements.split_stock(self,home))
        #self.split_stock_button.place(relx=0.05,rely=0.9,anchor="w")


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
                
            
            
        
                
