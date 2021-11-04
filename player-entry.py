#
#           Name: player-entry.py
#           Author: Stephen Coyne & Gage Underwood
#

from tkinter import *
import dbconnect
import json
import time

def convertToInt(string):
    num = 0
    try:
        num = int(string)
    except:
        pass
    return num

def setName(self, text):
    self.delete('0', 'end')
    self.insert('0', text)

def Send_data():
    for i in range(15):
        if len(r_id[i].get()) != 0:
            id = convertToInt(r_id[i].get())
            name = red[i].get()
            if not(dbconnect.checkdb(id)):
                record = (id,name)
                dbconnect.addRecord(record)
    for i in range(15):
        if len(g_id[i].get()) != 0:
            id = convertToInt(g_id[i].get())
            name = g[i].get()
            if not(dbconnect.checkdb(id)):
                record = (id,name)
                dbconnect.addRecord(record)

def pullNames(event):
    for i in range(15):
        if len(r_id[i].get()) != 0:
            red_id = convertToInt(r_id[i].get())
            if(dbconnect.checkdb(red_id)):
                setName(red[i], dbconnect.retrieveCode(red_id))
    for i in range(15):
        if len(g_id[i].get()) != 0:
            green_id = convertToInt(g_id[i].get())
            if(dbconnect.checkdb(green_id)):
                setName(g[i], dbconnect.retrieveCode(green_id))

def clearData():
    for i in range(15):
        red[i].delete(0, 'end')
        r_id[i].delete(0, 'end')
        g[i].delete(0, 'end')
        g_id[i].delete(0, 'end')

def writeInfo():
    redTeam = []
    greenTeam = []
    for i in range(15):
        if len(r_id[i].get()) != 0:
            name = red[i].get()
            redTeam.append(name)
        if len(g_id[i].get()) != 0:
            name = g[i].get()
            greenTeam.append(name)
    with open('redTeam.txt', 'w') as file:
        file.write(json.dumps(redTeam))
    with open('greenTeam.txt', 'w') as file:
        file.write(json.dumps(greenTeam))

root = Tk()
root.title(' Entry Terminal')

#Initial Calculations
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()
x_mid = int(root.winfo_screenwidth() / 2)
y_mid = int(root.winfo_screenheight() / 2)
red_offset = x_mid - 300
green_offset = x_mid + 300
root.geometry("%dx%d" % (swidth, sheight))

#Creates Canvas
my_canvas = Canvas(root, width=swidth, height=swidth, background="black")
my_canvas.pack(fill="both", expand=True)

#Important Functions for Switching to player action
def killScreen():
    writeInfo()
    root.destroy()

def countdown(event):
    my_canvas.delete('all')

    sec = StringVar()
    def countdownTimer():
        seconds = 30
        while seconds > -1:
            sec.set(seconds)
            root.update()
            time.sleep(1)
            seconds -= 1

    timer = Label(my_canvas, textvariable=sec, font='Times 300', fg='Purple', bg='Black')
    timer.place(relx=0.5, rely=0.5, anchor=CENTER)
    countdownTimer()
    killScreen()

my_canvas.create_text(x_mid, 50, text="Edit Current Game", font=("Times New Roman",50), fill="Blue")
my_canvas.create_text(red_offset, 200, text="Red Team", font=("Times New Roman", 25), fill="Red" )
my_canvas.create_text(green_offset, 200, text="Green Team", font=("Times New Roman", 25), fill="Green")
my_canvas.create_text(x_mid, 125, text="Press enter to get your code name if you have played before, otherwise, Submit your team before playing", font=("Times New Roman", 15), fill="White")
my_canvas.create_text(x_mid, sheight - 300, text="Press F5 to start game!", font=("Times New Roman", 30), fill="White")

#Red Names
red = []
for i in range(15):
    red.append(Entry(my_canvas, width=30))

#Red Id
r_id = []
for i in range(15):
    r_id.append(Entry(my_canvas, width=3))

#placement
input_window = my_canvas.create_window(red_offset, 250, window=red[0])
input_window = my_canvas.create_window(red_offset, 285, window=red[1])
input_window = my_canvas.create_window(red_offset, 320, window=red[2])
input_window = my_canvas.create_window(red_offset, 355, window=red[3])
input_window = my_canvas.create_window(red_offset, 390, window=red[4])
input_window = my_canvas.create_window(red_offset, 425, window=red[5])
input_window = my_canvas.create_window(red_offset, 460, window=red[6])
input_window = my_canvas.create_window(red_offset, 495, window=red[7])
input_window = my_canvas.create_window(red_offset, 530, window=red[8])
input_window = my_canvas.create_window(red_offset, 565, window=red[9])
input_window = my_canvas.create_window(red_offset, 600, window=red[10])
input_window = my_canvas.create_window(red_offset, 635, window=red[11])
input_window = my_canvas.create_window(red_offset, 670, window=red[12])
input_window = my_canvas.create_window(red_offset, 705, window=red[13])
input_window = my_canvas.create_window(red_offset, 740, window=red[14])

