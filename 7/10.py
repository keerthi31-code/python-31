#creating a graph through user input
n=int(input("enter the number of vertices: "))
e=int(input("enter the number of edges: "))
graph={}
for i in range(n):
    graph[i]=[]

for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(graph)
print('keerthi')