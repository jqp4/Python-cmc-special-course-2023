# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_DungeonMap


passed_locations = {}
tunnels_map = {}
begin = None
end = None


def add_route(a, b):
    global tunnels_map

    if not a in tunnels_map:
        tunnels_map[a] = [b]
    elif not b in tunnels_map[a]:
        tunnels_map[a].append(b)


def fill_in_routes():
    global begin, end, passed_locations

    while not begin:
        line = input()

        if not " " in line:
            begin = line
            end = input()
            break

        pair = line.split()
        add_route(pair[0], pair[1])
        add_route(pair[1], pair[0])
        passed_locations[pair[0]] = False
        passed_locations[pair[1]] = False


def find_way_long(current_location):
    global end, tunnels_map, passed_locations

    if end == current_location:
        print("Нашли выход!")
        return True

    if passed_locations[current_location]:
        print("Здесь мы уже были!")
        return False

    if not current_location in tunnels_map:
        print("Дальше пути нет!")
        return False

    passed_locations[current_location] = True
    for next_location in tunnels_map[current_location]:
        print(f">>> {current_location} --> {next_location}")
        if find_way_long(next_location):
            return True

    passed_locations[current_location] = False
    return False


def find_way(current_location):
    global end, tunnels_map, passed_locations

    passed_locations[current_location] = True
    for next_location in tunnels_map[current_location]:
        if end == next_location or (
            not passed_locations[next_location]
            and next_location in tunnels_map
            and find_way(next_location)
        ):
            return True

    passed_locations[current_location] = False
    return False


fill_in_routes()

for a, b in tunnels_map.items():
    print(f"{a} --> {b}")

if find_way(begin):
    print("YES")
else:
    print("NO")
