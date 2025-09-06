import tkinter as ui
from tkinter import messagebox
from pathlib import Path
from cryptography.fernet import Fernet
import Userhandeling as uh
import subprocess
import sys
import platform
from PIL import Image,ImageTk
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
    label = ui.Label(second, text="Enter ADMIN password",bg="white")
    label.place(relx=0.5, rely=0.3, anchor=ui.CENTER)
    passwd = ui.Entry(second, width=20, font=("Times", 15), bd=2, show="*")
    passwd.place(relx=0.5, rely=0.5, anchor=ui.CENTER)
    enter = ui.Button(second, text="Continue", command=check_passwd,bg="white")
    enter.place(relx=0.5, rely=0.75, anchor=ui.CENTER)
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
        a.geometry("500x300")
        #a.grab_set()
        a.focus_set()
        a.configure(bg="white")
        label = ui.Label(a, text="Enter username", bg="white")
        label.place(relx=0.05, rely=0.1)
        username = ui.Entry(a, width=20, font=("Times", 15), bd=2)
        username.place(relx=0.05, rely=0.2)
        passwd_lable = ui.Label(a, text="Enter password", bg="white")
        passwd_lable.place(relx=0.05, rely=0.35)
        passwd = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
        passwd.place(relx=0.05, rely=0.45)
        passwd2_lable = ui.Label(a, text="Re-enter password", bg="white")
        passwd2_lable.place(relx=0.05, rely=0.6)
        passwd2 = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
        passwd2.place(relx=0.05, rely=0.7)
        enter = ui.Button(a, text="Add User", command=match_passwd,bg="white")
        enter.place(relx=0.5, rely=0.92, anchor=ui.CENTER)
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
        enter = ui.Button(a,text="Remove User",command=lambda: remove(),bg="white")
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
        a.geometry("300x200")
        a.configure(bg="white")
        a.focus_set()
        lable = ui.Label(a, text="Enter username to update", bg='white')
        lable.place(relx=0.05, rely=0.1)
        entry = ui.Entry(a, width=20, font=("Times", 15), bd=2)
        entry.place(relx=0.05, rely=0.25)
        lable2 = ui.Label(a, text="Enter new password", bg='white')
        lable2.place(relx=0.05, rely=0.45)
        entry2 = ui.Entry(a, width=20, font=("Times", 15), bd=2, show="*")
        entry2.place(relx=0.05, rely=0.6)
        enter = ui.Button(a, text="Update User", command=lambda: update(),bg="white")
        enter.place(relx=0.5, rely=0.9, anchor=ui.CENTER)


#login window
login = ui.Tk()
login.title("Login")

# Maximize based on OS
system = platform.system()
if system == "Windows":
    login.state('zoomed')  # This maximizes the window on Windows
elif system == "Darwin":  # macOS
    login.attributes('-zoomed', True)  # May work on some versions
else:
    # Fallback for Linux
    login.attributes('-zoomed', True)


#login.attributes("-fullscreen", True)
#login.geometry("400x400")
image=Image.open(base_path / "src" / "images" / "backgrounds" / "login_bg.png")
canvas = ui.Canvas(login)
canvas.pack(fill="both",expand="True")

#image=image.resize((canvas.winfo_width(),canvas.winfo_height()),)
login.update()
image_width=image.width
image_height=image.height
canvas_width=canvas.winfo_width()
canvas_height=canvas.winfo_height()
image=image.resize((canvas_width,canvas_height))
bg_login = ImageTk.PhotoImage(image)
canvas.create_image(canvas_width//2,canvas_height//2, image=bg_login,anchor="center")
#menu bar

menu = ui.Menu(login)
login.config(menu=menu)
Users = ui.Menu(menu, tearoff=0)
menu.add_cascade(label="Administration", menu=Users)
Users.add_command(label="Add User", command=add_user)
Users.add_command(label="Remove User", command=lambda: remove_user())
Users.add_command(label="Update User", command=lambda: update_user())
#menu.configure(background="black",foreground="white")
#Users.configure(foreground="white",background="black")
# login bg




#Users.add_command(label="List Users", command=lambda: list_user())
#Exit=ui.Menu(menu,tearoff=0)
#menu.add_cascade(label="Exit",menu=Exit)
#Exit.add_command(label="Exit the software ",command=login.destroy)

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

login_frame= ui.Frame(login, bg="white", height=550,width=450,bd=3,highlightbackground="black",highlightthickness=3 )
login_frame.place(relx=0.5,rely=0.5,anchor=ui.CENTER)
header_main = ui.Label(login_frame, text="WAREHOUSE MANAGEMENT SYSTEM",bg="white")
header_main.config(font=("Times", 16, "bold"))
header_main.place(relx=0.5, rely=0.1, anchor=ui.CENTER)
image1=Image.open(base_path / "src" / "images" / "icons" / "login_icon.jpg")
image1=image1.resize((100,100),)
icon_width=image1.width
icon_height=image1.height
icon_login = ImageTk.PhotoImage(image1)  # Use your image file path here
canvas1 = ui.Canvas(login_frame,width=100,height=100)
canvas1.place(relx=0.5,rely=0.3,anchor="center")
canvas1.create_image(icon_width//2,icon_height//2 , image=icon_login,anchor="center")
        

username_lable = ui.Label(login_frame,text="Username", font=("Arial", 10, "bold"), bg="white")
username_lable.place(relx=0.5, rely=0.45, anchor=ui.CENTER)
username = ui.Entry(login_frame, width=20, font=("Times", 15), bd=2)
username.place(relx=0.5, rely=0.5, anchor=ui.CENTER)

passwd_lable = ui.Label(login_frame, text="Password",font=("Arial", 10, "bold"), bg="white")
passwd_lable.place(relx=0.5, rely=0.57, anchor="center")
passwd = ui.Entry(login_frame, width=20, font=("Times", 15), bd=2, show="*")
passwd.place(relx=0.5, rely=0.62, anchor=ui.CENTER)
enter = ui.Button(login_frame, text="Login", command=lambda: auth(),width="12",bg="white")
enter.place(relx=0.5, rely=0.75, anchor=ui.CENTER)


login.mainloop()
