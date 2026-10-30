
import text_to_speech
import datetime
import webbrowser
import weather


def Action(data):

    if data is None or not data.strip():
        return "Sorry, I couldn't understand."

    user_data = data.lower()

    if "what is your name" in user_data:
        response = "My name is AI Assistant"
        text_to_speech.text_to_speech(response)
        return response

    elif "hello" in user_data or "hi" in user_data:
        response = "Hi sir, how can I help you?"
        text_to_speech.text_to_speech(response)
        return response

    elif "good morning" in user_data:
        response = "Good morning sir"
        text_to_speech.text_to_speech(response)
        return response

    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = current_time.strftime("%I:%M %p")
        response = "The current time is " + Time
        text_to_speech.text_to_speech(response)
        return response

    elif "shutdown" in user_data:
        response = "Completed"
        text_to_speech.text_to_speech(response)
        return response

    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        response = "Spotify is ready now"
        text_to_speech.text_to_speech(response)
        return response

    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        response = "YouTube is ready now"
        text_to_speech.text_to_speech(response)
        return response

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        response = "Google is ready now"
        text_to_speech.text_to_speech(response)
        return response

    elif "weather" in user_data:
        try:
            print("Weather action called")
            ans = weather.weather()
            print("Weather result:", ans)
            text_to_speech.text_to_speech(ans)
            return ans

        except Exception as e:
            print("Weather Error:", repr(e))
            response = "Sorry, I could not get the weather."
            text_to_speech.text_to_speech(response)
            return response

    else:
        response = "I am not able to understand. Please try again."
        text_to_speech.text_to_speech(response)
        return response
