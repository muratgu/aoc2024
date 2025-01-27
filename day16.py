import utils as U
import math

def solve(lines):
    DEBUG = True
    arrows = ['>', 'v', '<', '^']
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]

    def find_cell(maze, c):
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == c:
                    return (i, j)    
                
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
        a_dir = nodes[a]['d']
        for d in dirs:
            b = (a[0]+d[0], a[1]+d[1])
            if b in nodes:                
                a_to_b_cost = a_cost + abs(d[0]) + abs(d[1]) 
                if a_dir != d: 
                    a_to_b_cost += 1000
                if nodes[b]['cost'] > a_to_b_cost:
                    nodes[b] = {'cost': a_to_b_cost, 'prev': a, 'd': d}

    def plot_route(maze, route):
        m = maze.copy()
        for pos in route:
            m[pos[0]][pos[1]] = 'O'
        return m
    
    def find_node_costs(maze, start, target, d):
        unvisited = {}
        for i in range(len(maze)): 
            for j in range(len(maze[0])):
                if maze[i][j] != '#':
                    unvisited[(i,j)] = {'cost': math.inf, 'prev': None}
        unvisited[start] = {'cost': 0, 'prev': None, 'd': d}

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
        while curr_pos:
            trace.append(curr_pos)
            curr_pos = visited[curr_pos]['prev']

        route = {}
        for pos in reversed(trace):
            route[pos] = visited[pos]

        cost = visited[target]['cost']

        return route, cost

    # trace back nodes on 'weights' from 'target' to 'source'
    # scanning all possible connections with the best cost
    # and recording the path in 'trace'
    def trace_paths(weights, pos, seen={}, route=[], routes=[]):        
        seen[pos]=True
        route.append(pos)

        next_pos = weights[pos]['prev']

        if not next_pos:
            routes.append(route.copy())
        else:
            next_node = weights[next_pos]
            next_cost = next_node['cost']
            #print(next_pos, next_cost)
            for d in dirs:
                other_pos = (pos[0]+d[0], pos[1]+d[1])
                #print(other_pos)
                if not other_pos in seen \
                and other_pos in weights \
                and weights[other_pos]['cost'] <=  next_cost+1000:
                    trace_paths(weights, other_pos, seen, route, routes)

        route.pop() #backtrack
        del seen[pos]
        

    maze = [[c for c in line.strip()] for line in lines]

    start = find_cell(maze, 'S')
    target = find_cell(maze, 'E')
    
    U.display(maze)

    if DEBUG: print('start', start, 'target' ,target)

    visited = find_node_costs(maze, start, target, (0, 1)) 

    #part1
    route, cost = trace_shortest_path(visited)
    
    routes = []
    trace_paths(visited, target, {}, [], routes=routes)
    seats = len(set([s for r in routes for s in r]))
    all_plotted = maze.copy()
    for r in routes:
        all_plotted = plot_route(all_plotted, r)
    U.display(all_plotted)

        
    return len(route), cost, seats

with open('day16-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    len_route, cost, seats = solve(lines)
    print('day16 part1', cost)
    print('day16 part2', seats)
