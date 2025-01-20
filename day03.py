def is_enabled_at(s, i):
    j = s.rfind('do()', 0, i)
    k = s.rfind('don\'t()', 0, i)
    if k > -1 and k > j: 
        return False
    return True

with open("day03-input.txt", "r") as f:
    lines = ''.join(f.readlines())
    i = 0
    sum = 0 
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
                                    #print('mul2(', num1, num2)
                                    if is_enabled_at(lines, j):
                                        sum += num1*num2
                                    i = j + 1
                            except:
                                #print (num2s, ' is corrupt')                
                                pass
                except:
                    #print (num1s, ' is corrupt')                
                    pass
            else:
                break
        else:
            break
    print('sum=', sum)
    # 56275602