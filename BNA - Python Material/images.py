

'''IMAGES'''

import png

img = create_matrix(100, 100, (255, 0, 255) ) #purple
images.save(img, 'insertimagename.png')

# we just created a 100x100 image full of purple
# now we can change rows and columns to other colors

img[0] = [(255, 0, 255)] * len(img) # first row now yellow

def draw_line(img, color): # generalized version
    img[row] = [color] * len(img) 
    
'''you have to save the image each time to see the result!'''

def draw_line(img, color): # lets do this for columns
    img[row] = [color] * len(img)

def draw_col(img, col, color):
    for row in range(len(img)):
       img[row][col] = [color] * len(img) 