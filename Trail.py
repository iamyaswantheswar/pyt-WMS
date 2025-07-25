import tkinter as tk

def open_second_window():
    second = tk.Toplevel(root)
    second.title("Second Window")
    second.geometry("300x150")

    label = tk.Label(second, text="This is the second window.")
    label.pack(pady=20)

    close_btn = tk.Button(second, text="Close", command=second.destroy)
    close_btn.pack()

# Main window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x200")

open_btn = tk.Button(root, text="Open Second Window", command=open_second_window)
open_btn.pack(pady=60)

root.mainloop()