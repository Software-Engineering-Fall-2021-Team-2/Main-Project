#
#           Name: player-entry.py
#           Author: Stephen Coyne & Gage Underwood
#
# A todo list
# TODO (FRAME): Convert to frame based architecture
# TODO (RESTRUCT): Restructure for easier reading
# TODO (TABLE): Convert to tkinter tables
# TODO (SNAKE): Standardise snake case

from tkinter import *
import dbconnect
import json
import time

NUM_PLAYERS = 15
SCREEN_HEIGHT = 586
SCREEN_WIDTH = 919

"""FUNCTIONS START"""
# TODO: Move too a different file
def hide_all_frames():
    frame_splash_screen.pack_forget()
    frame_player_entry.pack_forget()
    frame_player_action.pack_forget()

def to_player_entry():
    hide_all_frames()
    frame_player_entry.pack(fill="both", expand=True)



"""FUNCTIONS FINISH"""

root = Tk()
root.title(' Entry Terminal')

# TODO: Land on window size
# DEL: Depreciated
#root.attributes('-fullscreen', False)
# TODO: Figure out how to resize image properly
root.geometry("{}x{}".format(SCREEN_WIDTH, SCREEN_HEIGHT))
#root.minsize(800, 600)
#root.maxsize(1600, 1200)
#root.resizable(TRUE, TRUE)

# Initial Calculations
# DEL: DEPRECIATED
x_mid = int(root.winfo_screenwidth() / 2)
y_mid = int(root.winfo_screenheight() / 2)
red_offset = x_mid - 300
green_offset = x_mid + 300

# TODO (FRAME)
# Creates Canvas
# DEL: DEPRECIATED
#canvas_splash_screen = Canvas(root, bg="black", highlightthickness=0)
#canvas_splash_screen.pack(fill="both", expand=True)
"""ALL FRAMES"""
frame_splash_screen = Frame(root, bg="black")
#frame_splash_screen = Frame(root)
frame_splash_screen.pack(fill="both", expand=True)

# Define image
image_splash_screen = PhotoImage(file="logo.png")

# Define label to contain image
label_splash_screen = Label(
    frame_splash_screen, image=image_splash_screen)

label_splash_screen.place(relx=.5, rely=.5, anchor=CENTER)

frame_player_entry = Frame(root, bg="black")
top_label = Label(frame_player_entry, text="Press enter to get your code name if you have played before, otherwise, submit your team before playing", 
        font=("Times New Roman", 15), fg="White", background="Black")
top_label.pack()


frame_player_action = Frame(root, bg="black")

"""SPLASH SCREEN START"""
# End splash screen after 1 secnods
frame_splash_screen.after(1000, to_player_entry())
"""SPLASH SCREEN FINISH"""

"""PLAYER ENTRY START"""
#frame_player_entry = Frame(root, bg="black")



root.mainloop()


