n = int(input())
time = n*45 + n//2*5 + ((n+1)//2-1)*15
print(time//60 + 9, time%60)
