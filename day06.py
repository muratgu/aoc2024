
guards = ['^','>','V','<']
dirs   = [(0,-1), (1,0), (0,1), (-1,0)] # directions
cw90s  = [(1,0), (0,1), (-1,0), (0,-1)] # right turns

def where_is_the_guard(lines):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            cell = lines[y][x]
            if cell in guards:
                dir = dirs[guards.index(cell)]
                return ((x, y), dir)
    raise 'guard not found'

def turn_cw90(dir):
    return 

def next_step(room, p):
    x, y = p[0]
    dir = p[1]
    my = len(room)
    mx = len(room[0])
    for i in range(4):
        nx = x + dir[0]
        ny = y + dir[1]
        if nx < 0 or ny < 0 or nx >= mx or ny >= my:
            # get out 
            return ('OUT', ((nx, ny), dir)) 
        cell = room[ny][nx]
        if cell == '#' or cell == 'O':
            # turn right and try again
            dir = cw90s[dirs.index(dir)] 
        else: 
            # keep walking
            return ('WALK', ((nx, ny), dir)) 
    raise 'no exit'

def walk_guard(room):
    path = []
    seen = set()
    p = where_is_the_guard(room)
    while True:
        result, p = next_step(room, p)
        if result == 'OUT':
            return 'DONE', path # done
        path.append(p)        
        if p in seen:
            return 'LOOP', path # loop
        seen.add(p)

def display_path(room, path, obs=None):
    path_xy = [xyd[0] for xyd in path]
    for y in range(len(room)):
        line = ''
        for x in range(len(room[0])):
            cell = room[y][x]
            line += cell if guards.find(cell)>-1 \
                else 'O' if obs == (x, y) \
                else 'X' if path_xy.count((x, y)) > 0 \
                else cell
        print(line)
    print("%s distinct steps" % len(set(path_xy)))


def solve(lines):
    room = [list(line.strip()) for line in lines]
    result, path = walk_guard(room)
    path_xy = list(set([xyd[0] for xyd in path]))

    part1 = len(path_xy)
    print('day06 part1', part1)

    obs = []
    gxy, gdir = where_is_the_guard(room)
    for i in range(len(path_xy)-1):
        xy = path_xy[i+1] # next step
        if xy == gxy: continue # skip guard location
        x, y = xy
        room[y][x] = 'O' # obstacle
        result, _ = walk_guard(room)
        room[y][x] = '.' # restore
        if result == 'LOOP':
            obs.append(xy)
            #print('obstacle %s=%s' % (len(obs), xy))
        else:
            #print("no loop found")
            pass

    #print('%s obstacle locations found to cause a loop' % len(obs))
    part2 = len(obs)
    print('day06 part2', part2)

with open('day06-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)