import collections
import random

#역의 정보를 담아 둘 Station Class
class Station:
    def __init__(self, name):
        self.name=name
        self.adjacent_stations = {}

    def __str__(self):
        return self.name

#서울 지하철 노선 저장 및 경로 탐색을 위한 Class
class Map:
    def __init__(self, stations, connections):
        self.stations = stations
        self.connect_stations(connections)
        self.path = None

    #BFS를 이용하여 연결되어 저장되어 있는 모든 역 이름을 출력한다.
    def get_available_station(self):
        if not len(self.stations):
            return None
        else:
            #random한 역 하나를 추출하여 그 역에서부터 탐색을 진행한다.
            start = random.sample(list(self.stations), 1)[0] 
            station_list = [start]

            queue = collections.deque([start])
            while queue:
                vertex = queue.popleft()
                
                for next_station in self.stations[vertex].adjacent_stations:
                    if next_station not in station_list:
                        station_list.append(next_station)
                        queue.append(next_station)

        #추출된 역은 정렬하여 화면에 표시한다.
        station_list.sort()
        for station in station_list:
            print(station, end="  ")

    #역과 역 사이를 연결하고 Weight를 지정한다.
    def connect_stations(self, connections):
        for connection in connections:
            if len(connection) != 3:
                continue
            station1 = connection[0]
            station2 = connection[1]
            weight = connection[2]
            self.stations[station1].adjacent_stations[station2] = weight
            self.stations[station2].adjacent_stations[station1] = weight

    #다익스트라 알고리즘을 사용하여 최소 경로를 구한다. 
    def get_path(self, start, end):
        #distance는 경로 확정이 되지 않은 역들이 모여있는 Dictionary
        #final_distance는 경로 확정이 된 역들이 모여있는 Dictionary 

        #첫 initialize
        distance = {start:[0, start]}
        final_distance = {}

        #시작역에서부터 주변에 있는 역들과 그 weight를 먼저 distance에 넣음
        cur = self.stations[start]
        for station in cur.adjacent_stations:
            distance[station] = [cur.adjacent_stations[station], cur.name]

        #distance에 들어있는 역들 중 가장 weight 즉 거리가 짧은 역을 distance에서 제거하고 final_distance에 넣음
        #이 경우에는 가장 첫 역이 들어가게 됨
        nearest, weight = sorted(distance.items(), key=lambda item: item[1][0])[0]
        del distance[nearest]
        final_distance[nearest] = weight

        #distance에 아무 역도 남아있지 않을 때 까지 실행한다.
        while len(distance) != 0:
            #distance에 들어있는 역들 중 가장 weight 즉 거리가 짧은 역을 distance에서 제거하고 final_distance에 넣음
            nearest, weight = sorted(distance.items(), key=lambda item: item[1][0])[0]
            del distance[nearest]
            final_distance[nearest] = weight

            #distance에서 제거한 역의 인접 역과 weight를 저장하기 위해 cur에 해당 역을 할당하고 
            #시작점부터 그 역까지의 거리를 start_to_current_weight에 할당한다.
            cur = self.stations[nearest]
            start_to_current_weight = weight[0]

            for station in cur.adjacent_stations:
                path = {**distance, **final_distance}

                #distance와 final_distance 중 어느 부분에 존재하던 역이라면 더 짧은 거리의 정보로 업데이트한다.
                if station in path:
                    path1 = path[station]
                    path2 = [cur.adjacent_stations[station] + start_to_current_weight, cur.name]
                    if path1[0] > path2[0]:
                        distance[station] = path2
                #아직 distance와 final_distance어디에도 없던 역이면 새로 추가한다.
                else:
                    distance[station] = [cur.adjacent_stations[station] + start_to_current_weight, cur.name]

        self.path = final_distance
        self.printing_path(start, end)

    #구한 결과 path를 출력하고 None으로 다시 초기화한다.
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
        self.path = None

        

#모든 역을 Dictionary에 선언했다.
all_stations = {
    "중앙": Station("중앙"), "금정" : Station("금정"), "인덕원" : Station("인덕원"), "과천": Station("과천"), "사당" : Station("사당"),
    "이수": Station("이수"), "동작" : Station("동작"), "동대문" : Station("동대문"), "당고개" : Station("당고개"), "성균관대": Station("성균관대"), 
    "문래": Station("문래"), "안양" : Station("안양"), "가산디지털단지" : Station("가산디지털단지"), "신도림": Station("신도림"), 
    "노량진": Station("노량진"), "가양": Station("가양"), "서초": Station("서초"), "서울대입구": Station("서울대입구"), 
    "광명사거리": Station("광명사거리"), "대림": Station("대림"), "상도": Station("상도"), "고속터미널": Station("고속터미널"),
    "흑석": Station("흑석"), "당산": Station("당산"),
}
#역과 역 사이의 Edge와 Weight를 선언했다.
all_directions = [
    ['가양', '당산', 6], ['당산', '노량진', 4], ['노량진', '흑석', 2], ['흑석', '동작', 1], ['동작', '고속터미널', 3],
    ['고속터미널', '이수', 2], ['이수', '상도', 3], ['상도', '대림', 5], ['대림', '가산디지털단지', 2], ['가산디지털단지', '광명사거리', 2],
    ['당산', '문래', 2], ['문래', '신도림', 1], ['신도림', '대림', 1], ['대림', '서울대입구', 5], ['서울대입구', '사당', 2],
    ['사당', '서초', 2], ['성균관대', '금정', 4], ['금정', '안양', 2], ['안양', '가산디지털단지', 5], ['가산디지털단지', '신도림', 2],
    ['신도림', '노량진', 4], ['노량진', '동대문', 8], ['중앙', '금정', 7], ['금정', '인덕원', 4], ['인덕원', '과천', 2],
    ['과천', '사당', 5], ['사당', '이수', 1], ['이수','동작', 1], ['동작', "동대문", 10], ['동대문', "당고개", 9],
]

#Seoul_Train 클래스를 all_stations와 all_directions를 이용해서 initialize 한다.
Seoul_Train = Map(all_stations, all_directions)

while True:
    print("갈 수 있는 역의 종류입니다.")
    #갈 수 있는 역을 BFS로 표시한다.
    Seoul_Train.get_available_station()
    #사용자에게 역을 입력받는다.
    print("\n출발역과 도착역을 입력한다.")
    start = input("출발역 : ")
    end = input("도착역 : ")

    #사용자의 입력에 따라 경로를 구하여 표시하거나 다시 입력을 받도록 한다.
    if start in Seoul_Train.stations and end in Seoul_Train.stations:
        print("경로와 거리를 표시한다.")
        Seoul_Train.get_path(start, end)
    else:
        print("존재하는 역을 입력해주세요\n\n")
