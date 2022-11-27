binary = int(input())
n = 1
decimal = 0
while(binary):
    decimal += binary%10 * n
    binary //= 10
    n *= 2
print(decimal)