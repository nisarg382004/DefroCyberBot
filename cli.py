import sys
import os
import requests
import json
import psutil
import whois
import shodan
import matplotlib.pyplot as plt
import socket
import platform
import openai

# Replace 'your-api-key-here' with your actual OpenAI API key
openai.api_key = 'Your API KEY'

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you don't have access to GPT-4
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def show_help():
    print("Available commands:")
    print("  search <query>          - Searches for the specified query.")
    print("  help                    - Displays this help message.")
    print("  status                  - Displays system status.")
    print("  resources               - Lists available resources.")
    print("  plot <data>             - Plots data using matplotlib.")
    print("  record <audio_file>     - Records audio from the microphone.")
    print("  execute <command>       - Executes a shell command.")
    print("  code <language> <code>  - Executes code in the specified language.")
    print("  exit                    - Exits the program.")
    print("  chat <prompt>           - Gets a response from OpenAI's API.")

def search(query):
    """
    Placeholder for search functionality.
    """
    print(f"Searching for '{query}' on Instagram...")
    # Simulated response
    print("Advanced search functionality not yet implemented.")

def show_status():
    print("System Status:")
    print(f"  OS: {platform.system()} {platform.release()}")
    print(f"  CPU: {psutil.cpu_percent()}%")
    print(f"  Memory: {psutil.virtual_memory().percent}%")
    print(f"  Disk: {psutil.disk_usage('/').percent}%")

def list_resources():
    print("Available resources:")
    # Add code to list available resources

def plot_data(data):
    """
    Plots data using matplotlib.
    """
    try:
        data = json.loads(data)
        plt.plot(data)
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title('Data Plot')
        plt.show()
    except json.JSONDecodeError:
        print("Invalid data format. Please provide valid JSON data.")

def record_audio(audio_file):
    """
    Records audio from the microphone.
    """
    # Placeholder implementation
    print(f"Recording audio to {audio_file} (Feature not implemented yet).")

def execute_command(command):
    """
    Executes a shell command.
    """
    try:
        output = os.popen(command).read()
        print(output)
    except Exception as e:
        print(f"Error executing command: {e}")

def execute_code(language, code):
    """
    Executes code in the specified language.
    """
    # Placeholder implementation
    print(f"Executing {language} code...")
    print(code)

def handle_command(command):
    """
    Handles different commands input by the user.
    """
    if command.startswith("search "):
        query = command[len("search "):]
        search(query)
    elif command == "help":
        show_help()
    elif command == "status":
        show_status()
    elif command == "resources":
        list_resources()
    elif command.startswith("plot "):
        data = command[len("plot "):]
        plot_data(data)
    elif command.startswith("record "):
        audio_file = command[len("record "):]
        record_audio(audio_file)
    elif command.startswith("execute "):
        shell_command = command[len("execute "):]
        execute_command(shell_command)
    elif command.startswith("code "):
        parts = command[len("code "):].split(' ', 1)
        if len(parts) == 2:
            language, code = parts
            execute_code(language, code)
        else:
            print("Invalid code command format.")
    elif command.startswith("chat "):
        prompt = command[len("chat "):]
        response = get_openai_response(prompt)
        print("OpenAI Response:", response)
    elif command == "exit":
        sys.exit()
    else:
        print("Unknown command. Type 'help' for a list of commands.")

def main():
    """
    Main function to run the command loop.
    """
    while True:
        command = input("Enter command: ")
        handle_command(command)
        print()  # For better readability

if __name__ == "__main__":
    main()
