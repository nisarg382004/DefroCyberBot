from flask import Flask, request, jsonify

import os



app = Flask(__name__)



@app.route('/')

def home():

    """Root route providing basic information about the bot."""

    return "Welcome to DefroCyberBot! Use /bot to interact with the bot or /honeypot for honeypot information."



@app.route('/bot', methods=['POST'])

def bot():

    """Endpoint to handle user input and provide a response."""

    try:

        # Get the user input from the request

        user_input = request.json.get('input')



        if user_input:

            # Generate a response (echoing the input back)

            response = f"You said: {user_input}"

        else:

            response = "No input provided. Please send a JSON object with 'input' field."



        return jsonify({'response': response}), 200

    except Exception as e:

        # Catch and return any error that occurs

        return jsonify({'error': str(e)}), 500



@app.route('/honeypot', methods=['GET'])

def honeypot():

    """Honeypot endpoint to provide information or a trap."""

    return jsonify({'message': 'This is a honeypot endpoint'}), 403



if __name__ == '__main__':

    try:

        # Set the port for the Flask app to run on

        port = int(os.environ.get("PORT", 5000))

        app.run(host='0.0.0.0', port=port)

    except Exception as e:

        print(f"An error occurred: {e}")

