def countvowels(s):
    count=0
    for ch in s:
        if ch in "aeiou":
            count +=1
    return count
print(countvowels("lasya"))
print(countvowels("keerthi"))
print(countvowels("navya"))

def remove_duplicates(n):
    result=[]
    
    for i in n:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicates([1,2,3,4,5,5,6,7,8,8,9]))        
