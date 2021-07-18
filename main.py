from morse import morse_dictionary

text_to_translate = input("Type something to translate to morse code: ").lower()

if all(char in morse_dictionary for char in text_to_translate):
    morse_word = [morse_dictionary[letter] for letter in text_to_translate if letter != " "]
    print(morse_word)
else:
    text_to_translate = input("Invalid input detected, please type something to translate to morse code: ").lower()
