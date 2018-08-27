def m_click(event):  # start mouse click event
    global x1, y1
    x1, y1 = event.x, event.y
    if choice == 3:
        dot_process()
    return x1, y1


def m_release(event):  # release mouse clicking event
    global x1, y1, x2, y2
    print("Mouse pos from (%s %s) to (%s %s)" % (x1, y1, event.x, event.y))
    x2, y2 = event.x, event.y
    draw_process()


def m_log(event):  # logging mouse position
    global x, y, x_temp, y_temp
    x, y = event.x, event.y
    pos_log.config(text="[%s %s]" % (x, y))
    return


def rand_color():
    global color
    color = ""
    str_r1 = hex(randrange(0, 16))
    str_r2 = hex(randrange(0, 16))
    str_g1 = hex(randrange(0, 16))
    str_g2 = hex(randrange(0, 16))
    str_b1 = hex(randrange(0, 16))
    str_b2 = hex(randrange(0, 16))
    color = "#"+str_r1[2:]+str_r2[2:]+str_g1[2:]+str_g2[2:]+str_b1[2:]+str_b2[2:]
    # [2:] = from pos 2nd to end, RGB color
    print(color)
    return color


def draw_rec():
    global choice
    choice = 1
    print("Draw Rectangle "+str(choice))


def draw_ova():
    global choice
    choice = 2
    print("Draw Oval "+str(choice))


def draw_dot():
    global choice
    choice = 3
    print("Draw Dot "+str(choice))


def draw_process():
    global choice
    if choice == 1:
        can.create_rectangle(x1, y1, x2, y2, outline='red')
    if choice == 2:
        can.create_oval(x1, y1, x2, y2, outline='red')
    else:
        pass


def dot_process():  # Draw line with dot
    global x1, y1, x_temp, y_temp
    if x_temp != x1:
        if x_temp != -1:
            can.create_line(x1, y1, x_temp, y_temp, fill='red')
        x_temp = x1
    if y_temp != y1:
        if y_temp != -1:
            can.create_line(x1, y1, x_temp, y_temp, fill='red')
        y_temp = y1
    return


def clear():
    global x1, y1, x2, y2, x_temp, y_temp
    can.create_rectangle(0, 0, 500, 500, outline='dark grey', fill='dark grey')
    x1, y1, x2, y2, x_temp, y_temp = 0, 0, 0, 0, -1, -1
    print("Canvas has been cleared")


def input_size():  # Create Canvas size with user input
    global x, y
    x, y = input("Width"), input("Height")


def window_exit():  # under construction - work but for luck
    try:
        master.destroy()
    except SystemError:  # For unknown error occurs
        master.destroy()
        print("System Error found")
        pass  # Do nothing
    finally:
        sys.exit()
        master.destroy()
        print("Unexpected error found")


# Main
x, y, x1, y1, x2, y2, x_temp, y_temp, choice = 0, 0, 0, 0, 0, 0, -1, -1, None
color = rand_color()
master = Tk()
# master.attributes('-disabled', True)
can = Canvas(master, bg='dark grey', height=500, width=500)
master.geometry("550x530+30+30")  # Size (Width*Height + W_offset + H_offset)
can.place(x=0, y=0)

# Button config
# Clear
clear_but = Button(master, text='Clear', command=clear)
clear_but.place(x=504, y=1, width=45, height=25)

# Quit
quit_but = Button(master, text='Quit', command=window_exit)
quit_but.place(x=504, y=504, width=45, height=25)

# Rectangle drawing
rect_but = Button(master, text='Rect', command=draw_rec)
rect_but.place(x=504, y=27, width=45, height=25)

# Oval drawing
oval_but = Button(master, text='Oval', command=draw_ova)
oval_but.place(x=504, y=53, width=45, height=25)

# Dot drawing
oval_but = Button(master, text='Dot', command=draw_dot)
oval_but.place(x=504, y=79, width=45, height=25)

# Main config
can.bind('<Button-1>', m_click)
can.bind('<ButtonRelease-1>', m_release)
can.bind('<Motion>', m_log)

pos_log = tk.Label(master)
# master.title("My paint - "+str(pos_log))
pos_log.place(x=10, y=505)
master.title("My paint")

master.mainloop()
# master.destroy()
