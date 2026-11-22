# find the max number in array
# numbers = [12, 45, 7, 89, 23] #the answer should be 89
# numbers = [5, 3, 9, 2] # the answer should be 9
numbers = [-10, -3, -25, -1]  # the answer should be -1
# numbers = []
if numbers:
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n

    print(largest)
else:
    print("Array is empty")
