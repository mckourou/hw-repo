def power(a: float, n: float) -> float:
    return a**n


a = input().split()
print(power(float(a[0]), float(a[1])))