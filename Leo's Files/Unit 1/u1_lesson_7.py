# Programming Unit 1

# --------------------- Lesson 7 ---------------------

"""
N-ary trees

We already know something about trees, while working with binary trees. Binary trees are nothing more than an N-ary tree
with only 2 branches per node. In other cases, trees have N branches, depending on the sort of tree.

Say that we have a list L = ["A", "B", "C"] and we want to see all the combinations that we can get with those 3 items:
our tree will look something like this:

""
 ├"A"
 | ├-"AB"
 | |  └---"ABC"
 | └-"AC"
 |    └---"ACB"
 ├"B"
 | ├-"BA"
 | |  └--"BAC"
 | └-"BC"
 |    └--"BCA"
 └"C"
   ├-"CA"
   |  └--"CAB"
   └-"CB"
      └--"CBA"

We have N! branches in an N-ary tree. In this case we have 3! branches, thus 3*2*1 = 6 branches.
Let's write a recursive function that:
- receives as input a list L of N characters;
- generates a game-tree in which:
  - each leaf is a combination of the N characters in L;
  - each intermediate node M contains a combination of a subset S of L, such that all the nodes in the game-tree
    starting from M are supersets of S;
  - the leaves contain all the possible combinations of the N characters.
For example, given L = ["a", "b", "c"], the function will compute and return the game-tree listed above
"""

class Node:
    def __init__(self, value):
        """
        Builds an N-ary tree with no children by default. A node value must be provided to initialize a tree.

        INPUTS:
         - value: It's the value of the node
        """
        self.value = value
        self.children = []

    def addChild(self, node_to_child) -> None:
        """
        Sets a node as a children of the tree

        INPUTS:
         - "node": It's the node that will be set as children of the tree itself"""
        self.children.append(node_to_child)

    def __repr__(self, prefix = ""):
        result = prefix + str(self.value) + "\n"
        for item in self.children:
            result += item.__repr__(prefix + "-|")
        return result


def createTree(nodeValue, childrenInList):
    node = Node(nodeValue)
    for i, item in enumerate(childrenInList):
        newnode = createTree(nodeValue )

def checkNode(node, L):
    nodeVal, out = node.value, []
    print(node.children)
    if nodeVal != "":
        for value in nodeVal:
            L.remove(value)
    for item in L:
        out.append(nodeVal + item)
    return out

def AllStrings(L: list):
    pass

if __name__ == "__main__":
    itemsInList = ["a", "b", "c", "d", "e"]

    aTree = createTree("", itemsInList)
    print(aTree)

    root = AllStrings(itemsInList)
    #print(root)