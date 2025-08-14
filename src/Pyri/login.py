import tkinter as ui
from tkinter import messagebox
from pathlib import Path
from cryptography.fernet import Fernet
import Userhandeling as uh
import subprocess
import sys
# Get the path to the current script
base_path = Path(__file__).parent.parent.parent

##functions
def Check_admin():
    isadmin = False

    def check_passwd():
        nonlocal isadmin
        if uh.check_admin(passwd.get()):
            isadmin = True
            messagebox.showinfo("Success", "Welcome Admin")
            second.destroy()
        else:
            messagebox.showerror("Error", "Invalid password")
            isadmin = False
            second.destroy()

    second = ui.Toplevel(login)
    second.title("ADMIN LOGIN")
    second.geometry("300x150")
    second.grab_set()
    second.focus_set()
    second.configure(bg="white")
    label = ui.Label(second, text="Enter ADMIN password")
    label.place(relx=0.5, rely=0.3, anchor=ui.CENTER)
    passwd = ui.Entry(second, width=20, font=("Times", 15), bd=2, show="*")
    passwd.place(relx=0.5, rely=0.5, anchor=ui.CENTER)
    enter = ui.Button(second, text="Continue", command=check_passwd)
    enter.place(relx=0.5, rely=0.7, anchor=ui.CENTER)
    login.wait_window(second)
    #passwd.bind("<Return>", lambda event:get_passwd)
    if isadmin:
        second.destroy()
        return True


def add_user(i=None,b=None):

    def match_passwd():
        if passwd.get() == passwd2.get()and uh.user_check(username.get()):
            uh.add_user(username.get(), passwd.get())
            messagebox.showinfo("Success", "User added successfully")
            a.destroy()
        else:
            if passwd.get() != passwd2.get():
                messagebox.showerror("Error", "Passwords do not match")
                a.destroy()
                add_user()
            if not uh.user_check(username.get()):
                messagebox.showerror("Error", "user alredy exist")
                a.destroy()
                add_user()

    if Check_admin():
        print("Admin logged in to add user")
        a = ui.Toplevel(login)
        a.title("Add User")
        a.geometry("500x500")
        #a.grab_set()
        a.focus_set()
        a.configure(bg="white")
        label = ui.Label(a, text="Enter username", bg="white")
        label.place(relx=0.5, rely=0.4, anchor=ui.CENTER)
        username = ui.Entry(a, width=20, font=("Times", 15), bd=2)
        username.place(relx=0.5, rely=0.45, anchor=ui.CENTER)
        passwd_lable = ui.Label(a, text="Enter password", bg="white")
        passwd_lable.place(relx=0.5, rely=0.5, anchor=ui.CENTER)
        passwd = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
        passwd.place(relx=0.5, rely=0.55, anchor=ui.CENTER)
        passwd2_lable = ui.Label(a, text="Re-enter password", bg="white")
        passwd2_lable.place(relx=0.5, rely=0.6, anchor=ui.CENTER)
        passwd2 = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
        passwd2.place(relx=0.5, rely=0.65, anchor=ui.CENTER)
        enter = ui.Button(a, text="Add User", command=match_passwd)
        enter.place(relx=0.5, rely=0.7, anchor=ui.CENTER)
        #login.wait_window(a)


#remove user
def remove_user():
    if Check_admin():
        def remove():
            if uh.remove_user(entry.get()):
                messagebox.showinfo("Success", "User removed successfully")
                a.destroy()
            else:
                messagebox.showerror("Error", "User not found")
                a.destroy()
        print("Admin logged in to remove user")
        a = ui.Toplevel(login)
        a.title("Remove User")
        a.geometry("300x150")
        a.configure(bg="white")
        a.focus_set()
        lable = ui.Label(a, text="Enter username to delete", bg='white')
        lable.place(relx=0.5, rely=0.3, anchor=ui.CENTER)
        entry = ui.Entry(a, width=20, font=("Times", 15), bd=2)
        entry.place(relx=0.5, rely=0.45, anchor=ui.CENTER)
        enter = ui.Button(a,
                          text="Remove User",
                          command=lambda: remove())
        enter.place(relx=0.5, rely=0.7, anchor=ui.CENTER)


