
# DefroCyberBot GitHub Page Manual

## Overview

DefroCyberBot is a chatbot designed to interact with users via a simple web interface. This manual provides detailed instructions for setting up, running, and contributing to the project.

## Table of Contents

1. [Project Setup](#project-setup)
2. [Installation Instructions](#installation-instructions)
3. [Running the Bot](#running-the-bot)
4. [Testing the Bot](#testing-the-bot)
5. [Contributing](#contributing)
6. [License](#license)

---

## Project Setup

### Cloning the Repository

To get started with DefroCyberBot, you need to clone the repository to your local machine:

```bash
git clone https://github.com/nisarg382004/DefroCyberBot.git
cd DefroCyberBot
```

## Installation Instructions

### For Linux/MacOS

1. **Create and Activate Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Installation**:

   Check that Flask and other dependencies are installed correctly:

   ```bash
   pip show Flask
   ```

### For Windows

1. **Create and Activate Virtual Environment**:

   ```batch
   python -m venv venv
   venv\Scripts\activate.bat
   ```

2. **Install Dependencies**:

   ```batch
   pip install -r requirements.txt
   ```

3. **Verify Installation**:

   Check that Flask and other dependencies are installed correctly:

   ```batch
   pip show Flask
   ```

## Running the Bot

### For Linux/MacOS

1. **Activate Virtual Environment**:

   ```bash
   source venv/bin/activate
   ```

2. **Start the Bot**:

   ```bash
   bash setup.sh
   ```

### For Windows

1. **Activate Virtual Environment**:

   ```batch
   venv\Scripts\activate.bat
   ```

2. **Start the Bot**:

   ```batch
   setup.bat
   ```

## Testing the Bot

### Using cURL

To test the bot, you can send a POST request using `cURL`:

```bash
curl -X POST http://127.0.0.1:5000/bot -H "Content-Type: application/json" -d '{"input":"Hello"}'
```

### Using Postman

1. Open Postman.
2. Set the request type to POST.
3. Enter the URL: `http://127.0.0.1:5000/bot`.
4. In the Body tab, select raw and JSON format.
5. Enter the JSON data: `{"input":"Hello"}`.
6. Send the request and verify the response.

## Contributing

### How to Contribute

1. **Fork the Repository**: Click on the "Fork" button on the top right of the repository page.
2. **Create a Feature Branch**:

   ```bash
   git checkout -b feature-branch
   ```

3. **Make Changes**: Implement your changes in the new branch.
4. **Commit Changes**:

   ```bash
   git add .
   git commit -m 'Add new feature'
   ```

5. **Push to the Branch**:

   ```bash
   git push origin feature-branch
   ```

6. **Create a Pull Request**: Go to the repository on GitHub and create a Pull Request from your feature branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This guide provides a comprehensive overview for setting up, running, and contributing to the DefroCyberBot project. If you need further assistance or have any questions, feel free to ask!
