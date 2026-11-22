numbers = [1, 2, 2, 3, 4, 4];

let duplicates = [];
for (let i = 0; i < numbers.length; i++) {
  for (let j = i + 1; j < numbers.length; j++) {
    if (numbers[i] == numbers[j]) {
      duplicates.push(numbers[i]);
      numbers.pop(i);
    }
  }
}

console.log(duplicates);
console.log(numbers);
