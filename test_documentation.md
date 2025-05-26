# Test Documentation for Book Management System

## Overview
This document provides information about the test implementation for the Book Management System, specifically focusing on the "Update Book Information" functionality.

## Test Files
- `test_book_management.py`: Contains tests for both adding and updating books in the library system.

## Test Functions

### `test_add_book()`
Tests the functionality to add a new book to the library system.
- Initializes a clean test database
- Adds a book with test data
- Verifies the book was added correctly

### `test_update_book()`
Tests the functionality to update existing book information.
- Initializes a clean test database
- Adds a test book to be updated
- Performs multiple test cases:
  1. **Test 1**: Updates a book with new information (title, publisher, quantity)
  2. **Test 2**: Attempts to update a non-existent book (expected to fail)
  3. **Test 3**: Attempts to update with invalid data (non-existent author ID, expected to fail)
  4. **Test 4**: Updates with empty updates (should succeed but not change anything)

### `run_all_tests()`
Runs both the add book and update book tests sequentially and reports the overall results.

## Running the Tests

### Command Line Options
The test script can be run with command-line arguments to specify which tests to run:
```
python test_book_management.py [mode]
```

Where `mode` can be:
- `1`: Run only the add book test
- `2`: Run only the update book test
- Any other value or no value: Run all tests

### Examples
```
# Run all tests
python test_book_management.py

# Run only the add book test
python test_book_management.py 1

# Run only the update book test
python test_book_management.py 2
```

## Test Design Principles
1. **Isolation**: Each test initializes a fresh database to ensure tests don't interfere with each other
2. **Comprehensive Testing**: Tests cover both successful operations and expected failure cases
3. **Edge Cases**: Tests include edge cases like empty updates and invalid data
4. **Verification**: Each test verifies the results to ensure the operations worked correctly

## Notes
- The tests use `force_reset=True` when initializing the database to ensure a clean state for testing
- When updating a book's quantity, the available_quantity remains unchanged, which appears to be the intended behavior
- The tests include proper error handling and verification to ensure the system behaves as expected