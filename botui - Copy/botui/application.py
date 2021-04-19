from flask import Flask,render_template,request,jsonify
#import sqlite3 as sql
from check import check
from preprocess import preprocess
from fetch import fetch
from keywords import keywords
from store import store
from flask_socketio import SocketIO,send,emit
from chat import reply


app=Flask(__name__)
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.secret_key='secret'
socketio = SocketIO(app, cors_allowed_origins="*")
coun=0
@app.route("/")

def index():
 return render_template("user.html")

@app.route("/agent1") 
def index2():
 return render_template("agent.html")
@app.route("/agent2") 
def index3():
 return render_template("agent.html")
@app.route("/agent3") 
def index4():
 return render_template("agent.html")
@app.route("/agent4") 
def index5():
 return render_template("agent.html")
## This socket deals with the messages sent by both user and agent to communicate with each other

@socketio.on('agent')
def user_resp(data):
    if data['id']==1:
        socketio.emit('agent2',data['data'],broadcast=True)
    else:
        socketio.emit('user',data['data'],broadcast=True)





## This the event to handle bot responses
@socketio.on('bot')
def bot_resp(data):
    
    userText = data
    #store('usermessage','messages',userText)
    userText=userText.lower()
    userText=preprocess(userText)
    id=check(keywords,userText,0)
    if id ==-1:
        result=reply(data)
        
    else :
        result=fetch(id)
        
    socketio.emit('bot',result,broadcast=True)

    

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
    #socketio.run(app,debug=True)
    app.run()