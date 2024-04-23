from tree import Tree
from node import Node

tree = Tree()

tree.add(4)
tree.add(2)
tree.add(6)
tree.add(1)
tree.add(3)
tree.add(5)
tree.add(7)

tree.printTree()
print()
tree.printTree(order='postorder')
print()
tree.printTree(order='preorder')