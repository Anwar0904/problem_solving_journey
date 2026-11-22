word = "hello"
reverseWord = ""

for i in range(len(word)):
    reverseWord = reverseWord + word[len(word) - i - 1]

print(reverseWord)
