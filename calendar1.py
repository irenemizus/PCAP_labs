class WeekDayError(Exception):
    pass


class Weeker:
    __days_accept = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        self.__day = day
        if not self.__day in Weeker.__days_accept:
            raise WeekDayError
        self.__day_num = Weeker.__days_accept.index(self.__day)

    def __str__(self):
        return self.__day

    def add_days(self, n):
        assert isinstance(n, int)
        self.__day = Weeker.__days_accept[self.__day_num + n % 7]

    def subtract_days(self, n):
        assert isinstance(n, int)
        self.__day = Weeker.__days_accept[self.__day_num - (n - 1) % 7]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")