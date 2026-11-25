# Two Sum: First Matching Pair

## Difficulty

Beginner

## Learning Objectives

- Examine pairs using nested loops.
- Use distinct positions, including when the values at those positions are equal.
- Return indices that identify the selected pair.

## Problem Statement

Given a list of numbers and a target, find the first pair of distinct indices whose values add up to the target. Display the addition expression and the two indices. If there is no such pair, display `Combination not found`.

“First” follows the search order in the existing script: indices are checked with the first index increasing, and for each one the second index increases.

## Examples

```text
Input: numbers = [2, 7, 11, 15], target = 9
Output:
2 + 7 = 9
[0, 1]
```

```text
Input: numbers = [3, 3], target = 6
Output:
3 + 3 = 6
[0, 1]
```

```text
Input: numbers = [1, 2, 3], target = 10
Output: Combination not found
```

## Constraints

The original script uses integer lists and an integer target. It searches pairs at different indices, so one list position cannot be used twice. No input size or numeric range is specified.

## Rules

The original implementation uses nested loops. No prohibition on other approaches is stated, but this exercise documents the brute-force version.

## Expected Behavior

- Display the first matching pair according to the nested-loop order, as an expression and a list of indices.
- Equal values may form a pair if they are at different indices.
- If no pair matches, display `Combination not found`.
- Empty or one-element inputs have no valid pair and therefore use the no-solution message.

## Hints

- Hint 1: A pair is about two positions, not necessarily two different values.
- Hint 2: For each position, compare it with positions that come after it.
- Hint 3: Stop at the first pair whose sum equals the target.

## How to Submit Your Solution

Add an alternative under `Day6/solutions/`. Preserve the original script and state whether your approach returns the first pair or any matching pair. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Concepts Practiced

Lists, nested iteration, indices, pair search, conditionals, and early termination.

## Complexity Challenge

How many pairs can the nested loops inspect for `n` values? What extra space does the current search use besides the returned/displayed pair?
