def solve(lines):
    rules = []
    pages = []
    i = 0
    while len(lines[i].strip()) > 0:
        rules.append([int(y) for y in lines[i].strip().split('|')])
        i += 1
    i+=1
    pagelist = [[int(y) for y in line.strip().split(',')] for line in lines[i:]]

    checksum = 0
    failedlist = []
    passedlist = []

    for pages in pagelist:
        if find_conflict(pages, rules):
            failedlist += [pages]
        else:
            passedlist += [pages]
            
    print('day05 part1', sum(mid_page(p) for p in passedlist))

    fixedlist = []
    for pages in failedlist:
        while True:
            conflict = find_conflict(pages, rules)
            if conflict:                
                pages = rearrange(pages, conflict)                
            else:
                break
        fixedlist += [pages]

    for fixed in fixedlist:
        if find_conflict(fixed, rules):
            raise 'failed to resolve conflicts'

    print('day05 part2', sum([mid_page(p) for p in fixedlist]))

def find_conflict(pages, rules):
    for i in range(len(pages)):
        page = pages[i]
        rlist = [r[1] for r in rules if r[0] == page]
        if len(rlist) > 0:
            for r in rlist:
                try: 
                    p2 = pages.index(r)
                    if i > p2: 
                        return (i, p2)
                except: 
                    pass 
    return None

def mid_page(pages):
    return pages[len(pages) // 2]

def rearrange(pages, pair):
    i, j = pair
    # i is found after j, i.e.  ...j..i...
    # swap elements to make it  ...i..j...
    if j == 0:
        pages = [pages[i]] + pages[j:i] + pages[i+1:]
    else:
        pages = pages[:j] + [pages[i]] + pages[j:i] + pages[i+1:]
    return pages

with open('day05-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)