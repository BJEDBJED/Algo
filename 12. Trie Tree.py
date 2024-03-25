# Trie Tree

class Node:
    def __init__(self):
        self.child = {}
        self.end = False
        
    
class T:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.end = True

    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        return node.end


trie = T()
words = ['banan','banana','apple','kokos','koko','apache']

for w in words:
    trie.insert(w)
    
print(trie.search('banan'))
print(trie.search('ban'))