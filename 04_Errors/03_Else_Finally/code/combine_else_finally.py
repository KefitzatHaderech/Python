def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Result:", result)
    finally:
        print("Operation complete.")


# Test cases
safe_divide(10, 2)   # Output: Result: 5.0, Operation complete.
safe_divide(10, 0)   # Output: Error: Division by zero!, Operation complete.
