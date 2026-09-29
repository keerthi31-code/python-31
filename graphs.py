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


# BFS code pattern
from collections import deque
queue=deque([0]) # start from node 0
visited={0} # already visited 0
while queue:
    node = queue.popleft() # taking the first node from the queue
    for neighbour in graph[node]:
        if neighbour not in visited: #if already seen this node before
            visited.add(neighbour)
            queue.append(neighbour)# visited node and add ti the queue

#DFS code pattern
visited = set()

def dfs(node):

    visited.add(node)

    for neighbor in graph[node]:

        if neighbor not in visited:

            dfs(neighbor)

#Write a program that counts the frequency of each unique word 
#inside a text sentence.




sentence = input("Enter a sentence: ")#cat dog cat
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
count=0
for word in freq:
    if freq[word]==1:
        count+=1
print("count:",count)


