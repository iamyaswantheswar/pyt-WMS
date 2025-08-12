import tkinter as ui

class cmds:
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
        self.lable_frame = ui.Frame(self.home, bg="red")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        lbl = ui.Label(self.lable_frame, text="welcome to Dashboard")
        lbl.place(relx=0.5, rely=0.5, anchor="center")

    def inventory_ui(self):
        self.dest()
        print("user entered inventory")
        self.lable_frame = ui.Frame(self.home,bg="green")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        lbl = ui.Label(self.lable_frame, text="welcome to Inventory")
        lbl.place(relx=0.5, rely=0.5, anchor="center")

    def sales_ui(self):
        self.dest()
        print("user entered sales")
        self.lable_frame = ui.Frame(self.home,bg="blue")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        lbl = ui.Label(self.lable_frame, text="welcome to Sales")
        lbl.place(relx=0.5, rely=0.5, anchor="center")

    def purchases_ui(self):
        self.dest()
        print("user entered purchases")
        self.lable_frame = ui.Frame(self.home,bg="lightblue")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        lbl = ui.Label(self.lable_frame, text="welcome to Purchases")
        lbl.place(relx=0.5, rely=0.5, anchor="center")

    def demand_ui(self):
        self.dest()
        print("user entered demand")
        self.lable_frame = ui.Frame(self.home,bg="lightgreen")
        self.lable_frame.pack(side="top", fill="both", expand=True)
        lbl = ui.Label(self.lable_frame, text="welcome to Demand")
        lbl.place(relx=0.5, rely=0.5, anchor="center")

    def createcmd(self, name):
        func = getattr(self, name.lower() + "_ui", None)
        if callable(func):
            func()


class topbarelements:
    def __init__(self, label, topbar, command):
        self.button = ui.Button(topbar,text=label,bg="black",fg="white",bd=0,font=("Times", 10, "bold"),anchor="w",command=command)
        self.button.config(width=10, height=2, borderwidth=0, highlightthickness=0)
        self.button.bind("<Enter>", lambda e: self.button.config(bg="white", fg="black"))
        self.button.bind("<Leave>", lambda e: self.button.config(bg="black", fg="white"))

    def place(self, x, y):
        self.button.place(relx=x, rely=y)


# Main window
home = ui.Tk()
home.title("Home")
home.attributes("-fullscreen", True)

topbar = ui.Frame(home, bg="black", height=50)
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
