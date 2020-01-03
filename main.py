import sys

print("Witaj")

email = input("Podaj swój email: ") 

from getpass import getpass
password = getpass("A teraz podaj swoje hasło	\nHasło nie będzie widoczne podczas wpisywania: ")

from librus_tricks import create_session  
session = create_session(email, password)

#from appJar import gui #appJar doesnt work properly yet.
#app = gui()

exams = session.exams()  
print("Oto nadchodzące egzaminy: ")
print(*exams) 

# Get selected grades  
#grades = session.grades()  
#print(*grades)  
# + 2+ np - 5 + 

# Get timetable  
plan = input("Czy twoja szkoła udostępniła plan lekcji i chcesz go zobaczyć?")
if plan in ["Tak","tak"]:
	timetable = session.today_timetable  
	print(*timetable.lessons)  
else:
	if plan in ["Nie", "nie"]:
		pass
# {} {} {} Język angielski Język angielski Matematyka Matematyka Informatyka Informatyka {} {}  

mobilne = input("Czy posiadasz mobilne dodatki które pozwalają ci widzieć wiadomości? (tak/nie)")
if mobilne in ["tak","Tak"]:
	messages = session.messages()
	print("Oto wszystkie wiadomości")
	print(*messages)
else:
	if mobilne in ["nie,", "Nie"]:
		print("My też nie, 3 dychy to za dużo :p ")
		exit()



#if mobilne == tak:
#	messages = session.messages()
#	print("Oto wszystkie wiadomości")
# 	print(*messages)
#else:
#	print("My też nie, 3 dychy to za dużo :p ")
#	sys.exit(0)
#messages = session.messages() # Requires mobilne dodatki  
#print("Oto wszystkie wiadomośći: ")
#print(*messages)  
#messages = session.message_reader.read_messages() # Uses html scrapper to read messages, doesn't require mobilne dodatki print(*messages)  
