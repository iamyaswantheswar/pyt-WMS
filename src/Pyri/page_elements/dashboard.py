import tkinter as ui
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from pathlib import Path
base_path = Path(__file__).parent.parent.parent.parent

class dashboard_elements:
    def dashboard_ele(self, frame, value=75):
        # SALES OVER A MONTH
        self.lbl = ui.Label(frame, text='SALES OVER A MONTH', font=("Arial", 30), bg="#001F3F", fg="white")
        self.lbl.place(relx=0.6, rely=0.58, anchor="center")
        fig = Figure(figsize=(6,3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([0, 1, 2, 3], [0, 1, 4, 9])  
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.6, rely=0.8, anchor="center")

        #profit over a month
        self.lbl = ui.Label(frame, text='PROFITS OVER A MONTH', font=("Arial", 30), bg="#001F3F", fg="white")
        self.lbl.place(relx=0.6, rely=0.1, anchor="center")
        fig = Figure(figsize=(6,3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([0, 1, 2, 3], [0, 1, 4, 9])  
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.6, rely=0.32, anchor="center")

        # THE NET PROFIT
        self.lbl1 = ui.Label(frame, text='NET PROFIT', font=("Arial", 30), bg="#001F3F", fg="white")
        self.lbl1.place(relx=0.15, rely=0.09, anchor="center")  

        numbers = 11
        self.lbl2 = ui.Label(frame, text=numbers, font=("Arial", 100), bg="#001F3F", fg="white")
        self.lbl2.place(relx=0.15, rely=0.22, anchor="center")
        #TODAY SALES
        self.lbl1 = ui.Label(frame, text='TODAY SALES', font=("Arial", 30), bg="#001F3F", fg="white")
        self.lbl1.place(relx=0.15, rely=0.35, anchor="center")  

        numbers = 11
        self.lbl2 = ui.Label(frame, text=numbers, font=("Arial", 100), bg="#001F3F", fg="white")
        self.lbl2.place(relx=0.15, rely=0.5, anchor="center")
        #MONTH SLALES 
        self.lbl1 = ui.Label(frame, text='MONTH SLALES', font=("Arial", 30), bg="#001F3F", fg="white")
        self.lbl1.place(relx=0.15, rely=0.69, anchor="center")  

        numbers = 11
        self.lbl2 = ui.Label(frame, text=numbers, font=("Arial", 100), bg="#001F3F", fg="white")
        self.lbl2.place(relx=0.15, rely=0.85, anchor="center")


if __name__ == "__main__":
    root = ui.Tk()
    root.geometry("1000x1000")
    root.configure(bg='#001F3F')  # A darker blue background

    frm = ui.Frame(root, bg='#001F3F')
    frm.pack(fill="both", expand=True)

    dash = dashboard_elements()
    dash.dashboard_ele(frm, value=75)  # Pass speedometer value 0-100

    root.mainloop()
