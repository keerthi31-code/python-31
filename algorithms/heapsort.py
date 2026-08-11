# heap queue a data structure commonly used to implement a prority queue efficient
#priority is process the elements to its prority queue
import heapq
a=[]
heapq.heappush(a,10)
heapq.heappush(a,5)
heapq.heappush(a,25)
heapq.heappush(a,7)
heapq.heappush(a,9)
print(a)
print(a[0])
#parent <= child nodes

import heapq
num =[10,5,20,2,8]
heapq.heapify(num)
print(num)

# min heap
import heapq
num=[10,5,20,2,8]
heapq.heapify(num)
while num:
    print(heapq.heappop(num),end=" ")

#max heap
import heapq
heap=[]
num=[10,5,20,2,8]
for i in num:
    heapq.heappush(heap,-i) #insert negative values
print(heap)
while heap: #continue as long as heap is not empty
    print(-heapq.heappop(heap),end=" ") # removes the smallest value from the heap

# 3largst elements
import heapq
num=[10,5,3,5,4]
res=heapq.nlargest(3,num)
print(res)

import heapq
num=[10,5,3,5,4]
res=heapq.nsmallest(3,num)
for i in res:
    print(i)


#practice questions
arr=[10,5,20,2,8]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

arr=[15, 3, 20, 8, 10]
heap=[]
for i in arr:
    heapq.heappush(heap, -i)
print(arr)
while heap:
    print(-heapq.heappop(heap))

arr=[4,10,2,30,8]
res=heapq.nlargest(1,arr)
print(res)

arr=[4,10,2,30,8]
res=heapq.nsmallest(1,arr)
print(res)