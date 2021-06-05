import collections

class Station:
    def __init__(self, name):
        self.name=name
        self.adjacent_station = []

    def __str__(self):
        return self.name

class Map:
    def __init__(self):
        self.stations = None
        self.distance_map = None

    def set_map(self, stations, connections):
        self.stations = stations
        self.connect_stations(connections)
        self.distance_map = self.get_distance_map()

    def get_available_station(self):
        return self.stations.keys()

    def connect_stations(self, connections):
        return

    def get_distance_map(self):
        pass



all_station = {
    Station("중앙") : 0, Station("금정") : 1, Station("인덕원") : 2, Station("과천") : 3, Station("사당") : 4,
    Station("이수") : 5, Station("동작") : 6, Station("동대문") : 7, Station("당고개") : 8, Station("성균관대") : 9, 
    Station("문래") : 10, Station("안양") : 11, Station("가산디지털단지") : 12, Station("신도림") : 13, 
    Station("노량진") : 14, Station("가양") : 15, Station("서초") : 16, Station("서울대입구") : 17, 
    Station("광명사거리"): 18, Station("대림") : 19, Station("상도") : 20, Station("고속터미널"): 21,
    Station("흑석") : 22, Station("당산") : 23,
}

Seoul_Train = Map()
Seoul_Train.set_map(all_station)

for i in Seoul_Train.get_available_station():
    print(i, end=" ")