#!/usr/bin/env python3

import requests
import argparse

# URL of the bot endpoint
URL = 'http://127.0.0.1:5000/bot'

def interact_with_bot(user_input):
    """Send user input to the bot and get the response."""
    try:
        response = requests.post(URL, json={'input': user_input})
        data = response.json()
        print(f"Bot: {data.get('response', data.get('error', 'An error occurred.'))}")
    except requests.RequestException as e:
        print(f"Error: {e}")

def main():
    """Main function to handle CLI arguments and interaction."""
    parser = argparse.ArgumentParser(description="Interact with DefroCyberBot from the terminal.")
    parser.add_argument('input', type=str, help="Input message to send to the bot.")
    args = parser.parse_args()
    
    interact_with_bot(args.input)

if __name__ == '__main__':
    main()
