from tkinter import *
import dbconnect
import json
import time


LARGE_FONT = ("Verdana", 18)
MEDIUM_FONT = ("Verdana", 12)
NUM_PLAYERS = 15
SCREEN_HEIGHT = 586
SCREEN_WIDTH = 919
SPLASHSCREEN_LENGTH = 1  # in seconds

# TODO: Divide class into individual files

# Inherits from the Tk tkinter class


class Container(Tk):

    def __init__(self, *args, **kwargs,):

        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, "PHOTON")

        container = Frame(self, bg="black")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (SplashScreen, PlayerEntry, Countdown, PlayerAction):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SplashScreen)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def start_countdown(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.start_timer()


class SplashScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")

        image_splash_screen = PhotoImage(file="logo.png")

        image_container_splash_screen = Label(
            self, image=image_splash_screen)

        # HACK: IDK why this line is required, but it works
        image_container_splash_screen.image = image_splash_screen

        image_container_splash_screen.grid(row=0, column=0, sticky="NSEW")
        #image_container_splash_screen.place(relx=.5, rely=.5, anchor=CENTER)

        # after existing for x seconds, switch to PlayerEntry
        self.after(SPLASHSCREEN_LENGTH * 1000,
                   lambda: controller.show_frame(PlayerEntry))


class PlayerEntry(Frame):
    red_ids, red_names, green_ids, green_names = ([] for i in range(4))

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")

        top_label = Label(self, font=LARGE_FONT, fg="white", background="black",
                          text="Press enter to get your code name if you have played before, otherwise, submit your team before playing")
        top_label.pack(pady=5, padx=5)

        bottom_label = Label(self, font=MEDIUM_FONT, fg="white", background="black",
                             text="Press F5 to start game once teams have been submitted")
        bottom_label.pack(pady=5, padx=5)

        # Canvas for handling the grid
        grid_frame = Frame(self, bg="black", bd=1)
        grid_frame.pack(fill="both", expand=True, pady=50, padx=20)

        # grid setup
        grid_frame.columnconfigure([0, 2], weight=1, minsize=1)
        grid_frame.columnconfigure([1, 3], weight=20, minsize=1)
        grid_frame.rowconfigure(tuple(range(16)), weight=1)

        # Table header setup
        red_team_ids = Label(grid_frame, bg="black",
                             fg="red", font=MEDIUM_FONT, text="IDS")
        red_team_ids.grid(row=0, column=0, sticky="NSEW")

        red_team_label = Label(grid_frame, bg="black",
                               fg="red", font=LARGE_FONT, text="RED TEAM")
        red_team_label.grid(row=0, column=1, sticky="NSEW")

        green_team_ids = Label(grid_frame, bg="black",
                               fg="green", font=MEDIUM_FONT, text="IDS")
        green_team_ids.grid(row=0, column=2, sticky="NSEW")

        green_team_label = Label(
            grid_frame, bg="black", fg="green", font=LARGE_FONT, text="GREEN TEAM")
        green_team_label.grid(row=0, column=3, sticky="NSEW")

        # Initilazing every element in the table
        for i in range(1, 17):
            red_id = Entry(grid_frame, bg="grey", fg="black", width=3)
            red_id.grid(row=i, column=0, sticky="NSEW")
            self.red_ids.append(red_id)

            red_name = Entry(grid_frame, bg="grey", fg="black")
            red_name.grid(row=i, column=1, sticky="NSEW")
            self.red_names.append(red_name)

            green_id = Entry(grid_frame, bg="grey", fg="black", width=3)
            green_id.grid(row=i, column=2, sticky="NSEW")
            self.green_ids.append(green_id)

            green_name = Entry(grid_frame, bg="grey", fg="black")
            green_name.grid(row=i, column=3, sticky="NSEW"),
            self.green_names.append(green_name)

        controller.bind('<Return>', lambda event: self.pull_names(event))
        controller.bind('<a>', lambda event = NONE: controller.start_countdown(Countdown))
                      #"""lambda event = NONE:""" controller.start_countdown(Countdown))

    # pull names from db using ID entered
    def pull_names(self, event):
        print("called")
        for i in range(NUM_PLAYERS):
            if len(self.red_ids[i].get()) != 0:
                # * Changed from convertToInt to int() wrapper, test if this works
                red_id = int(self.red_ids[i].get())
                if(dbconnect.checkdb(red_id)):
                    self.set_name(
                        self.red_names[i], dbconnect.retrieveCode(red_id))
        for i in range(NUM_PLAYERS):
            if len(self.green_ids[i].get()) != 0:
                # TODO : HOW DO YOU HANDLE ERRORS FROM NOT AN INT
                green_id = int(self.green_ids[i].get())
                if(dbconnect.checkdb(green_id)):
                    self.set_name(
                        self.green_names[i], dbconnect.retrieveCode(green_id))

    # WHAT: What does this do?
    def set_name(self, name, text):
        name.delete('0', 'end')
        name.insert('0', text)        



# TODO: Make this work
"""
def send_data():
    for i in range(NUM_PLAYERS):
        if len(red_ids[i].get()) != 0:
            # * Changed from convertToInt to int() wrapper, test if this works
            id = int(red_ids[i].get())
            name = red_names[i].get()
            if not(dbconnect.checkdb(id)):
                record = (id, name)
                dbconnect.addRecord(record)
    for i in range(NUM_PLAYERS):
        if len(green_ids[i].get()) != 0:
            # * Changed from convertToInt to int() wrapper, test if this works
            id = int(green_ids[i].get())
            name = green_names[i].get()
            if not(dbconnect.checkdb(id)):
                record = (id, name)
                dbconnect.addRecord(record)
"""


class Countdown(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")
        # WHAT: StringVar()?
        self.sec = StringVar()

        self.timer = Label(self, textvariable=self.sec,
                      font='Times 300', fg='Purple', bg='Black')
        self.timer.pack()

    # BUG: 30 is not displayed properly on the screen
    def start_timer(self):
        seconds = 5
        while seconds > -1:
            self.sec.set(seconds)
            self.timer.update()
            time.sleep(1)
            seconds -= 1
            #if seconds == 0:
        lambda event = NONE: self.controller.start_countdown(PlayerAction)
        


class PlayerAction(Frame):

    red_names = []
    green_names = []
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")

        # Table Setup
        self.columnconfigure(tuple(range(5)), weight=1)
        self.rowconfigure(tuple(range(30)), weight = 1)

        # Title and label setup
        title = Label(self, bg= "black", font=LARGE_FONT, fg="purple", text="Play Screen", borderwidth=0)
        title.grid(row=0, column=0, sticky="NSEW", columnspan=5, rowspan=3)

        red_team = Label(self, bg= "black", font=MEDIUM_FONT, fg="red", text="Red Team", borderwidth=0)
        red_team.grid(row=3, column=0, sticky="NSEW", columnspan=1, rowspan=2)

        red_team_scores = Label(self, bg= "black", font=MEDIUM_FONT, fg="red", text="Scores", borderwidth=0)
        red_team_scores.grid(row=3, column=1, sticky="NSEW", columnspan=1, rowspan=2)

        green_team = Label(self, bg= "black", font=MEDIUM_FONT, fg="green", text="Green Team", borderwidth=0)
        green_team.grid(row=3, column=2, sticky="NSEW", columnspan=1, rowspan=2)

        green_team_scores = Label(self, bg= "black", font=MEDIUM_FONT, fg="green", text="Scores", borderwidth=0)
        green_team_scores.grid(row=3, column=3, sticky="NSEW", columnspan=1, rowspan=2)

        # Get CodeNames from file
        self.get_names()

        """# Setup Table
        for i in range(4, 20):
            red_name = Label(self, bg= "black", font=MEDIUM_FONT, fg="red", text=self.red_names[i-4], borderwidth=0)
            red_name.grid(row=i, column=0, sticky="NSEW", columnspan=1, rowspan=1)

            green_name = Label(self, bg= "black", font=MEDIUM_FONT, fg="green", text=self.green_names[i-4], borderwidth=0)
            green_name.grid(row=i, column=2, sticky="NSEW", columnspan=1, rowspan=1)"""

        # Timer setup
        self.sec = StringVar()

        self.timer = Label(self, textvariable=self.sec,
                      font='Times 300', fg='Purple', bg='Black')
        self.timer.grid()

    def get_names(self):
        with open('redTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.red_names.append(i)
        with open('greenTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.green_names.append(i)
        

    def start_timer(self):
        seconds = 30
        while seconds > -1:
            self.sec.set(seconds)
            self.timer.update()
            time.sleep(1)
            seconds -= 1





root = Container()
root.geometry("{}x{}".format(SCREEN_WIDTH, SCREEN_HEIGHT))

root.mainloop()
