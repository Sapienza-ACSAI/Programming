# Programming Unit 2

# --------------------- Lesson 15 ---------------------

import images

class pixel:
    def __init__(self, row: int, column: int, colour=None):
        """Creates a new pixel object with 2 data input:
        - a ROW integer;
        - a COLUMN integer."""
        if isinstance(row, int) and isinstance(column, int):
            self.row, self.column = row, column
        else:
            raise TypeError("A pixel needs 2 coordinates X and Y, and they must be integers")
        if isinstance(colour, tuple):
            self.colour = colour
        else:
            raise ValueError("The colour must be expressed as a (RRR, GGG, BBB) tuple")

    def get_neighbours(self):
        """Returns the neighbours of the pixel"""
        neighbours = {pixel(self.row + y, self.column + x) for x in range(-1, 2) for y in range(-1, 2)
                      if (y, x) != (0, 0)}
        return neighbours

    def distance(self, pixel2):
        """Returns the distance between the pixel and a second pixel"""
        return (((self.row - pixel2.row)**2)+(self.column - pixel2.column)**2)**(1/2)

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def __str__(self):
        return f"P:[{self.row}, {self.column}]"

    def __repr__(self):
        return self.__str__()

class image:
    def __init__(self, height: int, width: int, bgcolor: (int, int, int), filename=None):
        """Create an Image object with 3 necessary and 1 optional data input:
        - an HEIGHT;
        - a WIDTH;
        - a BACKGROUND COLOR

        - a FILENAME (it's not mandatory, you may omit it. It must be specified in case of saving the image)"""
        self.img, self.h, self.w = [[bgcolor] * width for _ in range(height)], height, width
        if filename:
            self.filename = filename
        else:
            self.filename = None

    def save(self, filename=None):
        if filename:
            images.save(self.img, filename)
        elif self.filename:
            images.save(self.img, self.filename)
        else:
            raise NameError("No filename parameter was given")

    def draw(self, obj, colour: (int, int, int)):
        if isinstance(obj, pixel):
            self.img[obj.row][obj.column] = colour
        elif isinstance(obj, rectangle):
            for row_loop in range(obj.pixel1.get_row(), obj.pixel2.get_row() + 1):
                for column_loop in range(obj.pixel1.get_column(), obj.pixel2.get_column() + 1):
                    self.img[row_loop][column_loop] = obj.colour

class rectangle:
    def __init__(self, pixel1, pixel2, colour=None):
        if isinstance(pixel1, pixel) or isinstance(pixel2, pixel):
            self.pixel1, self.pixel2, self.colour = pixel(min(pixel1.get_row(), pixel2.get_row()),
                                                          min(pixel1.get_column(), pixel2.get_column())),\
                                                    pixel(max(pixel1.get_row(), pixel2.get_row()),
                                                          max(pixel1.get_column(), pixel2.get_column())),\
                                                    colour if colour else pixel1.colour

    def height(self):
        return abs(self.pixel1.get_row() - self.pixel2.get_row())

    def width(self):
        return abs(self.pixel1.get_column() - self.pixel2.get_column())

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (2 * self.height()) + (2 * self.width())

    def area(self):
        """Returns the area of the rectangle"""
        return self.height() * self.width()

myImage = image(150, 150, (0, 128, 128), "test.png")

p1, p2 = pixel(100, 50, (255, 255, 255)), pixel(50, 10, (255, 255, 255))

myRectangle = rectangle(p1, p2, (128, 0, 128))

myImage.draw(myRectangle, (128, 0, 128))
