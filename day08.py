with open('day08-input.txt', 'r') as f:
    map = list([[c for c in line.strip()] for line in f.readlines()])
    
nrows = len(map)
ncols = len(map[0])
antens = [(map[row][col], row, col) for row in range(len(map)) for col in range(len(map[0])) if map[row][col]!='.']

antins = []
harmonics = True
for a in antens:
    for b in antens:
        if b == a: continue
        if b[0] != a[0]: continue
        h = 1  
        while True:
            d = h*(b[1]-a[1]), h*(b[2]-a[2])
            c = b[1]+d[0], b[2]+d[1]
            if c[0] > -1 and c[0] < nrows and c[1] > -1 and c[1] < ncols:
                antins.append(c)
            else:
                break
            if harmonics:
                h += 1
            else:
                break
        if harmonics:
            antins.append((a[1], a[2]))
            antins.append((b[1], b[2]))

print(sorted(set(antins)))
print ('day08 part-2 answer', len(set(antins)))
# 359 / 
