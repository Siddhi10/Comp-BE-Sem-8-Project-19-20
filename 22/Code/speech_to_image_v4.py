#!/usr/bin/env python
# coding: utf-8




import speech_recognition as sr
import sys
import glob
import cv2
import string
from tkinter import *
from functools import partial
import tkinter.font
from PIL import ImageTk,Image
import time





def speak():
    r=sr.Recognizer()
    with sr.Microphone(device_index=8,chunk_size=3024) as source:
        #saving the voice input in variable audio
        audio=r.listen(source,timeout=5,phrase_time_limit=5)

        
        try:
            inputDialogue=r.recognize_google(audio)
#             label3=Label(root,text='You Said: '+inputDialogue,fg='blue',font=tk_font,bg='#fff')
#             label3.place(relx=.5,rely=.2,anchor=CENTER)
#             inputDialogue='good morning how are you'
            process_text(inputDialogue)
        except:
            label1=Label(root,text='COULD NOT RECOGNIZE',fg='blue',font=tk_font,bg='#fff')
            label1.place(relx=.5,rely=.2,anchor=CENTER)
            root.update()
            time.sleep(2)
            label1.destroy()





def process_text(inputDialogue):
    
    
    wordsSpoken=inputDialogue.split()
    numberOfWordsSpoken=len(wordsSpoken)
    #to lower case
    for i in range(numberOfWordsSpoken):
        wordsSpoken[i]=wordsSpoken[i].lower()
                    
    
    for i in range(numberOfWordsSpoken):
        
        for words in glob.glob('./images/*'):
            actualWord=words.split("/")[2].split(".")[0]
            if actualWord !=wordsSpoken[i]:
                 continue
            else:
       
                label2=Label(root,text=actualWord,fg='blue',font=tk_font,bg='#fff')
                label2.place(relx=.5,rely=.25,anchor=CENTER)
                load = Image.open(words)
                render = ImageTk.PhotoImage(load)
                
                img = Label(root, image=render)
                img.image = render
                
                img.place(relx=.5, rely=.6, anchor=CENTER)
                root.update()
                time.sleep(3)
                img.destroy()
                label2.destroy()
               
                break





root = Tk()
root.geometry('1000x800+0+0')
root.title('Speech To Sign Language')
root.config(bg="#fff")

tk_font=tkinter.font.Font(root=root,family='Times',size='16')


speak_btn=Button(root,text='SPEAK',font=tk_font,width=25,height=3,bg='#42f498',fg='#fff',command=speak)
speak_btn.place(relx=.5, rely=.1, anchor=CENTER)

root.mainloop()






