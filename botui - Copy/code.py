
from flask import Flask,render_template,request,jsonify
#import sqlite3 as sql
from check import check
from preprocess import preprocess
from fetch import fetch
from keywords import keywords
from store import store
#from flask_socketio import SocketIO,send,emit


def bot_resp(data):
    
    userText = data
    #store('usermessage','messages',userText)
    userText=userText.lower()
    userText=preprocess(userText)
    id=check(keywords,userText,0)
    if id ==-1:
        result="Please wait a customer care agent will contact you"
        
    else :
        result=fetch(id)
    return result    

print(bot_resp('job'))    