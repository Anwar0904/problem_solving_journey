# Find the Second Largest Distinct Number

## Difficulty

Beginner

## Learning Objectives

- Track two candidate values while scanning a list.
- Distinguish the second largest distinct value from a repeated maximum.
- Decide how to report input that has no second distinct value.

## Problem Statement

Given a list of numbers, find the second largest **distinct** value. If there are fewer than two distinct values, display a message explaining that a second largest value cannot be determined.

The original script prints the second largest value first and the largest value second when a valid second value exists.

## Examples

```text
Input:  [5, 3, 9, 2]
Output:
5
9
```

```text
Input:  [1, 2, 2]
Output:
1
2
```

```text
Input:  [4, 4, 4]
Output: not much elements are there to find the second largest or all elements are same
```

## Constraints

The original script uses integers. It does not define an input range. Empty and single-element lists are not shown, but the script's fallback message covers cases where no second distinct value is recorded.

## Rules

No restriction on built-ins or libraries is stated in the original challenge. The demonstrated learning approach scans the list and tracks candidates.

## Expected Behavior

- With at least two distinct values, print the second largest and then the largest, each on its own line.
- With all equal values, an empty list, or fewer than two distinct values, print the fallback message.
- Repeated copies of the largest value do not count as the second largest distinct value.

## Hints

- Hint 1: Keep track of the largest and the next distinct candidate.
- Hint 2: A value equal to the current largest should not become the second largest.
- Hint 3: When a new maximum appears, the old maximum becomes the second candidate.

## How to Submit Your Solution

Add an alternative implementation in `Day2/solutions/` and describe how it treats duplicates and insufficient input. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Concepts Practiced

Lists, comparisons, distinctness, state tracking, and edge cases.

## Complexity Challenge

Can you solve this in one pass? Consider the time complexity and the number of values you need to retain.
