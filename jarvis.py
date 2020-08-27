import pyttsx3                    # pip install pyttsx3
import datetime     
import speech_recognition as sr   #pip install SpeechRecognition
import pyaudio                    #pip install pipwin     then    pipwin install pyaudio
import wikipedia                  #pip install wikipedia
import smtplib                    #pip install smtplib
import webbrowser as wb           #pip install webbrowser
import os                       
import pyautogui                  #pip install pyautogui
import psutil                     #pip install psutil
import pyjokes                    #pip insall pyjokes

engine = pyttsx3.init()

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

# speak("This is friday")

def time():
	Time = datetime.datetime.now().strftime("%I:%M:%S")
	speak(Time)
	

# time()

def date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	day = int(datetime.datetime.now().day)
	speak("The current date is ")
	speak(day)
	speak(month)
	speak(year)

# date()

def wishme():
	hour = int(datetime.datetime.now().hour)
	if(hour>=6 and hour<12):
		speak("Good morning, sir")
	elif(hour>=12 and hour<16):
		speak("Good afternoon, sir")
	elif(hour>=16 and  hour<21):
		speak("Good Evening, sir")
	else:
		speak("Good Night, sir")

	speak("Welcome back!")
	speak("How I can help you?")


# wishme()
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio  = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio)
		
	except Exception as e:
		print(e)
		speak("Say that again please...")
		return "None"

	return query

# takeCommand()

# ================ SCREENSHOT============
def screenshot():
	img = pyautogui.screenshot()
	img.save("image/ss.jpg")

#================CPU====================
def cpu():
	usage = str(psutil.cpu_percent())
	speak("CPU is at "+usage)

#================BATTERY=============
def battery():
	battery = psutil.sensors_battery()
	speak("battery is at ")
	percent = str(battery.percent)
	speak(percent+" percent")

#===============JOKES==============
def jokes():
	speak(pyjokes.get_joke())


#===================EMAIL============
def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login("YOUR EMAIL ID","YOUR EMAIL PASSWORD")
	server.sendmail("YOUR EMAIL ID",to,content)          # AFTER THAT U HAVE TO MAKE EMAIL LESS SECURE TO APPS (SEARCH ON GOOGLE HOW TO DO)
	server.close()

#==============================MAIN=======================
if __name__ == "__main__":
	wishme()

	while True:
		query = takeCommand().lower()
		

		if "time" in query:
			time()
		elif "date" in query:
			date()
		

		elif "wikipedia" in query:
			speak("Searching...")
			query = query.replace("wikipedia","")
			result = wikipedia.summary(query,sentences =2)
			print(result)
			speak(result)

		elif "send email" in query:
			try:
				speak("Enter email address On which you want to send email: ")
				to = input("To: ")
				speak("What should i say")
				content = takeCommand()
				
				sendEmail(to,content)
				speak("the mail sent successfully")
			except Exception as e:
				speak(e)
				speak("Unable to send mail")

		elif "chrome" in query :
			speak("What should i search?")
			search = takeCommand().lower()
			print(search)
			wb.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(search+".com")
		
		elif "logout" in query and ("system" in query or "laptop" in query):
			speak("loging out...")
			os.system("shutdown - l")

		elif "shut down" in query and ("system" in query or "laptop" in query):
			speak("shutting down...")
			os.system("shutdown /s /t 1")

		elif "restart" in query and ("system" in query or "laptop" in query):
			speak("restarting...")
			os.system("shutdown /r /t 1")


		elif "play song" in query:
			songs_dir = "E:\Music"
			songs = os.listdir(songs_dir)
			os.startfile(os.path.join(songs_dir, songs[0]))

		elif "remember that" in query:
			speak("What should I remeber?")
			data = takeCommand()
			speak("you said me to remeber "+data)
			remeber = open("remember/data.txt","w")
			remeber.write(data)
			remeber.close()

		elif ("do you know" in query) and ("remember" in query):
			remember = open('remember/data.txt','r')
			speak("you said me to remember that "+remember.read())
			remember.close()

		elif "screenshot" in query:
			screenshot()
			speak("done")

		elif "cpu" in query:
			cpu()

		elif "battery" in query:
			battery()

		elif "joke" in query:
			jokes()


		elif( ('run' in query or 'execute' in query or 'open' in query) and "photoshop" in query):
			print("Running photoshop! ")
			speak("Running photoshop! ")
			os.system("start photoshop")

		elif( ('run' in query or 'execute' in query or 'open' in query) and "chrome" in query ):
			print("Running chrome!")
			speak("Running chrome")
			os.system("chrome")

		elif( ('run' in query or 'execute' in query or 'open' in query) and "notepad" in query):
			print("Running notepad! ")
			speak("Running notepad")
			os.system("notepad")
		
		elif(  ('run' in query or 'execute' in query or 'open' in query) and "editor" in query):
			print("Which Editor notepad or sublime? ")
			speak("Which Editor, notepad or sublime? ")
			permit = takeCommand().lower()
			if("sublime" in permit):
				print("Running sublime! ")
				speak("Running sublime")
				os.system("subl")
			elif("notepad" in permit):
				print("Running notepad! ")
				speak("Running notepad")
				os.system("notepad")

		elif ( ('run' in query or 'execute' in query or 'open' in query) and "sublime" in query ):
			print("Running sublime! ")
			speak("Running sublime")
			os.system("subl")

		elif(  ('run' in query or 'execute' in query or 'open' in query) and "illustrator" in query):
			print("Running illustrator!")
			speak("Running illustrator")
			os.system("start illustrator")

		elif (("exit" in query ) or ("close" in query) or ("stop" in query) or ("offline" in query) or ("bye" in query)):
			print("Thank you Sir, Bye!")
			speak("Thank you Sir! Bye")
			hour = datetime.datetime.now().hour
			if(hour>=22 and hour<3):
				speak("good night")
			quit()

		elif("how are you" in query):
			print("I'm Fine sir. How can i Help You? ")
			speak("I'm Fine sir. How can i Help You? ")


		else:
			speak("I'm Unable to understand. Please try again")

