#Program 5
#Binary Tree
#Sneha Patel
#Nov 13, 2023


from BT import binaryTree
from binNode import binNode


# Create nodes with data
node1 = binNode(10)
node2 = binNode(5)
node3 = binNode(15)
node4 = binNode(3)
node5 = binNode(7)
node6 = binNode(12)
node7 = binNode(18)
node8 = binNode(19)

# Create a binary tree
my_tree = binaryTree()
my_tree1 = binaryTree()
my_tree2 = binaryTree()

# Insert nodes into the tree
my_tree.insert(node1)
my_tree.insert(node2)
my_tree.insert(node3)
my_tree.insert(node4)
my_tree.insert(node5)
my_tree.insert(node6)
my_tree.insert(node7)
my_tree.insert(node8)

my_tree2.insert(binNode("D"))
my_tree2.insert(binNode("B"))
my_tree2.insert(binNode("C"))
my_tree2.insert(binNode("S"))
my_tree2.insert(binNode("P"))

# Print the tree structure
print("Binary Tree 1 Structure:")
print(my_tree)

print("Binary Tree 2 Structure:")
print(my_tree1)
print(my_tree.getSize())
print()

print("Binary Tree 3 Structure:")
print(my_tree2)

# Test traversal methods
print("\nInorder Traversal Tree1:")
my_tree.traverseInOrder()

print("\nPreorder Traversal Tree1:")
my_tree.traversePreOrder()

print("\nPostorder Traversal tree1:")
my_tree.traversePostOrder()

# Test traversal methods
print("\nInorder Traversal Tree3:")
my_tree2.traverseInOrder()

print("\nPreorder Traversal Tree3:")
my_tree2.traversePreOrder()

print("\nPostorder Traversal tree3:")
my_tree2.traversePostOrder()


# Test delete method
node_to_remove = 12
print(f"\nRemoving node with data {node_to_remove}")
my_tree.remove(node_to_remove)
print("Updated Tree Structure:")
print(my_tree)

# Test search method
search_data = 7
print(f"\nSearching for node with data {search_data}:")
result_node = my_tree.search(search_data)
if result_node:
    print(f"Node found: {result_node.data}")
else:
    print("Node not found.")
print()
print(f"Max number in the tree {my_tree.getMax()}")
print()
print(f"Min number in the tree {my_tree.getMin()}")