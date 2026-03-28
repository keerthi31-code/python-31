n=int(input("enter the value: "))
if n & 1:
    print("odd")
else: 
    print("even")  

for i in range(1,6):
    if i &1:
        print(i,"odd") 
    else:
        print(i, "even")   

lst=[2,3,2,4,4]
result =0
for i in lst:
    result=result^i
print(result) 

lst=[5,1,2,1,2]
result=0
for i in lst:
    result ^=i #XOR
print(result)    

#Input: "GeeksforGeeks"
# Output: ['G', 'e', 'k', 's']
# Try to print the characters which are present more than
# one time in a given string

s="geeksforgeeks"
lst=[]
for ch in s:
    if s.count(ch)>1 and ch not in lst:
        lst.append(ch)
print(lst)

s="GEEKFORGEEKS"
lst=[]
for ch in s:
    if s.count(ch)>1 and ch.lower() not in lst:
        lst.append(ch.lower())
print(lst)        

s="KEERTHI"
lst=[]
for ch in s:
    lst.append(ch.lower())
print(lst)   

lst=[12,345,67,890,7654]
count=0
for i in lst:
    num = len(str(i))
    if num %2==0:
        count+=1
print(count)   

lst=[12,345,67,890,7654]
count=0
for i in lst:
    num = len(str(i))
    if num %2!=0:
        count+=1
print(count)   

s="KEERTHI"
lst=[]
for ch in s:
    if s.count(ch)>1 and ch.lower() not in lst:
        lst.append(ch.lower())
print(lst) 
