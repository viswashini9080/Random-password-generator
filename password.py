import string
import random

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))
        use_letters = input("Use letters? (y/n): ").lower() == 'y'
        use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Use symbols? (y/n): ").lower() == 'y'
    except ValueError:
        print("Invalid input. Please enter a valid number for the length.")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
