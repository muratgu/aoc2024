#
# adventofcode day 9
#

# 2333133121414131402
# 00...111...2...333.44.5555.6666.777.888899
# 0099811188827773336446555566..............
# 0099811188827773336446555566..............
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
        end = scan_end(lo, end)
        if (start == -1 or start > end):
            break
        lo[start], lo[end] = lo[end], lo[start]
    return lo

def scan_start(lo, start):
    while True:
        if lo[start] == '.':
            return start
        start += 1
        if start >= len(lo):
            return -1 
    
def scan_end(lo, end):
    while True:
        if lo[end] != '.':
            return end
        end -= 1
        if end < 0:
            return -1 
    
input_txt = 'day09-input.txt'
with open(input_txt, 'r') as f:
    diskmap = [int(c) for c in f.readline()]
    lo = layout(diskmap)
    #lo = defrag(lo)
    #cs = checksum(lo)
    #print('day09 part-1 answer', cs)
    # 6385338159127

part2_test = '00992111777.44.333....5555.6666.....8888..'
lo = [c for c in '00992111777.44.333....5555.6666.....8888..']
print(lo)
print(checksum(lo))

    
