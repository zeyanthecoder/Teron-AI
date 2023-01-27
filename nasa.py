import requests
import os
from PIL import Image
import pyttsx3

from TeronUi import takecommand

# from jarvis import takecommand

Api_Key = "v7wIjE8msJog8Hgw99aoEoDNVSzUc0ZSFcPinl0j"

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)

def speak(audio):
    print("      ")
    Assistant.say(audio)
    print(f":  {audio}")
    print("      ")
    Assistant.runAndWait()

def NasaNews(Date):

            speak("Extracting Data From Nasa For Your Search...")

            Url = "https://api.nasa.gov/planetary/apod?api_key="+str(Api_Key)

            Params = {'date':str(Date)}
            r = requests.get(Url,params = Params)
            Data = r.json()
            print(Data)
            Info = Data['explanation']
            title = Data['title']
            Image_Url = Data['url']
            Image_r = requests.get(Image_Url)
            print(Info)
            print(title)
            FileName = str(Date) + '.jpg'
            print(FileName)
            with open(FileName, 'wb') as f:
                f.write(Image_r.content)

            Path_1 = "C:\\Users\\zeyan\\OneDrive\\Desktop\\Teron 2.0\\" + str(FileName)
            Path_2 = "C:\\Users\\zeyan\\OneDrive\\Desktop\\Teron 2.0\\Nasa Images\\" + str(FileName)

            os.rename(Path_1, Path_2)

            img = Image.open(Path_2)

            img.show()

            speak(f"Title: {title}")
            speak(f"According To Nasa: {Info}")

def Mars():
    name = 'curiosity'
    date = '2020-12-3'
    Api = str(Api_Key)
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_Key}"
    r =  requests.get(url)
    Data = r.json()
    Photos = Data['photos'][:10]

    try:
        for index , photo in enumerate(Photos):
                camera = photo['camera']
                rover = photo['rover']
                rover_name = rover['name']
                camera_name = camera['name']
                full_camera_name = camera['full_name']
                data_of_photo = photo['earth_date']
                img_url = photo['img_src']
                p = requests.get(img_url)
                img = f'{index} .jpg'
                with open(img, 'wb') as file:
                    file.write(p.content)
                Path_1 = "C:\\Users\\zeyan\\OneDrive\\Desktop\\Jarvis\\" +str(img)
                # Path_2 = "C:\\Users\\zeyan\\OneDrive\\Desktop\\Jarvis\\Mars Images\\"+ str(img) 
                # os.rename(Path_1, Path_2)
                os.startfile(Path_1)
                speak(f"This Image Was Captured With : {full_camera_name}")
                speak(f"This Image Was Captured On {data_of_photo}")

    except:
            speak("There Was An Error!")

def DateConverter(Query):
    Date = takecommand()
    Date = Date.replace(" and ", "-")
    Date = Date.replace(" and ", "-")
    Date = Date.replace(" and ", "-")
    Date = Date.replace("  ", "")

    return str(Date)

def SolarBodies(Body):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    r = requests.get(url)
    Data = r.json()
    bodies = Data['bodies']
    Number = len(bodies)
    url2 = f"https://api.le-systeme-solaire.net/rest/bodies/ {Body}"
    rrr = requests.get(url2)
    data2 = rrr.json()
    print(data2)
    mass = data2['mass']['massValue']
    volume = data2['vol']['volValue']
    density = data2['density']
    gravity = data2['gravity']
    escape = data2['escape']
    speak(f"Number Of Bodies In Solar System: {Number}")
    speak(f"Volume Of {Body}  Is {volume} cubic meter ")
    speak(f"Density Of {Body}  Is {density} kilogram per cubic meter")
    speak(f"Gravity Of {Body}  Is {gravity} metres per second")
    speak(f"Escape Velocity Of {Body}  Is {escape} km/s")
