# Other trees

class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []

    def add(self, node):
        self.child.append(node)

    def dfs(self):
        visit = []

        def _dfs(node):
            visit.append(node.data)
            for ch in node.child:
                _dfs(ch)       

        _dfs(self)
        return visit
    
    def bfs(self):
        visit=[]
        queue=[self]

        while queue:
            node=queue.pop(0)
            visit.append(node.data)
            for ch in node.child:
                queue.append(ch)

root=Tree('1')
a=Tree('2')
a1=Tree('3')
a2=Tree('4')
a3=Tree('5')
a4=Tree('6')
a5=Tree('7')

root.add(a1)
root.add(a2)
a2.add(a3)
