# numbers = [3, 3]
# target = 6

# Test 1  Passed
# numbers = [2, 7, 11, 15]
# target = 9
# Expected: [0, 1]

# Test 2 passed
# numbers = [3, 2, 4]
# target = 6
# Expected: [1, 2]

# Test 3 passed
# numbers = [3, 3]
# target = 6
# Expected: [0, 1]

# Test 4 also passed
# numbers = [1, 2, 3]
# target = 10
# Expected: No solution

# Test 5
numbers = [1, 2, 3, 4, 5, 3, 3]
target = 6


n = len(numbers)
indexes = []
result = ""
found = False
for i in range(n):
    if found:
        break
    for j in range(i + 1, n):

        if numbers[i] + numbers[j] == target:
            result = f"{numbers[i]} + {numbers[j]} = {target}"
            indexes.append(i)
            indexes.append(j)
            found = True


if result:
    print(result)
    print(indexes)
else:
    print("Combination not found")
