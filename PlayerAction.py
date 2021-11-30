
from tkinter import font
from BaseFrame import *
import datetime
import json
import UDPClient
import random
import time


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
        self.red_names = []
        self.green_names = []
        self.red_ids = []
        self.green_ids = []

        with open('redTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.red_names.append(i)
        self.red_team = {key: None for key in self.red_names}

        with open('greenTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.green_names.append(i)
        self.green_team = {key: None for key in self.green_names}

        with open('redID.txt', 'r') as file:
            p =json.load(file)
            for i in p:
                self.red_ids.append(i)

        with open('greenID.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.green_ids.append(i)

        # Populate
        header = Header(self, self.header_text, self.subheader_text)
        master_widget = MasterWidget(self, self.red_names, self.green_names, self.red_ids, self.green_ids)

        # Layout
        header.grid(row=0, column=1, sticky='NSEW')
        master_widget.grid(row=1, column=1, sticky='NSEW')

        # Debug
        #print(self.red_team)

class MasterWidget(Frame):
    def __init__(self, master: MyBaseFrame, red_team: list, green_team: list, redID: list, greenID: list):
        """MasterWidget - displays team information, game action, and time

        Args:
            master (Tk): Widget that is directly resposible for owning this widget (Container)
        """
        # Set Object Attributes
        super().__init__(master)
        self.red_names = red_team
        self.green_names = green_team
        self.red_ids = redID
        self.green_ids = greenID

        # Configure - 3x4 grid
        self.config(borderwidth=1, bg='black')
        self.columnconfigure((0, 2), weight=15)             # Content Columns
        self.columnconfigure(1, weight=3)                   # Spacer Column
        self.rowconfigure((0, 4), weight=1)                 # Team & Timer Rows
        self.rowconfigure(1, weight=3)                      # Player/Score Row
        self.rowconfigure(2, weight=4)                      # Game Feed Row

        # Populate
        red_team_label = TableHeaderLabel(self, "RED TEAM", 'red')
        green_team_label = TableHeaderLabel(self, "GREEN TEAM", 'green')
        timer = MyTimer(self, self.master.time_seconds)
        red_info = RedInformation(self, self.red_names)
        green_info = GreenInformation(self, self.green_names)
        action_screen = ActionScreen(self, self.red_ids, self.green_ids, self.red_names,
        self.green_names)

        # Layout
        red_team_label.grid(row=0, column=0, sticky='NSEW')
        green_team_label.grid(row=0, column=2, sticky='NSEW')
        timer.grid(row=4, column=2, columnspan=2, sticky='SE')
        red_info.grid(row=1, column=0, sticky='NSEW')
        green_info.grid(row=1, column=2, sticky='NSEW')
        action_screen.grid(row=2,column=0, columnspan=3, sticky='NSEW')


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


class RedInformation(Frame):
    def __init__(self, master: Frame, players: list):
        """[summary]

        Args:
            master (Frame): Frame that is directly resposible for owning this widget (Container)
            players (list): List of Red team players
        """
        # Set Object Attributes
        super().__init__(master)
        self.players = players

        # Configure
        self.config(bg='black')
        self.rowconfigure(tuple(range(15)), weight=1)
        self.columnconfigure(0, weight=8)
        self.columnconfigure(1, weight=2)

        for index, value in enumerate(players):
            tmp = 0
            name = Label(self, bg='black', fg='red',
                         text=value, font=SUBHEADER_FONT)
            name.grid(row=index, column=0, sticky='NSW')

            score = Label(self, bg='black', fg='red',
                          text=tmp, font=SUBHEADER_FONT)
            score.grid(row=index, column=1, sticky='NSE')

            # TODO: make UDP thing update this guy
            self.master.master.red_team[value] = score

            total = name = Label(self, bg='black', fg='red',
                         text=0, font=SUBHEADER_FONT)
            total.grid(row=15,column=1,sticky='NSE')

class GreenInformation(Frame):
    def __init__(self, master: Frame, players: list):
        """[summary]

        Args:
            master (Frame): Frame that is directly resposible for owning this widget (Container)
            players (list): List of Green team players.
        """
        # Set Object Attributes
        super().__init__(master)
        self.players = players

        # Configure
        self.config(bg='black')
        self.rowconfigure(tuple(range(15)), weight=1)
        self.columnconfigure(0, weight=8)
        self.columnconfigure(1, weight=2)

        for index, value in enumerate(players):
            tmp = 0
            name = Label(self, bg='black', fg='green',
                         text=value, font=SUBHEADER_FONT)
            name.grid(row=index, column=0, sticky='NSW')

            score = Label(self, bg='black', fg='green',
                          text=tmp, font=SUBHEADER_FONT)
            score.grid(row=index, column=1, sticky='NSE')

            # TODO: make UDP thing update this guy
            self.master.master.green_team[value] = score

        total = name = Label(self, bg='black', fg='green',
                         text=0, font=SUBHEADER_FONT)
        total.grid(row=15,column=1,sticky='NSE')

class ActionScreen(Frame):
        def __init__(self, master: Frame, redID: list, greenID: list, redName: list, greenName: list):
            """[summary]

            Args:
            master (Frame): Frame that is directly resposible for owning this widget (Container)
                redID (list): [description]
                greenID (list): [description]
                redName (list): [description]
                greenName (list): [description]
            """
            # Set Object Attributes
            super().__init__(master)
            self.red_names = redName
            self.green_names = greenName
            self.red_ids = redID
            self.green_ids = greenID
            self.counter = 0

            # Configure
            self.config(bg='grey')
            self.rowconfigure(tuple(range(5)), weight=1)
            self.columnconfigure(0, weight=8)
            self.columnconfigure(1, weight=2)

            #Execute Game Action
            self.action()

        def action(self):
            if self.counter > 20:
                return
            message = UDPClient.UDPconnect(self.red_ids, self.green_ids)
            ids = message.split(':')
            if ids[0] in self.red_ids:
                index1 = self.red_ids.index(ids[0])
                player1 = self.red_names[index1]
                print(player1)
                if ids[1] in self.green_ids:
                    index2 = self.green_ids.index(ids[1])
                    player2 = self.green_names[index2]
                    print(player2)
                elif ids[1] in self.red_ids:
                    index2 = self.red_ids.index(ids[1])
                    player2 = self.red_names[index2]
                    print(player2)
            elif ids[0] in self.green_ids:
                index1 = self.green_ids.index(ids[0])
                player1 = self.green_names[index1]
                print(player1)
                if ids[1] in self.green_ids:
                    index2 = self.green_ids.index(ids[1])
                    player2 = self.green_names[index2]
                    print(player2)
                elif ids[1] in self.red_ids:
                    index2 = self.red_ids.index(ids[1])
                    player2 = self.red_names[index2]
                    print(player2)

            displayMessage = str(player1) + ' hit ' + str(player2)
            print(displayMessage)
            name = Label(self, bg='gray', fg='black',
                         text=displayMessage, font=SUBHEADER_FONT)
            name.grid(row=self.counter, column=0, sticky='NSW')
            self.update()
            self.counter += 1
            t = random.randint(1,3) * 1000
            self.after(t, self.action)
