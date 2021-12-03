
# All library imports are done in Config.py
from Config import *

from Countdown import Countdown
from PlayerEntry import PlayerEntry
from SplashSceen import SplashScreen
from PlayerAction import PlayerAction


class Container(Tk):

    """The container widget that holds all of the frames. Only one exists.

    Args:
        Tk (Tk): A base tkinter widget
    """

    # Main Class for the file
    # Sets up "global variables" for the file
    def __init__(self):
        Tk.__init__(self)

        # Configure
        Tk.wm_title(self, "PHOTON")
        self.geometry("{}x{}".format(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # - Close Keystroke
        self.bind('<:>', lambda event=None: self.destroy())

        # - Exit Entry Box Keystroke
        self.bind("<Escape>", lambda event=None: self.focus_set())

        # Populate
        # - Private variable to hold a frame object
        self._frame = None

        # Layout
        # - Set the first frame
        self.to_SplashScreen()

    def to_SplashScreen(self):
        """Destroys current frame and replaces it with SplashScreen.
        """
        new_frame = SplashScreen(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

    def to_PlayerEntry(self):
        """Destroys current frame and replaces it with PlayerEntry.
        """
        new_frame = PlayerEntry(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

    def to_Countdown(self):
        """Destroys current frame and replaces it with Countdown.
        """
        new_frame = Countdown(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

    def to_PlayerAction(self):
        """Destroys current frame and replaces it with PlayerAction.
        """
        new_frame = PlayerAction(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)
