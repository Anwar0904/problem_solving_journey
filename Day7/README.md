# First Non-Repeating Character

## Difficulty

Beginner

## Learning Objectives

- Count occurrences of characters.
- Normalize characters before comparing them.
- Preserve the original order when selecting a qualifying character.
- Use a dictionary for counting and lookup.

## Problem Statement

Given a string, find and display the first character that occurs exactly once, treating uppercase and lowercase forms as the same character. The script displays the selected character in lowercase. If no such character exists, display `No non-repeating character`.

## Examples

```text
Input:  swiss
Output: w
```

```text
Input:  aabb
Output: No non-repeating character
```

```text
Input:  aAbBcD
Output: c
```

```text
Input:  ""
Output: No non-repeating character
```

## Constraints

The existing script applies Python's `lower()` method to each character. It does not specify a restricted alphabet, treatment of multi-character Unicode case mappings, or maximum string length.

## Rules

No library restrictions are stated. The current approach uses a dictionary to count normalized characters, then scans the original string's character sequence by normalized key.

## Expected Behavior

- Choose the first character in input order whose lowercase form occurs once.
- Display the selected character in lowercase.
- If every normalized character occurs more than once, or the input is empty, display `No non-repeating character`.
- Case variants count together: `A` and `a` are treated as the same character.

## Hints

- Hint 1: The answer depends both on counts and on the original order.
- Hint 2: Normalize each character consistently before counting.
- Hint 3: Make one pass to count, then another pass to find the first normalized character with count one.

## How to Submit Your Solution

Add an alternative under `Day7/solutions/`. Explain how you normalize characters and whether your method preserves the required input order. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Concepts Practiced

Strings, dictionaries, frequency counting, hashing, normalization, and order-sensitive selection.

## Complexity Challenge

For a string of length `n`, how many passes are made? What is the additional space usage in terms of the number of distinct normalized characters?
