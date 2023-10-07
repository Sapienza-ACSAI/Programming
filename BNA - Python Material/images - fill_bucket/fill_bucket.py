
import images
"""
Write a function that takes an image as a list of lists as an input and a x, y pair representing a point into the image, and a color and fills the area between the border of a non-black color within the image with the color. ->     Fill_bucket
"""
img = images.load('bucketsample.png')

def neighbor(img, x, y, background):
    to_fill = set()
    for x, y in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
        if 0 <= x < len(img[0]) and 0 <= y < len(img) and img[y][x] == background:
        # not equal to len bc. we start from zero, len would be out of range
        # img[0] for xbecause x is for # of items in a list in img
        # img for y y is for len of # of lists in img
            to_fill.add((y,x))
    return to_fill
            
def fill_bucket(img, x, y, color):
    background = img[y][x]
    to_fill = set()
    to_fill.add((y,x)) # we add the tuple of y and x to to_fill
    while to_fill: # while the set to_fill is not zero
        y, x = to_fill.pop() # random element from set
        if img[y][x] == background:
           img[y][x] = color
#       to_fill = to_fill.union(neighbor(img, x, y))
        to_fill.update(neighbor(img, x, y, background))
    
# start from one point and consider the background color
# we look for the point that is in every direction from the point

fill_bucket(img, 51, 23, (255, 0, 0))
images.save(img, 'new1.png')