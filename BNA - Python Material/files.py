

'''IN THE EXAMS, DONT FORGET TO ENCODE YOUR FILE IN UTF8'''
fileRef = open("filePath.txt", "w", encoding="utf8")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def readfile(filename):
  try:
    fileRef = open(filename, "r", encoding="utf8")
    print("hello")
    fileRef.close() # if you close a file, THEN you can re-open it
  except IOError:
    print("file does not exist")
    print("continue...")

readfile("nonexistent-filename.txt")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

