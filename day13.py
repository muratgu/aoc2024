def solve(lines):

    def simulate(m):
        a, b = m['a']
        c, d = m['b']
        p, q = m['p']

        x = (p*b - q*b) // (a*b - a*d)
        y = (p*c - q*a) // (b*c - d*a)
        m['x'] = x
        m['y'] = y

        s = x*a + y*b
        t = x*c + y*d

        cost = x*3 + y

        return (p-s, q-t, cost)

    machines = []
    m = -1
    for line in lines:
        if line.startswith('Button A:'):
            x, y = line.split(',')
            x = x.split('+')[1]
            y = y.split('+')[1]
            machines.append({})
            m += 1
            machines[m]['a'] = (int(x), int(y))
        if line.startswith('Button B:'):
            x, y = line.split(',')
            x = x.split('+')[1]
            y = y.split('+')[1]
            machines[m]['b'] = (int(x), int(y))
        if line.startswith('Prize:'):
            x, y = line.split(',')
            x = x.split('=')[1]
            y = y.split('=')[1]
            #machines[m]['p'] = (int(x)+10000000000000, int(y)+10000000000000)
            machines[m]['p'] = (int(x), int(y))

    total = 0
    i = 0
    for m in machines:
        dx, dy, cost = simulate(m)
        #print(m['x'], m['y'], cost)
        if dx+dy==0:
            #print ('machine', i, cost)
            total += cost
        i += 1

    print('day13 part1', total)
    # 29201

with open('day13-input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)