def solve(lines):

    pvs = [line.split(' ') for line in lines]
    ps = [tuple(int(v) for v in pv[0].split('=')[1].split(',')) for pv in pvs]
    vs = [tuple(int(v) for v in pv[1].split('=')[1].split(',')) for pv in pvs]
    robots = list(zip(ps, vs))
    
    width, height = (101, 103)

    i = 0
    while True:
        simulate(robots, width, height, 1)
        cluster_size = find_cluster_max(robots, width, height)        
        if cluster_size > 100:
            maxi = i
            maxn = cluster_size
            display(robots, width, height)        
            print(maxi, maxn)
            exit()
        i+=1

def calc_risk(robots, width, height):
    w, h = (width // 2, height // 2)
    dw, dh = (width % 2, height % 2)
    quads = [ ( 0   , 0    ), ( w+dw, 0    ), 
              ( 0   , h+dh ), ( w+dw, h+dh ) ]
    risk = 1
    for q in quads:
        qx, qy = q
        n = 0
        for r in robots:
            px, py = r[0]
            if qx <= px < qx+w \
           and qy <= py < qy+h:
                n += 1
        risk *= 1 if n == 0 else n
    return risk
            
def simulate(robots, width, height, steps):
    for i in range(len(robots)):
        r = robots[i]
        p, v = r
        robots[i] = ( (((p[0] + v[0]*steps) % width), ((p[1] + v[1]*steps) % height)), v )
    return 

def find_cluster_max(robots, width, height):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    occupied = set([r[0] for r in robots])
    visited = set()
    clusters = []

    def bfs(start):
        cluster = set()
        queue = [start]
        visited.add(start)
        while queue:
            x,y = queue.pop(0)
            cluster.add((x,y))
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if (nx,ny) in occupied and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    queue.append((nx,ny))
        return cluster
    maxn = 0
    for cell in occupied:
        if cell not in visited:
            cluster = bfs(cell)
            if len(cluster) > maxn:
                maxn = len(cluster)
    return maxn

def display(robots, width, height):
    print()
    for h in range(height):
        line = []
        for w in range(width):
            n = sum([1 for r in robots if r[0] == (w,h)])
            line.append('.' if n == 0 else str(n))
        print(''.join(line))

with open('day14-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    print(solve(lines))

