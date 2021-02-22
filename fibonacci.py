count=int(input("Please enter a positive integer greater than 1:"))
a=1
b=1
print(a)
print(b)
for i in range(count-2):
    a=a+b
    b=a-b
    print(a)