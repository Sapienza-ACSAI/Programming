
import images
# ------------------- Exercises for Wednesday 23/11 on Q2A

# Write the following functions:
# v_flip(img) that returns a copy of the image img flipped w.r.t. the vertical axis

img = images.load('testimage.png')
img2 = images.load('smiley.png')

def v_flip(img):
    new_img = []
    for row in img:
        new_img.append(list(reversed(row)))
    return new_img


def v_flip(img):
    return [row[x] for x in range(len(img)-1, -1, -1) for row in img]


# h_flip(img) that returns a copy of the image img flipped w.r.t. the horizontal axis

def h_flip(img):
    new_img = []
    for row in reversed(img):
        new_img.append(row[:])
    return new_img

# rotate_90(img) that returns a copy of the image rotated by 90 degrees


def rotate_90(img):
    new_img = []
    for col in range(len(img[0])):
        new_row = []
        for row in range(len(img)-1, -1, -1):
            new_row.append(img[row][col])
        new_img.append(new_row)
    return new_img    
    
    
# draw_filled_rect(img, x1, y1, x2, y2, color) that draws an filled rectangle of color color defined by the corners x1,y1 and x2,y2

def draw_filled_rect(img, x1, y1, x2, y2, color):
    if x1 > x2:
        x2, x1 = x1, x2
    if y1 > y2:
        y2, y1 = y1, y2
#    x1, x2 = min(x1, x2), max(x1, x2)
#    x1, x2 = sorted((x1, x2))
#    x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
       
    for x in range(x1, x2):
        for y in range(y1, y2):
            img[x][y] = color
    return img


# draw_rect(img, x1, y1, x2, y2, color) that draws an empty rectangle of color color defined by the corners x1,y1 and x2,y2

def draw_rect(img, x1, y1, x2, y2, color):
    if x1 > x2:
        x2, x1 = x1, x2
    if x1 < 0:
        x1 = 0
    elif x1 > len(img):
        x1 = len(img)-1
#    if x2 < 0:
#        x2 = 0
#    elif x2 > len(img):
#        x2 = len(img)-1
    if y1 > y2:
        y2, y1 = y1, y2
#    if y1 < 0:
#        y1 = 0
#    elif y1 > len(img):
#        y1 = len(img)-1
#    if y2 < 0:
#        y2 = 0
#    elif y2 > len(img):
#        y2 = len(img)-1
#    x1, x2 = min(x1, x2), max(x1, x2)
#    x1, x2 = sorted((x1, x2))
#    x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
       
    for x in (min(max(0,x1), len(img)-1),min(x2, len(img))):
        for y in range(y1, y2+1):
            img[x][y] = color
#        for y in range(y1, y2):
#            img[x1][y] = color
#            img[x2][y] = color
#        img[x1][y1:y2] = [color]*(y2-y1)
#        img[x2][y1:y2] = [color]*(y2-y1)
        
    for x in range(min(max(0,x1), len(img)-1), min(x2, len(img))):
        img[x][y1] = color
        img[x][y2] = color
    return img


images.save(v_flip(img), 'vflipped.png')
images.save(h_flip(img), 'hflipped.png')
images.save(rotate_90(img), 'rotate90.png')
images.save(draw_filled_rect(img2, 10, 9, 30, 39, (0, 162, 232)), 'smiley-rect.png')
images.save(draw_rect(img2, 10, 9, 30, 39, (0, 162, 232)), 'smiley-emptyrect.png')

# draw rect is doing filled

