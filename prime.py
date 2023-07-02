n = int(input())
count = 0
if n == 2:
    print(n,"is not a prime number")
if n>1:
    for i in range(2,n):
        if n%i == 0:
            count = 1
            break
if count == 0:
    print (n,"is prime number")
else:
    print(n,"is not a prime number")

