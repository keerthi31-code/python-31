'''
Question 1 — Binary Tree Traversals Write a Python program to create a binary tree and display Preorder, Inorder, and Postorder traversals. 
Requirements: 
1. Create a Node class with data, left, and right. 
2. Create the binary tree using user input. 
3. Implement all three traversals using recursion. 
Example input values: 1 2 3 4 5 6 7 
Expected output: Preorder: 1 2 4 5 3 6 7 
Inorder: 4 2 5 1 6 3 7 
Postorder: 4 5 2 6 7 3 1
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create(values,i):
    if i>=len(values):
        return None
    root=Node(values[i])
    root.left=create(values, 2*i+1)
    root.right=create(values, 2*i+2)
    return root

def preorder(root):
    if root is None:
        return None
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
a = list(map(int, input().split()))
root=create(a, 0)
print("preorder:",end=" ")
preorder(root)
print("\ninorder:",end=" ")
inorder(root)
print("\npostorder:",end=" ")
postorder(root)