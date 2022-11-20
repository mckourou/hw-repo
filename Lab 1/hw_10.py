a = int(input())
b = int(input())
c = int(input())

while not a<=b<=c:
    if(a>b):
        a,b = b,a
    elif(b>c):
        b,c = c,b
print(a,b,c)