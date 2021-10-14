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

    root = Tk()
    root.title(' Entry Terminal')
    swidth = root.winfo_screenwidth()
    sheight = root.winfo_screenheight()
    x_mid = int(root.winfo_screenwidth() / 2)
    y_mid = int(root.winfo_screenheight() / 2)
    red_offset = x_mid - 300
    green_offset = x_mid + 300
    root.geometry("%dx%d" % (swidth, sheight))



    my_canvas = Canvas(root, width=swidth, height=swidth, background="black")
    my_canvas.pack(fill="both", expand=True)


    my_canvas.create_text(x_mid, 50, text="Edit Current Game", font=("Times New Roman",50), fill="Blue")
    my_canvas.create_text(red_offset, 200, text="Red Team", font=("Times New Roman", 25), fill="Red" )
    my_canvas.create_text(green_offset, 200, text="Green Team", font=("Times New Roman", 25), fill="Green")

    #red team names
    r1 = Entry(my_canvas, width=30)
    r2 = Entry(my_canvas, width=30)
    r3 = Entry(my_canvas, width=30)
    r4 = Entry(my_canvas, width=30)
    r5 = Entry(my_canvas, width=30)
    r6 = Entry(my_canvas, width=30)
    r7 = Entry(my_canvas, width=30)
    r8 = Entry(my_canvas, width=30)
    r9 = Entry(my_canvas, width=30)
    r10 = Entry(my_canvas, width=30)
    r11 = Entry(my_canvas, width=30)
    r12 = Entry(my_canvas, width=30)
    r13 = Entry(my_canvas, width=30)
    r14 = Entry(my_canvas, width=30)
    r15 = Entry(my_canvas, width=30)


    #red team id
    r1_id = Entry(my_canvas, width=3)
    r2_id = Entry(my_canvas, width=3)
    r3_id = Entry(my_canvas, width=3)
    r4_id = Entry(my_canvas, width=3)
    r5_id = Entry(my_canvas, width=3)
    r6_id = Entry(my_canvas, width=3)
    r7_id = Entry(my_canvas, width=3)
    r8_id = Entry(my_canvas, width=3)
    r9_id = Entry(my_canvas, width=3)
    r10_id = Entry(my_canvas, width=3)
    r11_id = Entry(my_canvas, width=3)
    r12_id = Entry(my_canvas, width=3)
    r13_id = Entry(my_canvas, width=3)
    r14_id = Entry(my_canvas, width=3)
    r15_id = Entry(my_canvas, width=3)

    #placement
    input_window = my_canvas.create_window(red_offset, 250, window=r1)
    input_window = my_canvas.create_window(red_offset, 285, window=r2)
    input_window = my_canvas.create_window(red_offset, 320, window=r3)
    input_window = my_canvas.create_window(red_offset, 355, window=r4)
    input_window = my_canvas.create_window(red_offset, 390, window=r5)
    input_window = my_canvas.create_window(red_offset, 425, window=r6)
    input_window = my_canvas.create_window(red_offset, 460, window=r7)
    input_window = my_canvas.create_window(red_offset, 495, window=r8)
    input_window = my_canvas.create_window(red_offset, 530, window=r9)
    input_window = my_canvas.create_window(red_offset, 565, window=r10)
    input_window = my_canvas.create_window(red_offset, 600, window=r11)
    input_window = my_canvas.create_window(red_offset, 635, window=r12)
    input_window = my_canvas.create_window(red_offset, 670, window=r13)
    input_window = my_canvas.create_window(red_offset, 705, window=r14)
    input_window = my_canvas.create_window(red_offset, 740, window=r15)
    #id placement
    input_window = my_canvas.create_window(red_offset-150, 250, window=r1_id)
    input_window = my_canvas.create_window(red_offset - 150, 285, window=r2_id)
    input_window = my_canvas.create_window(red_offset - 150, 320, window=r3_id)
    input_window = my_canvas.create_window(red_offset - 150, 355, window=r4_id)
    input_window = my_canvas.create_window(red_offset - 150, 390, window=r5_id)
    input_window = my_canvas.create_window(red_offset - 150, 425, window=r6_id)
    input_window = my_canvas.create_window(red_offset - 150, 460, window=r7_id)
    input_window = my_canvas.create_window(red_offset - 150, 495, window=r8_id)
    input_window = my_canvas.create_window(red_offset - 150, 530, window=r9_id)
    input_window = my_canvas.create_window(red_offset - 150, 565, window=r10_id)
    input_window = my_canvas.create_window(red_offset - 150, 600, window=r11_id)
    input_window = my_canvas.create_window(red_offset - 150, 635, window=r12_id)
    input_window = my_canvas.create_window(red_offset - 150, 670, window=r13_id)
    input_window = my_canvas.create_window(red_offset - 150, 705, window=r14_id)
    input_window = my_canvas.create_window(red_offset - 150, 740, window=r15_id)


    #green team names
    g1 = Entry(my_canvas, width=30)
    g2 = Entry(my_canvas, width=30)
    g3 = Entry(my_canvas, width=30)
    g4 = Entry(my_canvas, width=30)
    g5 = Entry(my_canvas, width=30)
    g6 = Entry(my_canvas, width=30)
    g7 = Entry(my_canvas, width=30)
    g8 = Entry(my_canvas, width=30)
    g9 = Entry(my_canvas, width=30)
    g10 = Entry(my_canvas, width=30)
    g11 = Entry(my_canvas, width=30)
    g12 = Entry(my_canvas, width=30)
    g13 = Entry(my_canvas, width=30)
    g14 = Entry(my_canvas, width=30)
    g15 = Entry(my_canvas, width=30)
    # green team id
    g1_id = Entry(my_canvas, width=3)
    g2_id = Entry(my_canvas, width=3)
    g3_id = Entry(my_canvas, width=3)
    g4_id = Entry(my_canvas, width=3)
    g5_id = Entry(my_canvas, width=3)
    g6_id = Entry(my_canvas, width=3)
    g7_id = Entry(my_canvas, width=3)
    g8_id = Entry(my_canvas, width=3)
    g9_id = Entry(my_canvas, width=3)
    g10_id = Entry(my_canvas, width=3)
    g11_id = Entry(my_canvas, width=3)
    g12_id = Entry(my_canvas, width=3)
    g13_id = Entry(my_canvas, width=3)
    g14_id = Entry(my_canvas, width=3)
    g15_id = Entry(my_canvas, width=3)

    #placement
    input_window = my_canvas.create_window(green_offset, 250, window=g1)
    input_window = my_canvas.create_window(green_offset, 285, window=g2)
    input_window = my_canvas.create_window(green_offset, 320, window=g3)
    input_window = my_canvas.create_window(green_offset, 355, window=g4)
    input_window = my_canvas.create_window(green_offset, 390, window=g5)
    input_window = my_canvas.create_window(green_offset, 425, window=g6)
    input_window = my_canvas.create_window(green_offset, 460, window=g7)
    input_window = my_canvas.create_window(green_offset, 495, window=g8)
    input_window = my_canvas.create_window(green_offset, 530, window=g9)
    input_window = my_canvas.create_window(green_offset, 565, window=g10)
    input_window = my_canvas.create_window(green_offset, 600, window=g11)
    input_window = my_canvas.create_window(green_offset, 635, window=g12)
    input_window = my_canvas.create_window(green_offset, 670, window=g13)
    input_window = my_canvas.create_window(green_offset, 705, window=g14)
    input_window = my_canvas.create_window(green_offset, 740, window=g15)



    #placement id
    input_window = my_canvas.create_window(green_offset - 150, 250, window=g1_id)
    input_window = my_canvas.create_window(green_offset - 150, 285, window=g2_id)
    input_window = my_canvas.create_window(green_offset - 150, 320, window=g3_id)
    input_window = my_canvas.create_window(green_offset - 150, 355, window=g4_id)
    input_window = my_canvas.create_window(green_offset - 150, 390, window=g5_id)
    input_window = my_canvas.create_window(green_offset - 150, 425, window=g6_id)
    input_window = my_canvas.create_window(green_offset - 150, 460, window=g7_id)
    input_window = my_canvas.create_window(green_offset - 150, 495, window=g8_id)
    input_window = my_canvas.create_window(green_offset - 150, 530, window=g9_id)
    input_window = my_canvas.create_window(green_offset - 150, 565, window=g10_id)
    input_window = my_canvas.create_window(green_offset - 150, 600, window=g11_id)
    input_window = my_canvas.create_window(green_offset - 150, 635, window=g12_id)
    input_window = my_canvas.create_window(green_offset - 150, 670, window=g13_id)
    input_window = my_canvas.create_window(green_offset - 150, 705, window=g14_id)
    input_window = my_canvas.create_window(green_offset - 150, 740, window=g15_id)

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
