
"""THE BINARY TREE"""
# A binary tree is a recursive data structure

# Every node in a binary tree is a binary tree, a BINARY tree can have 0,1,2 child nodes

class BinaryTree:
    node, left, right, level = None, None, None, None
    
    def __init__(self, nodeval): # a constructor
        self.level = 0
        self.node = nodeval
    
    def SetLeft(self, leftnode):
        leftnode.level = self.level + 1
        self.left = leftnode
    def SetRight(self, rightnode):
        rightnode.level = self.level + 1
        self.right = rightnode
    
    def __repr__(self): # this is for printing the node
        res = str(self.node) + "\n"
        if self.left is not None:
            res += "--|" * self.left.level + self.left.__repr__()
        if self.right is not None:
            res += "--|" * self.right.level + self.right.__repr__()
        return res
        
# Let's create a 3-node structure

N0 = BinaryTree('a')
N1 = BinaryTree('b')
N2 = BinaryTree('c')

# Now to assemble them into a tree structure:

N0.SetLeft(N1)
N0.SetRight(N2)    # https://imgur.com/d9qYQYv