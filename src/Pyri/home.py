import tkinter as ui

def dashboard_ui(s=None):
    print("dasbord working")

def createcmd(name):
    cmd=name.lower() + "_ui"
    func=globals().get(cmd)
    if func:
      func()
  
class topbarelements:
  
  def __init__(self,name):
    self.name=name
    self.name=ui.Button(topbar,text=name,bg="black",fg="white",bd=0,font=("Times", 10, "bold"),anchor="w" ,command= lambda: createcmd(name))
    self.name.config(width=10,height=2,borderwidth=0,highlightthickness=0)
    self.name.bind("<Enter>",lambda event: self.name.config(bg="white",fg="black"))
    self.name.bind("<Leave>",lambda event: self.name.config(bg="black",fg="white"))
    
  def place(self,x,y):
    self.name.place(relx=x,rely=y)

    
    
      
home=ui.Tk()
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
  
