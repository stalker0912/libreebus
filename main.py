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
#	timetable = session.today_timetable  
#print(*timetable.lessons)  
# {} {} {} Język angielski Język angielski Matematyka Matematyka Informatyka Informatyka {} {}  

#mobilne = str(input("Czy posiadasz mobilne dodatki które pozwalają ci widzieć wiadomości? (tak/nie)"))

mobilne = input("Czy posiadasz mobilne dodatki które pozwalają ci widzieć wiadomości? (tak/nie)")
if answer in ["tak","Tak","nie,", "Nie"]:
	messages = session.messages()
	print("Oto wszystkie wiadomości")
	print(*messages)
else:
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
