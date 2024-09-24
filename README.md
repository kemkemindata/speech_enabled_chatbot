## Speech-Enabled Chatbot with Streamlit
This project is a Speech-Enabled Chatbot built using Streamlit and SpeechRecognition. 
The chatbot interacts with users either via text input or speech, converting spoken words into text and generating responses using a simple pattern-matching algorithm from NLTK. 
The chatbot is capable of recognizing patterns and responding with predefined messages.

## Table of Contents

Features
Installation
Usage
Technologies Used


## Features
-Speech recognition: Allows users to interact with the chatbot using voice commands.

-Text-based input: Provides an alternative for users to type questions.

-Predefined responses: The chatbot responds to a set of predefined patterns (e.g., jokes, greetings, and general inquiries).

-Real-time response: Displays responses to users' queries on the web interface.

-Simple UI: Uses Streamlit to create an easy-to-use interface with minimal setup.

## Installation
To run this project locally, follow these steps:

**Clone the repository:**

git clone 'add your github repository here'

cd speech-enabled-chatbot


**Set up a virtual environment**

python -m venv venv

source venv/bin/activate    # For Linux/MacOS

venv\Scripts\activate       # For Windows

**Install the required dependencies:**
pip install -r requirements.txt

Ensure you have all necessary libraries installed:

Streamlit: For the web interface.
SpeechRecognition: For speech-to-text functionality.
NLTK: For the chatbot logic using pattern matching.
Pyttsx3: (Optional) For future text-to-speech features.
Download NLTK resources:

Inside the app.py file, the necessary NLTK package (punkt) is downloaded with the following command:

python
Copy code
nltk.download("punkt")
📄 Usage
To run the app:

Run the Streamlit app:

bash
Copy code
streamlit run app.py
Select input method:

Text Input: Type your question into the text box and click "Submit".
Speech Input: Ensure your microphone is connected, click "Start Recording", and speak your question.
Chatbot Interaction:

The chatbot will provide responses based on the predefined rules set in the code.
Example interactions:
User: What is your name?
Chatbot: My name is ChatBot. Nice to meet you!
User: Tell me a joke.
Chatbot: Why don't scientists trust atoms? Because they make up everything!
🧰 Technologies Used
Python: The programming language used to build the app.
Streamlit: For creating the interactive web interface.
SpeechRecognition: For converting speech to text.
NLTK: For handling the chatbot logic.
Pyttsx3: (Optional) For adding text-to-speech functionality in future updates.
🤝 Contributing
We welcome contributions to improve the project! Feel free to fork the repository and submit a pull request.

Fork the project
Create a new branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some amazing features')
Push to the branch (git push origin feature/AmazingFeature)
Open a pull request
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
