"""Instead of using basic tkinter, ttkthemes is used. It just looks prettier"""
from ttkthemes import ThemedTk, THEMES, ThemedStyle
from tkinter import ttk
from tkinter import font as tkfont


class Container(ThemedTk):

    # Main Class for the file
    # Sets up "global variables" for the file
    def __init__(self, *args, **kwargs) -> None:

        ThemedTk.__init__(self, fonts=True, themebg=True,
                          toplevel=True, *args, **kwargs)
        self.set_theme("equilux")

        # Font setup
        # TODO: Setup colors
        self.HEADER_FONT = tkfont.Font(
            family='Verdana', size=18, weight="bold")
        self.SUBHEADER_FONT = tkfont.Font(
            family='Verdana', size=12, weight="bold")

        self.NUM_PLAYERS = 15

        # Screen size in px
        self.SCREEN_HEIGHT = 600
        self.SCREEN_WIDTH = 1000

        # Time lengths in seconds
        self.SPLASHSCREEN_LENGTH = 1
        self.COUNTDOWN_LENGTH = 10
        self.PLAYERACTION_LENGTH = 60

        # Window title
        ThemedTk.wm_title(self, "PHOTON")

        # Basic grid set up
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_frame(self, container):
        # Pull up the correct frame, setting Container as the container
        # TODO: Make this initialize the frame rather than just raise it
        frame = self.frames[container]
        frame.tkraise()


if __name__ == "__main__":
    root = Container()
    root.mainloop()
