import os
import pyttsx3
pyttsx3.speak("welcome to artificial searching chatroom")
while True:	
	print("\n\n")
	print("				WELCOME TO ARTIFICIAL SEARCHING CHATROOM")
	print("				________________________________________")
	print("\n")
	print("				Following applications can be searched: ")
	print("")
	print("					Internet Surfing App                 ")
	print("				               Notepad                  ")
	print("				          Windows Media Player          ")
	print("				               VS Code                  ")
	print("						Wordpad                  ")
	print("						 Excel                 ")
	print("						 Paint                ")
	print("\n")
	print("				*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
	print("\n")
	print("			    Chat with me,which application you want to open?")
	print("\n")
	p=input("                       Type here:")
	p=p.lower()  
	print("\n\n")
	if ("don't" in p)or("do not" in p)or("didn't" in p)or("did not" in p)or("no" in p):
		pyttsx3.speak("As you directed,not opening your suggested app")	
		print("                     As you directed,not opening your suggested app")
		print("                     ______________________________________________")
	else:
		if (("run" in p)or("open" in p)or("start" in p)or("launch" in p)) and (("notepad" in p)or("editor" in p)):
			pyttsx3.speak("opening notepad")	
			print("                           Notepad has been opened")
			os.system("notepad")
		elif (("run" in p)or("open" in p)or("start" in p)or("launch" in p))and("internet surfing app" in p):
			print("          Choose the internet surfing application from the list given below:")
			print("                                     Chrome                       ")
			print("                                     Firefox                       ")
			print("                                 Internet Explorer                      ")
			q=input("               Type here:")
			q=q.lower()	
			if (("run" in q)or("open" in q)or("start" in q)or("launch" in q)) and ("chrome" in q):
				pyttsx3.speak("opening chrome")	
				print("                      Chrome has been opened")		
				os.system("chrome")
			elif (("run" in q)or("open" in q)or("start" in q)or("launch" in q)) and ("firefox" in q):	
				pyttsx3.speak("opening mozilla firefox")	
				print("                   Mozilla firefox has been opened")
				os.system("firefox")
			elif (("run" in q)or("open" in q)or("start" in q)or("launch" in q))and("internet explorer" in q) or ("Internet explorer" in q):
				pyttsx3.speak("opening internet explorer")	
				print("                   Internet explorer has been opened")
				os.system("iexplore")
			else:
				pyttsx3.speak("SORRY! no such application available")
				print("                        SORRY! No such application available in the list")
		elif (("run" in p)or("open" in p)or("start" in p)or("launch" in p))and("vs code" in p):
			pyttsx3.speak("opening V s code")	
			print("                                VScode has been opened")
			os.system("Code")
		elif (("run" in p)or("open" in p)or("start" in p)or("launch" in p)) and ("wordpad" in p):
			pyttsx3.speak("opening wordpad")	
			print("                                Wordpad has been opened")
			os.system("wordpad")
		elif (("run" in p)or("open" in p)or("play" in p)or("start" in p)or("launch" in p))and(("wmplayer" in p)or("player" in p) or ("song" in p)):
			pyttsx3.speak("opening windows media player")	
			print("                             Windows media player has been opened")
			os.system("wmplayer")
		elif (("run" in p)or("open" in p)or("start" in p)or("launch" in p)) and ("excel" in p):
			pyttsx3.speak("opening excel")	
			print("                                    Excel has been opened")
			os.system("excel")
		elif (("run" in p)or("open" in p)or("start" in p)or("launch" in p)) and ("paint" in p):
			pyttsx3.speak("opening paint")	
			print("                                     Paint has been opened")
			os.system("mspaint")
		elif ("thanks" in p)or("thank you" in p)or("thank" in p):
			pyttsx3.speak("It's my pleasure!")	
			print("                                       It's my pleasure!")
		elif ("angry" in p)or("annoying" in p)or("late" in p)or("annoy" in p):
			pyttsx3.speak("Sorry to hear that,we will try better next time")	
			print("                              Sorry to hear that,we will try better next time!")
		elif ("hi" in p)or("hello" in p)or("hey" in p):
			pyttsx3.speak("hi,how can i help you?")	
			print("                                      Hi! How can I help you?")
		elif ("ok" in p)or("okay" in p):
			pyttsx3.speak("okay!")	
			print("                                              :);)")
		elif (len(p)==0):
			pyttsx3.speak("i haven't received any input from you.")	
			print("                                 I haven't received any input from you")
		elif ("exit" in p)or("end" in p)or("quit" in p):
			pyttsx3.speak("Thankyou for chatting with us")
			print("                                 Thankyou for chatting with us        ")
			break
		else:
			pyttsx3.speak("SORRY! no such application available")
			print("                        SORRY! No such application available in the list")