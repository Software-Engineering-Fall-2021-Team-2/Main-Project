#
#           Name: player-action.py
#           Authors: Stephen Coyne & Gage Underwood
#

from tkinter import *
import json
import datetime

# Kills current screen


def killScreen(event):
    actionS.destroy()


actionS = Tk()
actionS.title(' Action Screen ')
actionS.attributes('-fullscreen', True)

# Intial Calculations for window\
x_mid = int(actionS.winfo_screenwidth() / 2)
y_mid = int(actionS.winfo_screenheight() / 2)
red_offset = x_mid - 300
green_offset = x_mid + 300

my_canvas = Canvas(actionS, bg="black", highlightthickness=0)
my_canvas.pack(fill="both", expand=True)

# Create Headers
my_canvas.create_text(x_mid, 50, text="Play Screen",
                      font=("Times New Roman", 50), fill="Purple")
my_canvas.create_text(red_offset-200, 150, text="Red Team",
                      font=("Times New Roman", 25), fill="Red")
my_canvas.create_text(x_mid+100, 150, text="Green Team",
                      font=("Times New Roman", 25), fill="Green")
my_canvas.create_text(x_mid, 90, text="Game Action",
                      font=("Times New Roman", 25), fill="Purple")
my_canvas.create_text(x_mid-100, 150, text="Scores",
                      font=("Times New Roman", 25), fill="Red")
my_canvas.create_text(green_offset+200, 150, text="Scores",
                      font=("Times New Roman", 25), fill="Green")

# Create Rectangles
offset = 170
my_canvas.create_rectangle(red_offset-300, 130, x_mid,
                           offset+450, outline='White')
my_canvas.create_rectangle(
    x_mid, 130, green_offset+300, offset+450, outline='White')
my_canvas.create_rectangle(red_offset-300, offset +
                           450, green_offset+300, y_mid+500, outline='White')

# Get CodeNames from file
redTeam = []
greenTeam = []
with open('redTeam.txt', 'r') as file:
    p = json.load(file)
    for i in p:
        redTeam.append(i)
with open('greenTeam.txt', 'r') as file:
    p = json.load(file)
    for i in p:
        greenTeam.append(i)

# Fills codenames on player table
offset = 20
for i in redTeam:
    my_canvas.create_text(red_offset-200, 165+offset,
                          text=i, font=('Times New Roman', 16), fill='Red')
    offset += 30

offset = 20
for i in greenTeam:
    my_canvas.create_text(x_mid+100, 165+offset, text=i,
                          font=('Times New Roman', 16), fill='Green')
    offset += 30

# Creates lines for score table
offset = 170
my_canvas.create_line(red_offset-300, offset,
                      green_offset+300, offset, fill='White')
my_canvas.create_line(red_offset-300, offset+30,
                      green_offset+300, offset+30, fill='White')
my_canvas.create_line(red_offset-300, offset+60,
                      green_offset+300, offset+60, fill='White')
my_canvas.create_line(red_offset-300, offset+90,
                      green_offset+300, offset+90, fill='White')
my_canvas.create_line(red_offset-300, offset+120,
                      green_offset+300, offset+120, fill='White')
my_canvas.create_line(red_offset-300, offset+150,
                      green_offset+300, offset+150, fill='White')
my_canvas.create_line(red_offset-300, offset+180,
                      green_offset+300, offset+180, fill='White')
my_canvas.create_line(red_offset-300, offset+180,
                      green_offset+300, offset+180, fill='White')
my_canvas.create_line(red_offset-300, offset+210,
                      green_offset+300, offset+210, fill='White')
my_canvas.create_line(red_offset-300, offset+240,
                      green_offset+300, offset+240, fill='White')
my_canvas.create_line(red_offset-300, offset+270,
                      green_offset+300, offset+270, fill='White')
my_canvas.create_line(red_offset-300, offset+300,
                      green_offset+300, offset+300, fill='White')
my_canvas.create_line(red_offset-300, offset+330,
                      green_offset+300, offset+330, fill='White')
my_canvas.create_line(red_offset-300, offset+360,
                      green_offset+300, offset+360, fill='White')
my_canvas.create_line(red_offset-300, offset+390,
                      green_offset+300, offset+390, fill='White')
my_canvas.create_line(red_offset-300, offset+420,
                      green_offset+300, offset+420, fill='White')
my_canvas.create_line(red_offset, offset, red_offset, offset+450, fill='White')
my_canvas.create_line(green_offset, offset, green_offset,
                      offset+450, fill='White')

# End the game/return to player entry screen
actionS.bind('<KeyPress-F1>', killScreen)

time_frame = Frame(my_canvas, bg='Black', height=800, width=150, bd=10)
time_frame.pack(side=RIGHT)

timer_label = Label(time_frame, text="Time Left",
                    font='Times 50', fg='white', bg='Black')
timer_label.pack(anchor=CENTER)

# HACK: timer handler
sec = StringVar()

timer = Label(time_frame, textvariable=sec,
              font='Times 50', fg='white', bg='Black')
timer.pack(anchor=CENTER)

time_seconds = 360
while time_seconds > -1:
    tmp = str(datetime.timedelta(seconds=time_seconds))
    
    sec.set(tmp[2:])
    actionS.update()
    timer.after(1000)
    time_seconds -= 1

# Executes Player Action Screen
actionS.mainloop()
