from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import wolframalpha
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import base64



class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = Canvas(parent, width=500, height=500)     
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(Image.open('maingif.gif'))]
        self.image = self.canvas.create_image(250,250, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'name':'your email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window1 = Tk()
window1.configure(bg="Black")
window1.geometry("1000x800")


#create a mainframe.
main_frame=Frame(window1)
main_frame.pack(fill=BOTH,expand=1)

# Create Frame for X Scrollbar
sec = Frame(main_frame)
sec.pack(fill=X,side=BOTTOM)


#create a Canvas
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT ,fill=BOTH,expand=1)

#add a scrollbar to the canvas
my_scrollbar=Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

my_scrollbarx=Scrollbar(main_frame,orient=HORIZONTAL,command=my_canvas.xview)
my_scrollbarx.pack(side=BOTTOM,fill=X)

#configure the canvas
my_canvas.configure(bg ="Black",xscrollcommand=my_scrollbarx.set)
my_canvas.configure(bg ="Black",yscrollcommand=my_scrollbar.set)

my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))



#create another frame inside the canvas
sec_frame=Frame(my_canvas)

#Add that new frame to a window in the canvas
my_canvas.create_window((400,0),window = sec_frame,anchor="nw")


#defining image
bg=PhotoImage(file="bg.png")
#create a label
my_label=Label(sec_frame,text="Welcome!",image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)




global var
global var1

var = StringVar()
var1 = StringVar()

password="Senders Email Password"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akshaychaturvedi544@gmail.com', password) # email id - use any email id whose security/privacy is off
    server.sendmail('akshaychaturvedi544@gmail.com', to, content)
    server.close()
    
username="Shiva Sir!"
ainame="Jarvis 1.o"
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set(f"Good Morning {username}") #Name - your Name
        sec_frame.update()
        speak(f"Good Morning {username}")
    elif hour >= 12 and hour <= 18:
        var.set(f"Good afternoon {username}")
        sec_frame.update()
        speak(f"Good afternoon {username}")
    else:
        var.set(f"Good evening {username}")
        sec_frame.update()
        speak(f"Good evening {username}")
    speak(f"Myself {ainame} How may I help you sir") #BotName - Give a name to your assistant

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        sec_frame.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        sec_frame.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        var.set(f"{username}, Can you repeat the command please?")
        sec_frame.update()
        speak(f"{username}, Can you repeat the command please?")
        return "None"
    
    var1.set(query)
    sec_frame.update()
    return query

def takeEmail():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        sec_frame.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        sec_frame.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        var.set(f"{username}, Can you repeat the command please?")
        sec_frame.update()
        speak(f"{username}, Can you repeat the command please?")
        return "None"
    
    var1.set(query)
    sec_frame.update()
    return query.replace(" ","")

count=0

