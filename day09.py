def solve(lines):

    def layout(m):
        lo = [] 
        for i in range(len(m) // 2):
            lo += int(m[i*2]) * [str(i)]
            lo += int(m[i*2+1]) * ['.']
        if len(m) % 2 == 1:
            i = len(m)-1
            lo += int(m[i]) * [str(i // 2)]
        return lo

    def checksum(lo):
        result = sum([i*int(c) for i,c in enumerate(lo) if c!='.'])
        return result

    def defrag(lo):
        start = 0
        end = len(lo) - 1
        while True:
            start = scan_start(lo, start)
            end, _ = scan_end(lo, end)
            if (start == -1 or start > end):
                break
            lo[start], lo[end] = lo[end], lo[start]
        return lo

    def defrag2(lo):
        end = len(lo) - 1
        while True:
            end, n = scan_end(lo, end)
            if end < 0: 
                break
            start = scan_start(lo, 0, size=n)
            if (start == -1 or start > end):
                pass
            else:
                for i in range(n):
                    lo[start+i], lo[end-i] = lo[end-i], lo[start+i]
            end -= n
        return lo

    def scan_start(lo, start, size=1):
        while True:
            if lo[start] == '.':
                i = 0
                while start+i < len(lo) and lo[start+i] == '.':
                    i += 1
                    if i == size:
                        return start
            start += 1
            if start >= len(lo):
                return -1
    
    def scan_end(lo, end):
        while True:
            if lo[end] != '.':
                i = 0
                while end-i >= 0 and lo[end-i] == lo[end]:
                    i += 1
                if end-i >= 0:
                    return end, i     
            end -= 1
            if end < 0:
                return -1, -1 
    
    diskmap = [int(c) for c in lines[0]]
    lo = layout(diskmap)
    lo = defrag(lo)
    cs = checksum(lo)
    print('day09 part1', cs)

    lo = layout(diskmap)
    lo = defrag2(lo)
    cs = checksum(lo)
    print('day09 part2', cs)

with open('day09-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    solve(lines)    
