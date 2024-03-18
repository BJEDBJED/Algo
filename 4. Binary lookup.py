#Binary lookup

tablica=[19, 21, 23, 29, 45, 45, 76, 83]

def binarylook(tablica,x):
    left=0
    right=len(tablica)-1
    
    while left<=right:
        mid=left+(right-left)//2

        if tablica[mid]==x:
            return f"znaleziono {x}"
        
        elif tablica[mid]<x:
            left=mid+1

        elif tablica[mid]>x:
            right=mid-1
    
    return f"ni ma go"

x=22
z=binarylook(tablica,x)
print(z)

#BST od podstaw

from graphviz import Digraph

class Node:
           
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

    def insert(self, data):
        if data < self.data:
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
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False
            
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
        else:
            return

    #delete O(n)    
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
        else:
            return
        
    #copy O(n)
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
        else:
            return
    
root=Node(30)
root.insert(20)
root.insert(24)
root.insert(54)
root.insert(17)
root.insert(67)
root.insert(11)
root.insert(66)

print(root.search(20))
print(root.search(7))

root.inorder(root)
print("-----------")
root.postorder(root)
print("-----------")
root.preorder(root)

