#creating a graph through user input
# n=int(input("enter the number of vertices: "))
# e=int(input("enter the number of edges: "))
# graph={}
# for i in range(n):
#     graph[i]=[]

# for i in range(e):
#     a,b=map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# print(graph)

# given a number n- generate all strs of len n using only 'A' & 'B'
def subsets(n): #n=2
    r=[]# empty list
    def generate(current_s):
        if len(current_s)==n:#a
            r.append("".join(current_s))# a,a, a,b
            return
        for i in ['a','b']:
            current_s.append(i)
            generate(current_s)
            current_s.pop()
    generate([])
    return r
print(subsets(2))
print(subsets(4))
print(subsets(7))

