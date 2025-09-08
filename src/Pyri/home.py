import tkinter as ui
import sys
from pathlib import Path
import platform
from tkinter import messagebox

from page_elements.purchases import *
from page_elements.dashboard import *
from page_elements.inventory import *
from page_elements.demand import *
from page_elements.sales import *


class cmds():
    def __init__(self, home):
        self.home = home
        self.lable_frame = None
        
        self.dashboard_ui()

    def dest(self):
        if self.lable_frame is not None:
            self.lable_frame.destroy()

    def dashboard_ui(self):
        self.dest()
        print("user entered dashboard")
        self.lable_frame = ui.Frame(self.home, bg="#001F3F")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        dashboard_elements.dashboard_ele(self,self.lable_frame)
        

    def inventory_ui(self):
        self.dest()
        print("user entered inventory")
        self.lable_frame = ui.Frame(self.home,bg="#001F3F")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        inventory_elements.inventory_ele(self,self.lable_frame)

    def sales_ui(self):
        self.dest()
        print("user entered sales")
        self.lable_frame = ui.Frame(self.home,bg="#001F3F")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        sales_elements.sales_ele(self,self.lable_frame,self.home)

    def purchases_ui(self):
        self.dest()
        print("user entered purchases")
        self.lable_frame = ui.Frame(self.home,bg="#001F3F")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        purchases_elements.purchases_ele(self,self.lable_frame,self.home)

    def demand_ui(self):
        self.dest()
        print("user entered demand")
        self.lable_frame = ui.Frame(self.home,bg="#001F3F")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        demand_elements.demand_ele(self,self.lable_frame,home)

    def createcmd(self, name):
        func = getattr(self, name.lower() + "_ui", None)
        if callable(func):
            func()


class topbarelements:
    def __init__(self, label, topbar, command):
        self.button = ui.Button(topbar,text=label,bg="#001F3F",fg="white",bd=0,font=("Times", 10, "bold"),anchor="w",command=command)
        self.button.config(width=10, height=2, borderwidth=0, highlightthickness=0)
        self.button.bind("<Enter>", lambda e: self.button.config(bg="#001F3F", fg="black"))
        self.button.bind("<Leave>", lambda e: self.button.config(bg="#001F3F", fg="white"))

    def place(self, x, y):
        self.button.place(relx=x, rely=y)


# Main window
home = ui.Tk()
home.title("WAREHOUSE MANAGEMENT SYSTEM")
home.geometry("700x500")
#home.attributes("-fullscreen", True)
# Maximize based on OS
system = platform.system()
if system == "Windows":
    home.state('zoomed')  
elif system == "Darwin":  # macOS
    home.attributes('-zoomed', True)
else:
    home.attributes('-zoomed', True)
topbar = ui.Frame(home, bg="#001F3F", height=50)
topbar.pack(side="top", fill="x")
topbar.pack_propagate(False)

# One instance to control all pages
controller = cmds(home)

# Create buttons
elementpos = 0.07
pages = ["Dashboard", "Inventory", "Sales", "Purchases", "Demand"]
for page in pages:
    btn = topbarelements(page, topbar, lambda p=page: controller.createcmd(p))
    btn.place(elementpos, 0.05)
    elementpos += 0.15



home.mainloop()
