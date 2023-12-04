# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_DungeonMap


all_locations = {}
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
    global begin, end, all_locations

    while not begin:
        line = input()

        if not " " in line:
            begin = line
            end = input()
            break

        pair = line.split()
        add_route(pair[0], pair[1])
        add_route(pair[1], pair[0])
        all_locations[pair[0]] = 0
        all_locations[pair[1]] = 0


def find_way(current_step):
    global end, tunnels_map, all_locations

    there_are_changes = False

    for location, step in all_locations.items():
        if step == current_step:
            for next_location in tunnels_map[location]:
                if all_locations[next_location] == 0:
                    all_locations[next_location] = current_step + 1
                    there_are_changes = True

    if there_are_changes:
        return find_way(current_step + 1)

    return all_locations.get(end, 0) != 0


fill_in_routes()
all_locations[begin] = 1

if find_way(1):
    print("YES")
else:
    print("NO")
