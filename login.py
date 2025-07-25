import tkinter as ui
from tkinter import messagebox
import csv


##functions
def Check_admin():
    def get_passwd():
        f=open("Root/Admin.txt","r")
        admin_password = f.read().strip()
        f.close()
        if passwd.get() == admin_password:
            messagebox.showinfo("Success","Welcome Admin")
            second.destroy()
            open_add_user_window()
        else:
            messagebox.showerror("Error","Invalid password")
            passwd.delete(0, ui.END)

    second = ui.Toplevel(login)
    second.title("ADMIN LOGIN")
    second.geometry("300x150")
    second.grab_set()
    second.focus_set()
    second.configure(bg="white")
    label = ui.Label(second, text="Enter ADMIN password", bg="white")
    label.place(relx=0.5, rely=0.3, anchor=ui.CENTER)
    passwd = ui.Entry(second, width=20, font=("Times", 15), bd=2, show="*")
    passwd.place(relx=0.5, rely=0.5, anchor=ui.CENTER)
    enter = ui.Button(second, text="Continue", command=get_passwd)
    enter.place(relx=0.5, rely=0.7, anchor=ui.CENTER)
    passwd.bind("<Return>", lambda event: get_passwd())

def open_add_user_window():
    def save_user():
        if passwd.get() == passwd2.get() and username.get().strip() != "":
            with open("Root/Users.csv","a", newline='') as f:
                writer=csv.writer(f)
                writer.writerow([username.get(),passwd.get()])
            messagebox.showinfo("Success","User added successfully")
            a.destroy()
        else:
            if username.get().strip() == "":
                messagebox.showerror("Error","Username cannot be empty")
            else:
                messagebox.showerror("Error","Passwords do not match")

    a = ui.Toplevel(login)
    a.title("Add User")
    a.geometry("400x300")
    a.grab_set()
    a.focus_set()
    a.configure(bg="white")

    label = ui.Label(a, text="Enter username", bg="white")
    label.place(relx=0.5, rely=0.2, anchor=ui.CENTER)
    username = ui.Entry(a, width=20, font=("Times", 15), bd=2)
    username.place(relx=0.5, rely=0.3, anchor=ui.CENTER)

    passwd_lable = ui.Label(a, text="Enter password", bg="white")
    passwd_lable.place(relx=0.5, rely=0.4, anchor=ui.CENTER)
    passwd = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
    passwd.place(relx=0.5, rely=0.5, anchor=ui.CENTER)

    passwd2_lable = ui.Label(a, text="Re-enter password", bg="white")
    passwd2_lable.place(relx=0.5, rely=0.6, anchor=ui.CENTER)
    passwd2 = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
    passwd2.place(relx=0.5, rely=0.7, anchor=ui.CENTER)

    save_button = ui.Button(a, text="Add User", command=save_user)
    save_button.place(relx=0.5, rely=0.8, anchor=ui.CENTER)

def add_user():
    Check_admin()





##Main window

login = ui.Tk()
login.title("Login")
login.attributes("-fullscreen", True)
login.configure(bg="white")

#menu bar

menu = ui.Menu(login)
login.config(menu=menu)
Users = ui.Menu(menu, tearoff=0)
menu.add_cascade(label="Administration", menu=Users)
Users.add_command(label="Add User", command= add_user)
#Users.add_command(label="Remove User", command=lambda: login.destroy())
#Users.add_command(label="Update User", command=lambda: update_user())
#Users.add_command(label="List Users", command=lambda: list_user())
#Exit=ui.Menu(menu,tearoff=0)
#menu.add_cascade(label="Exit",menu=Exit)
#Exit.add_command(label="Exit the software ",command=login.destroy)

## heading

header_main = ui.Label(login, text="WareHouse management system", bg="white")
header_main.config(font=("Times", 30, "bold"))
header_main.place(relx=0.5, rely=0.1, anchor=ui.CENTER)

#input labels and entry

username_lable = ui.Label(login, text="Enter username", bg="white")
username_lable.place(relx=0.5, rely=0.4, anchor=ui.CENTER)
username = ui.Entry(login, width=20, font=("Times", 15), bd=2)
username.place(relx=0.5, rely=0.45, anchor=ui.CENTER)
passwd_lable = ui.Label(login, text="Enter password", bg="white")
passwd_lable.place(relx=0.5, rely=0.5, anchor=ui.CENTER)
passwd = ui.Entry(login, width=20, font=("Times", 15), bd=2, show="*")
passwd.place(relx=0.5, rely=0.55, anchor=ui.CENTER)

login.mainloop()