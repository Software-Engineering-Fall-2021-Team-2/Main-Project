
from BaseFrame import *
import datetime
import json


class PlayerAction(MyBaseFrame):

    red_names, green_names = ([] for i in range(2))

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

        with open('redTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.red_names.append(i)

        with open('greenTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.green_names.append(i)

        # Populate
        header = Header(self, self.header_text, self.subheader_text)
        master_widget = MasterWidget(self)

        # Layout
        header.grid(row=0, column=1, sticky='NSEW')
        master_widget.grid(row=1, column=1, sticky='NSEW')

        # Debug
        print(self.red_names)


class MasterWidget(Frame):
    def __init__(self, master: MyBaseFrame):
        """MasterWidget - displays team information, game action, and time

        Args:
            master (MyBaseFrame): [description]
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure - 3x4 grid
        self.config(borderwidth=1, bg='black')

        self.columnconfigure((0, 2), weight=15)              # Content Columns
        self.columnconfigure(1, weight=3)                   # Spacer Column

        # Team & Timer Rows
        self.rowconfigure((0, 4), weight=1)
        # Players & Score Row
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=4)                      # Game Feed Row

        # Populate
        red_team_label = TableHeaderLabel(self, "RED TEAM", 'red')
        green_team_label = TableHeaderLabel(self, "GREEN TEAM", 'green')
        timer = MyTimer(self, self.master.time_seconds)

        # Layout
        red_team_label.grid(row=0, column=0, sticky='NSEW')
        green_team_label.grid(row=0, column=2, sticky='NSEW')
        timer.grid(row=4, column=2, columnspan=2, sticky='SE')


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
        self.config(font='Times 20', fg='yellow',
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
