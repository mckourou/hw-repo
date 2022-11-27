def Election(x: bool, y:bool, z:bool) -> bool:
    return 0 if [x,y,z].count('0')>[x,y,z].count('1') else 1

numbers = input().split()

print(Election(numbers[0], numbers[1], numbers[2]))