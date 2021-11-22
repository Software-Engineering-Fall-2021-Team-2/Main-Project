
from tkinter import *
from BaseFrame import MyBaseFrame
import dbconnect


class PlayerEntry(MyBaseFrame):

    # Lists to hold the information, replaces the need for file transfer
    # TODO: move the lists to main3.py
    red_ids, red_names, green_ids, green_names = ([] for i in range(4))
    header_text = "Press enter to get your code name if you have played before, otherwise, submit your team before playing"
    subheader_text = "Press F5 to start game once teams have been submitted"

    def __init__(self, parent, controller, *args, **kwargs):
        MyBaseFrame.__init__(self, parent, controller,
                             self.header_text, self.subheader_text, *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller

        # Configuration
        # - binds the escape key to remove focus from the entry boxes
        self.bind_all("<Escape>", lambda event: self.esc_hit())

        # Layout
        entry_widget = EntryWidget(self, self.controller)

    def esc_hit(self, *event):
        """An on click event that sets the focus to the controller - used for exiting the entry boxes"""
        self.controller.focus_set()


class EntryWidget(Frame):
    """Creates the action grid in the (1,1) cell that contains the table titles, as well as the player entry section"""

    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent,  *args, **kwargs)
        # Object Attributes
        self.parent = parent
        self.controller = controller

        # Configuration
        # - places the frame into the parent
        self.config(borderwidth=1)
        self.grid(column=1, row=1, sticky="NSEW")

        # - sets up the internal grid of the frame
        # - row 0 contains the titles
        # - rows 1-16 contian the player entry section
        self.columnconfigure([0, 2], weight=1, minsize=1)
        self.columnconfigure([1, 3], weight=5, minsize=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(tuple(range(1, 16)), weight=1)

        # Populate
        # - title row setup
        red_ids_label = Label(self, bg="black",
                              fg="red", font=self.controller.SUBHEADER_FONT, text="IDS", justify="center").grid(row=0, column=0, sticky="NSEW")

        red_team_label = Label(self, bg="black",
                               fg="red", font=self.controller.SUBHEADER_FONT, text="RED TEAM", justify="center").grid(row=0, column=1, sticky="NSEW")

        green_ids_label = Label(self, bg="black",
                                fg="green", font=self.controller.SUBHEADER_FONT, text="IDS", justify="center").grid(row=0, column=2, sticky="NSEW")

        green_team_label = Label(self, bg="black", fg="green", font=self.controller.SUBHEADER_FONT,
                                 text="GREEN TEAM", justify="center").grid(row=0, column=3, sticky="NSEW")

        # - entry boxes setup
        # - utilizes 4 loops so that you can use tab to move bewteen cells
        # TODO: Make it so that you can exit the entry boxes
        for i in range(1, 16):
            red_ids = Entry(self, bg="grey", fg="black",
                            width=3).grid(row=i, column=0, sticky="NSEW")
            self.parent.red_ids.append(red_ids)

        for i in range(1, 16):
            red_name = Entry(self, bg="grey", fg="black").grid(
                row=i, column=1, sticky="NSEW")
            self.parent.red_names.append(red_name)

        for i in range(1, 16):
            green_id = Entry(self, bg="grey", fg="black",
                             width=3).grid(row=i, column=2, sticky="NSEW")
            self.parent.green_ids.append(green_id)

        for i in range(1, 16):
            green_name = Entry(self, bg="grey", fg="black").grid(
                row=i, column=3, sticky="NSEW")
            self.parent.green_names.append(green_name)

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
