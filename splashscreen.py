
from tkinter import *
from BaseFrame import MyBaseFrame
from PlayerEntry import PlayerEntry


class SplashScreen(Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        Frame.__init__(self, parent)

        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.image = PhotoImage(file="logo.png")

        # Configuration
        self.config(bg='black')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Populate
        screen = ImageCanvas(self, controller, self.image)

        # Layout
        self.set_timer()

    def set_timer(self):
        self.after(self.controller.SPLASHSCREEN_LENGTH *
                   1000, lambda: self.controller.switch_frame(PlayerEntry))


class ImageCanvas(Canvas):
    def __init__(self, parent, controller, image, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.image = image

        # Configuration
        self.config(bg='black')

        # Populate
        # TODO: figure out how to stretch the image to fill the frame
        self.create_image(self.controller.SCREEN_WIDTH/2,
                          self.controller.SCREEN_HEIGHT/2, anchor=CENTER, image=self.image)

        # Layout
        self.pack(expand="YES", fill="both")
