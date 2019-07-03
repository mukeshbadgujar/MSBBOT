# This File Is For Bot Working  The Bot Name Is Raju
import botfunction,botarguments
import random
import speech_recognition as sr

greetings = ('hi', 'hello', 'raju')
rajuResponse = ('Hello MSB, How can i help you')


def ask_raju():
    for word in userInput.split():
        if word.lower() in greetings:
            return rajuResponse   # random.choice(rajuResponse)


userInput = input("Enter Your Arg :")
print(ask_raju())

