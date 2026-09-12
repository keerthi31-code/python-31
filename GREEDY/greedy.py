price = 40
people = [20, 15, 5, 1]

people.sort(reverse=True)

count = 0

for money in people:
    if money <= price:
        price = price - money
        count += 1

    if price == 0:
        break

print(count)


##ls = [sun, mon, tue, wed, thur, fri, sat]
#mon, 2
#output= wed

#frid, 2000
#output: tue

lst=['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
s=input("enter the day: ")
n=int(input("enter the num: "))
index=lst.index(s)
new_index=(index+n) % 7
print(lst[new_index])


def fib(n,memo={}):#6,m-5,4
    if n<=1:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fib(n-1, memo)+fib(n-2,memo)#{6:

    return memo[n]

print(fib(6))
print("keerthi")