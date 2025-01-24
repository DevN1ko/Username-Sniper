import random
import string
import requests
from concurrent.futures import ThreadPoolExecutor

def generate_random_name(length=4):
    """Generate a random 4-letter username."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def check_username_availability(username):
    """Check if a Roblox username is available."""
    url = f"https://auth.roblox.com/v1/usernames/validate"
    try:
        response = requests.post(url, json={"username": username})
        if response.status_code == 200:
            data = response.json()
            return username, data.get("code") == 0  # `code` 0 indicates availability
        else:
            return username, None
    except Exception as e:
        return username, None

def main():
    """Generate and check multiple usernames concurrently."""
    num_names = 50  # Number of usernames to check
    usernames = [generate_random_name() for _ in range(num_names)]

    with ThreadPoolExecutor(max_workers=10) as executor:
