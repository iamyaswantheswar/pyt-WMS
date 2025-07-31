import tkinter as ui
print("login successful")
home=ui.Tk()
home.title("Home")
home.attributes("-fullscreen", True)
label=ui.Label(home,text="Welcome to Pyri",font=("Arial",40))
label.pack(pady=50)
home.mainloop()