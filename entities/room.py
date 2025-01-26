class RoomEntity:
    def __init__(self, name, capacity, location):
        self.__name = name
        self.__capacity = capacity
        self.__location = location

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location
