from tkinter import *
import dbconnect
import json
import time
import datetime


LARGE_FONT = ("Verdana", 18)
MEDIUM_FONT = ("Verdana", 12)
NUM_PLAYERS = 15
SCREEN_HEIGHT = 586
SCREEN_WIDTH = 919
SPLASHSCREEN_LENGTH = 1  # in seconds
red_names, green_names, red_ids, green_ids = ([] for i in range(4))

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
    r_id, r_name, g_id, g_name = ([] for i in range(4))

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
            self.r_id.append(red_id)

            red_name = Entry(grid_frame, bg="grey", fg="black")
            red_name.grid(row=i, column=1, sticky="NSEW")
            self.r_name.append(red_name)

            green_id = Entry(grid_frame, bg="grey", fg="black", width=3)
            green_id.grid(row=i, column=2, sticky="NSEW")
            self.g_id.append(green_id)

            green_name = Entry(grid_frame, bg="grey", fg="black")
            green_name.grid(row=i, column=3, sticky="NSEW"),
            self.g_name.append(green_name)

        controller.bind('<Return>', lambda event: self.connection(event))
        controller.bind('<a>', lambda event = NONE: controller.start_countdown(Countdown))
                      #"""lambda event = NONE:""" controller.start_countdown(Countdown))

    def writeInfo(self):
        redTeam, greenTeam, redID, greenID = ([] for i in range(4))

        for i in range(15):
            if len(self.r_id[i].get()) != 0:
                id = self.r_id[i].get()
                name = self.r_name[i].get()
                redTeam.append(name)
                redID.append(id)
            if len(self.g_id[i].get()) != 0:
                id = self.g_id[i].get()
                name = self.g_name[i].get()
                greenTeam.append(name)
                greenID.append(id)
            with open('redTeam.txt', 'w') as file:
                file.write(json.dumps(redTeam))
            with open('greenTeam.txt', 'w') as file:
                file.write(json.dumps(greenTeam))
            with open('redID.txt', 'w') as file:
                file.write(json.dumps(redID))
            with open('greenID.txt', 'w') as file:
                file.write(json.dumps(greenID))

    # connects to database
    def connection(self, event):
        records = []

        for i in range(15):
            if len(self.r_id[i].get()) != 0:
                red_id = int(self.r_id[i].get())
                red_name = self.r_name[i].get()
                record = (red_id, red_name)
                records.append(record)
            if len(self.g_id[i].get()) != 0:
                green_id = int(self.g_id[i].get())
                green_name = self.g_name[i].get()
                record = (green_id, green_name)
                records.append(record)

        newRecords = dbconnect.connect(records)

        for x in newRecords:
            id = x[0]
            name = x[1]
            for i in range(15):
                if len(self.r_id[i].get()) != 0:
                    if (int(self.r_id[i].get()) == id):
                        self.setName(self.r_name[i], name)
                if len(self.g_id[i].get()) != 0:
                    if (int(self.g_id[i].get()) == id):
                        self.setName(self.g_name[i], name)

        self.writeInfo()

    # Puts names in Entry boxes if codename exists in database (Doesn't work right now)
    def setName(self, name, text):
        name.delete(0, 'end')
        name.insert(0, text)

class Countdown(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")
        # WHAT: StringVar()?
        self.sec = StringVar()
        self.controller = controller

        self.timer = Label(self, textvariable=self.sec,
                      font='Times 300', fg='Purple', bg='Black')
        self.timer.place(relx=0.5, rely=0.5, anchor=CENTER)

    # BUG: 30 is not displayed properly on the screen
    def start_timer(self):
        seconds = 5
        while seconds > -1:
            self.sec.set(seconds)
            self.timer.update()
            time.sleep(1)
            seconds -= 1
            #if seconds == 0:
        self.controller.start_countdown(PlayerAction)



class PlayerAction(Frame):

    r_name = []
    g_name = []

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

        # Setup Table
        count = 5
        for i in self.r_name:
            red_name = Label(self, bg= "black", font=MEDIUM_FONT, fg="red", text=i, borderwidth=0)
            red_name.grid(row=count, column=0, sticky="NSEW", columnspan=1, rowspan=1)
            count +=1

        count = 5
        for i in self.g_name:
            green_name = Label(self, bg= "black", font=MEDIUM_FONT, fg="green", text=i, borderwidth=0)
            green_name.grid(row=count, column=2, sticky="NSEW", columnspan=1, rowspan=1)
            count +=1

    def get_names(self):
        with open('redTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.r_name.append(i)
        with open('greenTeam.txt', 'r') as file:
            p = json.load(file)
            for i in p:
                self.g_name.append(i)


    def start_timer(self):
        sec = StringVar()
        self.timer = Label(self, textvariable=sec,
                      font='Times 50', fg='Purple')
        self.timer.place(relx=1.0, rely=1.0, anchor=SW)
        time_seconds = 360
        while time_seconds > -1:
            tmp = str(datetime.timedelta(seconds=time_seconds))
            sec.set(tmp[2:])
            self.timer.update()
            self.timer.after(1000)
            time_seconds -= 1





root = Container()
root.geometry("{}x{}".format(SCREEN_WIDTH, SCREEN_HEIGHT))

root.mainloop()
