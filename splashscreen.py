
from tkinter import *
from BaseFrame import MyBaseFrame


class SplashScreen(MyBaseFrame):

    def __init__(self, controller):
        MyBaseFrame.__init__(self, controller)

        # TODO: figure out how to stretch the image to fill the frame
        image_container = Canvas(self)
        image_container.pack(expand="YES", fill="both")

        splash_image = PhotoImage(file="logo.png")
        image_container.create_image(
            self.controller.SCREEN_WIDTH/2, self.controller.SCREEN_HEIGHT/2, anchor=CENTER, image=splash_image)
        image_container.image = splash_image

        self.set_timer()

    # TODO: make timer start player entry
    def set_timer(self):
        self.after(self.controller.SPLASHSCREEN_LENGTH *
                   1000, lambda: print("Passaged"))
