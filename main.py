from tkinter import *
import tkinter as tk
from random import randrange
from draw_process import draw_process


def mouse_click_pos(event):
    global x1, y1
    x1, y1 = event.x, event.y
    return x1, y1


def mouse_hold_pos(event):
    global x3, y3, m_pos
    x3, y3 = event.x, event.y
    # print("length m_pos = %s" % len(m_pos))
    if len(m_pos) == 0:
        m_pos.append(x3)
        m_pos.append(y3)
    elif (x3 != m_pos[len(m_pos)-2]) or (y3 != m_pos[len(m_pos)-1]):
        m_pos.append(x3)
        m_pos.append(y3)
    print(m_pos)
    print("length m_pos = %s" % len(m_pos))
    return m_pos


def mouse_release_pos(event):
    global x2, y2
    x2, y2 = event.x, event.y
    pos = draw_process(x1, y1, x2, y2, m_pos, choice, can, master)
    pos.check_choice()
    clear_var()
    return x2, y2


def mouse_pos(event):
    global x, y
    x, y = event.x, event.y
    mouse_pos.config(text="[%s, %s]" % (x, y))


def rand_color():
    global color
    color = ""
    str_r1 = hex(randrange(0, 16))
    str_r2 = hex(randrange(0, 16))
    str_g1 = hex(randrange(0, 16))
    str_g2 = hex(randrange(0, 16))
    str_b1 = hex(randrange(0, 16))
    str_b2 = hex(randrange(0, 16))
    color = "#" + str_r1[3:] + str_r2[3:] + str_g1[3:] + str_g2[3:] + str_b1[3:] + str_b2[3:]
    # [2:] = from pos 2nd to end, RGB color
    print(color)
    return color


def clear():
    global choice
    choice = 0
    clr = draw_process(x1, y1, x2, y2, m_pos, choice, can, master)
    clr.check_clear()
    choice = None
    clear_var()
    print("Canvas cleared "+str(choice))


def clear_var():
    global x, y, x1, y1, x2, y2, x3, y3, choice, m_pos
    x, y, x1, y1, x2, y2, x3, y3, choice = 0, 0, 0, 0, 0, 0, 0, 0, None
    m_pos = []


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


def window_exit():  # under construction - work but for luck
    try:
        master.destroy()
    except SystemError:  # For unknown error occurs
        master.destroy()
        print("System Error found")
        pass  # Do nothing


# Main
x, y, x1, y1, x2, y2, x3, y3, choice = 0, 0, 0, 0, 0, 0, 0, 0, None
m_pos = []
color = rand_color()
master = Tk()
master.overrideredirect(1)
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
can.bind('<Button-1>', mouse_click_pos)
can.bind('<ButtonRelease-1>', mouse_release_pos)
can.bind('<Motion>', mouse_pos)
can.bind('<B1-Motion>', mouse_hold_pos)

mouse_pos = tk.Label(master)
# master.title("My paint - "+str(pos_log))
mouse_pos.place(x=10, y=505)
master.title("My paint")

master.mainloop()
# master.destroy()
