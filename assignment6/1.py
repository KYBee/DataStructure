import collections
import random

class Station:
    def __init__(self, name):
        self.name=name
        self.adjacent_stations = {}

    def __str__(self):
        return self.name

class Map:
    def __init__(self, stations, connections):
        self.stations = None
        self.path = None
        self.set_map(stations, connections)


    def set_map(self, stations, connections):
        self.stations = stations
        self.connect_stations(connections)


    def get_available_station(self):
        if not len(self.stations):
            return None
        else:
            #random한 역 하나를 추출하여 bfs를 한다.
            start = random.sample(list(self.stations), 1)[0] 
            station_list = [start]

            queue = collections.deque([start])
            while queue:
                vertex = queue.popleft()
                
                for next_station in self.stations[vertex].adjacent_stations:
                    if next_station not in station_list:
                        station_list.append(next_station)
                        queue.append(next_station)

        station_list.sort()
        for station in station_list:
            print(station, end="  ")

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
        #initialize
        distance = {start:[0, start]}
        final_distance = {}

        cur = self.stations[start]
        for station in cur.adjacent_stations:
            distance[station] = [cur.adjacent_stations[station], cur.name]

        nearest, weight = sorted(distance.items(), key=lambda item: item[1][0])[0]
        del distance[nearest]
        final_distance[nearest] = weight

        while len(distance) != 0:
            #가장 작은 weight를 가진 역을 하나 뽑아서 target으로 설정한다. 비교하는 key 값은 거리
            nearest, weight = sorted(distance.items(), key=lambda item: item[1][0])[0]
            del distance[nearest]
            final_distance[nearest] = weight

            cur = self.stations[nearest]
            start_to_current_weight = weight[0]

            for station in cur.adjacent_stations:
                path = {**distance, **final_distance}

                if station in path:
                    path1 = path[station]
                    path2 = [cur.adjacent_stations[station] + start_to_current_weight, cur.name]
                    if path1[0] > path2[0]:
                        distance[station] = path2
                else:
                    distance[station] = [cur.adjacent_stations[station] + start_to_current_weight, cur.name]

        self.path = final_distance
        self.printing_path(start, end)


    def printing_path(self, start, end):
        
        path = [end]

        cur = self.path[end]
        distance = cur[0]
        while cur[1] != start:
            path.append(cur[1])
            cur = self.path[cur[1]]
        
        path.append(start)

        for i in range(len(path) - 1, -1, -1):
            print(path[i], end=" - ")
        
        print(" (%dkm)\n\n" % distance)

        


all_stations = {
    "중앙": Station("중앙"), "금정" : Station("금정"), "인덕원" : Station("인덕원"), "과천": Station("과천"), "사당" : Station("사당"),
    "이수": Station("이수"), "동작" : Station("동작"), "동대문" : Station("동대문"), "당고개" : Station("당고개"), "성균관대": Station("성균관대"), 
    "문래": Station("문래"), "안양" : Station("안양"), "가산디지털단지" : Station("가산디지털단지"), "신도림": Station("신도림"), 
    "노량진": Station("노량진"), "가양": Station("가양"), "서초": Station("서초"), "서울대입구": Station("서울대입구"), 
    "광명사거리": Station("광명사거리"), "대림": Station("대림"), "상도": Station("상도"), "고속터미널": Station("고속터미널"),
    "흑석": Station("흑석"), "당산": Station("당산"),
}

all_directions = [
    ['가양', '당산', 6], ['당산', '노량진', 4], ['노량진', '흑석', 2], ['흑석', '동작', 1], ['동작', '고속터미널', 3],
    ['고속터미널', '이수', 2], ['이수', '상도', 3], ['상도', '대림', 5], ['대림', '가산디지털단지', 2], ['가산디지털단지', '광명사거리', 2],
    ['당산', '문래', 2], ['문래', '신도림', 1], ['신도림', '대림', 1], ['대림', '서울대입구', 5], ['서울대입구', '사당', 2],
    ['사당', '서초', 2], ['성균관대', '금정', 4], ['금정', '안양', 2], ['안양', '가산디지털단지', 5], ['가산디지털단지', '신도림', 2],
    ['신도림', '노량진', 4], ['노량진', '동대문', 8], ['중앙', '금정', 7], ['금정', '인덕원', 4], ['인덕원', '과천', 2],
    ['과천', '사당', 5], ['사당', '이수', 1], ['이수','동작', 1], ['동작', "동대문", 10], ['동대문', "당고개", 9],
]

Seoul_Train = Map(all_stations, all_directions)

while True:
    print("갈 수 있는 역의 종류입니다.")
    Seoul_Train.get_available_station()
    print("\n출발역과 도착역을 입력한다.")
    start = input("출발역 : ")
    end = input("도착역 : ")

    if start in Seoul_Train.stations and end in Seoul_Train.stations:
        print("경로와 거리를 표시한다.")
        Seoul_Train.get_distance(start, end)
    else:
        print("존재하는 역을 입력해주세요\n\n")
