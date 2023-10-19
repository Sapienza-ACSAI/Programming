# Programming Unit 1

# --------------------- Lesson 6 ---------------------

"""
Binary Trees are nodes which can have 0, 1 or 2 child / children. Each child node can be, or it is, a binary tree.
Nodes cannot be shared with other nodes. Binary trees are recursive
"""

class binaryTree:
    node, left, right, level = None, None, None, None

    def __init__(self, node_value: int):
        self.node, self.level = node_value, 0

    def setRight(self, right_value):
        right_value.level = self.level + 1
        self.right = right_value

    def setLeft(self, left_value):
        left_value.level = self.level + 1
        self.left = left_value

    def __repr__(self):
        output = f"{self.node}\n"
        if self.left is not None:
            output += f"{' ' * self.left.level}├-[L]: {self.left}"
        if self.right is not None:
            output += f"{' ' * self.right.level}└-[R]: {self.right}"
        return output

tree0 = binaryTree(5)
tree1 = binaryTree(2)
tree2 = binaryTree(3)
tree3 = binaryTree(15)
tree4 = binaryTree(32)
tree5 = binaryTree(21)

tree1.setRight(tree2)
tree1.setLeft(tree3)

tree0.setLeft(tree1)
tree0.setRight(tree4)

'''
5
 L_ Left: 2
    L_ Left: 15
    L_ Right: 3
 L_ Right: 32
'''

print(tree0)
print(f"Level of tree {tree2.level}")