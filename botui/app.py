from flask import Flask,render_template,request,jsonify
import sqlite3 as sql
from check import check
from preprocess import preprocess
from fetch import fetch
from keywords import keywords
from store import store


app=Flask(__name__)


@app.route("/")

def index():
  return render_template("index.html")


@app.route("/get")

def get_bot_response():
    userText = request.args.get('msg')
    store('usermessage','messages',userText)
    userText=userText.lower()
    userText=preprocess(userText)
    id=check(keywords,userText,0)
    if id ==-1:
        result="I didn't quite understand could you repeat "
    else :
        result=fetch(id)
    return jsonify({"result":result})
   
@app.route("/post")
def post_info():
    username = request.args.get('a')
    usernumber=request.args.get('b')
    usercompany=request.args.get('c')
    useremail=request.args.get("d")
    userreq=request.args.get("e")

    result={'username':username,"usernumber":usernumber,"usercompany":usercompany,"useremail":useremail,"userreq":userreq}
    return jsonify(result)


if __name__=="__main__":
    app.run()    