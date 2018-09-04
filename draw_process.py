from init import init


class draw_process(init):
    def __init__(self, x1, y1, x2, y2, choice, can, master):
        init.__init__(self, x1, y1, x2, y2, choice, can, master)
        print('draw_process received pos x1 = {}, y1 = {}, x2 = {}, y2 = {}'.format(self.x1, self.y1, self.x2, self.y2))

    def check_clear(self):
        try:
            if self.choice == 0:
                init.clear(self)
        except:
            pass

    def check_choice(self):
        print('Choice is being checked')
        try:
            if self.choice is None:
                print('Choice is None')
            elif self.choice == 1:
                print('Choice is 1')
                print('Drawing rectangle')
                init.rec_process(self)
            elif self.choice == 2:
                print('Choice is 2')
                print('Drawing Oval')
                init.ova_process(self)
            elif self.choice == 3:
                print('Choice is 3')
                print('Drawing Line')
                init.dot_process(self)
        except:
            pass
