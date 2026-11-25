# Reverse a String

## Difficulty

Beginner

## Learning Objectives

- Access characters using string indices.
- Traverse a sequence in reverse order.
- Build a result from individual characters.

## Problem Statement

Given a string, display its characters in reverse order. The original script uses the example string `hello`.

## Examples

```text
Input:  hello
Output: olleh
```

```text
Input:  a
Output: a
```

```text
Input:  ""
Output: ""
```

## Constraints

The original script specifies no character set, maximum length, or input mechanism. Examples here show the intended sequence reversal for ordinary strings.

## Rules

The original challenge does not specify whether slicing or built-in helpers are permitted. The existing implementation practices index-based traversal and character concatenation.

## Expected Behavior

- Display all characters in reverse order.
- A one-character string remains unchanged.
- An empty string produces an empty result.

## Hints

- Hint 1: String positions have indices beginning at zero.
- Hint 2: The last character is at an index derived from the string's length.
- Hint 3: Visit indices from the end toward the beginning while appending each character to a result.

## How to Submit Your Solution

Write an alternative in `Day3/solutions/`, noting whether you use indexing, slicing, or another approach. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Concepts Practiced

Strings, indexing, loops, sequence order, and result construction.

## Complexity Challenge

If the string has `n` characters, how many characters must be visited? How does repeatedly concatenating immutable strings affect the space and running time in Python?
