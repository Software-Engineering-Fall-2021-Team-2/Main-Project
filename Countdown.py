
from tkinter import *
from BaseFrame import MyBaseFrame
import datetime


class Countdown(MyBaseFrame):

    def __init__(self, parent, controller, *args, **kwargs):
        MyBaseFrame.__init__(self, parent, controller, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller

        self._time_seconds = controller.COUNTDOWN_LENGTH
        self._sec = StringVar()
        self._timer = Label(self, textvariable=self._sec,
                           font='Times 300', fg='Purple', bg='Black')
        self._timer.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="NSEW" )

        self._update_clock()

    def _update_clock(self):
        if self._time_seconds < 1:
            # switch screen
            return
        # Set the sec var to contain the correct time
        self._sec.set(self._time_seconds)
        self.update()
        self._time_seconds -= 1
        self.after(1000, self._update_clock)
