# Find the Maximum Number

## Difficulty

Beginner

## Learning Objectives

- Scan a list one value at a time.
- Keep track of the greatest value seen so far.
- Handle an empty list explicitly.

## Problem Statement

Given a list of numbers, determine and display its greatest value. If the list contains no values, display `Array is empty`.

## Examples

```text
Input:  [12, 45, 7, 89, 23]
Output: 89
```

```text
Input:  [-10, -3, -25, -1]
Output: -1
```

```text
Input:  []
Output: Array is empty
```

## Constraints

The original script shows integer lists and an empty-list case. It does not specify a numeric range or whether other numeric types are in scope.

## Rules

The original challenge does not state restrictions on built-in functions or libraries. The learning objective is to practice finding the maximum by comparing values; the example solution uses a loop.

## Expected Behavior

- For a non-empty list, display one greatest value.
- For an empty list, display `Array is empty`.
- Negative numbers are valid; the greatest value need not be positive.

## Hints

- Hint 1: You only need to remember one candidate as you inspect the list.
- Hint 2: Start with a value from the input rather than assuming zero is a valid answer.
- Hint 3: Compare every remaining value with the current candidate and update it when appropriate.

## How to Submit Your Solution

Write your implementation in a separate file or contribute an alternative under `Day1/solutions/`. Explain how it handles an empty list. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Concepts Practiced

Lists, iteration, comparisons, conditionals, and edge-case handling.

## Complexity Challenge

For a list of `n` values, how many comparisons are needed? How much extra space does a one-pass approach use?
