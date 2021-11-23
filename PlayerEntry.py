
from BaseFrame import *
import dbconnect


class PlayerEntry(MyBaseFrame):

    # Lists to hold the information, replaces the need for file transfer
    # TODO: move the lists to main3.py or Container or a different class ?
    red_ids, red_names, green_ids, green_names = ([] for i in range(4))

    header_text = "Press enter to get your code name if you have played before, otherwise, submit your team before playing"
    subheader_text = "Press F5 to start game once teams have been submitted"

    def __init__(self, master: Tk):
        """[summary]

        Args:
            master (Tk): Widget that is directly resposible for owning this widget (Container)
        """
        # Set Object Attributes
        super().__init__(master, self.header_text, self.subheader_text)

        # Configure

        # Layout

        # Populate
        entry_widget = EntryWidget(self)

class EntryWidget(Frame):

    def __init__(self, master: MyBaseFrame):
        """Creates the action grid in the (1,1) cell that contains the table titles, as well as the player entry section

        Args:
            master (MyBaseFrame): [description]
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(borderwidth=1, bg='black')
        self.grid(column=1, row=1, sticky='NSEW')

        self.columnconfigure([0, 3], weight=1, minsize=1)   # ID Cols
        self.columnconfigure(2, weight=2, minsize=1)        # Filler Col
        self.columnconfigure([1, 4], weight=5, minsize=1)   # Team Cols
        self.rowconfigure(0, weight=2)                      # Title Row
        self.rowconfigure(tuple(range(1, 16)), weight=1)    # Entry Rows

        # Populate
        self.create_headers()

        # for i in range(1, 16):
        #red_ids = Entry(self, bg="grey", fg="black",width=3)
        #red_ids = EntryBox(self, ).grid(row=i, column=0, sticky="NSEW")
        # self.master.red_ids.append(red_ids)

        """for i in range(1, 16):
            red_name = Entry(self, bg="grey", fg="black").grid(
                row=i, column=1, sticky="NSEW")
            self.master.red_names.append(red_name)

        for i in range(1, 16):
            green_id = Entry(self, bg="grey", fg="black",
                             width=3).grid(row=i, column=3, sticky="NSEW")
            self.master.green_ids.append(green_id)

        for i in range(1, 16):
            green_name = Entry(self, bg="grey", fg="black").grid(
                row=i, column=4, sticky="NSEW")
            self.master.green_names.append(green_name)"""

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

    def create_headers(self):
        red_ids_label = TableHeaderLabel(self, 'IDS', 'red').grid(
            row=0, column=0, sticky="NSEW")
        red_team_label = TableHeaderLabel(self, 'RED TEAM', 'red').grid(
            row=0, column=1, sticky="NSEW")
        green_ids_label = TableHeaderLabel(self, 'IDS', 'green').grid(
            row=0, column=3, sticky="NSEW")
        green_team_label = TableHeaderLabel(self, 'GREEN TEAM', 'green').grid(
            row=0, column=4, sticky="NSEW")

    # WHAT: What does this do? - Alters the database somehow
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


class TableHeaderLabel(Label):

    def __init__(self, master: Frame, text: str, color: str):
        """Table header label class.

        Args:
            master (Frame): Frame widget thats directly owns this.
            text (str): Text to be dispalyed.
            color(str): Team color to be used as text color
        """
        # Set Object Attributes
        super().__init__(master)
        self.text = text
        self.color = color

        # Configure
        self.config(text=self.text, fg=self.color,
                    font=SUBHEADER_FONT, bg='black', justify='center')


class EntryBox(Entry):

    def __init__(self, master: Frame):
        """Entry box class

        Args:
            master (Frame): Frame widget thats directly owns this.
        """
        # Set Object Attributes
        super().__init__(master)

        # Configure
        self.config(bg='grey', fg='black')
