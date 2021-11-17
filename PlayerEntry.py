
from tkinter import *
from BaseFrame import MyBaseFrame
import dbconnect


class PlayerEntry(MyBaseFrame):

    # Lists to hold the information, replaces the need for file transfer
    red_ids, red_names, green_ids, green_names = ([] for i in range(4))

    def __init__(self, controller):
        MyBaseFrame.__init__(self, controller)
        self.controller = controller

        # Sets header & subheader
        header_text = "Press enter to get your code name if you have played before, otherwise, submit your team before playing"
        subheader_text = "Press F5 to start game once teams have been submitted"
        self.header_subheader_set(header_text, subheader_text)

        self.screen_setup_TESTING()

        # Sets the center cell, (1,1) to contain the table and it's title
        # self.set_center()

        entry_widget = EntryWidget(self, self.controller)
        

        # Binds the click of mouse button 1 to set the focus on the main frame
        # Used to handle exiting of the entry
        #self.bind_all("<Button-1>", lambda event: event.self.focus_set())
        # TODO: bind a damn whatever to click out of entry frame
        #self.bind_all("<Button-1>", lambda event: self.onClick())

        #self.header_subheader_frame.bind("<Button-1>", lambda event: self.onClick())
        #self.bind('<Return>', lambda event: self.pull_names(event))

        # TODO: Make this call start func in the main
        #self.bind('<a>', lambda event = NONE: controller.start_countdown(Countdown))
        # """lambda event = NONE:""" controller.start_countdown(Countdown))

    """def onClick(self, *event):
        print("fart4")
        self.controller.focus_set()"""


class EntryWidget(Frame):
    """Creates the action grid in the (1,1) cell that contains the table titles, as well as the player entry section"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent = parent
        self.controller = controller

        # Master frame in the cell, divided into 2 rows and 1 column
        # Row 0 contains the titles
        # Rows 1-16 contains the player entry section

        # Place in parent 
        self.config(borderwidth=1)
        self.grid(column=1, row=1, sticky="NSEW")


        # Internalgrid setup
        self.columnconfigure([0, 2], weight=1, minsize=1)
        self.columnconfigure([1, 3], weight=5, minsize=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(tuple(range(1, 16)), weight=1)

    # Title row setup
        red_ids_label = Label(self, bg="black",
                            fg="red", font=self.controller.SUBHEADER_FONT, text="IDS", justify="center").grid(row=0, column=0, sticky="NSEW")

        red_team_label = Label(self, bg="black",
                            fg="red", font=self.controller.SUBHEADER_FONT, text="RED TEAM", justify="center").grid(row=0, column=1, sticky="NSEW")

        green_ids_label = Label(self, bg="black",
                                fg="green", font=self.controller.SUBHEADER_FONT, text="IDS", justify="center").grid(row=0, column=2, sticky="NSEW")

        green_team_label = Label(self, bg="black", fg="green", font=self.controller.SUBHEADER_FONT,
                                text="GREEN TEAM", justify="center").grid(row=0, column=3, sticky="NSEW")

        # Initilazing every element in the table
        # TODO: Make it so that you can exit the entry boxes
        for i in range(1, 16):
            red_ids = Entry(self, bg="grey", fg="black",
                            width=3).grid(row=i, column=0, sticky="NSEW")
            self.red_ids.append(red_ids)

            red_name = Entry(self, bg="grey", fg="black").grid(
                row=i, column=1, sticky="NSEW")
            self.red_names.append(red_name)

            green_id = Entry(self, bg="grey", fg="black",
                            width=3).grid(row=i, column=2, sticky="NSEW")
            self.green_ids.append(green_id)

            green_name = Entry(self, bg="grey", fg="black").grid(
                row=i, column=3, sticky="NSEW")
            self.green_names.append(green_name)

    # pull names from db using ID entered

    def pull_names(self, event):
        print("called")
        for i in range(self.controller.NUM_PLAYERS):
            if len(self.red_ids[i].get()) != 0:
                # * Changed from convertToInt to int() wrapper, test if this works
                red_id = int(self.red_ids[i].get())
                if(dbconnect.checkdb(red_id)):
                    self.set_name(
                        self.red_names[i], dbconnect.retrieveCode(red_id))
        for i in range(self.controller.NUM_PLAYERS):
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
