
# Write the following functions:
import images
img = images.load("res-initial.png")
# draw_square(img, x, y, side, color, fill_color=None) that draws a square of the given side and color. If fill_color is different from None, the function fills the square with the given color.

def draw_square(img, x, y, side, color, fill_color=None):
    # keep in mind that you draw half the square if it goes over
    
    for i in range(x, min(x+side+1, len(img[0]))):
        # draw top horizontal side
        img[y][i] = color 
        # draw bottom horizontal side ONLY IF IT'S IN THE IMAGE
        if y+side < len(img)-1:
            img[y+side][i] = color
        
    # draw columns
    for j in range(y, min(y+side++1, len(img))):
        img[j][x] = color
        
        if x+side < len(img[0]):
            img[j][x+side] = color
    
    # if fill color is available → draw all lines inbetween
    if x < 0:
        x = -1
    if fill_color:
        for j in range(y+1, min(y+side, len(img))):
            for i in range(x+1, min(x+side, len(img[0]))):
                img[j][i] = fill_color

# count_crosses(img_file) that takes as input a filename with a PNG image with a black background and several horizontal and vertical white lines and returns the number of pixels that are crossed between a horizontal and a vertical white line.

def count_crosses(img_file):
    '''idea for this exercise:
        after detecting the lines, put the positions in a list
        check if a point is in both lists'''
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    
    pass

# longer_segment(img_file) that takes as input a filename with a PNG image with a black background and several white paths and returns the length of the longest white path.

def follow_the_line(img, x, y):
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    neighbours = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    to_follow = set()
    to_follow.add((x,y))
    count == 0
    
    while to_follow:
        x, y = to_follow.pop() # similar to the bucket, we get a random point
        count += 1
        img[y][x] = black # we dye it so that we don't count it again
        for i, j in neighbours:
            try:
                if img[j][i] == white:
                    to_follow.add((i,j))
            except IndexError:
                pass
    return count

def longer_segment(img_file):
    white = (255, 255, 255)
    
    img = images.load(img_file)
    max_len = 0
    
    for j in range(len(img)):
        for i in range(len(img[0])):
            if img[j][i] == white:
                length = follow_the_line(img, i, j)
                if length > max_len:
                    max_len = len
    return max_len
    
    
    
draw_square(img, -100, 55, 25, (255,0,0), (0,255,0))
images.save(img, 'square-drawn.png')

longer_segment("exerciseimage.png")
