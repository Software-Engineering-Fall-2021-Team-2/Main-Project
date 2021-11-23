
from tkinter import *
from tkinter import font as tkfont
import datetime
import dbconnect


class MyBaseFrame(Frame):

    def __init__(self, parent: Tk, controller: Tk, header_text: str = "", subheader_text: str = "", *args, **kwargs):
        """ Basis for all frames - Uses a 3x3 grid to display widgets - 2x2 position used for main interactions.

        Args:
            parent (Tk) : Widget that is directly resposible for owning this widget - always Container. 
            controller (Tk) : Top widget - passed down to every widget in order to maintain a heirarchy of widgets - always Container.
            header_text (str, optional) : Text to be used in the header position. 
            subheader_text (str, optional) : Text to be used in the subheader position.
            *args : unused
            **kwargs : unused
        """
        # Set Object Attributes
        super().__init__(parent)
        self.controller = controller
        self.header_text = header_text
        self.subheader_text = subheader_text

        # Configure
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=20)

        self.columnconfigure((0, 2), weight=1, minsize=5)
        self.columnconfigure(1, weight=20)

        # Populate
        header_subheader = HeaderSubheader(self, controller)

        # Testing 
        self.screen_setup_TESTING()

    # TODO: Remove before submission
    def screen_setup_TESTING(self):
        """Layout testing function"""
        label1 = Label(self, bg='red',)
        label1.grid(row=0, column=0, sticky="NSEW")
        label2 = Label(self, bg='red')
        label2.grid(row=1, column=1, sticky="NSEW")
        label3 = Label(self, bg='red')
        label3.grid(row=2, column=2, sticky="NSEW")


class HeaderSubheader(Frame):

    def __init__(self, parent: MyBaseFrame, controller: Tk):
        """Creates a label to hold a 1x2 grid within the (0,1) position in the MyBaseFrame grid.

        Args:
            parent (MyBaseFrame): Widget that is directly resposible for owning this widget - contains text information.
            controller (Tk): Top widget - passed down to every widget in order to maintain a heirarchy of widgets.
        """
        # Set Object Attributes
        super().__init__(parent)
        self.controller = controller

        # Configure
        self.config(borderwidth=0)
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        # Populate
        header = Header(self, controller, parent.header_text)
        subheader = SubHeader(self, controller, parent.subheader_text)

        # Layout
        self.grid(row=0, column=1, sticky="NEW")


class Header(Label):
    def __init__(self, parent: HeaderSubheader, controller: Tk, header_text: str):
        """Header text label.

        Args:
            parent (HeaderSubheader): HeaderSubheader frame - (0,1) - top center of screen.
            controller (Tk): Top widget - passed down to every widget in order to maintain a heirarchy of widgets.
            header_text (str): Text to be displayed.
        """
        # Set Object Attributes
        super().__init__(parent)
        self.controller = controller

        # Configure
        self.config(text=header_text, font=self.controller.HEADER_FONT,
                    wraplength=750, justify="center")

        # Layout
        self.grid(row=0, column=0, sticky="N")


class SubHeader(Label):
    def __init__(self, parent: HeaderSubheader, controller: Tk, subheader_text: str):
        """Subheader text label.

        Args:
            parent (HeaderSubheader) : HeaderSubheader frame - (0,1) - top center of screen.
            controller (Tk): Top widget - passed down to every widget in order to maintain a heirarchy of widgets.
            subheader_text (str): Text to be displayed.
        """
        # Set Object Attributes
        super().__init__(parent)
        self.controller = controller

        # Configure
        self.config(text=subheader_text, font=self.controller.SUBHEADER_FONT,
                    wraplength=750, justify="center")

        # Layout
        self.grid(row=1, column=0, sticky="N")
