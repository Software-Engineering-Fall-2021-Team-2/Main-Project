from os import kill
from BaseFrame import *


class SplashScreen(MyBaseFrame):

    def __init__(self, controller):
        MyBaseFrame.__init__(self, controller)

        # width=self.controller.SCREEN_WIDTH, height=self.controller.SCREEN_HEIGHT)
        image_container = Canvas(self, bg='black')
        image_container.pack(expand="YES", fill="both")

        splash_image = PhotoImage(file="logo.png")
        #image_container.create_image(self.controller.SCREEN_WIDTH/2, self.controller.SCREEN_HEIGHT/2, anchor=CENTER, image=splash_image)
        image_container.create_image(20, 20, anchor=CENTER, image=splash_image)

        """
        image_container_splash_screen = Label(
            self, image=spalsh_image)

        # HACK: IDK why this line is required, but it works
        image_container_splash_screen.image = spalsh_image

        image_container_splash_screen.grid(
            row=0, column=0, sticky="NSEW", rowspan=3, columnspan=3)
        #image_container_splash_screen.place(relx=.5, rely=.5, anchor=CENTER)"""

        # after existing for x seconds, switch to PlayerEntry
        """self.after(self.controller.SPLASHSCREEN_LENGTH *
                   1000, print("Passaged"))"""
