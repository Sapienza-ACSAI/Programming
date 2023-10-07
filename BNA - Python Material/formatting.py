
""" FORMATTING """

'{} {}'.format('one', 'two')
# output: 'one two'

print(*listname) # output: prints list without the []

M = [1, 2, 3] [100, 100, 100] [6.89, 9, 100]
print(*M, sep = '\n')
# output: prints each in new line

'''PADDING AND ALIGNING STRINGS'''

'{:>10}'.format('test') # output:       test (aligns left, fits in 10)
'{:^10}'.format('test') # output:   test    (aligns middle, fits in 10)

'''USING FORMATTING FOR MATRICES'''

def print_matrix(M):
    s="{:4}"*len(M[0])
    for row in M:
        print(s.format(*row))
        
# output is the perfectly aligned matrix 
#    1   2   3
#  100 100 100
# 6.89   9 100
