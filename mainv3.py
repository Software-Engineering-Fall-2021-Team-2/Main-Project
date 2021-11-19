
from tkinter import *
from tkinter import font as tkfont
from BaseFrame import *
from PlayerEntry import *
from SplashScreen import *


class Container(Tk):

    # Main Class for the file
    # Sets up "global variables" for the file
    def __init__(self, *args, **kwargs) -> None:

        Tk.__init__(self,  *args, **kwargs)
        self.GLOBAL_VAR_INIT()
        self._frame = None

        self.switch_frame(SplashScreen)

        self.bind('<a>', lambda event = None: self.destroy())

        


    def GLOBAL_VAR_INIT(self):
        """Method to define class variables that act as the global variables for the application"""
        # Font setup
        # TODO: Setup colors
        # TODO: Make a config file?
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



    def start_frame(self, container):
        # Pull up the correct frame, setting Container as the container
        # TODO: Make this initialize the frame rather than just raise it

        frame = self.frames[container]
        # NOTE: Used to set the frame in the column correctly
        frame.pack(side="top", fill="both", expand=True, ipadx=10, ipady=10)

        frame.tkraise()

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
