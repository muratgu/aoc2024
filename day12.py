def solve(lines):

    maze = [[c for c in x.strip()] for x in lines]
    
    #print('day12 %sx%s' % (len(maze), len(maze[0])))
    
    nrow = len(maze)
    ncol = len(maze[0])

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def count_border(c, pos, visited=[]):
        # already visited, ignore
        if (c, pos) in visited:
            return 0, 0, 0
        # are we still inside? 
        if  0 <= pos[0] < len(maze) \
        and 0 <= pos[1] < len(maze[0]) \
        and maze[pos[0]][pos[1]] == c:
            # explore
            visited += [(c, pos)]
            border, area = 0, 1
            corners = count_corners(c, pos)
            for dir in dirs:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                b, a, z = count_border(c, new_pos, visited)
                border += b
                area += a
                corners += z
            return border, area, corners
        # outside ... need a fence here
        return 1, 0, 0

    def cell_at_eq(pos, c):
        x, y = pos
        if 0 <= x < nrow and 0 <= y < ncol: 
            return maze[x][y] == c
        return False

    def count_corners(c, pos):
        n = 0
        # convex cases
        dirs1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        c0 = cell_at_eq((pos[0]+dirs1[0][0], pos[1]+dirs1[0][1]), c)
        c1 = cell_at_eq((pos[0]+dirs1[1][0], pos[1]+dirs1[1][1]), c)
        c2 = cell_at_eq((pos[0]+dirs1[2][0], pos[1]+dirs1[2][1]), c)
        c3 = cell_at_eq((pos[0]+dirs1[3][0], pos[1]+dirs1[3][1]), c)
        n += 1 if not c0 and not c1 else 0
        n += 1 if not c1 and not c2 else 0
        n += 1 if not c2 and not c3 else 0
        n += 1 if not c3 and not c0 else 0
        # concave cases
        dirs2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        c01 = cell_at_eq((pos[0]+dirs2[0][0], pos[1]+dirs2[0][1]), c)
        c12 = cell_at_eq((pos[0]+dirs2[1][0], pos[1]+dirs2[1][1]), c)
        c23 = cell_at_eq((pos[0]+dirs2[2][0], pos[1]+dirs2[2][1]), c)
        c30 = cell_at_eq((pos[0]+dirs2[3][0], pos[1]+dirs2[3][1]), c)
        n += 1 if c0 and c1 and not c01 else 0
        n += 1 if c1 and c2 and not c12 else 0
        n += 1 if c2 and c3 and not c23 else 0
        n += 1 if c3 and c0 and not c30 else 0
        return n

    def survey():
        visited = []    
        surveyed = {}
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                c, pos = maze[i][j], (i, j)
                if not (c, pos) in visited:
                    border, area, corners = count_border(c, pos, visited)                
                    surveyed[(c, pos)] = [border, area, corners]
        return surveyed

    surveyed = survey()
    cost1 = sum([s[0]*s[1] for s in surveyed.values()])
    print('day12 part1', cost1)

    surveyed = survey()
    cost2 = sum([s[1]*s[2] for s in surveyed.values()])
    print('day12 part2', cost2)


with open('day12-input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)