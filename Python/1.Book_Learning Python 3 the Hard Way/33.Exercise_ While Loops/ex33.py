i = 0
numbers = []

def listgen(max, numbers, i):
    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

listgen(6, numbers, i)

print("The numbers: ")

for num in numbers:
    print(num)