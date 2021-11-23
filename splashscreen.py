
from BaseFrame import *


class SplashScreen(MyBaseFrame):

    def __init__(self, parent: Tk, controller: Tk, *args, **kwargs):
        """Splash screen frame - shows for x number of seconds - denoted in main

        Args:
            parent (Tk): Widget that is directly resposible for owning this widget - always Container.
            controller (Tk): Top widget - passed down to every widget in order to maintain a heirarchy of widgets - always Container.
        """
        # Set Object Attributes
        super().__init__(parent, controller)
        self.image = PhotoImage(file="logo.png")

        # Configure
        self.config(bg='black')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Populate
        splash = ImageCanvas(self, controller, self.image)


        # Countdown
        # self.set_timer()
"""
    def set_timer(self):
        # Switches the screen after x seconds - denoted in main
        self.after(self.controller.SPLASHSCREEN_LENGTH *
                   1000, lambda: self.controller.switch_frame(PlayerEntry))
"""


class ImageCanvas(Canvas):
    def __init__(self, parent: SplashScreen, controller: Tk, image: PhotoImage):
        """Canvas for holding the the splash screen image - needed because tkinter requires images be held in a canvas

        Args:
            parent (SplashScreen): Widget that is directly resposible for owning this widget.
            controller (Tk): Top widget - passed down to every widget in order to maintain a heirarchy of widgets - always Container.
            image (PhotoImage): Photo to be displayed
        """
        # Set Object Attributes
        super().__init__(parent)
        self.controller = controller
        self.image = image

        # Configure
        # TODO: figure out how to stretch the image to fill the frame
        self.config(bg='black')
        self.create_image(self.controller.SCREEN_WIDTH/2,
                          self.controller.SCREEN_HEIGHT/2, anchor=CENTER, image=self.image)

        # Layout
        self.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="NSEW")
