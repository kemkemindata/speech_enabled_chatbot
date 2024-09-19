
# ---------------- New code -------------------
import speech_recognition as sr
import nltk
from nltk.chat.util import Chat
import streamlit as st
import pyttsx3

# Load the chatbot algorithm
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
       [
        r"what is your name",
        ["My name is ChatBot. Nice to meet you!",]
    ],
     [
        r"how are you",
        ["I'm doing well, thank you! How about you?"]
    ],
    [
        r"tell me a joke",
        ["Sure! Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"how old are you",
        ["I am an AI, so I don't have an age!"]
    ],
    [
        r"what is the meaning of life",
        ["The meaning of life is subjective and can vary for each individual."]
    ],
    [
        r"where are you from",
        ["I am an AI-based chatbot and don't have a physical location."]
    ],
    [
        r"what are your hobbies",
        ["As an AI, I don't have hobbies, but I enjoy assisting and providing information."]
    ],
    [
        r"do you have any pets",
        ["I'm afraid I don't have any pets. I'm purely a digital entity."]
    ],
    [
        r"what is your favorite color",
        ["I don't have a favorite color since I don't possess personal preferences."]
    ],
    # Add more patterns and responses here
]

chatbot = Chat(pairs)

# Function to transcribe speech into text using speech recognition
def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
    try:
        st.write("Transcribing...")
        text = r.recognize_google(audio)
        st.write("You said:", text)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand your speech.")
    except sr.RequestError:
        st.write("Sorry, there was an issue with the speech recognition service.")

# Function to generate a response from the chatbot
def get_chatbot_response(user_input):
    return chatbot.respond(user_input)

# Streamlit app
def main():
    st.title("Speech-enabled Chatbot")
    st.sidebar.image('pngwing.com (20).png')

    # User input method selection
    input_method = st.radio("Select input method:", ("Text", "Speech"))

    if input_method == "Text":
        user_input = st.text_input("User Input:")
        if st.button("Submit"):
            response = get_chatbot_response(user_input)
            st.text_area("Chatbot Response:", value=response)

    elif input_method == "Speech":
        st.write("Please ensure you have a microphone connected to your device.")
        if st.button("Start Recording"):
            user_input = transcribe_speech()
            response = get_chatbot_response(user_input)
            st.text_area("Chatbot Response:", value=response)

            # chat_history = []

            # chat_history.append({"user": user_input, "chatbot": chatbot_response})

            # Assuming you have a chat_history_container element in your HTML
        # st.sidebar.title("Chat History")


        # for entry in chat_history:
        #     user_input = entry["user"]
        #     chatbot_response = entry["chatbot"]
        #     # Update the chat_history_container element with the user input and chatbot response
        #     # For example, you can use JavaScript or a templating library to dynamically update the HTML
        #     chatbot_response = entry["chatbot"]
        #     st.write(f"User: {user_input}")
        #     st.write(f"ChatBot: {chatbot_response}")


if __name__ == "__main__":
    nltk.download("punkt")  # Download the necessary NLTK data
    main()



# chat_history = []

# user_input = "Hello"
# chatbot_response = "Hi, how can I assist you?"
# chat_history.append({"user": user_input, "chatbot": chatbot_response})

# # Assuming you have a chat_history_container element in your HTML
# for entry in chat_history:
#     user_input = entry["user"]
#     chatbot_response = entry["chatbot"]
#     # Update the chat_history_container element with the user input and chatbot response
#     # For example, you can use JavaScript or a templating library to dynamically update the HTML