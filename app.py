from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message":"Hello World!",
        "version":"0.1",
    }
    

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    sentence = request.args["sentence"]
    lower = request.args.get("lower", False)
    return str(tokenize(sentence, lower=lower))


#if we have to kill what is in the port: lsof -i:portnumber. to see the process ID to kill. kill PID
#for the group exercise, we will have to transform variables with bool(), int() and more complex structure