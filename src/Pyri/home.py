import tkinter as ui
class cmds:
  def __init__(self,home):
    self.home=home
    self.lables=[]
  def destroy(self):
    for i in self.lables:
      i.destroy()
    
  def dashboard_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.home,text="welcome to Dashboard")
    self.lbl.place(relx=0.5,rely=0.5)
    self.lables.append(self.lbl)
  def inventory_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.home,text="welcome to Inventory")
    self.lbl.place(relx=0.5,rely=0.5)
    self.lables.append(self.lbl)
  def sales_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.home,text="welcome to Sales")
    self.lbl.place(relx=0.5,rely=0.5)
    self.lables.append(self.lbl)
  def purchases_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.home,text="welcome to Purchases")
    self.lbl.place(relx=0.5,rely=0.5)
    self.lables.append(self.lbl)
  def demand_ui(self):
    self.destroy()
    self.lbl=ui.Label(self.home,text="welcome to Demand")
    self.lbl.place(relx=0.5,rely=0.5)
    self.lables.append(self.lbl)
  
      
    

  def createcmd(self,name):
      func=getattr(self,name.lower() + "_ui")
      if callable(func):
        func()
  
class topbarelements(cmds):
  
  def __init__(self,name):
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
  i=topbarelements(i)
  i.place(elementpos,0.05)
  elementpos+=0.15
home.mainloop()
  
