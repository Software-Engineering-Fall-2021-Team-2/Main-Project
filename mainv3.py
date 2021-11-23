
from tkinter import *
from tkinter import font as tkfont
from BaseFrame import *
from Countdown import Countdown
from PlayerEntry import *
from splashscreen import *
from PlayerAction import *


class Container(Tk):
    """[summary]

    Args:
        Tk ([type]): [description]
    """

    # Main Class for the file
    # Sets up "global variables" for the file
    def __init__(self, *args, **kwargs) -> None:

        Tk.__init__(self,  *args, **kwargs)
    
        # Object Configuration
        self.GLOBAL_VAR_INIT()

        # Private variable to hold a frame object
        self._frame = None

        # Set the first frame
        self.switch_frame(Countdown)

        # Close Keystroˇke
        self.bind('<a>', lambda event = None: self.destroy())

        


    def GLOBAL_VAR_INIT(self):
        """Method to define class variables that act as the global variables for the application"""
        # Font setup
        # TODO: Setup colors, Make a config file?
        self.HEADER_FONT = tkfont.Font(
            family='Verdana', size=18, weight="bold")
        self.SUBHEADER_FONT = tkfont.Font(
            family='Verdana', size=12, weight="bold")

        self.NUM_PLAYERS = 15

        # Screen size in px
        self.SCREEN_HEIGHT = 600
        self.SCREEN_WIDTH = 1000
        self.geometry("{}x{}".format(self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Time lengths in seconds
        self.SPLASHSCREEN_LENGTH = 5
        self.COUNTDOWN_LENGTH = 10
        self.PLAYERACTION_LENGTH = 60

        # Window title
        Tk.wm_title(self, "PHOTON")

        # Basic grid set up
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self,self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = Container()
    root.mainloop()
