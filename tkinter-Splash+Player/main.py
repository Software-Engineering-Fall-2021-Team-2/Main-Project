# Import module
from tkinter import *


splash_root = Tk()
splash_root.title("Splash Screen")
splash_root.geometry("919x586")

# centering
x_left = int(splash_root.winfo_screenwidth() / 2 - 919 / 2)
y_top = int(splash_root.winfo_screenheight() / 2 - 586 / 2)
splash_root.geometry("+{}+{}".format(x_left, y_top))

# define img
img = PhotoImage(file="logo.png")

# hide title bar
splash_root.overrideredirect(True)

splash_label = Label(splash_root, image=img)
splash_label.place(x=0, y=0, relwidth=1, relheight=1)


def player_entry():
    splash_root.destroy()
    global bk_grd
    root = Tk()
    root.title(' Entry Terminal')
    swidth = root.winfo_screenwidth()
    sheight = root.winfo_screenheight()
    x_mid = int(root.winfo_screenwidth() / 2)
    y_mid = int(root.winfo_screenheight() / 2)
    red_offset = x_mid - 300
    green_offset = x_mid + 300
    root.geometry("%dx%d" % (swidth, sheight))
    #root.geometry("800x800")
    bk_grd = PhotoImage(file="bk_grd.png")

    my_canvas = Canvas(root, width=swidth, height=swidth, background="black")
    my_canvas.pack(fill="both", expand=True)
    #my_canvas.create_image(0,0, image=bk_grd, anchor="nw")

    my_canvas.create_text(x_mid, 50, text="Edit Current Game", font=("Times New Roman",50), fill="Blue")
    my_canvas.create_text(red_offset, 200, text="Red Team", font=("Times New Roman", 25), fill="Red" )
    my_canvas.create_text(green_offset, 200, text="Green Team", font=("Times New Roman", 25), fill="Green")

    #red team
    r1 = Entry(my_canvas, width=30)
    r2 = Entry(my_canvas, width=30)
    r3 = Entry(my_canvas, width=30)
    r4 = Entry(my_canvas, width=30)
    r5 = Entry(my_canvas, width=30)
    r6 = Entry(my_canvas, width=30)
    #placement
    input_window = my_canvas.create_window(red_offset, 250, window=r1)
    input_window = my_canvas.create_window(red_offset, 285, window=r2)
    input_window = my_canvas.create_window(red_offset, 320, window=r3)
    input_window = my_canvas.create_window(red_offset, 355, window=r4)
    input_window = my_canvas.create_window(red_offset, 390, window=r5)
    input_window = my_canvas.create_window(red_offset, 425, window=r6)


    #green team
    g1 = Entry(my_canvas, width=30)
    g2 = Entry(my_canvas, width=30)
    g3 = Entry(my_canvas, width=30)
    g4 = Entry(my_canvas, width=30)
    g5 = Entry(my_canvas, width=30)
    g6 = Entry(my_canvas, width=30)

    #placement
    input_window = my_canvas.create_window(green_offset, 250, window=g1)
    input_window = my_canvas.create_window(green_offset, 285, window=g2)
    input_window = my_canvas.create_window(green_offset, 320, window=g3)
    input_window = my_canvas.create_window(green_offset, 355, window=g4)
    input_window = my_canvas.create_window(green_offset, 390, window=g5)
    input_window = my_canvas.create_window(green_offset, 425, window=g6)

    #buttons
    btn = Button(root, text='Submit Teams', font=("Times New Roman", 12), width=10, height=2, bd='3')
    btn.configure(width=10)
    btn_window = my_canvas.create_window(x_mid, sheight-150, window=btn)

    s_btn = Button(root, text='Start', font=("Times New Roman", 12), width=10, height=2, bd='3')
    s_btn.configure(width=10)
    btn_window = my_canvas.create_window(green_offset, sheight - 150, window=s_btn)

    c_btn = Button(root, text='Clear', font=("Times New Roman", 12), width=10, height=2, bd='3')
    s_btn.configure(width=10)
    btn_window = my_canvas.create_window(red_offset, sheight - 150, window=c_btn)



splash_root.after(3000, player_entry)
# Execute tkinter
mainloop()
