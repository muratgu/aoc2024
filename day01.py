#day01.py

# a is sorted
def count(v, a):
    n = 0
    for x in a:
        if x == v: n += 1
        if int(x) > int(v): return n

with open('day01-input.txt', 'r') as f:
    lines = f.readlines()
    a, b = zip(*[line.split() for line in lines])
    a, b = sorted(a), sorted(b)
    c = sum( [ abs(int(x[0])-int(x[1])) for x in zip(a,b)] )
    print('day01 part-1 answer = ', c)
    # 1110981

    d = sum([int(x) * count(x, b) for x in a])
    print('day01 part-2 answer = ', d)
    # 24869388



