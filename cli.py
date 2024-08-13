import sys
import logging
import subprocess

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_command(command):
    # Process commands and provide responses
    if command.lower() == "help":
        return "Available commands: help, search, interactive, exit"
    elif command.lower().startswith("search"):
        query = command[len("search"):].strip()
        return f"Searching for resources related to '{query}'..."
    elif command.lower() == "interactive":
        return "Opening interactive terminal. Please grant permission."
    elif command.lower() == "exit":
        return "Exiting the bot. Goodbye!"
    else:
        return "Unknown command. Type 'help' for a list of commands."

def open_interactive_terminal():
    # Open a new terminal window and run the bot
    try:
        if sys.platform == "win32":
            subprocess.Popen(['start', 'cmd', '/k', 'python', 'cli.py'], shell=True)
        elif sys.platform == "linux":
            subprocess.Popen(['gnome-terminal', '--', 'python3', 'cli.py'])
        else:
            return "Unsupported platform for opening a new terminal."
    except Exception as e:
        logging.error(f"Error opening interactive terminal: {e}")
        return "Failed to open interactive terminal."

def main():
    print("DefroCyberBot is now running. Type 'help' for assistance.")
    
    while True:
        try:
            command = input("Enter command: ")
            response = process_command(command)
            print(response)
            logging.info(f"User command: {command} - Response: {response}")
            if command.lower() == "interactive":
                open_interactive_terminal()
            elif command.lower() == "exit":
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
