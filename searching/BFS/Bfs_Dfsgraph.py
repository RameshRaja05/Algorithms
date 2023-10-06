from collections import defaultdict

class Graph:
    def __init__(self):
      self.numofnodes=0
      self.graph={}
    def add_vertex(self,u):
        self.graph[u]=[]
        self.numofnodes+=1
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def bfs(self,s):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end=' ')
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
    def dfs(self,s):
        visited=set()
        self.dfsutil(s,visited)
    def dfsutil(self,s,visited):
        visited.add(s)
        print(s,end=" ")
        for i in self.graph[s]:
            if i not in visited:
                self.dfsutil(i,visited)





mygraph=Graph()
mygraph.add_vertex(0)
mygraph.add_vertex(1)
mygraph.add_vertex(2)
mygraph.add_vertex(3)
mygraph.add_edge(0, 1)
mygraph.add_edge(0, 2)
mygraph.add_edge(1, 2)
mygraph.add_edge(2, 0)
mygraph.add_edge(2, 3)
mygraph.add_edge(3, 3)
mygraph.dfs(2)