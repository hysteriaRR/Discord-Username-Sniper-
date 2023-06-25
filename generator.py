import random
import string

def generate_random_string(length):
    """Generate a random string of specified length containing letters and numbers."""
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_random_string_set(size, length):
    """Generate a set of random strings."""
    random_string_set = set()
    while len(random_string_set) < size:
        random_string_set.add(generate_random_string(length))
    return random_string_set

def main():
    size = int(input("Enter the number of random strings to generate: "))
    length = int(input("Enter the length of each random string: "))
    random_string_set = generate_random_string_set(size, length)
    print("Random String Set:")
    for random_string in random_string_set:
        print(random_string)

if __name__ == "__main__":
    main()
