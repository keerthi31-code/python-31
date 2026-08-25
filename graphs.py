graph={}
n=int(input("enter no of nodes: "))
for i in range(n):
    node=input("enter node:")
    graph[node]=[]
t=int(input("enter the no. of edges: "))
for j in range(t):
    print("enter edge:",j+1)
    n1=input("enter 1st node:")
    n2=input("enter 2nd node:")
    graph[n1].append(n2)
    graph[n2].append(n1)
print("adjacency list:")
for k in graph:
    print(k,":",graph[k])