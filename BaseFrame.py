"""Instead of using basic tkinter, ttkthemes is used. It just looks prettier"""
from ttkthemes import ThemedTk as tk
from tkinter import *
from tkinter import font as tkfont


class MyBaseFrame(Frame):
    """ 
    Base frame uses a 3x3 grid to display widgets with the middle widget being the largest to accompnay for player entry
    """

    def __init__(self, controller, header_text="Header Test", subheader_text="subheader test", *args, **kwargs):
        Frame.__init__(self, controller, *args, **kwargs)
        self.controller = controller
        self.header_text = header_text
        self.subheader_text = subheader_text

        # Grid setup
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=15)

        # Testing method to highlight page layout
        #self.setup_test(header_text, subheader_text)

        self.header_subheader(header_text, subheader_text)

    def header_subheader_set(self, header_text, subheader_text):
        """Creates a label to hold a 1x2 grid within the (0,1) position in the BaseFrame grid"""
        # Grid setup
        header_subheader_frame = Frame(self, borderwidth=1)
        header_subheader_frame.grid_rowconfigure((0, 1), weight=1)
        header_subheader_frame.grid_columnconfigure(0, weight=1)
        header_subheader_frame.grid(row=0, column=1, sticky="NSEW")

        # Header setup
        header_label = Label(
            header_subheader_frame, text=header_text, font=self.controller.HEADER_FONT)
        header_label.grid(row=0, column=0, sticky="NSEW")

        # Subheader setup
        subheader_label = Label(
            header_subheader_frame, text=subheader_text, font=self.controller.SUBHEADER_FONT)
        subheader_label.grid(row=1, column=0, sticky="NSEW")

        #splash_label = Label(splash_root, image=img)
        #splash_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def screen_setup_TESTING(self, header_text, subheader_text):
        """Layout testing function"""
        label1 = Label(self, bg='red',)
        label1.grid(row=0, column=0, sticky="NSEW")
        label2 = Label(self, bg='red')
        label2.grid(row=1, column=1, sticky="NSEW")
        label3 = Label(self, bg='red')
        label3.grid(row=2, column=2, sticky="NSEW")
