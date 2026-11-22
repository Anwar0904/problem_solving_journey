# numbers = [1, 2, 2, 3, 4, 4, 4]
# duplicates = []
# updatedNumbers = []

# n = len(numbers)
# for i in range(n):
#     for j in range(i + 1, n):
#         if numbers[i] == numbers[j]:
#             if numbers[i] not in duplicates:
#                 duplicates.append(numbers[i])

# print(duplicates)

# for num in numbers:
#     if num not in updatedNumbers:
#         updatedNumbers.append(num)
# print(updatedNumbers)


# Attempt no 2

numbers = [1, 2, 2, 3, 4, 4, 4]
duplicates = []
seen = []

for num in numbers:
    if num not in seen:
        seen.append(num)
    elif num not in duplicates:
        duplicates.append(num)

print(seen)
print(duplicates)
