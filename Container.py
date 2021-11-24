
# All library imports are done in Config.py
from Config import *

from BaseFrame import MyBaseFrame
from Countdown import Countdown
from PlayerEntry import PlayerEntry
from SplashSceen import SplashScreen
from PlayerAction import PlayerAction


class Container(Tk):

    """[summary]

    Args:
        Tk ([type]): [description]
    """

    # Main Class for the file
    # Sets up "global variables" for the file
    def __init__(self):
        Tk.__init__(self)

        # Configure
        Tk.wm_title(self, "PHOTON")
        self.geometry("{}x{}".format(SCREEN_WIDTH, SCREEN_HEIGHT))

        # - Close Keystroke
        self.bind('<a>', lambda event=None: self.destroy())

        # - Exit Entry Box Keystroke
        self.bind("<Escape>", lambda event=None: self.focus_set())

        # Layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Populate

        # - Private variable to hold a frame object
        self._frame = None

        # - Set the first frame
        self.switch_frame(SplashScreen)

    def switch_frame(self, frame_class: MyBaseFrame):
        """Destroys current frame and replaces it with a new one."

        Args:
            frame_class (MyBaseFrame): [description]
        """
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)