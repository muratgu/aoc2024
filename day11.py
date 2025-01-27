def solve(lines):

    m = {}
    def evolve(stone, n):
        if n < 1:
            return 1
        elif (stone, n) in m:
            return m[(stone, n)]
        elif stone == 0:
            next_num = 1
            val = evolve(next_num, n-1)
        elif len(str_stone := str(stone)) % 2 == 0:
            next_num1 = int(str_stone[0:len(str_stone)//2])
            next_num2 = int(str_stone[len(str_stone)//2:])
            val = evolve(next_num1, n-1) + evolve(next_num2, n-1)
        else:
            next_num = stone * 2024
            val = evolve(next_num, n-1)
        m[(stone, n)] = val
        return val

    stones = [int(c) for c in lines[0].split()]
    total = 0
    for stone in stones:
        total += evolve(stone, 25)

    print(total)
    print('day11 part1', total)

    total = 0
    for stone in stones:
        total += evolve(stone, 75)
    print('day11 part2', total)


with open('day11-input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)
