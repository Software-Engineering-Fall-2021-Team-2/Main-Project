from tkinter import *
from tkinter import font as tkfont


class MyBaseFrame(Frame):
    """ 
    Base frame uses a 3x3 grid to display widgets with the middle widget being the largest to accompnay for player entry
    """

    def __init__(self, parent, controller, header_text: str = "Header", subheader_text: str = "subheader", *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.header_text = header_text
        self.subheader_text = subheader_text

        # Configuration
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=20)
        self.columnconfigure((0, 2), weight=1, minsize=5)
        self.columnconfigure(1, weight=20)

        # Populate
        header_subheader = HeaderSubheader(
            self, controller, self.header_text, self.subheader_text)

        # self.screen_setup_TESTING()

    # TODO: Remove when done
    def screen_setup_TESTING(self):
        """Layout testing function"""
        label1 = Label(self, bg='red',)
        label1.grid(row=0, column=0, sticky="NSEW")
        label2 = Label(self, bg='red')
        label2.grid(row=1, column=1, sticky="NSEW")
        label3 = Label(self, bg='red')
        label3.grid(row=2, column=2, sticky="NSEW")

    def onClick(self, *event):
        print("fart3")
        self.controller.focus_set()


class HeaderSubheader(Frame):
    """Creates a label to hold a 1x2 grid within the (0,1) position in the BaseFrame grid"""

    def __init__(self, parent, controller, header_text: str = "HEADER FILLING IN HeaderSubheader", subheader_text: str = "subheader filling in HeaderSubheader", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.header_text = header_text
        self.subheader_text = subheader_text

        # Configuration
        self.config(borderwidth=0)
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        # Populate
        header = Header(self, controller, header_text)
        subheader = SubHeader(self, controller, subheader_text)

        # Layout
        self.grid(row=0, column=1, sticky="NEW")


class Header(Label):
    def __init__(self, parent, controller, header_text: str = "HEADER FILLING IN Header", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.text = header_text

        # Configuration
        self.config(text=self.text, font=self.controller.HEADER_FONT,
                    wraplength=750, justify="center")

        # Layout
        self.grid(row=0, column=0, sticky="N")


class SubHeader(Label):
    def __init__(self, parent, controller, subheader_text: str = "subheader filling in SubHeader", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.text = subheader_text

        # Configuration
        self.config(text=self.text, font=self.controller.SUBHEADER_FONT,
                    wraplength=750, justify="center")

        # Layout
        self.grid(row=1, column=0, sticky="N")
