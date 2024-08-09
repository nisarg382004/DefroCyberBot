from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    try:
        user_input = request.json.get('input')
        if user_input:
            response = f"You said: {user_input}"
        else:
            response = "No input provided."
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/honeypot', methods=['GET'])
def honeypot():
    return jsonify({'message': 'This is a honeypot endpoint'}), 403

if __name__ == '__main__':
    try:
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    except Exception as e:
        print(f"An error occurred: {e}")
