import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
import shutil
from datetime import datetime
from tkinter import messagebox

base_path = Path(__file__).parent.parent.parent.parent
class sales_elements:
        def sales_ele(self,frame,home):
                frame.grid_columnconfigure(0,minsize=250)
                self.new_sale_button=ui.Button(frame,text="Add customer",command = lambda : None ,width=25,font=("Arial",10,"bold"))
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

















