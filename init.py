class init:
    def __init__(self, x1, y1, x2, y2, m_pos, choice, can, master):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.m_pos = m_pos
        self.choice = choice
        self.can = can
        self.master = master
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
        for i in range(int(len(self.m_pos)/2)):
            if i <= 0:
                pass
            else:
                dx = self.m_pos[i*2]-self.m_pos[i*2-2]
                dy = self.m_pos[i*2+1] - self.m_pos[i*2-1]
                max_d = 2*max(abs(dx), abs(dy))
                for j in range(max_d):
                    self.can.create_oval(int(self.m_pos[i*2]+dx*j/max_d),               # x1
                                         int(self.m_pos[i*2+1]+dy*j/max_d),             # y1
                                         int(self.m_pos[i*2]+dx*j/max_d),               # x2
                                         int(self.m_pos[i*2+1]+dy*j/max_d),             # y2
                                         outline='red')