"""
my_canvas.create_text(x_mid, 50, text="Edit Current Game",
                      font=("Times New Roman", 50), fill="Blue")
my_canvas.create_text(red_offset, 200, text="Red Team",
                      font=("Times New Roman", 25), fill="Red")
my_canvas.create_text(green_offset, 200, text="Green Team",
                      font=("Times New Roman", 25), fill="Green")
my_canvas.create_text(x_mid, 125, text="Press enter to get your code name if you have played before, otherwise, Submit your team before playing", font=(
    "Times New Roman", 15), fill="White")
my_canvas.create_text(
    x_mid, 145, text="Press F5 to start game once teams have been submitted", font='Times 15', fill='White')


# Red Names
red_names = []
for i in range(NUM_PLAYERS):
    red_names.append(Entry(my_canvas, width=30))


# Red Id
red_ids = []
for i in range(NUM_PLAYERS):
    red_ids.append(Entry(my_canvas, width=3))

# TODO (TABLE)
# placement
input_window = my_canvas.create_window(red_offset, 250, window=red_names[0])
input_window = my_canvas.create_window(red_offset, 285, window=red_names[1])
input_window = my_canvas.create_window(red_offset, 320, window=red_names[2])
input_window = my_canvas.create_window(red_offset, 355, window=red_names[3])
input_window = my_canvas.create_window(red_offset, 390, window=red_names[4])
input_window = my_canvas.create_window(red_offset, 425, window=red_names[5])
input_window = my_canvas.create_window(red_offset, 460, window=red_names[6])
input_window = my_canvas.create_window(red_offset, 495, window=red_names[7])
input_window = my_canvas.create_window(red_offset, 530, window=red_names[8])
input_window = my_canvas.create_window(red_offset, 565, window=red_names[9])
input_window = my_canvas.create_window(red_offset, 600, window=red_names[10])
input_window = my_canvas.create_window(red_offset, 635, window=red_names[11])
input_window = my_canvas.create_window(red_offset, 670, window=red_names[12])
input_window = my_canvas.create_window(red_offset, 705, window=red_names[13])
input_window = my_canvas.create_window(red_offset, 740, window=red_names[14])

# id placement
input_window = my_canvas.create_window(red_offset-150, 250, window=red_ids[0])
input_window = my_canvas.create_window(
    red_offset - 150, 285, window=red_ids[1])
input_window = my_canvas.create_window(
    red_offset - 150, 320, window=red_ids[2])
input_window = my_canvas.create_window(
    red_offset - 150, 355, window=red_ids[3])
input_window = my_canvas.create_window(
    red_offset - 150, 390, window=red_ids[4])
input_window = my_canvas.create_window(
    red_offset - 150, 425, window=red_ids[5])
input_window = my_canvas.create_window(
    red_offset - 150, 460, window=red_ids[6])
input_window = my_canvas.create_window(
    red_offset - 150, 495, window=red_ids[7])
input_window = my_canvas.create_window(
    red_offset - 150, 530, window=red_ids[8])
input_window = my_canvas.create_window(
    red_offset - 150, 565, window=red_ids[9])
input_window = my_canvas.create_window(
    red_offset - 150, 600, window=red_ids[10])
input_window = my_canvas.create_window(
    red_offset - 150, 635, window=red_ids[11])
input_window = my_canvas.create_window(
    red_offset - 150, 670, window=red_ids[12])
input_window = my_canvas.create_window(
    red_offset - 150, 705, window=red_ids[13])
input_window = my_canvas.create_window(
    red_offset - 150, 740, window=red_ids[14])


# green team names
green_names = []
for i in range(NUM_PLAYERS):
    green_names.append(Entry(my_canvas, width=30))


# green team id
green_ids = []
for i in range(NUM_PLAYERS):
    green_ids.append(Entry(my_canvas, width=3))

# placement
input_window = my_canvas.create_window(
    green_offset, 250, window=green_names[0])
input_window = my_canvas.create_window(
    green_offset, 285, window=green_names[1])
input_window = my_canvas.create_window(
    green_offset, 320, window=green_names[2])
input_window = my_canvas.create_window(
    green_offset, 355, window=green_names[3])
input_window = my_canvas.create_window(
    green_offset, 390, window=green_names[4])
input_window = my_canvas.create_window(
    green_offset, 425, window=green_names[5])
input_window = my_canvas.create_window(
    green_offset, 460, window=green_names[6])
input_window = my_canvas.create_window(
    green_offset, 495, window=green_names[7])
input_window = my_canvas.create_window(
    green_offset, 530, window=green_names[8])
input_window = my_canvas.create_window(
    green_offset, 565, window=green_names[9])
input_window = my_canvas.create_window(
    green_offset, 600, window=green_names[10])
input_window = my_canvas.create_window(
    green_offset, 635, window=green_names[11])
input_window = my_canvas.create_window(
    green_offset, 670, window=green_names[12])
input_window = my_canvas.create_window(
    green_offset, 705, window=green_names[13])
input_window = my_canvas.create_window(
    green_offset, 740, window=green_names[14])

# placement id
input_window = my_canvas.create_window(
    green_offset - 150, 250, window=green_ids[0])
input_window = my_canvas.create_window(
    green_offset - 150, 285, window=green_ids[1])
input_window = my_canvas.create_window(
    green_offset - 150, 320, window=green_ids[2])
input_window = my_canvas.create_window(
    green_offset - 150, 355, window=green_ids[3])
input_window = my_canvas.create_window(
    green_offset - 150, 390, window=green_ids[4])
input_window = my_canvas.create_window(
    green_offset - 150, 425, window=green_ids[5])
input_window = my_canvas.create_window(
    green_offset - 150, 460, window=green_ids[6])
input_window = my_canvas.create_window(
    green_offset - 150, 495, window=green_ids[7])
input_window = my_canvas.create_window(
    green_offset - 150, 530, window=green_ids[8])
input_window = my_canvas.create_window(
    green_offset - 150, 565, window=green_ids[9])
input_window = my_canvas.create_window(
    green_offset - 150, 600, window=green_ids[10])
input_window = my_canvas.create_window(
    green_offset - 150, 635, window=green_ids[11])
input_window = my_canvas.create_window(
    green_offset - 150, 670, window=green_ids[12])
input_window = my_canvas.create_window(
    green_offset - 150, 705, window=green_ids[13])
input_window = my_canvas.create_window(
    green_offset - 150, 740, window=green_ids[14])

# buttons
submit_teams_button = Button(root, text='Submit Teams', font=("Times New Roman",
                                                              12), width=10, height=2, bd='3', command=send_data)
submit_teams_button.configure(width=10)
btn_window = my_canvas.create_window(
    green_offset, 1000, window=submit_teams_button)

clear_button = Button(root, text='Clear', font=("Times New Roman", 12),
                      width=10, height=2, bd='3', command=clear_data)
clear_button.configure(width=10)
btn_window = my_canvas.create_window(red_offset, 1000, window=clear_button)

# Pull names when enter is pressed
root.bind('<Return>', pull_names)

# Action screen keypress
root.bind('<KeyPress-F5>', countdown)
root.bind('<KeyPress-F1>', kill_screen)



# DEL
# WHAT: why is this used rather that the int() wrapper?


def string_to_int(string):
    num = 0
    try:
        num = int(string)
    except:
        pass
    return num

# WHAT: What does this do?


def set_name(self, text):
    self.delete('0', 'end')
    self.insert('0', text)


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


def pull_names(event):
    for i in range(NUM_PLAYERS):
        if len(red_ids[i].get()) != 0:
            # * Changed from convertToInt to int() wrapper, test if this works
            red_id = int(red_ids[i].get())
            if(dbconnect.checkdb(red_id)):
                set_name(red_names[i], dbconnect.retrieveCode(red_id))
    for i in range(NUM_PLAYERS):
        if len(green_ids[i].get()) != 0:
            # TODO : will change from convetToInt to int() wrapper, currently testing
            green_id = string_to_int(green_ids[i].get())
            if(dbconnect.checkdb(green_id)):
                set_name(green_names[i], dbconnect.retrieveCode(green_id))


def clear_data():
    for i in range(NUM_PLAYERS):
        red_names[i].delete(0, 'end')
        red_ids[i].delete(0, 'end')
        green_names[i].delete(0, 'end')
        green_ids[i].delete(0, 'end')


def write_info():
    red_team = []
    greenTeam = []
    for i in range(NUM_PLAYERS):
        if len(red_ids[i].get()) != 0:
            name = red_names[i].get()
            red_team.append(name)
        if len(green_ids[i].get()) != 0:
            name = green_names[i].get()
            greenTeam.append(name)
    with open('redTeam.txt', 'w') as file:
        file.write(json.dumps(red_team))
    with open('greenTeam.txt', 'w') as file:
        file.write(json.dumps(greenTeam))


# WHAT: Why do we writeInfo() in this function?
# Important Functions for Switching to player action


def kill_screen():
    write_info()
    root.destroy()


def countdown(event):
    my_canvas.delete('all')

    sec = StringVar()

    def countdown_timer():
        seconds = 30
        while seconds > -1:
            sec.set(seconds)
            root.update()
            time.sleep(1)
            seconds -= 1

    timer = Label(my_canvas, textvariable=sec,
                  font='Times 300', fg='Purple', bg='Black')
    timer.place(relx=0.5, rely=0.5, anchor=CENTER)
    countdown_timer()
    kill_screen()
    """
