import itertools

def test_calc(target, source, ops):
    result = int(source[0])
    for i in range(1, len(source)):
        if ops[i-1] == '*': 
            result *= int(source[i])
        elif ops[i-1] == '+':
            result += int(source[i])
        elif ops[i-1] == '|':
            result = int(str(result) + source[i])
    return 'SUCCESS' if result == int(target) else 'FAILED', result

def solve(lines):
    lines = [list(line.strip().split(' ')) for line in lines]
    table = []
    for line in lines:
        table.append({ 
            'target': line[0].removesuffix(':'),
            'source': [d for d in line if not d.endswith(':')]        
        })

    totals = 0
    for item in table:
        op_kinds = ['*', '+']
        all_ops = list(itertools.product(op_kinds, repeat=len(item['source'])-1))
        for ops in all_ops: 
            result, total = test_calc(item['target'], item['source'], ops)
            if result == 'SUCCESS':
                #print(item['target'], item['source'], ops, total)
                totals += total 
                break
    print('day07 part1', totals)

    totals = 0
    for item in table:
        op_kinds = ['*', '+', '|']
        all_ops = list(itertools.product(op_kinds, repeat=len(item['source'])-1))
        for ops in all_ops: 
            result, total = test_calc(item['target'], item['source'], ops)
            if result == 'SUCCESS':
                #print(item['target'], item['source'], ops, total)
                totals += total 
                break
    print('day07 part2', totals)

with open('day07-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)