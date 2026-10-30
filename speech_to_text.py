
import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")
        voice_data = r.recognize_google(audio)
        print("You said:", voice_data)
        return voice_data

    except sr.UnknownValueError:
        print("Could not understand your voice.")
        return None

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return None

    except sr.RequestError as e:
        print("Google Speech Recognition error:", e)
        return None

    except OSError as e:
        print("Microphone error:", e)
        return None
