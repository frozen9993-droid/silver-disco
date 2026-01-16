# Copilot Instructions for silver-disco

## Project Overview
This is a simple Python utility called "Stoit" (стоит - Russian for "is worth it") that compares numeric values against costs to determine worthiness. The project demonstrates bilingual output (Russian/English) and interactive CLI design.

## Architecture
- **Single-module design**: All core logic in `stoit.py` with one main function (`is_worth_it()`)
- **No external dependencies**: Pure Python standard library only
- **Test-driven**: Unit tests in `test_stoit.py` using Python's built-in `unittest` framework

## Development Workflows

### Running the Application
```bash
python3 stoit.py
```
Interactive CLI prompts for value and cost inputs, then displays comparison result.

### Running Tests
```bash
# Run all tests
python3 -m unittest test_stoit.py

# Run with verbose output
python3 -m unittest test_stoit.py -v

# Run specific test
python3 -m unittest test_stoit.TestStoit.test_worth_it_when_value_greater
```

### Testing Philosophy
- Test edge cases: zero values, negative values, equal values
- Import testable functions directly from `stoit.py` (e.g., `from stoit import is_worth_it`)
- Use descriptive test method names following pattern: `test_<condition>_when_<scenario>`

## Code Conventions

### Bilingual Output Pattern
All user-facing output includes both Russian and English:
```python
print("✓ Да, стоит! (Yes, it's worth it!)")
print("✗ Нет, не стоит. (No, it's not worth it.)")
```
This pattern should be maintained for any new messages.

### Error Handling
- Catch `ValueError` for invalid numeric input
- Catch `KeyboardInterrupt` for graceful exit
- Provide user-friendly error messages

### Function Design
- Keep functions pure and testable (like `is_worth_it()`)
- Separate I/O logic in `main()` from business logic
- Use clear docstrings with Args/Returns sections

## File Structure
```
silver-disco/
├── stoit.py         # Main application with CLI
├── test_stoit.py    # Unit tests
├── README.md        # Usage documentation
└── .gitignore       # Excludes __pycache__/ and *.pyc
```

## Key Patterns
- **Executable script**: Both `stoit.py` and `test_stoit.py` use shebang (`#!/usr/bin/env python3`) and `if __name__ == "__main__"` guards
- **Simple comparison logic**: Core function uses straightforward `>=` operator
- **Interactive input**: Uses `input()` with `float()` casting for numeric values
