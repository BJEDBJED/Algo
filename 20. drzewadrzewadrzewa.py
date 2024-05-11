#drzewadrzewadrzewa

#BST

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

    def insert(self,data):
        if self.data > data:
            if self.left is None:
                self.left=Node(data)
            else:
                self.left.insert(data)

        if data>self.data:
            if self.right is None:
                self.right=Node(data)
            else:
                self.right.insert(data)

    def search(self,data):
        if self.data==data:
            return True
        
        if self.data>data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        
        if self.data<data:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def inorder(self,root):
        if root:
            root.inorder(root.left)
            print(root.data)
            root.inorder(root.right)
        else:
            return
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.data


root=Node(15)
root.insert(4)
root.insert(40)
root.insert(14)
root.insert(20)
root.insert(8)

print(root.search(14))
print(root.search(100))
        
print(root.inorder(root))

print(root.get_max())


class BST:
    def __init__(self,data=None):
        self.left=None
        self.right=None
        self.data=data

    def insert(self,data):
        if self.data is None:
            self.data=data
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=BST(data)
            
        
        if data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right=BST(data)
                    
    def get_min(self):
        current=self
        while current.left is not None:
            current=current.left
        return current.data
    
    def get_max(self):
        current=self
        while current.right is not None:
            current=current.right
        return current.data
    
    def delete(self,data):
        if self.data is None:
            return None

        if data<self.data:
            if self.left:
                self.left=self.left.delete(data)
            
        elif data>self.data:
            if self.right:
                self.right=self.right.delete(data)
        
        else:    
            if self.right is None:
                return self.left
        
            if self.left is None:
                return self.right
        
            min_larger_node=self.right
            while min_larger_node.left:
                min_larger_node=min_larger_node.left
            self.data=min_larger_node.data
            self.right=self.right.delete(min_larger_node.data)
        return self

    def search(self,data):
        if self.data==data:
            return True
        
        if self.data<data:
            if self.right:
                return self.right.search(data)
            else:
                return False

        if self.data>data:
            if self.left:
                return self.left.search(data)
            else:
                return False

    def inorder(self,bst):
        if bst:
            bst.inorder(bst.left)
            print(bst.data)
            bst.inorder(bst.right)
        else:
            return
        
    def preorder(self,bst):
        if bst:
            print(bst.data)
            bst.inorder(bst.left)
            bst.inorder(bst.right)
        else:
            return
        
    def postorder(self,bst):
        if bst:
            bst.inorder(bst.left)
            bst.inorder(bst.right)
            print(bst.data)
        else:
            return

nums=[2,4,7,3,5,6,9,11,21]
bst=BST()
for num in nums:
    bst.insert(num)
bst.delete(9)
bst.preorder(bst)
print(bst.search(5))
print(bst.search(9))

#TRY
print("---------------------")

from collections import deque

class BSTNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
             
        if self.data>data:
            if self.left is None:
                self.left=BSTNode(data)
            else:
                self.left.insert(data)

        if self.data<data:
            if self.right is None:
                self.right=BSTNode(data)
            else:
                self.right.insert(data)

    def search(self,data):
        if self.data==data:
            return f"Mamy to - {data}"
        
        if self.data>data:
            if self.left:
                return self.left.search(data)
            else:
                return f"ni ma {data}"

        if self.data<data:
            if self.right:
                return self.right.search(data)
            else:
                return f"ni ma {data}"
            
    def delete(self,data):
            
        if data<self.data:
            if self.left:
                self.left=self.left.delete(data)

        elif data>self.data:
            if self.right:
                self.right=self.right.delete(data)

        else:
            if self.right is None:
                return self.left
            
            if self.left is None:
                return self.right
            
            min_larger_node=self.right
            while min_larger_node.left:
                min_larger_node=min_larger_node.left

            self.data=min_larger_node.data
            self.right=self.right.delete(min_larger_node.data)
        
        return self

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def get_min(self):
        current=self
        while current.left:
            current=current.left
        return current.data

    def get_max(self):
        current=self
        while current.right:
            current=current.right
        return current.data

    def bfs(self):
        queue=deque([self])
        while queue:
            node = queue.popleft()
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

bst=BSTNode(15)
bst.insert(3)
bst.insert(6)
bst.insert(13)
bst.insert(18)
bst.delete(6)
print(bst.search(6))
print(bst.search(9))
bst.inorder()
print("---------")
print(bst.get_max())
print(bst.bfs())