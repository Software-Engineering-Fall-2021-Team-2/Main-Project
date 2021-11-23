import datetime
from tkinter import *

import dbconnect
from BaseFrame import MyBaseFrame


class PlayerAction(MyBaseFrame):
    """[summary]

    Args:
        MyBaseFrame ([type]): [description]
    """
    header_text = "Play Screen"
    subheader_text = "Game Action"

    def __init__(self, parent, controller, *args, **kwargs):
        MyBaseFrame.__init__(self, parent, controller,
                             self.header_text, self.subheader_text, *args, **kwargs)
        # Object Attributes
        self.time_seconds = controller.PLAYERACTION_LENGTH

        # Layout
        timer = MyTimer(self, self.controller, time_seconds = self.time_seconds)


class MyTimer(Label):

    def __init__(self, parent, controller, *args, **kwargs):
        Label.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.grid(row=0, column=2, sticky="NSEW")

        self.time_seconds = kwargs.get('time_seconds')
        self.time_mmss = StringVar()

        # Config
        self.config(font='Times 50', fg='yellow',
                    bg='black', textvariable=self.time_mmss)

        # Layout

        # Update
        self.update_timer()

    def update_timer(self):
        if self.time_seconds < 1:
            # switch screen
            return

        tmp = str(datetime.timedelta(seconds=self.time_seconds))

        self.time_mmss.set(tmp[2:])
        self.update()
        self.time_seconds -= 1
        self.after(1000, self.update_timer)
