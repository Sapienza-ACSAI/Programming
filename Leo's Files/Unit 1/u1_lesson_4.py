# Programming Unit 1

# --------------------- Lesson 4 ---------------------

# write function that loads an image from a file whose name is passed as a parameter
# and counts and returns the number of red pixels in the image

# a red pixel is defined as a pixel P whose color code is in the range:
# (127, 0, 0) < color(P) < (255, 32, 32)

import pngmatrix

def CountRedPixels(filename : str) -> int:
  redCount = 0
  image = pngmatrix.load_png8(filename)
  for line in image:
    for pixel in line:
      print(pixel)
  pass

if __name__ == "__main__":
  print(CountRedPixels("red-pixel-background.png")) # 58272
#-----------------------------------------------------------------------------------

# task 1: write a function that rotates an image provided by parameter by 90 degrees
# clockwise; the function modifies the image in-place, so it does not
# return anything

# task 2: write a function that rotates an image provided by parameter by 90 degrees
# clockwise; the function modifies the image in-place, so it does not
# return anything; you cannot allocate any auxiliary image inside the function!

import pngmatrix


def RotateImage_task1(image: list) -> None:
    print("-----Starting...-----")
    newImg, tempLine = [], []
    print(f"IMG Size: {len(image[0])}x{len(image)}")
    for index, line in enumerate(image):
        for i in range(len(image[0])):
            tempLine.append(line[i])
        newImg.insert(0, tuple(tempLine))
        tempLine = []
    print(f"New IMG Size: {len(newImg[0])}x{len(newImg)}")
    pngmatrix.save_png8(tuple(newImg), "result3.png")
    print("-----Image ready-----")
    # print(newImg)
    pass


def RotateImage_task2(image: list) -> None:
    print("-----Starting...-----")
    width, height = len(image[0]), len(image)
    print(f"IMG Size: {width}x{height}")
    auxImg = [[(0, 0, 0) for i in range(width)] for k in range(height)]
    # for X in range
    pngmatrix.save_png8(tuple(auxImg), "result3.png")
    print("-----Image ready-----")
    pass


if __name__ == "__main__":
    img = pngmatrix.load_png8("Shape+Square+Clipart-881591175.png")
    # RotateImage_task1(img)
    # pngmatrix.save_png8(img, "result1.png")
    RotateImage_task2(img)
    # pngmatrix.save_png8(img, "result2.png")
