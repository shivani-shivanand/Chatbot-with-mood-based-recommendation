import os
from win32com.client import GetObject
import win32api

WMI = GetObject('winmgmts:')
processes = WMI.InstancesOf('Win32_Process')

for p in WMI.ExecQuery('select * from Win32_Process where Name="cmd.exe"'):
    
    os.system("taskkill /pid "+str(p.Properties_('ProcessId').Value))


#**************************************************************************************************************#

import io
import random
import string # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
import nltk
from nltk.stem import WordNetLemmatizer
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import subprocess
import os

from win32com.client import GetObject
import win32api


from tkthread import tk, TkThread     
import threading, time               

#**************************************************************************************************************#

warnings.filterwarnings('ignore')

#**************************************************************************************************************#

nltk.download('popular', quiet=True)                                                            # for downloading packages

#**************************************************************************************************************#

with open('chatbot.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#**************************************************************************************************************#
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words

#**************************************************************************************************************#

lemmer = WordNetLemmatizer()

#**************************************************************************************************************#

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

#**************************************************************************************************************#

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

#**************************************************************************************************************#

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#**************************************************************************************************************#

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

#**************************************************************************************************************#

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

#**************************************************************************************************************#

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

#**************************************************************************************************************#
    
flag=True
print("Moodbot")

#**************************************************************************************************************#

def face_detection():
    WMI = GetObject('winmgmts:')
    processes = WMI.InstancesOf('Win32_Process')

    for p in WMI.ExecQuery('select * from Win32_Process where Name="cmd.exe"'):
        os.system("taskkill /pid "+str(p.Properties_('ProcessId').Value))
    def newt():
        os.chdir(r"C:\Users\Shivani\Documents\1 final project\Chatbot with mood based recommendation\Emotion-detection\src")
        os.system('cmd /k "python emotions.py --mode display"')   
           # p=subprocess.call('start' , shell=True)
    t = threading.Thread(target=newt)
    t.start()
    
#**************************************************************************************************************#
    
def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    txt=msg.lower()
  #  txt=re.sub('[^a-zA-Z.\d\s]', '', txt)
    EntryBox.delete("0.0",END)

    print (msg)
    if(txt == 'bye'):
        ChatLog.config(state=NORMAL)
        send_message(msg)
        res = response(msg)
        bot_message("Bye! take care..")
          
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif(txt == 'hi' or txt=='hello' or txt=='hey'):
        ChatLog.config(state=NORMAL)
        send_message(msg)
        res = response(msg)
        bot_message("Hi..")
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
    elif(txt == 'how are you ?'):
        ChatLog.config(state=NORMAL)
        send_message(msg)
        
        res = response(msg)
        bot_message("I'm good, thanks for asking")
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

    elif(txt == 'about you' or txt=='who are you' or txt=='what do you do'):
        ChatLog.config(state=NORMAL)
        send_message(msg)
        
        res = response(msg)
        bot_message("I'm here to play you songs and recommend awesome movies, all of it based on your mood and not to forget you can always text me !")
           
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
    elif(txt=='thanks' or txt=='thank you' ):
        ChatLog.config(state=NORMAL)
        send_message(msg)
        
        res = response(msg)
        bot_message("You are welcome..")
          
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
    elif txt != '':
        ChatLog.config(state=NORMAL)
        send_message(msg)
       
        res = response(msg)
        bot_message(res)
          
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    else:
        pass

        
#**************************************************************************************************************#

base = Tk()
base.title("MoodBot")
base.geometry("400x600")
base.resizable(width=FALSE, height=FALSE)
base.configure(bg="#FDFD96")

base.iconbitmap("./icon2.ico")


canvas=Canvas(base,bg="#FDFD96")
canvas.grid(row=0,column=0,columnspan=2)
canvas.pack(fill=BOTH, expand=True)



#Create Chat window
ChatLog = Text(base, bd=0, bg="#FDFD96", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)


scrollbar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((386, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)


scrollbar.pack(side="right", fill="y")


SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#FF756D", activebackground="#3c9d9b",fg='black',
                    command= send )


EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")


#ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=14, y=482, height=50, width=267)
SendButton.place(x=280, y=482, height=50,width=105)

faceButton = Button(base, font=("Verdana",12,'bold'), text="My Mood", width="12", height=3,
                    bd=0, bg="#FF756D", activebackground="#3c9d9b",fg='black',
                    command= face_detection )
faceButton.place(x=14, y=538, height=50, width=372 )

#Chat bubbles

bubbles = []

class BotBubble1:
    def __init__(self,master,message=""):
        self.master = master
        self.frame = Frame(master,bg="light grey")
        self.i = self.master.create_window(350,350,window=self.frame, tags=('textmsg'), anchor=E) 
        Label(self.frame, wraplength=180, text=message,font=("Purisa", 12),bg="#ade6bb").grid(row=0, column=1,sticky="w",padx=5,pady=3)
        base.update_idletasks()
        self.master.create_polygon(self.draw_triangle(self.i), fill="light grey", tags=('textmsg'), outline="light grey")

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x2, y2 - 10, x2 + 15, y2 + 10, x2, y2

def send_message(msg1):
    if bubbles:
        canvas.move('textmsg', 0, -65)
    a = BotBubble1(canvas,message=msg1)
    bubbles.append(a)

class BotBubble:
    def __init__(self,master,message=""):
        self.master = master
        self.frame = Frame(master,bg="light grey")
        self.i = self.master.create_window(40,360,window=self.frame, tags=('textmsg'), anchor=W) 
        Label(self.frame, wraplength=180, text=message,font=("Purisa", 12),bg="#add8e6").grid(row=1, column=0,sticky="w",padx=5,pady=3)
        base.update_idletasks()
        self.master.create_polygon(self.draw_triangle(self.i), fill="light grey", tags=('textmsg'), outline="light grey")

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2

def bot_message(msg):
    if bubbles:
        canvas.move('textmsg', 0, -65)
    a = BotBubble(canvas,message=msg)
    bubbles.append(a)

msg="Hey there, I'm MoodBot, your friendly mood detecting chatbot and how can I help you today ?"
bot_message(msg)


base.mainloop()

#**************************************************************************************************************#





        

