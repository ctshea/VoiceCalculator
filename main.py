import speech_recognition as sr
import pyttsx3
import re
import operator


def calculate(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
        tts_op = "plus"
    elif operator == "-":
        result = num1 - num2
        tts_op = "minus"
    elif operator == "*":
        result = num1 * num2
        tts_op = "multiplied by"
    elif operator == "/":
        result = num1 / num2
        tts_op = "divided by"
    return result, tts_op

def trigger_word(trigger_word="calculator"):
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        engine.say("Starting program")
        engine.runAndWait()
        while True:
            try:
                audio = recognizer.listen(source)
                print(recognizer.recognize_google(audio))
                if (recognizer.recognize_google(audio) == trigger_word):
                    engine.say("Listening")
                    engine.runAndWait()
                    audio = recognizer.listen(source)
                    phrase = recognizer.recognize_google(audio)
                    print(phrase)
                    match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)', phrase)

                    if match:
                        num1 = int(match.group(1))
                        operator = match.group(2)
                        num2 = int(match.group(3))
                        result, tts_op = calculate(num1, operator, num2)
                        num1_string = str(num1)
                        num2_string = str(num2)
                        result_string = str(result)
                        new_phrase = (num1_string + tts_op + num2_string + "equals" + result_string)
                        engine.say(new_phrase)
                        engine.runAndWait()

                    else:
                        print("no match")

            except sr.UnknownValueError:
                print("unknown word")
                pass
            except sr.RequestError:
                print("ERROR")
                break

if __name__ == '__main__':
    trigger_word()

