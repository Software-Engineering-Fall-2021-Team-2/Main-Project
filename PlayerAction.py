from tkinter import *
from BaseFrame import MyBaseFrame
import dbconnect
import datetime


class PlayerAction(MyBaseFrame):
    """[summary]

    Args:
        MyBaseFrame ([type]): [description]
    """
    _header_text = "Play Screen"
    _subheader_text = "Game Action"

    def __init__(self, parent, controller, *args, **kwargs):
        MyBaseFrame.__init__(self, parent, controller,
                             self._header_text, self._subheader_text, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller

        self._time_seconds = controller.PLAYERACTION_LENGTH
        self._time_mmss = StringVar()


        # Layout
        #timer = MyTimer(self, self.controller)
        self._timer = Label(self, textvariable=self._time_mmss,
                           font='Times 50', fg='yellow', bg='Black')
        self._timer.grid(row=0, column=2, rowspan=1, columnspan=1, sticky="NSEW" )

        self._update_timer()

    def _update_timer(self):
        if self._time_seconds < 1:
            # switch screen
            return
        tmp = str(datetime.timedelta(seconds=self._time_seconds))

        self._time_mmss.set(tmp[2:])
        self.update()
        self._time_seconds -= 1
        self.after(1000, self._update_timer)




"""
class MyTimer(Label):

    def __init__(self, parent, controller, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self._parent = parent
        self._controller = controller
        self._time_seconds = controller.PLAYERACTION_LENGTH
        self._time_mmss = StringVar()

        # Config
        self.config(font='Times 50', fg='yellow',
                    bg='black', textvariable=self._time_mmss)

        # Layout
        self.grid(row=0, column=0, sticky="NSEW")

        # Update
        self._update_timer()

    def _update_timer(self):
        if self._time_seconds < 1:
            # switch screen
            return

        tmp = str(datetime.timedelta(seconds=self._time_seconds))

        self._time_mmss.set(tmp[2:])
        self.update()
        self._time_seconds -= 1
        self.after(1000, self._update_timer)
"""