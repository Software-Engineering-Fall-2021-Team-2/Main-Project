
from tkinter import *
from BaseFrame import MyBaseFrame


class Countdown(MyBaseFrame):

    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(self, parent, controller, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller
        self.sec = StringVar()
        self.timer = Label(self, textvariable=self.sec,
                           font='Times 300', fg='Purple', bg='Black')
        self.timer.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="NSEW" )

        self.start_timer()

    # BUG: 30 is not displayed properly on the screen
    def start_timer(self):
        seconds = 5
        while seconds > -1:
            self.sec.set(seconds)
            self.timer.update()
            self.timer.after.(1000)
            seconds -= 1
            # if seconds == 0:
