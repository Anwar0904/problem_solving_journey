# Finding second largest number in array
numbers = [1, 2, 2]
largest = float("-inf")
secondLargest = float("-inf")

for n in numbers:
    if n > largest:
        secondLargest = largest
        largest = n
    elif secondLargest < n < largest:
        secondLargest = n
if secondLargest == float("-inf"):
    print(
        "not much elements are there to find the second largest or all elements are same"
    )
else:
    print(secondLargest)
    print(largest)