def play():
    global count
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    if count==0:
        wishme()
    count=1
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'thank you' in query:
            var.set(f"It was Pleasure Helping You {username}")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            sec_frame.update()
            speak(f"It was Pleasure Helping You {username}")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to wikipedia")
                    #var.set("".join(l[0:len(l)//3])+"\n"+"".join(l[len(l)//3:len(l)*(2//3)])+ "\n" +"".join(l[len(l)*(2//3):]))
                    #z=results[0:len(results)//2]+"\n"+results[len(results)//2:]
                    l=results.split(" ")
                    n=len(l)
                    a1 = " ".join(l[0:5]) + "\n"+  " ".join(l[5: 10])+"\n" +" ".join(l[10:15])
                    var.set(a1)
                    sec_frame.update()
                    speak(results)
                except Exception as e:
                    var.set(f"sorry {username}, could not find any result")
                    sec_frame.update()
                    speak(f"sorry {username}, could not find any result")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'open youtube' in query:
            var.set('opening Youtube')
            sec_frame.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'open course era' in query:
            var.set('opening course era')
            sec_frame.update()
            speak('opening course era')
            webbrowser.open("coursera.com")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'open google' in query:
            var.set('opening google')
            sec_frame.update()
            speak('opening google')
            webbrowser.open("google.com")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'hello' in query:
            var.set('Hello Sir')
            sec_frame.update()
            speak("Hello Sir")
			
        elif 'open stack overflow' in query:
            var.set('opening stack overflow')
            sec_frame.update()
            speak('opening stack overflow')
            webbrowser.open('stackoverflow.com')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            sec_frame.update()
            speak('Here are your favorites')
            os.startfile("C:\\Users\Rajnish Chanchal\Desktop\Amazon Music.lnk")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break 

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" %strtime)
            sec_frame.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            sec_frame.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'what can you do for me' in query:
            var.set('I can do multiple tasks including calculation,browsing,weather update etc.,"\n" tell me whatever you want me to perform sir')
            sec_frame.update()
            speak('I can do multiple tasks including calculation,browsing,weather update etc.,"\n" tell me whatever you want me to perform sir')

        elif 'how old are you' in query:
            var.set("I am mature enough to help you sir")
            sec_frame.update()
            speak("I am mature enough to help you sir")

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            sec_frame.update()
            speak("opening V L C media player")
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player.lnk" #Enter the correct Path according to your system
            os.startfile(path)
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'your name' in query:
            var.set(f"Myself {ainame} Sir")
            sec_frame.update()
            speak(f'myself {ainame} sir')

        elif 'created you' in query:
            var.set('My Creator is Shivanshu and Rajnish')
            sec_frame.update()
            speak('My Creator is Shivanshu and Rajnish')

        elif 'say hello' in query:
            var.set(f'Hello Everyone! My self {ainame}')
            sec_frame.update()
            speak(f'Hello Everyone! My self {ainame}')

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            sec_frame.update()
            speak("Opening Google Chrome")
            path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk" #Enter the correct Path according to your system
            os.startfile(path)
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif 'send email' in query:
            try:
                var.set("What should I say")
                sec_frame.update()
                speak('what should I say')
                content = takeCommand()
                var.set('please give me reciever email id')
                sec_frame.update()
                speak('please give me reciever email id')
                
                to = takeEmail()
                
                var.set(f"sending email to {to}")
                sec_frame.update()
                var.set(f'confirm send email to {to}')
                sec_frame.update()
                speak(f'confirm send email to {to}')
                confirm=takeCommand()
                if 'yes' in confirm:
                    sendemail(to, content)
                    var.set('Email has been sent!')
                    sec_frame.update()
                    speak('Email has been sent!')
                elif 'no' in confirm:
                    var.set('email sending cancelled')
                    sec_frame.update()
                    speak('email sending cancelled')
                
            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                sec_frame.update()
                speak('Sorry Sir! I was not able to send this email')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
		
        elif "open python" in query:
            var.set("Opening Python Idle")
            sec_frame.update()
            speak('opening python Idle')
            os.startfile('C:\\Users\Rajnish Chanchal\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\IDLE (Python 3.8 64-bit)') #Enter the correct Path according to your system
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
        
        elif "write a note" in query:
            var.set('What should i write,sir')
            sec_frame.update()
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            var.set('Sir, should i include date and time')
            sec_frame.update()
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                var.set('done sir')
                sec_frame.update()
                speak('done sir')
            else:
                file.write(note)
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
                
        elif "show notes" in query:
            var.set('Showing Notes')
            sec_frame.update()
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            file.read()
            var.set(f'{file.read(6)}')
            sec_frame.update()
            speak(file.read(6))
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break

        elif "calculate" in query: 
             
            try:
                app_id = "V7KLV6-Y5GQ54UQR7"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate') 
                query = query.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer = next(res.results).text
                var.set(f"The answer is {answer} '\n' {answer} '\n' {answer} '\n' {answer}")
                sec_frame.update()
                speak(f"The answer is {answer}")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
            except:
                var.set("No result")
                sec_frame.update()
                speak("No result")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break
        
        elif "what is" in query or "who is" in query:
            app_id = "V7KLV6-Y5GQ54UQR7"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
             
            try:
                var.set(f"{next(res.results).text}")
                sec_frame.update()
                speak(f"{next(res.results).text}")
            except StopIteration:
                var.set("No results")
                sec_frame.update()
                speak("No results }")
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            break


label2 = Label(sec_frame, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said: Nothing Yet')
label2.pack()

label1 = Label(sec_frame, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

window1.title('JARVIS')

app=App(sec_frame)

btn0 = Button(sec_frame, text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(sec_frame, text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(sec_frame, text = 'EXIT',width = 20, command = window1.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()
window1.mainloop()
