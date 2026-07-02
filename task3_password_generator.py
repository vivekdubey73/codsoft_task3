"""
CodSoft Python Internship - Task 3
PASSWORD GENERATOR
Author: Vivek
"""

import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase  # always include lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Guarantee at least one character from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))

    # Fill remaining length
    remaining = length - len(password)
    password += random.choices(characters, k=remaining)

    # Shuffle to avoid predictable positions
    random.shuffle(password)
    return "".join(password)

def password_strength(length, use_upper, use_digits, use_symbols):
    score = 0
    if length >= 8:  score += 1
    if length >= 12: score += 1
    if length >= 16: score += 1
    if use_upper:    score += 1
    if use_digits:   score += 1
    if use_symbols:  score += 1

    if score <= 2:   return "🔴 Weak"
    elif score <= 4: return "🟡 Medium"
    else:            return "🟢 Strong"

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("  ⚠ Please enter y or n.")

def main():
    print("\n" + "=" * 45)
    print("    🔐 CodSoft Password Generator")
    print("=" * 45)

    while True:
        # Length input
        while True:
            try:
                length = int(input("\n  Enter password length (6-64): "))
                if 6 <= length <= 64:
                    break
                print("  ⚠ Length must be between 6 and 64.")
            except ValueError:
                print("  ⚠ Please enter a valid number.")

        # Complexity options
        print("\n  Select character types to include:")
        use_upper   = get_yes_no("  Include UPPERCASE letters? (y/n): ")
        use_digits  = get_yes_no("  Include DIGITS (0-9)?        (y/n): ")
        use_symbols = get_yes_no("  Include SYMBOLS (!@#...)?    (y/n): ")

        # Generate
        password = generate_password(length, use_upper, use_digits, use_symbols)
        strength = password_strength(length, use_upper, use_digits, use_symbols)

        print("\n" + "=" * 45)
        print(f"  🔑 Generated Password:\n")
        print(f"     {password}")
        print(f"\n  Strength : {strength}")
        print(f"  Length   : {len(password)} characters")
        print("=" * 45)

        again = input("\n  Generate another password? (y/n): ").strip().lower()
        if again != "y":
            print("\n  👋 Stay secure! Goodbye!\n")
            break

if __name__ == "__main__":
    main()
