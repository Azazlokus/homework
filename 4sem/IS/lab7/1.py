class BigBell:
    bell = True

    def sound(self):
        if self.bell:
            print("ding")
        else:
            print("dong")
        self.bell = not self.bell


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
