import tkinter as ui
import csv
from pathlib import Path
import time
from datetime import datetime
from PIL import Image,ImageTk
from database.DashboardDH import DashboardDataHandler
base_path = Path(__file__).parent.parent.parent.parent


class dashboard_elements:
    def dashboard_ele(self, frame,home):
        frame.grid_columnconfigure(0,minsize=20)
        frame.grid_rowconfigure(0,minsize=50)

        frame.grid_columnconfigure(1,minsize=250)
        frame.grid_rowconfigure(1,minsize=200)

        frame.grid_columnconfigure(2,minsize=20)
        frame.grid_rowconfigure(2,minsize=20)

        frame.grid_columnconfigure(3,minsize=250)
        frame.grid_rowconfigure(3,minsize=200)

        frame.grid_columnconfigure(4,minsize=20)
        frame.grid_rowconfigure(4,minsize=20)

        frame.grid_rowconfigure(5,minsize=200)

        frame.grid_rowconfigure(6,minsize=20)

        frame.grid_rowconfigure(7,minsize=200)

        frame.grid_rowconfigure(8,weight=1)
        frame.grid_columnconfigure(5,weight=1)


        


        self.frame_time = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_time.grid(row=1,column=1,sticky="nsew")

        def update_time():
            self.current_time=time.strftime('%I:%M:%S %p')
            self.time_lable.configure(text =self.current_time)
            self.frame_time.after(1000,update_time)

        self.time_label_title=ui.Label(self.frame_time,text="Hola Manager :)",font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.1)
        
        self.time_lable=ui.Label(self.frame_time,font=("Didot",18,"bold"),bg="white")
        self.time_lable.place(relx=0.05,rely=0.6)

        self.frame_date = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_date.grid(row=1,column=3,sticky="nsew")

        self.date_lable_title=ui.Label(self.frame_date,text="Today is",bg="white",font=("Didot",20,"bold")).place(relx=0.05,rely=0.1)

        self.current_date=datetime.now().strftime('%b %d %Y %a')
        self.date_lable=ui.Label(self.frame_date,text=self.current_date,font=("Didot",18,"bold"),bg="white")
        self.date_lable.place(relx=0.05,rely=0.6)

        self.frame_tprofit = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_tprofit.grid(row=3,column=1,sticky="nsew")

        self.tprofit_label_title=ui.Label(self.frame_tprofit,text="Todays profit ",font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.1)

        self.tprofit_lable=ui.Label(self.frame_tprofit ,text= "₹" + " "+ str(DashboardDataHandler.Todayprofit(self)),font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.6)

        self.frame_tsales = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_tsales.grid(row=3,column=3,sticky="nsew")

        self.tsales_label_title=ui.Label(self.frame_tsales,text="Todays sales ",font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.1)

        self.tsales_lable=ui.Label(self.frame_tsales,text= "₹" + " "+ str(DashboardDataHandler.Todaysale(self)),font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.6)

        self.frame_mprofit = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_mprofit.grid(row=5,column=1,sticky="nsew")

        self.mprofit_label_title=ui.Label(self.frame_mprofit,text="Months profit ",font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.1)

        self.mprofit_lable=ui.Label(self.frame_mprofit ,text="₹" + " "+ str(DashboardDataHandler.Monthprofit(self)),font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.6)

        self.frame_msales = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_msales.grid(row=5,column=3,sticky="nsew")

        self.msales_label_title=ui.Label(self.frame_msales,text="Month sales ",font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.1)

        self.msales_lable=ui.Label(self.frame_msales ,text="₹" + " "+ str(DashboardDataHandler.Monthsale(self)),font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.6)

        self.frame_stockvalue = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_stockvalue.grid(row=7,column=1,sticky="nsew")

        self.stockvalue_title=ui.Label(self.frame_stockvalue,text="Total Stock Value ",font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.1)

        self.stockvalue_lable=ui.Label(self.frame_stockvalue ,text="₹" + " "+ str(DashboardDataHandler.TotalStock(self)),font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.6)

        self.frame_demand = ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.frame_demand.grid(row=7,column=3,sticky="nsew")

        self.demand_title=ui.Label(self.frame_demand,text="Unfullfilled demands",font=("Didot",15,"bold"),bg="white").place(relx=0.05,rely=0.1)

        self.deamand_lable=ui.Label(self.frame_demand ,text=str(DashboardDataHandler.Demandcount(self)),font=("Didot",18,"bold"),bg="white").place(relx=0.05,rely=0.6)

        self.main_graph_frame=ui.Frame(frame, bg="#FFFFFF",highlightbackground="black", highlightcolor="black", highlightthickness=5)
        self.main_graph_frame.grid(column=5,row=1,rowspan=7,sticky="nsew")

        DashboardDataHandler.salesgraph(self)
        
        base_path = Path(__file__).parent.parent.parent.parent
        
        self.main_graph_frame.grid_columnconfigure(0,minsize=10)
        self.main_graph_frame.grid_rowconfigure(0,minsize=10)

        self.main_graph_frame.grid_columnconfigure(1,weight=1)
        self.main_graph_frame.grid_rowconfigure(1,minsize=400)

        self.main_graph_frame.grid_columnconfigure(2,minsize=10)

        self.main_graph_frame.grid_rowconfigure(2,minsize=10)
        self.main_graph_frame.grid_rowconfigure(3,minsize=400)
        self.main_graph_frame.grid_rowconfigure(4,minsize=20)

        self.canvas_sales=ui.Canvas(self.main_graph_frame,bg="white")
        self.canvas_sales.grid(column=1,row=1,sticky="nsew")

        self.sale_graph=Image.open(base_path / "src" / "images" / "Dashboard_graphs" / "Month_sales.png")

        self.sale_graph=self.sale_graph.resize((1440,400))

        self.image_obj = ImageTk.PhotoImage(self.sale_graph)

        self.canvas_sales.create_image(0,0, image=self.image_obj,anchor="nw")

        

        DashboardDataHandler.profitgraph(self)

        base_path = Path(__file__).parent.parent.parent.parent

        self.canvas_profit=ui.Canvas(self.main_graph_frame,bg="white")
        self.canvas_profit.grid(column=1,row=3,sticky="nsew")

        self.profit_graph=Image.open(base_path / "src" / "images" / "Dashboard_graphs" / "Month_profit.png")

        self.profit_graph = self.profit_graph.resize((1440,400))

        self.image_obj1 = ImageTk.PhotoImage(self.profit_graph)

        self.canvas_profit.create_image(0,0, image=self.image_obj1,anchor="nw")

        
        update_time()


        



