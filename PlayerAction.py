
from BaseFrame import *
import datetime


class PlayerAction(MyBaseFrame):

    header_text = "Play Screen"
    subheader_text = "Game Action"

    def __init__(self, master: Tk):
        """PlayerAction screen - updates with feed of whatever
        # TODO: Change the description of the PlayerAction screen

        Args:
            master (Tk): Widget that is directly resposible for owning this widget (Container)
        """
        # Set Object Attributes
        super().__init__(master)
        self.time_seconds = PLAYERACTION_LENGTH

        # Populate
        timer = MyTimer(self, self.controller, self.time_seconds)

        # Layout
        timer.grid(row=0, column=2, sticky='NSEW')


class MyTimer(Label):

    def __init__(self, master: MyBaseFrame, time: int):
        """MM:SS style timer.

        Args:
            master (MyBaseFrame): Frame that is directly resposible for owning this widget
            time (int): Time in seconds - derrived from main.py config method
        """
        # Set Object Attributes
        super().__init__(master)
        self.time_seconds = time
        self.time_mmss = StringVar()    # Placeholder Initilaization

        # Configure
        self.config(font='Times 50', fg='yellow',
                    bg='black', textvariable=self.time_mmss)

        # Run
        self.update_timer()

    def update_timer(self):
        if self.time_seconds < 1:
            # TODO: make this call another screen
            return
        tmp = str(datetime.timedelta(seconds=self.time_seconds))
        self.time_mmss.set(tmp[2:])
        self.update()
        self.time_seconds -= 1
        self.after(1000, self.update_timer)
