
from datetime import date
import math


def split_code(code):
    if not isinstance(code, str):
        raise ValueError("Coupon code must be a string")

    parts = code.strip().upper().split('-')

    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError("Invalid coupon code format")

    try:
        value = int(parts[1])
    except ValueError:
        raise ValueError("Coupon value must be an integer")

    return parts[0], value


def most_expensive(prices_csv):
    if not isinstance(prices_csv, str) or not prices_csv.strip():
        raise ValueError("Prices must be a non-empty string")

    try:
        prices = [float(p.strip()) for p in prices_csv.split(',')]
    except ValueError:
        raise ValueError("All prices must be valid numbers")

    if not prices or any(not math.isfinite(p) or p < 0 for p in prices):
        raise ValueError("Prices must be finite and non-negative")

    return max(prices)


def expiry_days(date_text):
    if not isinstance(date_text, str):
        raise ValueError("Date must be a string")

    try:
        expiry = date.fromisoformat(date_text)
    except ValueError:
        raise ValueError("Date must be a valid YYYY-MM-DD date")

    if expiry.isoformat() != date_text:
        raise ValueError("Date must use YYYY-MM-DD format")

    return (expiry - date(2024, 1, 1)).days

def main():
    print("==== Running split_code ====")
    user_input = input("Enter a coupon code (e.g. save-20): ")
    result = split_code(user_input)
    print("Prefix and Value:", result)

    print("\n==== Running most_expensive ====")
    user_input = input("Enter item prices as CSV (e.g. 199,49.5,320): ")
    result = most_expensive(user_input)
    print("Most Expensive Item:", result)

    print("\n==== Running expiry_days ====")
    user_input = input("Enter an expiry date as YYYY-MM-DD: ")
    result = expiry_days(user_input)
    print("Days Since 2024:", result)

if __name__ == "__main__":
    main()