#id placement
input_window = my_canvas.create_window(red_offset-150, 250, window=r_id[0])
input_window = my_canvas.create_window(red_offset - 150, 285, window=r_id[1])
input_window = my_canvas.create_window(red_offset - 150, 320, window=r_id[2])
input_window = my_canvas.create_window(red_offset - 150, 355, window=r_id[3])
input_window = my_canvas.create_window(red_offset - 150, 390, window=r_id[4])
input_window = my_canvas.create_window(red_offset - 150, 425, window=r_id[5])
input_window = my_canvas.create_window(red_offset - 150, 460, window=r_id[6])
input_window = my_canvas.create_window(red_offset - 150, 495, window=r_id[7])
input_window = my_canvas.create_window(red_offset - 150, 530, window=r_id[8])
input_window = my_canvas.create_window(red_offset - 150, 565, window=r_id[9])
input_window = my_canvas.create_window(red_offset - 150, 600, window=r_id[10])
input_window = my_canvas.create_window(red_offset - 150, 635, window=r_id[11])
input_window = my_canvas.create_window(red_offset - 150, 670, window=r_id[12])
input_window = my_canvas.create_window(red_offset - 150, 705, window=r_id[13])
input_window = my_canvas.create_window(red_offset - 150, 740, window=r_id[14])


#green team names
g = []
for i in range(15):
    g.append(Entry(my_canvas, width=30))

# green team id
g_id = []
for i in range(15):
    g_id.append(Entry(my_canvas, width=3))

#placement
input_window = my_canvas.create_window(green_offset, 250, window=g[0])
input_window = my_canvas.create_window(green_offset, 285, window=g[1])
input_window = my_canvas.create_window(green_offset, 320, window=g[2])
input_window = my_canvas.create_window(green_offset, 355, window=g[3])
input_window = my_canvas.create_window(green_offset, 390, window=g[4])
input_window = my_canvas.create_window(green_offset, 425, window=g[5])
input_window = my_canvas.create_window(green_offset, 460, window=g[6])
input_window = my_canvas.create_window(green_offset, 495, window=g[7])
input_window = my_canvas.create_window(green_offset, 530, window=g[8])
input_window = my_canvas.create_window(green_offset, 565, window=g[9])
input_window = my_canvas.create_window(green_offset, 600, window=g[10])
input_window = my_canvas.create_window(green_offset, 635, window=g[11])
input_window = my_canvas.create_window(green_offset, 670, window=g[12])
input_window = my_canvas.create_window(green_offset, 705, window=g[13])
input_window = my_canvas.create_window(green_offset, 740, window=g[14])

#placement id
input_window = my_canvas.create_window(green_offset - 150, 250, window=g_id[0])
input_window = my_canvas.create_window(green_offset - 150, 285, window=g_id[1])
input_window = my_canvas.create_window(green_offset - 150, 320, window=g_id[2])
input_window = my_canvas.create_window(green_offset - 150, 355, window=g_id[3])
input_window = my_canvas.create_window(green_offset - 150, 390, window=g_id[4])
input_window = my_canvas.create_window(green_offset - 150, 425, window=g_id[5])
input_window = my_canvas.create_window(green_offset - 150, 460, window=g_id[6])
input_window = my_canvas.create_window(green_offset - 150, 495, window=g_id[7])
input_window = my_canvas.create_window(green_offset - 150, 530, window=g_id[8])
input_window = my_canvas.create_window(green_offset - 150, 565, window=g_id[9])
input_window = my_canvas.create_window(green_offset - 150, 600, window=g_id[10])
input_window = my_canvas.create_window(green_offset - 150, 635, window=g_id[11])
input_window = my_canvas.create_window(green_offset - 150, 670, window=g_id[12])
input_window = my_canvas.create_window(green_offset - 150, 705, window=g_id[13])
input_window = my_canvas.create_window(green_offset - 150, 740, window=g_id[14])

#buttons
btn = Button(root, text='Submit Teams', font=("Times New Roman", 12), width=10, height=2, bd='3', command=Send_data)
btn.configure(width=10)
btn_window = my_canvas.create_window(green_offset, sheight-150, window=btn)

c_btn = Button(root, text='Clear', font=("Times New Roman", 12), width=10, height=2, bd='3', command=clearData)
c_btn.configure(width=10)
btn_window = my_canvas.create_window(red_offset, sheight - 150, window=c_btn)

#Pull names when enter is pressed
root.bind('<Return>', pullNames)
#Action screen keypress
root.bind('<KeyPress-F5>', countdown)

root.mainloop()
