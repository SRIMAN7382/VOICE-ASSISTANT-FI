import ctypes
import os
import subprocess
import winshell as winshell
import pyttsx3
import pywhatkit
import requests,json
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing



def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query




def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def self(args):
    pass


def tellTime():
    # This method will give the time
    time = str(datetime.datetime.now())

    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # nd then after slicing we can get time
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")



def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("hello sriman i am HIFI HOW MAY I HELP YOU")


def current_pressure():
    pass


def Take_query():
    # calling the Hello function for
    # making it more interactive
    Hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while (True):

        # taking the query and making it into
        # lower case so that most of the times
        # query matches and we get the perfect
        # output
        query = takeCommand().lower()
        if "open facebook" in query:
            speak("Opening facebook ")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            webbrowser.open("www.facebook.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.open("www.youtube.com")
        elif "open amazon" in query:
            speak("Opening amazon")
            webbrowser.open("www.amazon.in")
        elif "open insta" in query:
            speak("Opening insta")
            webbrowser.open("www.instagram.com")
        elif "open flipkart" in query:
            speak("Opening flipkart")
            webbrowser.open("www.flipkart.com")
        elif "open myntra" in query:
            speak("Opening myntra")
            webbrowser.open("www.myntra.com")
        elif "open sastra" in query:
            speak("Opening sastra")
            webbrowser.open("www.sastra.edu")
        elif "open micro" in query:
            speak("Opening micro")
            webbrowser.open("www.microsoft.com")
        elif "open mail" in query:
            speak("Opening mail")
            webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")
        elif 'play' in query:
            speak("playing...")
            song = query.replace('play','')
            pywhatkit.playonyt(song)
        elif 'open brave' in query:
            codePath = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            os.startfile(codePath)
        elif 'open zoom' in query:
            codePath = r"C:\Users\apple\AppData\Roaming\Zoom\bin\Zoom.exe"
            os.startfile(codePath)
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by SIMIAN")
        elif 'lock windows' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call('shutdown / h')
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif "weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "14f6e551a5c29e23c1c9708b66c41f3a"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                # current_pressure = y["pressure"]
                # current_humidiy = y["humidity"]
                z = x["weather"]

                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))



        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")






        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. THANKS FOR USING ME")
            exit()

        elif "who is" in query:

            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("who is", "")

            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am HIFI. Your deskstop Assistant")


if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()
