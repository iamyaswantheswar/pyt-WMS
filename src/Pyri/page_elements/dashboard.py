import tkinter as ui
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from pathlib import Path
import time
from datetime import datetime 
base_path = Path(__file__).parent.parent.parent.parent

class dashboard_elements:
    def dashboard_ele(self, frame,home):
        frame.grid_columnconfigure(0,minsize=20)
        frame.grid_rowconfigure(0,minsize=45)

        frame.grid_columnconfigure(1,minsize=250)
        frame.grid_rowconfigure(1,minsize=150)

        frame.grid_columnconfigure(2,minsize=20)
        frame.grid_rowconfigure(2,minsize=20)

        frame.grid_columnconfigure(3,minsize=250)
        frame.grid_rowconfigure(3,minsize=150)

        frame.grid_columnconfigure(4,minsize=20)
        frame.grid_rowconfigure(4,minsize=20)

        frame.grid_rowconfigure(5,minsize=150)

        frame.grid_rowconfigure(6,minsize=20)

        frame.grid_rowconfigure(7,minsize=150)


        


        self.frame_time = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_time.grid(row=1,column=1,sticky="nsew")

        def update_time():
            self.current_time=time.strftime('%I:%M:%S %p')
            self.time_lable.configure(text =self.current_time)
            self.frame_time.after(1000,update_time)


        self.time_lable=ui.Label(self.frame_time,font=("Times",20,"bold"),bg="white")
        self.time_lable.place(relx=0.5,rely=0.5,anchor="center")

        self.frame_date = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_date.grid(row=1,column=3,sticky="nsew")

        self.current_date=datetime.now().strftime('%a, %b %d, %Y')
        self.date_lable=ui.Label(self.frame_date,text=self.current_date,font=("Times",20,"bold"),bg="white")
        self.date_lable.place(relx=0.5,rely=0.7,anchor="center")

        self.frame_tprofit = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_tprofit.grid(row=3,column=1,sticky="nsew")

        self.frame_tsales = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_tsales.grid(row=3,column=3,sticky="nsew")

        self.frame_mprofit = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_mprofit.grid(row=5,column=1,sticky="nsew")

        self.frame_msales = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_msales.grid(row=5,column=3,sticky="nsew")

        self.frame_stockvalue = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_stockvalue.grid(row=7,column=1,sticky="nsew")

        self.frame_demand = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_demand.grid(row=7,column=3,sticky="nsew")

        update_time()


        



