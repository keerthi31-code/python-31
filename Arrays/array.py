# What is an array
# array is a special varibale, which can hold more than one value at a time
#access the elements of an array
cars=["Ford","Volvo","BMW"]
x=cars[0]
#modify the value of the first array item
cars[0]="toyota"
print(cars)

names=["keerthi","navya","aashritha","mansa","sriya"]
names[1]="choti"
print(names)

#length of an array
# use len() menthod to return the length of array
x=len(cars)
y=len(names)
print(x)
print(y)

#looping array elements
# for in loop tp loop through the elemnets of an array
for x in cars:
    print(x)
for y in names:
    print(y)

#adding array elements
#append()

cars.append("honda")
print(cars)
names.append("navya")
print(names)

# remove array elements -- using pop()
cars.pop(1)
cars.pop(2)
print(cars)

names.pop(5)
print(names)
# remove also used for remove an element
names.remove("mansa")
print(names)

names.remove("keerthi")
print(names)
cars.remove("BMW")
print(cars)

def mergeSort(left, right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return mergeSort(left,right)
arr=[4,5,3,2,9]
k=2
sorted_arr=merge_sort(arr)
print(merge_sort)
print(f"{k}nd smallest element:", sorted_arr[k - 1])