from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine=pp.init()
voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("College Enquiry Chatbot Created by MEET")

convo =[
    'hi',
    'Hello! .....Welcome to College Portal....Please type your enquiry to continue the chat. !',
    'Tell me about college facilities',
    'College provides hostel facilities, playground, labs equipped with high end systems',
    'Placements',
    'Our college proudly places 90% of its students every year',
    'Tell me about college timings',
    'The timings are as follows :- 1. For morning shift - 9:00 am to 4:00 pm',
    'Tell me about Scholarship',
    ' College provides scholarship to the students who'
    ' score high percentage.',
    'Tell me number of admissions',
    'Our college receives 60 students per batch every year',
    'Department Available', 
    'CSE, IT, ECE, EEE',
     'Okay thanks',
    'Any other query.....?',
     'NO',
    'Okay have a nice day...']

trainer = ListTrainer(bot)

# now training the bot with help of trainer

trainer.train(convo)

#answer=bot.get_response("what is your name?")
#print(answer)
'''
print("Talk to Bot")
while True:
    query=input()
    if query=='exit':
        break
    answer = bot.get_response(query)
    print("bot :", answer)
'''
root = Tk()

root.geometry("600x750")

root.title("My Chat bot")
img = PhotoImage(file="bot.png")

photoL=Label(root,image=img,height=300,width=500)

photoL.pack(pady=5)

# take query :  it takes audio from user and converts it to string.
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening...try to speak....")
    with s.Microphone() as m:
        audio=sr.listen(m)
        query=sr.recognize_google(audio,language='eng_in')
        print(query)
        textF.delete(0,END)
        textF.insert(0,query)
        ask_from_bot()
def ask_from_bot():
    query = textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you : " + query)
    msgs.insert(END,"bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)
frame = Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)

sc.pack(side=RIGHT,fill = Y)

msgs.pack(side=LEFT,fill=BOTH,pady=10)

frame.pack()

# creating text field

textF=Entry(root,font=("Verdana",20))
textF.pack(fill=X,pady=10)

btn=Button(root,text="Ask from bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()

# going to bind main window with enter key...

root.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)
t.start()

root.mainloop()
