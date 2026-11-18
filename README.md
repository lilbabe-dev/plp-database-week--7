# PLP Python Week 7 — Lists

## Assignment Overview

This repository contains my solutions for the PLP Python Week 7 assignment on Python lists and loops.

### Files

- **`list_warmup.py`** — Demonstrates list indexing, adding items with `append()`, removing items with `remove()`, and counting items using `len()`.
- **`shopping_list.py`** — Implements an interactive shopping list manager that allows users to add, remove, and show items, or quit the program.
- **`list_report.py`** — Prints a numbered list of items, counts item names with more than four letters, and finds the longest item name using a loop.
- **`screenshots/`** — Contains screenshots showing the output of each Python program.

## Why is it safer to check `in` before calling `.remove()`?

Checking whether an item exists in a list before using `.remove()` helps prevent errors. If the item is not in the list, `.remove()` raises a `ValueError`, which can stop the program unexpectedly. Using `in` first allows the program to display a helpful message and continue running safely.

## Author

PLP Software Engineering Student
