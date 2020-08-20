import os
import pyttsx3 
import winsound
color_b = ( 'e4' , '01' , 'e0' , '01' , '02' , '04' , '05' , '06' , '07' , '08' )
i = 0
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 


def beep_sound():
	return winsound.Beep(1000,100)


engine.say("Hello Welcome in the menu")
engine.say("Choose the options given below")
engine.runAndWait()



while True:
	
	print("""##########################################\n********CHOOSE OPTIONS FROM BELOW********\n##########################################""")
	
	
	print("""Press 1 for open Google Chrome
	\nPress 2 for open Notepad
	\nPress 3 for open Windows Media Player
	\nPress 4 for End the program""")
	cmd_input = int(input())

	os.system("COLOR  " + color_b[i] )
	i = i +1

	if cmd_input==1:
		beep_sound()
		os.system("chrome")
	elif cmd_input==2:
		beep_sound()
		os.system("notepad")
	elif cmd_input==3:
		beep_sound()
		os.system("wmplayer")
		continue
	else:
		engine.say("THANK YOU")
		engine.runAndWait()
		break
	

