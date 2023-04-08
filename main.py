import requests
import pyttsx3
import time

# Initializing the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Headers for making the API request
headers = {
    'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com',
    'x-rapidapi-key': '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'
}

# Function to fetch a random word from the WordsAPI
def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?number=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0:
            return data[0]
    print("Error fetching random word")
    return None

# Function to practice spelling a word
def practice_word(word):
    # Using the text-to-speech engine to say the word
    engine.say(word)
    engine.runAndWait()

    # Pausing the program to allow the user to read the word
    time.sleep(2)

    # Asking the user to spell the word
    user_input = input('Please spell the word: ')

    # Checking if the user wants to quit
    if user_input.lower() == 'quit':
        engine.say('Goodbye!')
        engine.runAndWait()
        return False

    # Checking if the user's input matches the correct spelling of the word
    while user_input.lower() != word:
        engine.say(f"Incorrect. The correct spelling is {word}.")
        engine.runAndWait()
        user_input = input(f'Please try again. The word is spelled "{word}". ')

    engine.say('Correct!')
    engine.runAndWait()
    return True

# Loop for the practice session
while True:
    # Getting a random word
    selected_word = get_random_word()

    # Calling the practice_word function with the selected word
    result = practice_word(selected_word)

    # Asking the user if they want to continue or quit
    user_input = input('Type "quit" to exit or press the Enter key to continue. ')

    if user_input.lower() == 'quit':
        engine.say('Goodbye!')
        engine.runAndWait()
        break

engine.say('Congratulations! You have practiced all the words.')
engine.runAndWait()
