from flask import Flask, send_from_directory
import threading
import time

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

def start_flask_server():
    app.run(host='0.0.0.0', port=5000)

def start_bot():
    # Your bot's functionality
    print("Bot is starting...")
    # Simulate bot work
    time.sleep(10)  # Replace with actual bot work

if __name__ == "__main__":
    # Start the Flask server in a separate thread
    threading.Thread(target=start_flask_server).start()
    
    # Start the bot
    start_bot()
