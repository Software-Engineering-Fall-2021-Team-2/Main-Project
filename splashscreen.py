
from tkinter import *
from BaseFrame import MyBaseFrame


class SplashScreen(Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.image = PhotoImage(file="logo.png")

        # Configuration
        self.config(bg='black')

        # Populate
        screen = ImageCanvas(self, controller, self.image)

        # Layout
        # TODO: figure out how to stretch the image to fill the frame
        # image_container = Canvas(self)
        # image_container.pack(expand="YES", fill="both")

        """splash_image = PhotoImage(file="logo.png")
        image_container.create_image(
            self.controller.SCREEN_WIDTH/2, self.controller.SCREEN_HEIGHT/2, anchor=CENTER, image=splash_image)
        image_container.image = splash_image """

        # self.set_timer()

    # TODO: make timer start player entry
    # TODO: Move timer to BaseFrame
    def set_timer(self):
        self.after(self.controller.SPLASHSCREEN_LENGTH *
                   1000, lambda: print("Passaged"))


class ImageCanvas(Canvas):
    def __init__(self, parent, controller, image, *args, **kwargs):
        Canvas.__init__(self, parent, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.image = image

        # Configuration

        # Populate
        self.create_image(self.controller.SCREEN_WIDTH/2,
                          self.controller.SCREEN_HEIGHT/2, anchor=CENTER, image=self.image)

        # Layout
        self.pack(expand="YES", fill="both")
