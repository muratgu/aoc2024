def solve(lines):

    def find_path(maze, start, step, path=[], paths=[]):

        # correct step ?
        if maze[start[0]][start[1]] == str(step):
            path.append( [start, maze[start[0]][start[1]]] )
            if step == 9:
                # reached the top 
                paths.append( (path[0][0], path[-1][0]) )
                return  
        else:
            # cannot even start ?
            if step == 0:
                return
    
        # explore
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_start = (start[0] + i, start[1] + j)
            if 0 <= new_start[0] < len(maze) \
            and 0 <= new_start[1] < len(maze[0]) \
            and maze[new_start[0]][new_start[1]] == str(step+1):
                find_path(maze, new_start, step+1, path, paths)
        return

    rating = 0 # distinct routes
    score = 0 # distinct summits
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            paths = []        
            find_path(lines, (i, j), 0, [], paths)
            if len(paths) > 0:
                rating += len(paths)
                score += len(set(paths))

    #print('size', len(lines), len(lines[0]))           
    print('day10 part1', score)
    print('day10 part2', rating)

with open('day10-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)