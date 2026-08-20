class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")



root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

inorder (root)
print()
preorder(root)
print()
postorder(root)
print()

#level order
from collections import  deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)

root.right.left=Node(60)
root.right.right=Node(70)

def level_order(root):
    if root is None:
        return
    queue=deque([root]) #[10]
    while queue:
        node=queue.popleft() #remove the first node
        print(node.data,end=" ")
        if node.left:
        #add its children
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
level_order(root)


