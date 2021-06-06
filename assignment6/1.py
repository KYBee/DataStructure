import collections

class Station:
    def __init__(self, name):
        self.name=name
        self.adjacent_stations = {}

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
        return self.stations.values()

    def connect_stations(self, connections):

        for connection in connections:
            if len(connection) != 3:
                continue
            station1 = connection[0]
            station2 = connection[1]
            weight = connection[2]
            self.stations[station1].adjacent_stations[station2] = weight
            self.stations[station2].adjacent_stations[station1] = weight

    def get_distance_map(self):
        pass



all_stations = {
    "중앙": Station("중앙"), "금정" : Station("금정"), "인덕원" : Station("인덕원"), "과천": Station("과천"), "사당" : Station("사당"),
    "이수": Station("이수"), "동작" : Station("동작"), "동대문" : Station("동대문"), "당고개" : Station("당고개"), "성균관대": Station("성균관대"), 
    "문래": Station("문래"), "안양" : Station("안양"), "가산디지털단지" : Station("가산디지털단지"), "신도림": Station("신도림"), 
    "노량진": Station("노량진"), "가양": Station("가양"), "서초": Station("서초"), "서울대입구": Station("서울대입구"), 
    "광명사거리": Station("광명사거리"), "대림": Station("대림"), "상도": Station("상도"), "고속터미널": Station("고속터미널"),
    "흑석": Station("흑석"), "당산": Station("당산"),
}

all_distance = [
    ['가양', '당산', 6],
    ['당산', '노량진', 4],
    ['노량진', '흑석', 2],
    ['흑석', '동작', 1],
    ['동작', '고속터미널', 3],
    ['고속터미널', '이수', 2],
    ['이수', '상도', 3],
    ['상도', '대림', 5],
    ['대림', '가산디지털단지', 2],
    ['가산디지털단지', '광명사거리', 2],
    ['당산', '문래', 2],
    ['문래', '신도림', 1],
    ['신도림', '대림', 1],
    ['대림', '서울대입구', 5],
    ['서울대입구', '사당', 2],
    ['사당', '서초', 2],
    ['성균관대', '금정', 4],
    ['금정', '안양', 2],
    ['안양', '가산디지털단지', 5],
    ['가산디지털단지', '신도림', 2],
    ['신도림', '노량진', 4],
    ['노량진', '동대문', 8],
    ['중앙', '금정', 7],
    ['금정', '인덕원', 4],
    ['인덕원', '과천', 2],
    ['과천', '사당', 5],
    ['사당', '이수', 1],
    ['이수','동작', 1],
    ['동작', "동대문", 10],
    ['동대문', "당고개", 8],
]

Seoul_Train = Map()
Seoul_Train.set_map(all_stations, all_distance)

for i in Seoul_Train.get_available_station():
    print(i, end=" ")
    print(i.adjacent_stations)