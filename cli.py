import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
import spacy

# Load the NLP model for better command recognition
nlp = spacy.load('en_core_web_sm')

def fetch_data_from_web(query):
    # Example of web scraping from a sample website
    url = f"https://www.example.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('div', class_='result').text

async def fetch_data_from_api(query):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.example.com/data?q={query}") as response:
            return await response.json()

async def process_query(query):
    # Choose between web scraping or API based on query type
    if "web" in query.lower():
        return fetch_data_from_web(query)
    else:
        return await fetch_data_from_api(query)

def process_command(command):
    doc = nlp(command)
    if '--temperature' in command:
        return "Adjusting randomness of the output."
    elif '--top-probablity' in command:
        return "Limiting to the highest probable tokens."
    elif '--chat' in command:
        return "Starting a conversation with a unique name."
    elif '--shell' in command:
        return "Preparing shell commands output."
    elif '--execute' in command:
        return "Executing commands from the --shell option."
    elif '--code' in command:
        return "Generating code output."
    elif 'help' in command:
        return start_tutorial()
    elif 'weather' in command:
        return fetch_weather_data(doc)
    elif 'search' in command:
        return advanced_search(command)
    elif 'api list' in command:
        return api_list_overview()
    else:
        return "Unknown command. Type 'help' for a list of commands."

def start_tutorial():
    return (
        "Tutorial:\n"
        "1. Type 'help' to see the list of available commands.\n"
        "2. Use 'weather [location]' to get weather information.\n"
        "3. Use 'search [query]' for advanced search functionality.\n"
        "4. Use 'api list' to get an overview of the available API commands.\n"
        "5. Use 'download [resource]' to download resources.\n"
        "6. Use '--temperature', '--top-probablity', '--chat', '--shell', '--execute', and '--code' for advanced features.\n"
    )

def advanced_search(query):
    # Simulated advanced search
    return "Performing an advanced search..."

def api_list_overview():
    return (
        "API List - Overview\n"
        "1. Analog I/O\n"
        "2. Communication\n"
        "3. Digital I/O\n"
        "4. Infrared Object Detection\n"
        "5. Timed I/O\n"
        "6. Servo Control\n"
        "7. feedback360 module\n"
        "8. drive class\n"
        "9. group_io module\n"
        "10. i2c_repeat module\n"
        "11. ping module\n"
        "12. qti module\n"
        "13. shift module\n"
        "14. tv_remote module\n"
        "For detailed usage of each API, type 'api [API name]'."
    )

async def interactive_mode():
    while True:
        try:
            command = input("Enter command: ")
            if command.lower() == 'exit':
                print("Exiting interactive mode.")
                break
            response = await process_query(command)
            print(response)
        except Exception as e:
            print(f"Error: {e}")

# Start the interactive terminal with asyncio
asyncio.run(interactive_mode())
