# Factorial Program

A simple recursive Python program to calculate the factorial of a number.

## Files

- `factorial.py` — Recursive `factorial()` function with a small CLI prompt.
- `test_factorial.py` — Unit tests for `factorial()`.

## Usage

```bash
python factorial.py
```

Example:
```
Enter a number: 5
Factorial of 5 = 120
```

## Running Tests

```bash
python -m unittest test_factorial.py -v
```

### Test Cases Covered

| Test | Description |
|------|-------------|
| `test_zero` | factorial(0) == 1 |
| `test_one` | factorial(1) == 1 |
| `test_small_numbers` | Checks 2!, 3!, 4!, 5! |
| `test_larger_number` | Checks 10! == 3628800 |
| `test_recursion_depth_reasonable_input` | Checks 15! for a moderately large value |

## Known Limitation

This version does not validate input. A negative number will recurse forever until Python raises a `RecursionError`, and a non-integer input will raise a `TypeError` from Python itself (not a custom one). Let me know if you'd like input validation added — happy to update the code and tests for that too.
