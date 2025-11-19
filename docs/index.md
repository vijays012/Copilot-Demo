# Copilot-Demo Project Documentation

## Overview
Copilot-Demo is a Python project for Unit-4 Assignment. It includes utility functions, practice questions, and automated testing with GitHub Actions.

## Project Structure

```
Copilot-Demo/
├── .github/
│   └── workflows/
│       └── python-tests.yml          # GitHub Actions workflow for automated testing
├── docs/
│   └── index.md                      # Project documentation
├── questions/
│   └── 6th_question/
│       ├── 7th.py
│       ├── 8.py
│       ├── 9th.py
│       └── average.py
├── tests/
│   └── test_basic.py                 # Unit tests
├── README.md                         # Project README
└── string_utils.py                   # Utility functions for string operations
```

## Features

- **String Utilities**: Helper functions for string manipulation
- **Practice Questions**: Solutions to unit-4 assignment problems
- **Unit Tests**: Comprehensive test suite with pytest
- **CI/CD Pipeline**: Automated testing on push and pull requests

## GitHub Actions Workflow

The project uses GitHub Actions for continuous integration:

- **Trigger**: Runs on push to `main` branch and on pull requests
- **Environment**: Ubuntu latest with Python 3.11
- **Steps**:
  1. Checkout repository
  2. Set up Python 3.11
  3. Install dependencies (pytest)
  4. Run test suite with pytest

## Getting Started

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install pytest
   ```

### Running Tests

Run the test suite using pytest:

```bash
pytest -q
```

Or for verbose output:

```bash
pytest -v
```

## Main Modules

### string_utils.py
Contains utility functions for string operations.

### questions/6th_question/
Contains solutions to unit-4 assignment questions:
- `7th.py` - Question 7 solution
- `8.py` - Question 8 solution
- `9th.py` - Question 9 solution (includes `add()` and `reverse_text()` functions)
- `average.py` - Average calculation solution

## Testing

All code is tested automatically through the CI/CD pipeline. Tests are located in the `tests/` directory and run on every push to `main` and on pull requests.

## Development

1. Create a feature branch
2. Make your changes
3. Ensure tests pass locally: `pytest`
4. Commit and push to trigger CI/CD
5. Create a pull request for review

## License

This project is part of Unit-4 Assignment.

## Usage

### String Utilities (`string_utils.py`)

#### Check if a string is a palindrome:
```python
from string_utils import is_palindrome

# Check palindrome (ignores non-alphanumeric characters and case)
result = is_palindrome("A man, a plan, a canal: Panama")
print(result)  # Output: True

result = is_palindrome("hello")
print(result)  # Output: False
```

#### Normalize a string:
```python
from string_utils import normalize_string

# Convert to lowercase and remove non-alphanumeric characters
normalized = normalize_string("Hello@World-123!")
print(normalized)  # Output: helloworld123

normalized = normalize_string("Python_3.11")
print(normalized)  # Output: python311
```

#### Cached string normalization (for performance):
```python
from string_utils import cached_normalize_string

# Returns cached results for repeated inputs (faster)
cached_normalized = cached_normalize_string("Test String")
print(cached_normalized)  # Output: teststring
```

### Question 9 - Basic Functions (`questions/6th_question/9th.py`)

#### Add two numbers:
```python
from questions.6th_question.9th import add

result = add(5, 3)
print(result)  # Output: 8

result = add(-2, 7)
print(result)  # Output: 5

result = add(3.5, 2.5)
print(result)  # Output: 6.0
```

#### Reverse a string:
```python
from questions.6th_question.9th import reverse_text

reversed_str = reverse_text("Hello")
print(reversed_str)  # Output: olleH

reversed_str = reverse_text("Python")
print(reversed_str)  # Output: nohtyP

reversed_str = reverse_text("12345")
print(reversed_str)  # Output: 54321
```

### Average Calculation (`questions/6th_question/average.py`)

#### Calculate average of numbers:
```python
from questions.6th_question.average import average

