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