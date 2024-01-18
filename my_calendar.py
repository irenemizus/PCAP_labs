from calendar import Calendar


class MyCalendar(Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year, weekday):
        assert weekday in range(0, 7)
        ndays = 0
        for month in range(1, 13):
            weeks = self.monthdays2calendar(year, month)
            for w in weeks:
                for el in w:
                    if el[1] == weekday and el[0]:
                        ndays += 1

        return ndays


year = int(input("Please enter the year: "))
weekday = int(input("Please enter the weekday number (from 0 to 6, where 0 for Monday and 6 for Sunday): "))

mc = MyCalendar()
print(mc.count_weekday_in_year(year, weekday))



