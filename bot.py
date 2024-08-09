from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    try:
        # Get the user input from the request
        user_input = request.json.get('input')
        
        if user_input:
            # Generate a response (echoing the input back)
            response = f"You said: {user_input}"
        else:
            response = "No input provided."
        
        return jsonify({'response': response})
    
    except Exception as e:
        # Catch and return any error that occurs
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        # Set the port for the Flask app to run on
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print(f"An error occurred: {e}")
