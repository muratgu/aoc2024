from PIL import Image
import time

def solve(lines, expanded=False):
    DEBUG = False
    ANIMATE = False

    warehouse = [[c for c in line] for line in lines if line.startswith('#')]
    itinerary = [c for line in lines if line > '' and not line.startswith('#') for c in line]
    moves = ['<','^','>','v']
    dirs = [(0,-1),(-1,0),(0,1),(1,0)]

    def expand(wh):
        wh2 = []
        for r in range(len(wh)):
            row = []
            for c in range(len(wh[0])):
                if wh[r][c] == '#':
                    row.append('#')
                    row.append('#')
                elif wh[r][c] == '.':
                    row.append('.')
                    row.append('.')
                elif wh[r][c] == 'O':
                    row.append('[')
                    row.append(']')
                elif wh[r][c] == '@':
                    row.append('@')
                    row.append('.')
            wh2.append(row)
        return wh2

    def make_move(m):
        d = dirs[moves.index(m)]
        new_pos = (pos[0]+d[0], pos[1]+d[1])
        queue = []
        if new_pos := push_cell('@', pos, d, queue):
            return new_pos
        else:
            # couldn't actually move, so rollback
            if DEBUG: print('rolling back the last', len(queue), moves)
            while queue:
                q = queue.pop()
                warehouse[q[1][0]][q[1][1]] = q[0]
                warehouse[q[2][0]][q[2][1]] = '.'
        return pos
    
    # push the piece and accumulate the moves
    # so we can rollback if it turns out a dud
    def push_cell(c, p, d, q):
        # next position
        np = ( p[0]+d[0], p[1]+d[1] )
        nc = warehouse[np[0]][np[1]]
        
        if DEBUG: print('push', c, 'at', p, 'to', np)

        if nc == '#': 
            if DEBUG: print('hit the wall at', np)
            return  
        
        if nc == '.':
            if DEBUG: print('empty cell at', np)

            # move
            warehouse[np[0]][np[1]] = c
            warehouse[p[0]][p[1]] = '.'
            q.append((c, p, np))

            # if it's a box and we are moving vertically
            # push the other piece too (if not moved already)
            if c in ('[',']') and d[0] != 0:
                other_p = (p[0], p[1] + (1 if c=='[' else -1) )
                other_c = warehouse[other_p[0]][other_p[1]]
                # if not moved already ...
                if other_c != '.':
                    # can we move this other piece in the same direction also ?
                    if DEBUG: print('try pushing', other_c, 'at', other_p, 'also')
                    if not push_cell(other_c, other_p, d, q):
                        # failed
                        return

            if DEBUG: print('moved', c, 'to', np)
            return np

        if push_cell(nc, np, d, q):
            if DEBUG: print('ok, now push', c, 'at', p, 'again')
            return push_cell(c, p, d, q)

    def find_robot():
        for r in range(len(warehouse)):
            for c in range(len(warehouse[0])):
                if warehouse[r][c] == '@':
                    return (r, c)

    def display():
        for r in range(len(warehouse)):
            line = []
            for c in range(len(warehouse[0])):
                line.append(warehouse[r][c])
            print(''.join(line))
    
    def checksum():
        gps_sum = 0
        for r in range(len(warehouse)):
            for c in range(len(warehouse[0])):
                if warehouse[r][c] in ('[', 'O'):
                    gps_sum += 100*r + c
        return gps_sum
    
    #part2 uses an expanded version
    if expanded: 
        warehouse = expand(warehouse)

    display()

    if ANIMATE: images = [create_bitmap(warehouse)]

    pos = find_robot()
    for i in range(len(itinerary)):
        if DEBUG: display()
        m = itinerary[i]
        pos = make_move(m)
        if ANIMATE: images.append(create_bitmap(warehouse))

    display()

    if ANIMATE: create_gif(images)

    return checksum()

def rect(pixels, x, y, sx, sy, color):
    for i in range(sx):
        for j in range(sy):
            pixels[sx*x+i, sy*y+j] = color

def create_gif(images):
    # get the current time to use in the filename
    timestr = time.strftime("%Y%m%d-%H%M%S")

    # calculate the frame number of the last frame (ie the number of images)
    last_frame = (len(images)) 

    # create 10 extra copies of the last frame (to make the gif spend longer on the most recent data)
    for x in range(0, 9):
        im = images[last_frame-1]
        images.append(im)

    # save as a gif   
    images[0].save(timestr + '.gif',
                save_all=True, append_images=images[1:], optimize=False, duration=300, loop=0)

def create_bitmap(wh):
    
    rows, cols = len(wh), len(wh[0])

    sx, sy = 2, 3
    img = Image.new( 'RGB', (cols*sx, rows*sy), "black") # Create a new black image
    pixels = img.load()
    for i in range(rows):
        for j in range(cols):
            if wh[i][j] == '@': 
                rect(pixels, j, i, sx, sy, (10, 200, 10))
            if wh[i][j] == '#': 
                rect(pixels, j, i, sx, sy, (200, 10, 10))
            elif wh[i][j] in ('O','['):
                rect(pixels, j, i, sx, sy, (10, 100, 100))
            elif wh[i][j] in (']'):
                rect(pixels, j, i, sx, sy, (10, 100, 200))
    return img

with open('day15-input.txt') as f:
    lines = [line.strip() for line in f.readlines() if not line.startswith('//')]
    #checksum = solve(lines)
    #print('day15 part1', checksum)
    
    checksum = solve(lines, expanded=True)
    print('day15 part2', checksum)
