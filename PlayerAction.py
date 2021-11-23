
from BaseFrame import *


class PlayerAction(MyBaseFrame):

    header_text = "Play Screen"
    subheader_text = "Game Action"

    def __init__(self, parent: Tk, controller: Tk):
        """PlayerAction screen - updates with feed of whatever
        # TODO: Change the description of the PlayerAction screen

        Args:
            parent (Tk): Widget that is directly resposible for owning this widget (Container)
            controller (Tk): Top widget - passed down to every widget in order to maintain a heirarchy of widgets - always Container.
        """
        # Set Object Attributes
        super().__init__(parent, controller, self.header_text, self.subheader_text)
        self.time_seconds = controller.PLAYERACTION_LENGTH

        # Populate
        timer = MyTimer(self, self.controller, self.time_seconds)


class MyTimer(Label):

    def __init__(self, parent: MyBaseFrame, controller: Tk, time: int):
        """MM:SS style timer.

        Args:
            parent (MyBaseFrame): Frame that is directly resposible for owning this widget - always Container.
            controller (Tk): Top widget - passed down to every widget in order to maintain a heirarchy of widgets - always Container.
            time (int): Time in seconds - derrived from main.py config method
        """
        # Set Object Attributes
        super().__init__(parent)
        self.controller = controller
        self.time_seconds = time
        self.time_mmss = StringVar()

        # Configure
        self.config(font='Times 50', fg='yellow',
                    bg='black', textvariable=self.time_mmss)

        # Layout
        self.grid(row=0, column=2, sticky="NSEW")

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
