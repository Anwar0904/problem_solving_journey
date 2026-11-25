# Find Duplicate Elements

## Difficulty

Beginner

## Learning Objectives

- Detect when a value has appeared before.
- Preserve the order in which values first appear.
- Report each duplicated value once, even if it occurs many times.

## Problem Statement

Given a list, display two lists: the distinct values in order of first appearance, and the values that occur more than once, in the order their repeated occurrence is first encountered. Each duplicate value should appear only once in the duplicate list.

This describes the active attempt in the original file. The file also contains an earlier commented-out approach; its current active code uses a `seen` list.

## Examples

```text
Input: [1, 2, 2, 3, 4, 4, 4]
Output:
[1, 2, 3, 4]
[2, 4]
```

```text
Input: [5, 1, 5, 1, 5]
Output:
[5, 1]
[5, 1]
```

```text
Input: [7, 8]
Output:
[7, 8]
[]
```

## Constraints

The original example uses integers. No value range, input size, or behavior for other types is specified.

## Rules

No built-in or library restrictions are stated. The current script checks membership in lists, which is useful for learning but can be slower for large inputs.

## Expected Behavior

- Preserve first-seen order in both output lists.
- Include a value in the duplicate list if it appears at least twice.
- Include each duplicated value only once, regardless of its number of occurrences.
- If there are no duplicates, display an empty duplicate list.
- An empty input would produce two empty lists; this case is not in the original script.

## Hints

- Hint 1: Track which values have appeared already.
- Hint 2: A repeated value and a newly encountered value need different handling.
- Hint 3: Track reported duplicates separately so a third occurrence does not add another copy.

## How to Submit Your Solution

Add another approach under `Day4/solutions/`. Explain how it preserves order and handles a value occurring three or more times. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Concepts Practiced

Lists, iteration, membership checks, duplicate detection, and ordering.

## Complexity Challenge

How does list membership affect the running time as the input grows? How could a different data structure change lookup cost while preserving output order?
