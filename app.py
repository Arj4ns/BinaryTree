
class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def binaryInsert(root, node):
    if(root == None):
        root = node
    else:
        if(root.data > node.data):
            if(root.left == None):
                root.left = node
            else:
                binaryInsert(root.left, node)
        else:
            if(root.right == None):
                root.right = node
            else:
                binaryInsert(root.right, node)

def printTree(node):
    if(node.left):
        printTree(node.left)
    print(node.data)
    if(node.right):
        printTree(node.right)

x = node(6)
binaryInsert(x, node(4))
binaryInsert(x, node(7))
binaryInsert(x, node(2))
binaryInsert(x, node(9))
binaryInsert(x, node(8))
binaryInsert(x, node(12))
binaryInsert(x, node(1))
binaryInsert(x, node(3))
binaryInsert(x, node(14))
binaryInsert(x, node(10))
binaryInsert(x, node(0))


printTree(x)

