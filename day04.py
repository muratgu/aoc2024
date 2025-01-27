def solve(lines):
    part1, part2 = 0, 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            part1 += scan_for(lines, 'XMAS', x, y)
            part2 += scan_for_mas(lines, x, y)
    print('day04 part1', part1)
    print('day04 part2', part2)

def scan_for(lines, word, x, y):
    
    def clamp(v, minv, maxv):
        return -1 if v < minv or v > maxv else v

    def scan_dir(dx, dy):
        for i in range(len(word)):
            x0, y0 = clamp(x+dx*i, 0, mx), clamp(y+dy*i, 0, my)
            if x0<0 or y0<0 or lines[y0][x0] != word[i]: 
                return 0
        return 1 
    
    found = 0
    mx = len(lines[0]) - 1
    my = len(lines) - 1
    rangex, rangey = [1, 0, -1], [0, 1, -1]
    for dx in rangex:
        for dy in rangey:
            if dx == 0 and dy == 0: continue
            found += scan_dir(dx, dy)   
    return found

# part 2: scan for X-MAS
def scan_for_mas(lines, x, y):
    
    def clamp(v, minv, maxv):
        return -1 if v < minv or v > maxv else v

    mx = len(lines[0]) - 1
    my = len(lines) - 1

    n = 0
    s = lines[y][x]
    x0, y0 = clamp(x-1, 0, mx), clamp(y-1, 0, my)
    if x0>-1 and y0>-1: s += lines[y0][x0]
    x0, y0 = clamp(x+1, 0, mx), clamp(y+1, 0, my)
    if x0>-1 and y0>-1: s += lines[y0][x0]
    if s == 'AMS' or s == 'ASM': n += 1

    s = lines[y][x]
    x0, y0 = clamp(x+1, 0, mx), clamp(y-1, 0, my)
    if x0>-1 and y0>-1: s += lines[y0][x0]
    x0, y0 = clamp(x-1, 0, mx), clamp(y+1, 0, my)
    if x0>-1 and y0>-1: s += lines[y0][x0]
    if s == 'AMS' or s == 'ASM': n += 1

    return 1 if n == 2 else 0
    
with open('day04-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)