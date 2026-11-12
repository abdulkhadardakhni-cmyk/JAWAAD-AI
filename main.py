
import speech_recognition as sr
import pyttsx3
import sounddevice as sd
from brain import ask_jawaad


# =====================================
# JAWAAD VOICE INITIALIZATION
# =====================================

engine = pyttsx3.init()

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)


# =====================================
# JAWAAD SPEAK FUNCTION
# =====================================


def speak(text):
    print("\nJAWAAD:", text)

    try:
        engine.stop()
        engine.say(str(text))
        engine.runAndWait()

    except Exception as error:
        print("VOICE ERROR:", error)



# =====================================
# JAWAAD LISTEN FUNCTION
# =====================================

def listen():

    recognizer = sr.Recognizer()

    try:
        print("\nListening, sir... Speak now!")

        # Select your laptop microphone
        device_index = 1

        device_info = sd.query_devices(device_index, "input")
        sample_rate = int(device_info["default_samplerate"])

        # Record your voice for 5 seconds
        recording = sd.rec(
            int(5 * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
            device=device_index
        )

        sd.wait()

        # Convert audio for speech recognition
        audio = sr.AudioData(
            recording.tobytes(),
            sample_rate,
            2
        )

        # Convert voice into text
        command = recognizer.recognize_google(audio)

        print("\nYOU:", command)

        return command.lower()

    except sr.UnknownValueError:
        print("Sorry sir, I could not understand.")

    except sr.RequestError:
        speak("Voice recognition connection problem.")

    except Exception as error:
        print("MICROPHONE ERROR:", error)

    return ""


# =====================================
# START JAWAAD
# =====================================

speak("Hello ASLAM. I AM JAWAAD YOUR PERSONAL AI ASSISTANT IS ONLINE . I AM HERE TO HELP YOU WITH ANYTHING YOU NEED. HOW CAN I HELP YOU TODAY?")

speak("I am ready to assist you.")


# =====================================
# MAIN ASSISTANT LOOP
# =====================================

while True:

    command = listen()

    if not command:
        continue

    # Shutdown command
    if "shutdown" in command or "goodbye" in command:

        speak("Goodbye sir. JAWAAD shutting down.")

        break

    # Ask JAWAAD its name
    elif "your name" in command:

        speak("I am JAWAAD, your personal artificial intelligence.")

    # Ask AI questions
    else:
        speak("Processing your request, sir.")

        answer = ask_jawaad(command)

        if answer:
            print("\nJAWAAD ANSWER:", answer)
            speak(answer)
        else:
            speak("Sorry sir, I received an empty response.")