# Average of a list of numbers
result = average([1, 2, 3, 4, 5])
print(result)  # Output: 3.0

result = average([10, 20, 30])
print(result)  # Output: 20.0

# Empty list returns 0
result = average([])
print(result)  # Output: 0
```

### Running Tests

Run all tests in the project:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run a specific test file:
```bash
pytest tests/test_basic.py -v
```

Run tests matching a pattern:
```bash
pytest -k "test_" -v
```

## API Overview

### string_utils Module

#### `is_palindrome(s: str) -> bool`
Checks if a string is a palindrome, ignoring non-alphanumeric characters and case sensitivity.

**Parameters:**
- `s` (str): The string to check

**Returns:**
- `bool`: True if the string is a palindrome, False otherwise

**Example:**
```python
is_palindrome("A man, a plan, a canal: Panama")  # Returns: True
is_palindrome("hello")                            # Returns: False
is_palindrome("Racecar")                          # Returns: True
```

---

#### `normalize_string(s: str) -> str`
Returns a normalized version of the string with only lowercase alphanumeric characters.

**Parameters:**
- `s` (str): The string to normalize

**Returns:**
- `str`: Normalized string with lowercase alphanumeric characters only

**Example:**
```python
normalize_string("Hello@World-123!")  # Returns: "helloworld123"
normalize_string("Python_3.11")       # Returns: "python311"
normalize_string("Test-Case_99")      # Returns: "testcase99"
```

---

#### `cached_normalize_string(s: str) -> str`
Returns a cached normalized version of the string. Uses LRU cache for performance optimization with repeated inputs.

**Parameters:**
- `s` (str): The string to normalize

**Returns:**
- `str`: Cached normalized string with lowercase alphanumeric characters only

**Cache Size:** 128 entries

**Example:**
```python
cached_normalize_string("Test String")  # Returns: "teststring" (cached)
cached_normalize_string("Test String")  # Returns: "teststring" (from cache)
```

---

### questions.6th_question.9th Module

#### `add(a, b)`
Adds two numbers and returns their sum.

**Parameters:**
- `a`: The first number to add (int or float)
- `b`: The second number to add (int or float)

**Returns:**
- The sum of a and b (int or float)

**Example:**
```python
add(5, 3)          # Returns: 8
add(-2, 7)         # Returns: 5
add(3.5, 2.5)      # Returns: 6.0
```

---

#### `reverse_text(s)`
Reverses a string.

**Parameters:**
- `s` (str): The string to reverse

**Returns:**
- `str`: The reversed string

**Example:**
```python
reverse_text("Hello")    # Returns: "olleH"
reverse_text("Python")   # Returns: "nohtyP"
reverse_text("12345")    # Returns: "54321"
```

---

### questions.6th_question.average Module

#### `average(nums)`
Calculates the average of a list of numbers. Returns 0 for empty lists.

**Parameters:**
- `nums` (list): A list of numbers (int or float)

**Returns:**
- `float` or `int`: The average of the numbers, or 0 if the list is empty

**Example:**
```python
average([1, 2, 3, 4, 5])  # Returns: 3.0
average([10, 20, 30])     # Returns: 20.0
average([])               # Returns: 0
average([5.5, 4.5])       # Returns: 5.0
```

---

## API Status Reference

| Function | Module | Status | Parameters | Return Type |
|----------|--------|--------|-----------|-------------|
| `is_palindrome()` | string_utils | ✅ Active | str | bool |
| `normalize_string()` | string_utils | ✅ Active | str | str |
| `cached_normalize_string()` | string_utils | ✅ Active | str | str |
| `add()` | 9th | ✅ Active | (a, b) | int/float |
| `reverse_text()` | 9th | ✅ Active | str | str |
| `average()` | average | ✅ Active | list | float |

---
