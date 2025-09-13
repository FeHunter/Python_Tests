import tkinter as tk
from datetime import datetime

def update():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    label.config(text=now)
    window.after(1000, update)

window = tk.Tk()
window.title("My Personal Clock")
window.geometry("300x100")
window.configure(bg="black")

label = tk.Label(window, font=("Arial", 20), fg="lime", bg="black")
label.pack(expand=True)

update()
window.mainloop()