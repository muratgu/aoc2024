import utils as U
import math

def solve(lines, w, h, times):
    DEBUG = True
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    def min_cost_cell(nodes):
        minimum = math.inf
        min_pos = None
        for pos in nodes:
            cost = nodes[pos]['cost']
            if cost < minimum:
                minimum = cost
                min_pos = pos
        return min_pos
    
    def update_costs(nodes, a):
        a_cost = nodes[a]['cost']
        for d in dirs:
            b = (a[0]+d[0], a[1]+d[1])
            if b in nodes:                
                a_to_b_cost = a_cost + abs(d[0]) + abs(d[1]) 
                if nodes[b]['cost'] > a_to_b_cost:
                    nodes[b] = {'cost': a_to_b_cost, 'prev': a, 'd': d}

    def plot_route(maze, route):
        m = [[col for col in row] for row in maze]
        i = 0
        for pos in route:            
            c = 'S' if i == 0 else 'E' if i == len(route)-1 else 'O'
            m[pos[0]][pos[1]] = c
            i += 1
        return m
    
    def calculate_costs(maze, start, target):
        unvisited = {}
        for i in range(len(maze)): 
            for j in range(len(maze[0])):
                if maze[i][j] != '#':
                    unvisited[(i,j)] = {'cost': math.inf, 'prev': None}
        unvisited[start] = {'cost': 0, 'prev': None}

        visited = {}
        while True:        
            pos = min_cost_cell(unvisited)
            if not pos:
                break
            if pos == target:
                visited[pos] = unvisited[pos]
                break
            update_costs(unvisited, pos)
            visited[pos] = unvisited[pos] 
            del unvisited[pos]
        return visited

    def trace_shortest_path(visited):
        trace, curr_pos = [], target
        while curr_pos and curr_pos in visited:
            trace.append(curr_pos)
            curr_pos = visited[curr_pos]['prev']

        route = {}
        for pos in reversed(trace):
            route[pos] = visited[pos]

        return route

    bytes = []
    for line in lines:
        xy = line.strip().split(',')
        bytes.append((int(xy[0]), int(xy[1])))

    # put the initial number of bytes into the maze 
    maze = [['#' if (i,j) in bytes[0:times] else '.' for i in range(w)] for j in range(h)]

    # start and end points are (0, 0) - (mx, my)
    start = (0,0)
    target = (len(maze)-1, len(maze[0])-1)
    
    #part1
    visited = calculate_costs(maze, start, target) 
    route = trace_shortest_path(visited)
    print ('day18 part1', len(route)-1)
    
    #part2
    slice = (len(bytes)-times) // 2
    sign = 1
    hits = []
    first_hit = None
    while slice > 0:
        times = int(times+sign*slice)
        m = [[col for col in row] for row in maze]
        for xy in bytes[0:times]:
            m[xy[1]][xy[0]] = '#'
        visited = calculate_costs(m, start, target) 
        route = trace_shortest_path(visited)
        if len(route) == 0:
            hits.append(times-1)
        else:
            if len(hits) == 1:
                first_hit = (hits[0], bytes[hits[0]])
                break
            else:
                hits.clear()
        sign = 1 if len(route) > 0 else -1
        slice = slice // 2
    print('day18 part2', first_hit[1])

with open('day18-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines, 71, 71, 1024)
