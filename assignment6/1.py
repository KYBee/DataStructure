import collections

class Station:
    def __init__(self, name):
        self.name=name
        #Dictionary로 구성되어 있으므로 따로 Sorting 할 필요가 없음
        self.adjacent_stations = {}

    def __str__(self):
        return self.name

class Map:
    def __init__(self):
        self.stations = None

    def set_map(self, stations, connections):
        self.stations = stations
        self.connect_stations(connections)

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

    def get_distance(self, start, end):
        distance = {}
        final_distance = {}
        final_distance[start] = [0, start]

        #initialize
        cur = self.stations[start]
        for station in cur.adjacent_stations.keys():
            distance[station] = [cur.adjacent_stations[station], cur.name]

        nearest, weight = sorted(distance.items(), key=lambda item: item[1])[0]
        del distance[nearest]
        final_distance[nearest] = weight


        for i in range(30):
        #while True:
            #가장 작은 weight를 가진 역을 하나 뽑아서 target으로 설정한다.
            
            cur = self.stations[nearest]

            for station in cur.adjacent_stations.keys():
                if station in final_distance:
                    continue
                elif station in distance.keys():
                    weight = [final_distance[cur.name][0] + cur.adjacent_stations[station], cur.name]
                    temp = distance[station]

                    if weight[0] < temp[0]:
                        distance[station] = weight

                else:
                    distance[station] = [cur.adjacent_stations[station], cur.name]

            print("distance 한 번 끝")
            print(distance)
            print(final_distance)
            print()
            print(cur)
            print()

            nearest, weight = sorted(distance.items(), key=lambda item: item[1])[0]
            del distance[nearest]
            final_distance[nearest] = weight
            print("final distance 한 번 끝")
            print(distance)
            print(final_distance)
            print()
            print()
            print()

        return final_distance
        


all_stations = {
    "중앙": Station("중앙"), "금정" : Station("금정"), "인덕원" : Station("인덕원"), "과천": Station("과천"), "사당" : Station("사당"),
    "이수": Station("이수"), "동작" : Station("동작"), "동대문" : Station("동대문"), "당고개" : Station("당고개"), "성균관대": Station("성균관대"), 
    "문래": Station("문래"), "안양" : Station("안양"), "가산디지털단지" : Station("가산디지털단지"), "신도림": Station("신도림"), 
    "노량진": Station("노량진"), "가양": Station("가양"), "서초": Station("서초"), "서울대입구": Station("서울대입구"), 
    "광명사거리": Station("광명사거리"), "대림": Station("대림"), "상도": Station("상도"), "고속터미널": Station("고속터미널"),
    "흑석": Station("흑석"), "당산": Station("당산"),
}

all_distance = [
    ['가양', '당산', 6], ['당산', '노량진', 4], ['노량진', '흑석', 2], ['흑석', '동작', 1], ['동작', '고속터미널', 3],
    ['고속터미널', '이수', 2], ['이수', '상도', 3], ['상도', '대림', 5], ['대림', '가산디지털단지', 2], ['가산디지털단지', '광명사거리', 2],
    ['당산', '문래', 2], ['문래', '신도림', 1], ['신도림', '대림', 1], ['대림', '서울대입구', 5], ['서울대입구', '사당', 2],
    ['사당', '서초', 2], ['성균관대', '금정', 4], ['금정', '안양', 2], ['안양', '가산디지털단지', 5], ['가산디지털단지', '신도림', 2],
    ['신도림', '노량진', 4], ['노량진', '동대문', 8], ['중앙', '금정', 7], ['금정', '인덕원', 4], ['인덕원', '과천', 2],
    ['과천', '사당', 5], ['사당', '이수', 1], ['이수','동작', 1], ['동작', "동대문", 10], ['동대문', "당고개", 9],
]

Seoul_Train = Map()
Seoul_Train.set_map(all_stations, all_distance)

for i in Seoul_Train.get_available_station():
    print(i, end=" ")
    print(i.adjacent_stations)

Seoul_Train.get_distance("중앙", "대림")