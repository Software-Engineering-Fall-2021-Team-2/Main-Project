#
#           Name: splashscreen.py
#           Author: Gage Underwood
#

from tkinter import *

splash_root = Tk()
splash_root.title("Splash Screen")
splash_root.geometry("919x586")

def killScreen():
    splash_root.destroy()

# centering
x_left = int(splash_root.winfo_screenwidth() / 2 - 919 / 2)
y_top = int(splash_root.winfo_screenheight() / 2 - 586 / 2)
splash_root.geometry("+{}+{}".format(x_left, y_top))

# define img
img = PhotoImage(file="logo.png")

# hide title bar
splash_root.overrideredirect(True)

splash_label = Label(splash_root, image=img)
splash_label.place(x=0, y=0, relwidth=1, relheight=1)

splash_root.after(3000, killScreen)

splash_root.mainloop()
