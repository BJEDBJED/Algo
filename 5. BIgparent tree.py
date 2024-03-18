#5. Bigparent tree

class Node:

    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

    def insert(self,data):
        if data>self.data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)
        
        else:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)

    def inorder(self,root):
        if root:
            print(root.data)
            self.inorder(root.left)
            self.inorder(root.right)
        else:
            return
        
root=Node(130)
root.insert(20)
root.insert(24)
root.insert(54)
root.insert(17)
root.insert(67)
root.insert(11)
root.insert(66)

root.inorder(root)