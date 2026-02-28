import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits

    # Combine all characters
    all_characters = lowercase + uppercase + numbers

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers)
    ]

    # Fill the remaining length
    for _ in range(length - 3):
        password.append(random.choice(all_characters))

    # Shuffle the password
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)


# Example usage
password_length = 12
print("Generated Password:", generate_password(password_length))