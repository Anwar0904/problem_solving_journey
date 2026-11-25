# Count Frequencies

## Difficulty

Beginner

## Learning Objectives

- Count how often each distinct value occurs.
- Preserve first-appearance order.
- Relate each value to its count.

## Problem Statement

Given a list of numbers, display the input, the distinct values in the order they first appear, and the frequency of each distinct value in a parallel list at the corresponding position.

For example, the first value in the distinct-values list is paired with the first count in the frequency list.

## Examples

```text
Input: [1, 2, 2, 3, 4, 4, 4, 1, 2]
Output:
[1, 2, 2, 3, 4, 4, 4, 1, 2]
[1, 2, 3, 4]
[2, 3, 1, 3]
```

```text
Input: [8, 8, 8]
Output:
[8, 8, 8]
[8]
[3]
```

## Constraints

The original example uses integers and does not specify a numeric range or a maximum list size.

## Rules

The original challenge does not prohibit any built-ins or libraries. The existing attempt uses two lists: one for first-seen values and one for their counts.

## Expected Behavior

- Show the original input, distinct values, and their counts.
- Keep distinct values in order of first appearance.
- Keep the count list aligned position by position with the distinct-values list.
- An empty input would produce three empty lists; this case is not shown in the original script.

## Hints

- Hint 1: Each new distinct value needs an initial count.
- Hint 2: When a value appears again, update the count associated with that value.
- Hint 3: Keep the distinct values and their counts aligned, or consider a mapping from values to counts.

## How to Submit Your Solution

Add an alternative in `Day5/solutions/`. Explain how your approach represents the relationship between values and counts. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Concepts Practiced

Lists, iteration, counting, membership lookup, indexing, and dictionaries as an alternative representation.

## Complexity Challenge

The current approach searches the distinct-values list when a value repeats. How does that affect the worst-case time? What space is needed to store the distinct values and counts?
