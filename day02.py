
def copy_except(a, i):
    if i < 0 or i > len(a)-1:
        return []
    copied = []
    for j in range(len(a)):
        if j != i: copied.append(a[j])
    return copied

def is_safe(r, exclude = -1, retry = None):
    if len(r) == 0:
        return 0
    if exclude > -1:
        r = copy_except(r, exclude)
    diff = 0
    for i in range(len(r) - 1):
        prev_diff = diff
        diff = int(r[i]) - int(r[i+1])
        if abs(diff) > 3 \
           or diff == 0 \
           or diff > 0 and prev_diff < 0 \
           or diff < 0 and prev_diff > 0:
            if retry and (is_safe(r, i) or is_safe(r, i+1) or is_safe(r, i-1)):
                return 1
            else: 
                return 0
    return 1

with open("day02-input.txt", "r") as f:
    lines = f.readlines()
    levels = [line.split() for line in lines]
    success = [is_safe(x) for x in levels]
    print('day02 part-1 answer = ', sum(success))
    # 299
    success = [is_safe(x, retry = True) for x in levels]
    print('day02 part-2 answer = ', sum(success))
    # 364
