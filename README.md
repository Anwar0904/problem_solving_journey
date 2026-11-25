# Problem Solving Journey

> Every problem is an opportunity to improve the way we think, not just the code we write.

This repository records a daily practice in programming and problem solving. Each day presents a small challenge, a problem-first guide for working through it, and the original Python attempt that documents the learning along the way.

The goal is to make these exercises useful beyond their author: read a problem, try it yourself, compare approaches, and share a thoughtful improvement.

## How to use this repository

1. Choose a challenge from the progress table and read its `DayN/README.md` first.
2. Work through the examples and hints before opening the original script.
3. Run the script with your own inputs, or write a separate implementation.
4. Compare behavior, edge cases, and complexity. The original scripts are learning snapshots and may use fixed example data.
5. See [CONTRIBUTING.md](CONTRIBUTING.md) to share an alternative or improve the learning material.

## Learning progress

| Day | Problem | Topic | Difficulty | Status |
|---|---|---|---|---|
| 01 | [Find the Maximum Number](Day1/README.md) | Lists, loops, comparisons | Beginner | Completed |
| 02 | [Find the Second Largest Distinct Number](Day2/README.md) | Lists, comparisons, state tracking | Beginner | Completed |
| 03 | [Reverse a String](Day3/README.md) | Strings, indexing, loops | Beginner | Completed |
| 04 | [Find Duplicate Elements](Day4/README.md) | Lists, membership, order | Beginner | Completed |
| 05 | [Count Frequencies](Day5/README.md) | Lists, counting, parallel lists | Beginner | Completed |
| 06 | [Two Sum: First Matching Pair](Day6/README.md) | Nested loops, indices | Beginner | Completed |
| 07 | [First Non-Repeating Character](Day7/README.md) | Strings, dictionaries, hashing | Beginner | Completed |
| 08 | [Two Sum: Hash Map Approach](#day-08-upcoming) | Hash maps, lookup | Intermediate | Upcoming |

## Quick navigation

- [Learning roadmap](docs/learning-roadmap.md)
- [Problem categories](docs/problem-categories.md)
- [Learning resources](docs/resources.md)
- [Contribution guide](CONTRIBUTING.md)

## For beginners

You do not need to follow the days in order. Start with a familiar topic, read the problem without opening the solution, and try a few examples by hand. If you get stuck, use the hints one at a time. When comparing code, focus on why it works, what happens at the edges, and what trade-offs another approach might make.

Python files currently contain small, hard-coded examples so the logic stays visible. They are not yet a uniform command-line application; use each day's README for the behavior that the exercise describes.

## Contributing

Contributions are welcome from beginners and experienced developers. You can propose an alternative solution, clarify an explanation, add test cases, suggest a problem, or point out a bug or complexity issue. Keep the original daily script intact; put alternative implementations in that day's `solutions/` directory. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## Repository structure

```text
Day1/ ... Day7/       Daily problem guide and original Python solution
DayN/solutions/       Optional community implementations
docs/                 Roadmap, topic index, and learning resources
.github/              Issue and pull request templates
```

Each existing day has a problem-first guide next to the original script. The original filenames and code are preserved.

## Learning roadmap

The current sequence moves from list traversal and comparisons into strings, duplicate detection, counting, pair search, and dictionary-based character counting. The next planned exercise is a hash-map version of Two Sum. See the [roadmap](docs/learning-roadmap.md) for the progression and possible next topics.

## Technologies

- Python 3; no third-party packages are required by the existing scripts.
- Markdown for problem guides and project documentation.

## Future direction

The repository will grow as new problems are practiced and documented. Possible next steps include a hash-map Two Sum exercise, more alternative implementations, and broader coverage of common data structures and algorithms. New entries should keep the same problem-first format and preserve the honest record of how the solutions developed.

## Day 08 — Upcoming

The planned next challenge is an optimized Two Sum implementation using a hash map. It is listed as upcoming and has no solution or problem guide yet.

---

This is a learning journal: clear reasoning, useful feedback, and steady practice matter as much as a polished final answer.
