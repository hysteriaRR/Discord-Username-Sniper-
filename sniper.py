import requests
import random
import string

def generate_username(length=8):
    """Generate a random username of specified length."""
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return username

def check_username_availability(username):
    """Check if a username is available using the Discord username API."""
    url = f"https://discord.com/api/v10/users/@me?username={username}"
    response = requests.get(url)
    if response.status_code == 200:
        return True  # Username is available
    elif response.status_code == 400:
        return False  # Username is unavailable
    else:
        raise Exception(f"Failed to check availability. Status code: {response.status_code}")

def main():
    username = generate_username()
    print(f"Generated username: {username}")
    if check_username_availability(username):
        print("Username is available!")
    else:
        print("Username is unavailable.")

if __name__ == "__main__":
    main()
