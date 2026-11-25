# student = "bbabbc"
frequency = {}


# Test 1
student = "swiss"
# Expected: w

# Test 2
# student = "aabb"
# Expected: No non-repeating character

# Test 3
# student = "aAbBcD"
# Expected: c (case-insensitive)

# Test 4
# student = ""
# Expected: No non-repeating character

for n in student:
    if n.lower() in frequency:
        frequency[n.lower()] += 1
    else:
        frequency[n.lower()] = 1

result = ""
for n in frequency:
    if frequency[n] == 1:
        result = n
        break
print(result if result else "No non-repeating character")


# All tests are passed

# Interview Question
# Take your time. This concept will help you understand why dictionaries are so powerful?

# answer of the question :
# python dictionaries uses hash table to jump directly to key's memory location so that's why no need to look after all others. while indexing in list look after each element and compare
