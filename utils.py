def display(maze):
    for i in range(len(maze)):
        line = []
        for j in range(len(maze[0])):
            line.append(maze[i][j])
        print(''.join(line))

def bitmap(maze):
    from PIL import Image
    rows, cols = len(maze), len(maze[0])
    sx, sy = 2, 3
    img = Image.new( 'RGB', (cols*sx, rows*sy), "black")
    pixels = img.load()
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S': 
                rect(pixels, j, i, sx, sy, (10, 100, 200))
            elif maze[i][j] == 'E': 
                rect(pixels, j, i, sx, sy, (10, 200, 10))
            elif maze[i][j] == '#': 
                rect(pixels, j, i, sx, sy, (200, 100, 10))
    return img

def rect(pixels, x, y, sx, sy, color):
    for i in range(sx):
        for j in range(sy):
            pixels[sx*x+i, sy*y+j] = color

