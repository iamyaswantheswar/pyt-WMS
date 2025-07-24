import tkinter as ui
import csv

##functions
def Check_admin():
  def verify():
    pwd=admin.get()
    f=open("Admin.txt","r")
    if pwd==f.read():
      return True
  super=ui.Toplevel(login)
  super.title("Administrative login")
  #frame=ui.Frame(super,height=200,width=300)
  #frame.pack()
  l=ui.Label(super,text="Enter admin password",bg="white")
  l.place(relx=0.5,rely=0.2,anchor=ui.CENTER)
  admin=ui.Entry(super,width=20,font=("Times",15),bd=2,show="*")
  admin.place(relx=0.5,rely=0.3,anchor=ui.CENTER)
  super.mainloop()
  return verify()
def add_user():
  if Check_admin():
    a=ui.Toplevel(login)
    a.title("Add user")
    f=ui.Frame(a,height=200,width=300,bg="white")
    f.pack()
    l=ui.Label(f,text="Enter username",bg="white")
    l.place(relx=0.5,rely=0.2,anchor=ui.CENTER)
    user=ui.Entry(f,width=20,font=("Times",15),bd=2)
    user.place(relx=0.5,rely=0.3,anchor=ui.CENTER)
    l=ui.Label(f,text="set password",bg="white")
    l.place(relx=0.5,rely=0.4,anchor=ui.CENTER)
    pwd=ui.Entry(f,width=20,font=("Times",15),bd=2,show="*")
    pwd.place(relx=0.5,rely=0.5,anchor=ui.CENTER)
    l=ui.Label(f,text="confirm password",bg="white")
    pwd2=ui.Entry(f,width=20,font=("Times",15),bd=2,show="*")
    pwd2.place(relx=0.5,rely=0.6,anchor=ui.CENTER)
    if pwd.get()==pwd2.get():
      with open("Users.csv","a") as f:
        writer=csv.writer(f)
        writer.writerow([user.get(),pwd.get()])
        f.close()
        ui.messagebox.showinfo("Success","User added successfully")
        a.destroy()
    else:
      ui.messagebox.showerror("Error","Passwords do not match")
      a.destroy()
    a.mainloop()
  else:
    ui.messagebox.showerror("Error","Invalid admin password")


      
##Main window

login=ui.Tk()
login.title("Login")
login.attributes("-fullscreen",True)
login.configure(bg="white")

#menu bar

menu=ui.Menu(login)
login.config(menu=menu)
Users=ui.Menu(menu,tearoff=0)
menu.add_cascade(label="Administration",menu=Users)
Users.add_command(label="Add User",command= lambda:add_user())
Users.add_command(label="Remove User",command= lambda:remove_user())
Users.add_command(label="Update User",command= lambda:update_user())
Users.add_command(label="List Users",command= lambda:list_user())
#Exit=ui.Menu(menu,tearoff=0)
#menu.add_cascade(label="Exit",menu=Exit)
#Exit.add_command(label="Exit the software ",command=login.destroy)

## heading

header_main=ui.Label(login,text="WareHouse management system",bg="white")
header_main.config(font=("Times",30,"bold"))
header_main.place(relx=0.5,rely=0.1,anchor=ui.CENTER)

#input labels and entry

username_lable=ui.Label(login,text="Enter username",bg="white")
username_lable.place(relx=0.5,rely=0.4,anchor=ui.CENTER)
username=ui.Entry(login,width=20,font=("Times",15),bd=2)
username.place(relx=0.5,rely=0.45,anchor=ui.CENTER)
passwd_lable=ui.Label(login,text="Enter password",bg="white")
passwd_lable.place(relx=0.5,rely=0.5,anchor=ui.CENTER)
passwd=ui.Entry(login,width=20,font=("Times",15),bd=2,show="*")
passwd.place(relx=0.5,rely=0.55,anchor=ui.CENTER)

login.mainloop()

##operations

def get_username():
    return username.get()
def get_passwd():
    return passwd.get()

