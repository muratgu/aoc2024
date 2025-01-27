def solve(lines):
    # a is sorted
    def count(v, a):
        n = 0
        for x in a:
            if x == v: n += 1
            if int(x) > int(v): return n

    a, b = zip(*[line.split() for line in lines])
    a, b = sorted(a), sorted(b)
    
    print('day01 part1', sum( [ abs(int(x[0])-int(x[1])) for x in zip(a,b)] ))
    print('day01 part2', sum( [int(x) * count(x, b) for x in a] ))

with open('day01-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)