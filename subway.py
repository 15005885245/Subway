file="C:\\Users\\青朽\Desktop\\地铁最短路径.txt"
"""
读入地铁信息文件，将地铁数据转化为图结构
"""
data=dict()
with open(file, "rt", encoding="utf-8") as file:
    n=int(file.readline())
    for i in range(n):
        value=""
        line=file.readline().split()
        for i in line[1:]:
            value=value+i+" "
        data[line[0]]=value
list=data


def build_subway(**lines):
    for key in lines.keys():
        value = lines[key]
        lines[key] = value.split()
    stations = set()
    for key in lines.keys():
        stations.update(set(lines[key]))
    system = {}
    for station in stations:
        next_station = {}
        for key in lines:
            if station in lines[key]:
                line = lines[key]
                idx = line.index(station)
                if idx == 0:
                    next_station[line[1]] = key
                elif idx == len(line) - 1:
                    next_station[line[idx - 1]] = key
                else:
                    next_station[line[idx - 1]] = key
                    next_station[line[idx + 1]] = key
        system[station] = next_station
    return system
sub=build_subway(**list)
def shorter_path(start, goal):
    if start == goal:
        return [start]
    explored = set()
    queue = [ [start] ]
    while queue:
        path = queue.pop(0)
        s = path[-1]
        for state, action in sub[s].items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    queue.append(path2)
    return []


def main():
    flag = input("请输入您要查询的功能（a.查询路线站点 b.查询两站之间最短路径）")
    if flag == "a":
        path = input("请输入您要查询的路线名：")
        print(list[path])
    elif flag=="b":
        start = input("请输入起始站：")
        end = input("请输入终点站：")
        print(shorter_path(start, end))
    else:
        print("请输入正确查询选项")
main()
