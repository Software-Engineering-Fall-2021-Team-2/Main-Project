
from tkinter import *
from BaseFrame import MyBaseFrame
import datetime


class Countdown(MyBaseFrame):

    def __init__(self, parent, controller, *args, **kwargs):
        MyBaseFrame.__init__(self, parent, controller, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller

        self.time_seconds = controller.COUNTDOWN_LENGTH
        self.sec = StringVar()
        self.timer = Label(self, textvariable=self.sec,
                           font='Times 300', fg='Purple', bg='Black')
        self.timer.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="NSEW" )

        self.update_clock()

    # BUG: 30 is not displayed properly on the screen
    def update_clock(self):
        if self.time_seconds < 1:
            # switch screen
            return
        # Set the sec var to contain the correct time
        self.sec.set(self.time_seconds)
        self.update()
        self.time_seconds -= 1
        self.after(1000, self.update_clock)
