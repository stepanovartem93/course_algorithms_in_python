from binarytree import tree, bst, Node, build

class MyNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

a = tree(height=4, is_perfect=False) #create non ideal tree
print(a)

b = bst(height=3, is_perfect=True) #create ideal tree
print(b)

# самостоятельное создание дерева 1
c = Node(7) #корень
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
print(c)

# самостоятельное создание дерева 2
d = build([7, 3, 11, 1, 5, 9, 13, None, 8, None, 3])
print(d)