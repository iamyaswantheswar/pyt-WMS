import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
import shutil
from datetime import datetime
from tkinter import messagebox
from database.CustomerDH import CustomerDataHandler


base_path = Path(__file__).parent.parent.parent.parent
class sales_elements:
        def sales_ele(self,frame,home):
                frame.grid_columnconfigure(0,minsize=250)
                self.new_sale_button=ui.Button(frame,text="Add customer",command = lambda : sales_elements.add_customer(self,frame,home),width=25,font=("Arial",10,"bold"))
                self.new_sale_button.place(relx=0.02,rely=0.05)
                
                self.sale_new_cus_button=ui.Button(frame,text="New Sale",command = lambda : None,width=25,font=("Arial",10,"bold"))
                self.sale_new_cus_button.place(relx=0.02,rely=0.25)
                
                self.modify_sale_button=ui.Button(frame,text="Modify sale ",command = lambda : None,width=25,font=("Arial",10,"bold"))
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
                            if i["Customer id"]==self.entry_vendor_id.get():
                                messagebox.showerror("Customer exists","Customer id already present in database")
                                self.add_customer_window.destroy()
                                sales_elements.add_customer(self,frame,home)
                                break
                        else:
                            CustomerDataHandler.add_customer(self,self.entry_customer_id.get(),self.entry_customer_name.get())
                            self.add_customer_window.destroy()











