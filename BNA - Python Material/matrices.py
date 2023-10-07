
M = [[1,-1, 3],[2, 4, -2],[9, 1, 5],[-5, 2, 8]]

def matrix_dimensions(M):
    return 'Rows:' + str(len(M)) + '\n' + 'Columns:' + str(len(M[0]))

print(matrix_dimensions(M))

def print_matrix(M):
    s = "{:4}"*len(M[0]) # this creates a string (used for formatting)
    # check python 3 formatting online for more examples
    for row in M:
        print (s.format(*row))

print_matrix(M)

def create_matrix(r, c, val):
    return [[val]*c for _ in range (r)]

            # OR → THE LONGER WAY
            
            # matrix = []
            # for row_n in range(r):
            #     row = []
            #     for col_n in range(c):
            #         row.append(val)
            #     matrix.append(row)
            # return matrix

print(create_matrix(5, 3, 0))
print_matrix(create_matrix(5, 3, 0))

# - - - - - - - - - - - - - - - - - - - - - - - 

import images

images.save(M2, 'first.png')