#!/usr/bin/env python3
"""
Simple utility to check if something is worth it (стоит).
"""


def is_worth_it(value, cost):
    """
    Check if something is worth its cost.
    
    Args:
        value: The perceived value
        cost: The actual cost
        
    Returns:
        bool: True if value is greater than or equal to cost
    """
    return value >= cost


def main():
    """Main entry point."""
    print("Стоит ли оно того? (Is it worth it?)")
    
    try:
        value = float(input("Enter the value: "))
        cost = float(input("Enter the cost: "))
        
        if is_worth_it(value, cost):
            print("✓ Да, стоит! (Yes, it's worth it!)")
        else:
            print("✗ Нет, не стоит. (No, it's not worth it.)")
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
