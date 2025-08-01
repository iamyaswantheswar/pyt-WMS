import tkinter as ui
class cmds:
  def __init__(self,home):
    self.home=home
    self.lable_frame=ui.Frame(self.home)
    self.lable_frame.place(relx=0.5,rely=0.5,anchor="center")
    self.lable_frame.config(width=500,height=500,bg="blue")
  def destroy(self):
      self.lable_frame.destroy()
  def dashboard_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.lable_frame,text="welcome to Dashboard")
    self.lbl.place(relx=0.5,rely=0.5)
  def inventory_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.lable_frame,text="welcome to Inventory")
    self.lbl.place(relx=0.5,rely=0.5)
  def sales_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.lable_frame,text="welcome to Sales")
    self.lbl.place(relx=0.5,rely=0.5)
  def purchases_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.lable_frame,text="welcome to Purchases")
    self.lbl.place(relx=0.5,rely=0.5)
  def demand_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.lable_frame,text="welcome to Demand")
    self.lbl.place(relx=0.5,rely=0.5)
  
      
    

  def createcmd(self,name):
      func=getattr(self,name.lower() + "_ui")
      if callable(func):
        func()
  
class topbarelements(cmds):
  
  def __init__(self,name,topbar,home):
    super().__init__(home)
    self.name=name
    self.name=ui.Button(topbar,text=name,bg="black",fg="white",bd=0,font=("Times", 10, "bold"),anchor="w" ,command= lambda :self.createcmd(name))
    self.name.config(width=10,height=2,borderwidth=0,highlightthickness=0)
    self.name.bind("<Enter>",lambda event: self.name.config(bg="white",fg="black"))
    self.name.bind("<Leave>",lambda event: self.name.config(bg="black",fg="white"))
    
  def place(self,x,y):
    self.name.place(relx=x,rely=y)

    
    
      
home=ui.Tk()
h=cmds(home)
home.title("Home")
home.attributes("-fullscreen", True)
topbar=ui.Frame(home,bg="black",height=50)
topbar.place(relx=0,rely=0,relwidth=1)
elementpos=0.07
top=["Dashboard","Inventory","Sales","Purchases","Demand"]
for i in top:
  y=len(top[1-top.index(i)])
  i=topbarelements(i,topbar,home)
  i.place(elementpos,0.05)
  elementpos+=0.15
home.mainloop()
  
