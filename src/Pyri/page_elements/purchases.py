import tkinter as ui
from tkcalendar import Calendar
class purchases_elements:
    def purchases_ele(self,frame,home):
        self.lbl = ui.Label(frame, text="welcome to purchases")
        self.lbl.place(relx=0.5, rely=0.5, anchor="center")
        self.add_product_button=ui.Button(frame,text="Add product",command = lambda : purchases_elements.add_product(self,home))
        self.add_product_button.place(relx=0.5,rely=0.7)

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
        self.label_product_name = ui.Label(self.add_product_window, text="Product Name")
        self.label_product_name.place(relx=0.1,rely=0.05,anchor="w")
                
        self.entry_product_name=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_name.place(relx=0.1, rely=0.1, anchor=ui.CENTER)
                
        self.label_product_id = ui.Label(self.add_product_window, text="Product ID")
        self.label_product_id.place(relx=0.1,rely=0.15,anchor="center")

        self.entry_product_id=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_id.place(relx=0.1, rely=0.2, anchor=ui.CENTER)
                
        self.label_product_quantity = ui.Label(self.add_product_window, text="Product Quantity")
        self.label_product_quantity.place(relx=0.25,rely=0.25,anchor="center")

        self.entry_product_quantity=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_quantity.place(relx=0.1, rely=0.3, anchor=ui.CENTER)
                                            
        self.label_product_cost = ui.Label(self.add_product_window, text="Product Cost price")
        self.label_product_cost.place(relx=0.1,rely=0.35,anchor="center")

        self.entry_product_cost=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_cost.place(relx=0.1, rely=0.4, anchor=ui.CENTER)
                
        self.label_product_exp = ui.Label(self.add_product_window, text="Product Expiry date DD-MM-YYYY")
        self.label_product_exp.place(relx=0.1,rely=0.45,anchor="center")

        self.entry_product_exp=ui.Entry(self.add_product_window, width=40,bd=2)
        self.entry_product_exp.place(relx=0.1, rely=0.5, anchor=ui.CENTER)
        
        
        self.cal_button=ui.Button(self.add_product_window,text="pickdate", command = lambda : purchases_elements.open_calendar(self,home))
        self.cal_button.pack(side="left")
        
                
        self.label_product_category = ui.Label(self.add_product_window, text="Product Categeory")
        self.label_product_category.place(relx=0.1,rely=0.55,anchor="w")
                
