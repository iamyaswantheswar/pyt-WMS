import tkinter as ui
from tkcalendar import Calendar
from pathlib import Path
from tkinter import ttk
import csv
from datetime import datetime
from tkinter import messagebox

class sales_elements:
        def sales_ele(self,frame,home):
                frame.grid_columnconfigure(0,minsize=300)
                self.new_sale_button=ui.Button(frame,text="New sale",command = lambda : None ,width=30,font=("Arial",10,"bold"))
                self.new_sale_button.place(relx=0.02,rely=0.05)
                
                self.sale_new_cus_button=ui.Button(frame,text="Sale to New Customer ",command = lambda : None,width=30,font=("Arial",10,"bold"))
                self.sale_new_cus_button.place(relx=0.02,rely=0.25)
                
                self.modify_sale_button=ui.Button(frame,text="Modify sale ",command = lambda : None,width=30,font=("Arial",10,"bold"))
                self.modify_sale_button.place(relx=0.02,rely=0.45)
                
                self.delete_sale_button=ui.Button(frame,text="Delete sale ",command = lambda : None,width=30,font=("Arial",10,"bold"))
                self.delete_sale_button.place(relx=0.02,rely=0.65)
                
                
                self.view_history_button=ui.Button(frame,text="View sales history ",command = lambda : None ,width=30,font=("Arial",10,"bold"))
                self.view_history_button.place(relx=0.02,rely=0.85)
