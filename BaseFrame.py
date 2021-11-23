from Config import *


class MyBaseFrame(Frame):

    def __init__(self, master: Tk, header_text: str = "", subheader_text: str = "", *args, **kwargs):
        """Basis for all frames - Uses a 3x3 grid to display widgets - 2x2 position used for main interactions.

        Args:
            master (Tk) : Widget that is directly resposible for owning this widget - always Container. 
            header_text (str, optional) : Text to be used in the header position. 
            subheader_text (str, optional) : Text to be used in the subheader position.
            *args : unused
            **kwargs : unused
        """
        # Set Object Attributes
        super().__init__(master)
        self.header_text = header_text
        self.subheader_text = subheader_text

        # Configure
        self.config(bg='black')

        # Layout
        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=20)

        self.columnconfigure((0, 2), weight=1, minsize=5)
        self.columnconfigure(1, weight=20)

        # Populate
        header_subheader = HeaderSubheader(self, header_text, subheader_text)

        # Testing
        #self.screen_setup_TESTING()

    # TODO: Remove before submission
    def screen_setup_TESTING(self):
        """Layout testing function"""
        label1 = Label(self, bg='red',)
        label1.grid(row=0, column=0, sticky='NSEW')
        label2 = Label(self, bg='red')
        label2.grid(row=1, column=1, sticky='NSEW')
        label3 = Label(self, bg='red')
        label3.grid(row=2, column=2, sticky='NSEW')


class HeaderSubheader(Frame):

    def __init__(self, master: MyBaseFrame, header_text: str, subheader_text: str):
        """Creates a label to hold a 1x2 grid within the (0,1) position in the MyBaseFrame grid.

        Args:
            master (MyBaseFrame): Widget that is directly resposible for owning this widget - contains text information.
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(borderwidth=0, bg='black')
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        # Layout
        self.grid(row=0, column=1, sticky='NEW')

        # Populate
        header = Header(self, header_text)
        subheader = SubHeader(self, subheader_text)


class Header(Label):
    def __init__(self, master: HeaderSubheader, header_text: str):
        """Header text label.

        Args:
            master (HeaderSubheader): HeaderSubheader frame - (0,1) - top center of screen.
            header_text (str): Text to be displayed.
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(text=header_text, font=HEADER_FONT,
                    wraplength=750, justify='center', fg='white', bg='black')

        # Layout
        self.grid(row=0, column=0, sticky='N')


class SubHeader(Label):
    def __init__(self, master: HeaderSubheader, subheader_text: str):
        """Subheader text label.

        Args:
            master (HeaderSubheader) : HeaderSubheader frame - (0,1) - top center of screen.
            subheader_text (str): Text to be displayed.
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(text=subheader_text, font=SUBHEADER_FONT,
                    wraplength=750, justify='center', fg='white', bg='black')

        # Layout
        self.grid(row=1, column=0, sticky='N')
