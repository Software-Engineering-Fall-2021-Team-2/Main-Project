
from tkinter import *
from BaseFrame import MyBaseFrame


class PlayerEntry(MyBaseFrame):
    
    # Lists to hold the information, replaces the need for file transfer
    red_ids, red_names, green_ids, green_names = ([] for i in range(4))


    def __init__(self, controller):
        MyBaseFrame.__init__(self, controller)

        header_text = "Press enter to get your code name if you have played before, otherwise, submit your team before playing"
        subheader_text = "Press F5 to start game once teams have been submitted"

        self.header_subheader_set(header_text, subheader_text)

        # Canvas for handling the grid
        grid_frame = Frame(self, bd=1)
        grid_frame.grid(column=1, row=1, ipady=10, ipadx=10, sticky="NSEW")

        # grid setup
        grid_frame.columnconfigure([0, 2], weight=1, minsize=1)
        grid_frame.columnconfigure([1, 3], weight=4, minsize=1)
        grid_frame.rowconfigure(tuple(range(15)), weight=1)

        # Table header setup
        red_team_ids = Label(grid_frame, bg="black",
                            fg="red", font=self.controller.SUBHEADER_FONT, text="IDS")
        red_team_ids.grid(row=0, column=0, sticky="NSEW")

        red_team_label = Label(grid_frame, bg="black",
                            fg="red", font=self.controller.SUBHEADER_FONT, text="RED TEAM")
        red_team_label.grid(row=0, column=1, sticky="NSEW")

        green_team_ids = Label(grid_frame, bg="black",
                            fg="green", font=self.controller.SUBHEADER_FONT, text="IDS")
        green_team_ids.grid(row=0, column=2, sticky="NSEW")

        green_team_label = Label(
            grid_frame, bg="black", fg="green", font=self.controller.SUBHEADER_FONT, text="GREEN TEAM")
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
        # TODO: Make this call start func in the main
        #controller.bind('<a>', lambda event = NONE: controller.start_countdown(Countdown))
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