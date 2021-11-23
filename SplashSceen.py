
from BaseFrame import *
# TODO: Figure out if this import is required here?
from PlayerEntry import PlayerEntry


class SplashScreen(MyBaseFrame):

    def __init__(self, master: Tk,):
        """Splash screen frame - shows for x number of seconds - denoted in main

        Args:
            master (Tk): Widget that is directly resposible for owning this widget - always Container.
        """
        # Set Object Attributes
        super().__init__(master)
        self.image = PhotoImage(file='logo.png')

        # Configure
        self.config(bg='black')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Populate
        splash = FullScreenImageCanvas(self, self.image)

        # Countdown
        self.set_timer()

    def set_timer(self):
        # Switches the screen after x seconds - denoted in main.py config
        self.after(SPLASHSCREEN_LENGTH *
                   1000, lambda: self.master.switch_frame(PlayerEntry))


class FullScreenImageCanvas(Canvas):
    def __init__(self, master: MyBaseFrame, image: PhotoImage):
        """Canvas for holding the the splash screen image - needed because tkinter requires images be held in a canvas

        Args:
            master (MyBaseFrame): Frame that is directly resposible for owning this widget.
            image (PhotoImage): Photo to be displayed
        """
        # Set Object Attributes
        super().__init__(master)
        self.image = image

        # Configure
        # TODO: figure out how to stretch the image to fill the frame
        self.config(bg='black')
        self.create_image(SCREEN_WIDTH/2,
                          SCREEN_HEIGHT/2, anchor=CENTER, image=self.image)

        # Layout
        self.grid(row=0, column=0, rowspan=3, columnspan=3, sticky='NSEW')
