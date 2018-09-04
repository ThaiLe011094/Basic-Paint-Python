class init:
    def __init__(self, x1, y1, x2, y2, choice, can, master):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.choice = choice
        self.can = can
        self.master = master
        # master = Tk()
        # self.master = master
        # can = Canvas(master, bg='dark grey', height=500, width=500)
        # self.can = can
        print('init received pos x1 = {}, y1 = {}, x2 = {}, y2 = {}'.format(self.x1, self.y1, self.x2, self.y2))

    def clear(self):
        print('Init is clearing canvas')
        self.can.create_rectangle(0, 0, 500, 500, outline='dark grey', fill='dark grey')

    def rec_process(self):
        print('rec_process received pos x1 = {}'.format(self.x1))
        self.can.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline='red')

    def ova_process(self):
        print('ova_process received pos x1 = {}'.format(self.x1))
        self.can.create_oval(self.x1, self.y1, self.x2, self.y2, outline='red')

    def dot_process(self):
        print('dot_process received pos x1 = {}'.format(self.x1))
        while (self.x2 != self.x1) or (self.y2 != self.y1):
            self.can.create_oval(self.x1, self.y1, self.x1, self.y1, outline='red')
