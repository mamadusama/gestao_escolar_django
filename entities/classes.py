class ClassEntity:
    def __init__(self, name, year, period, student_count, room):
        self.__name = name
        self.__year = year
        self.__period = period
        self.__student_count = student_count
        self.__room = room

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, period):
        self.__period = period

    @property
    def student_count(self):
        return self.__student_count

    @student_count.setter
    def student_count(self, student_count):
        self.__student_count = student_count

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room):
        self.__room = room
