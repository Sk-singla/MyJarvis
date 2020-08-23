import pyttsx3
import os

print("Hey! How can i help You? ")
pyttsx3.speak("Hey! How can i help You? ")



while(True):
	chat = input("\n>>>")
	print()
	
	if( ('run' in chat or 'execute' in chat or 'open' in chat) and "photoshop" in chat):
		print("Running photoshop! ")
		pyttsx3.speak("Running photoshop! ")
		os.system("start photoshop")

	elif( ('run' in chat or 'execute' in chat or 'open' in chat) and "chrome" in chat ):
		print("Running chrome!")
		pyttsx3.speak("Running chrome")
		os.system("chrome")

	elif( ('run' in chat or 'execute' in chat or 'open' in chat) and "notepad" in chat):
		print("Running notepad! ")
		pyttsx3.speak("Running notepad")
		os.system("notepad")
	
	elif(  ('run' in chat or 'execute' in chat or 'open' in chat) and "editor" in chat):
		print("Which Editor notepad or sublime? ")
		pyttsx3.speak("Which Editor, notepad or sublime? ")
		permit = input()
		if("sublime" in permit):
			print("Running sublime! ")
			pyttsx3.speak("Running sublime")
			os.system("subl")
		elif("notepad" in permit):
			print("Running notepad! ")
			pyttsx3.speak("Running notepad")
			os.system("notepad")

	elif ( ('run' in chat or 'execute' in chat or 'open' in chat) and "sublime" in chat ):
		print("Running sublime! ")
		pyttsx3.speak("Running sublime")
		os.system("subl")

	elif(  ('run' in chat or 'execute' in chat or 'open' in chat) and "illustrator" in chat):
		print("Running illustrator!")
		pyttsx3.speak("Running illustrator")
		os.system("start illustrator")

	elif (("exit" in chat ) or ("close" in chat) or ("stop" in chat)):
		print("Thank you Sir, Bye!")
		pyttsx3.speak("Thank you Sir! Bye")
		break

	elif("how are you" in chat):
		print("I'm Fine sir. How can i Help You? ")
		pyttsx3.speak("I'm Fine sir. How can i Help You? ")


	else:
		print("Sorry I'm Unable to Understand. Please repeat! ")
		pyttsx3.speak("Sorry I'm Unable to Understand. Please repeat! ")


