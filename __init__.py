import cv2
import numpy as np
from tkinter import *
import tkinter.font
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from PIL import ImageTk,Image
from bs4 import BeautifulSoup
from datetime import date
from googlesearch import search
import csv
import time, vlc
import pandas as pd
import requests
import urllib3
import sqlite3
import webbrowser
import speech_recognition as sr

import browse
import src
import speech
import database
import photoapp


cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,frame = cap.read()
    if ret ==True:
        face_cascade = cv2.CascadeClassifier("opencvTutorial-main/files/haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow('Frame',frame)
        if len(faces) !=0:
            print("face detected")
            cap.release()
            cv2.destroyAllWindows()
            root1 = Tk()
            Desired_font = tkinter.font.Font( family = "Comic Sans MS", 
                                             size = 13, 
                                             weight = "bold")
            root1.title("Login")
            frame2 = LabelFrame(root1,bg='white')
            frame2.grid(row=3,column=1,columnspan=4)
            user = Label(frame2,text = "Enter Username",fg='black',bg='white',font = Desired_font)
            pswd = Label(frame2,fg='black',bg='white',text="Enter Password",font = Desired_font)
            user.grid(row=1,column=1,columnspan=2)
            pswd.grid(row=2,column=1,columnspan=2)
            e1 = Entry(frame2,width=35,borderwidth=2,font = Desired_font)
            e1.grid(row =1,column=3,columnspan = 2,ipady=3)
            e2 = Entry(frame2,width=35,borderwidth=2,font = Desired_font)
            e2.grid(row =2,column=3,columnspan = 2,ipady=3)
            log_button = Button(frame2,text="Login",fg='black',bg='white',font = Desired_font,command = lambda:login(e1.get(),e2.get()))
            log_button.grid(row=3,column = 2,columnspan=2,ipadx=15)
            global my_label
            def login(user,pswd):
                if user == "Akshay" and pswd == "admin":
            #         root1.destroy()
                    root = Toplevel(root1,bg='white')
                    root.title("Welcome to Akshay_youloder")
                    img1 = ImageTk.PhotoImage(Image.open("Downloads/yd_img2.png").resize((850, 450), Image.ANTIALIAS))
                    img2 = ImageTk.PhotoImage(Image.open("Pictures/2.jpg").resize((850, 450), Image.ANTIALIAS))
                    img3 = ImageTk.PhotoImage(Image.open("Pictures/3.jpg").resize((850, 450), Image.ANTIALIAS))
                    img4 = ImageTk.PhotoImage(Image.open("Pictures/4.jpg").resize((850, 450), Image.ANTIALIAS))
                    img5 = ImageTk.PhotoImage(Image.open("Pictures/5.jpg").resize((850, 450), Image.ANTIALIAS))
                    img_lst = [img1,img2,img3,img4,img5]
                    frame = LabelFrame(root,bg = 'white')
                    frame.grid(row=1,column=2,columnspan=2)
                    l3 = Label(root,text = "Enter Song name!!",bg='white',fg='black',font = Desired_font)
                    l3.grid(row=1,column=0,columnspan=2)
                    global my_label
                    my_label = Label(root,image=img1)
                    my_label.grid(row=0,column=0,columnspan=4)
                    prev = Button(frame,text="prev",fg='black',bg='white',borderwidth=2,padx=30,command =backward,font = Desired_font)
                    nex = Button(frame,text="next",fg='black',bg='white',borderwidth=2,padx=30,command=forward,font = Desired_font)

                    prev.grid(row=1,column=0)
                    nex.grid(row=1,column=2)
                    frame1 = LabelFrame(root,bg='white')
                    frame1.grid(row=2,column=2)
                    e = Entry(root,width=35,borderwidth=2,font = Desired_font)
                    e.grid(row =2,column=0,columnspan = 2,ipady=3)

                    D_button = Button(frame1,text="Download",fg='black',bg='white',font = Desired_font,command = lambda:Down(e.get()))
                    D_button.grid(row=1,column = 2,columnspan=1,ipadx=15)
                    Exit_button = Button(frame1,fg='black',bg='white',text="Exit",command=root.destroy,font = Desired_font)
                    Exit_button.grid(row=1,column =3,columnspan=1,ipadx=15)
                    sh_rec = Button(root,fg='black',bg='white',text="Show downloads",command = show,font = Desired_font)
                    sh_rec.grid(row=2,column = 3,columnspan=1,ipadx=15)
                    br = Button(root,text="Browse",command=browse,fg='black',bg='white',font = Desired_font)
                    br.grid(row=3,column=3,columnspan=1,ipadx=15)


            mainloop()
            
        if cv2.waitKey(1) & 0xFF == ord('$'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