#update user
def update_user():
    if Check_admin():

        def update():
            if uh.update_user(entry.get(), entry2.get()):
                messagebox.showinfo("Success", "User updated successfully")
                a.destroy()
            else:
                ans=messagebox.askquestion("Error", "User not found Do you want to add this user ?")
                if ans == "yes":
                    uh.add_user(entry.get(), entry2.get())
                    messagebox.showinfo("Success", "User added successfully")
                    a.destroy()
                else:
                    a.destroy()

        print("Admin logged in to update user")
        a = ui.Toplevel(login)
        a.title("Update User")
        a.geometry("500x500")
        a.configure(bg="white")
        a.focus_set()
        lable = ui.Label(a, text="Enter username to update", bg='white')
        lable.place(relx=0.5, rely=0.3, anchor=ui.CENTER)
        entry = ui.Entry(a, width=20, font=("Times", 15), bd=2)
        entry.place(relx=0.5, rely=0.4, anchor=ui.CENTER)
        lable2 = ui.Label(a, text="Enter new password", bg='white')
        lable2.place(relx=0.5, rely=0.5, anchor=ui.CENTER)
        entry2 = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
        entry2.place(relx=0.5, rely=0.6, anchor=ui.CENTER)
        enter = ui.Button(a, text="Update User", command=lambda: update())
        enter.place(relx=0.5, rely=0.7, anchor=ui.CENTER)


#login window
login = ui.Tk()
login.title("Login")

login.attributes("-fullscreen", True)
login.geometry("400x400")

bg = ui.PhotoImage(file="C:/Users/vasanth/Desktop/pyt-WMS/src/images/Screenshot 2025-05-01 225259.png")  # Use your image file path here
canvas = ui.Canvas(login, width=400, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")
#menu bar

menu = ui.Menu(login)
login.config(menu=menu)
Users = ui.Menu(menu, tearoff=0)
menu.add_cascade(label="Administration", menu=Users)
Users.add_command(label="Add User", command=add_user)
Users.add_command(label="Remove User", command=lambda: remove_user())
Users.add_command(label="Update User", command=lambda: update_user())
#Users.add_command(label="List Users", command=lambda: list_user())
#Exit=ui.Menu(menu,tearoff=0)
#menu.add_cascade(label="Exit",menu=Exit)
#Exit.add_command(label="Exit the software ",command=login.destroy)

## heading

header_main = ui.Label(login, text="WareHouse management system", bg="white")
header_main.config(font=("Times", 30, "bold"))
header_main.place(relx=0.5, rely=0.1, anchor=ui.CENTER)

#input labels and entry
def auth():
    if uh.login_auth(username.get(), passwd.get()):
        messagebox.showinfo("Success", "Login successful")
        file_path = base_path / "src" / "Pyri" / "home.py"
        login.destroy()
        subprocess.run([sys.executable, file_path])
        sys.exit()
        
    else:
        messagebox.showerror("Error", "Invalid username or password")
        

username_lable = ui.Label(login, text="Enter username", bg="white")
username_lable.place(relx=0.5, rely=0.4, anchor=ui.CENTER)
username = ui.Entry(login, width=20, font=("Times", 15), bd=2)
username.place(relx=0.5, rely=0.45, anchor=ui.CENTER)
passwd_lable = ui.Label(login, text="Enter password", bg="white")
passwd_lable.place(relx=0.5, rely=0.5, anchor=ui.CENTER)
passwd = ui.Entry(login, width=20, font=("Times", 15), bd=2, show="*")
passwd.place(relx=0.5, rely=0.55, anchor=ui.CENTER)
enter = ui.Button(login, text="Login", command=lambda: auth())
enter.place(relx=0.5, rely=0.6, anchor=ui.CENTER)
login.mainloop()
