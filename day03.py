def solve(lines):
    lines = ''.join(lines)
    i = 0
    sum1, sum2 = 0, 0 
    while True:        
        j = lines.find('mul(', i)
        if j > -1:
            i = j + 4
            j = lines.find(',', i)
            if j > -1:
                num1s = lines[i:j]
                try:
                    num1 = int(num1s)
                    if str(num1) == num1s:
                        i = j + 1
                        j = lines.find(')', i)
                        if j > -1:
                            num2s = lines[i:j]
                            try:
                                num2 = int(num2s)
                                if str(num2) == num2s:
                                    sum1 += num1*num2
                                    if is_enabled_at(lines, j):
                                        sum2 += num1*num2
                                    i = j + 1
                            except:
                                pass
                except:
                    pass
            else:
                break
        else:
            break
    print('day03 part1', sum1)
    print('day03 part2', sum2)

def is_enabled_at(s, i):
    j = s.rfind('do()', 0, i)
    k = s.rfind('don\'t()', 0, i)
    if k > -1 and k > j: 
        return False
    return True

with open('day03-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)

