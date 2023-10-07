
import images

class Pixel:
    # A method is a function defined in a class
    
    # init is a constructor, it forms the basis for the class
    def __init__(self, row, col, color):
        # Checking if given is a number (use type or isinstance)
        if isinstance(row, int) and isinstance(col, int):
            self.row = row
            self.col = col
            self.color = color
        else:
            raise TypeError("Input is not integer")
    
    def get_col(self):
        return self.col
    
    def get_row(self):
        return self.row
    
    def get_neighbors(self):
        return {(self.col+x,self.row+y) for x in range(-1, 2) for y in range(-1, 2) if (y,x) != (0, 0)}
    
    def __str__(self):
        return f"Pixel({self.row}, {self.col})"
    
    # Repr is what the function returns 
    def __repr__(self):
        return self.__str__()
    
    # Finding the distance between 2 pixels using the pythagorean theorem
    def distance(self, pixel):
        s1 = (self.row - pixel.row)**2
        s2 = (self.col - pixel.col)**2 '''Question, how does pixel.row/col form??'''
        return (s1 + s2)**0.5
        
class Image:
    
    def __init__(self, height, width, bgcolor, filename = None):
        self.img = [[bgcolor]*width for _ in height]
        self.h = height
        self.w = width
        if filename:
            self.filename = filename
        else:
            self.filename = None
            
    def save(self, filename = None):
        if filename:
            images.save(self.img, filename)
        elif self.filename:
            images(self.img, filename) '''Question, what does the elif part do??'''
        else:
            raise Exception("The image does not have a filename to save")
        
    def draw(self, o):
        if isinstance (o, Pixel):
            self.img[o.row][o.col] = o.color
        if isinstance(o, Rectangle):
           for row in range(o.p1.get_row(), o.p2.get_row()+1):
               for col in range(o.p1.get_col(), o.p2.get_col()+1):                  
                   self.img[row][col] = o.color
           
class Rectangle:

    def __init__(self, p1, p2, color = None):
        if not isinstance(p1, Pixel) or not isinstance(p2, Pixel):
            raise TypeError("Rectangle needs two pixels")
            
        self.p1 = Pixel(min(p1.get_row(), p2.get_row()), min(p1.get_col(), p2,get_col())) '''why min?'''
        
        self.p2 = Pixel(max(p1.get_row(), p2.get_row()), max(p1.get_col(), p2,get_col()))  '''why max?'''
        
        self.color = color if color else p1.color
    
    def height(self):
        # Abs of difference between rows of two points, use get_row from class Image
        return abs(self.p1.get_row() - self.p2.get_row())
    
    def width(self):
        # Abs of difference between cols of two points, use get_col from class Image
        return abs(self.p1.get_col() - self.p2.get_col())
    
    def perimeter(self):
        return 2*self.width() + 2*self.height()
    
    def area(self):
        return self.width() * self.height()
    
    
            
            
            
            