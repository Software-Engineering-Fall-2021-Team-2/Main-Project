import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont


class BaseFrame(tk.Frame):

    def __init__(self, controller, *args, **kwargs):
        tk.Frame.__init__(self, controller, *args, **kwargs)
        self.controller = controller
        
        image_splash_screen = PhotoImage(file="logo.png")

        image_container_splash_screen = Label(
            self, image=image_splash_screen)

        # HACK: IDK why this line is required, but it works
        image_container_splash_screen.image = image_splash_screen

        image_container_splash_screen.grid(row=0, column=0, sticky="NSEW")
        #image_container_splash_screen.place(relx=.5, rely=.5, anchor=CENTER)

        # after existing for x seconds, switch to PlayerEntry
        self.after(SPLASHSCREEN_LENGTH * 1000,
                   lambda: controller.show_frame(PlayerEntry))
