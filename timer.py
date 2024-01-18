class Timer:
    def __init__(self, hrs = 0, mins = 0, secs = 0):
        self.__hrs = hrs
        self.__mins = mins
        self.__secs = secs

    def __str__(self):
        time_str_list = []
        for t in (self.__hrs, self.__mins, self.__secs):
            if t < 10:
                time_str_list.append(''.join(['0', str(t)]))
            else:
                time_str_list.append(str(t))

        return ':'.join(time_str_list)

    def next_second(self):
        self.__secs += 1
        if self.__secs > 59:
            self.__secs = 0
            self.__mins += 1
            if self.__mins > 59:
                self.__mins = 0
                self.__hrs += 1

    def prev_second(self):
        self.__secs -= 1
        if self.__secs < 0:
            self.__secs = 59
            self.__mins -= 1
            if self.__mins < 0:
                self.__mins = 59
                self.__hrs -= 1

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
