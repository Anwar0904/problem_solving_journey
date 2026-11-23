numbers = [1, 2, 2, 3, 4, 4, 4, 1,2]
frequency = []
seen = []
n = len(numbers)

for i in range(n):
    if numbers[i] not in seen:
        seen.append(numbers[i])
        frequency.append(1)
    else:
        frequency[seen.index(numbers[i])]+=1
        # frequency[len(frequency) - 1] += 1

print(numbers)
print(seen)
print(frequency)