from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    sentence = request.args["sentence"]
    lower = request.args.get("lower", False)
    return str(tokenize(sentence, lower=lower))


#if we have to kill what is in the port: lsof -i:portnumber. to see the process ID to kill. kill PID
#for the group exercise, we will have to transform variables with bool(), int() and more complex structure

if __name__=="__main__":
    import os
    port = int(os.environ["PORT"])
    app.run(host= "0.0.0.0", port=port)
    
    
    
#random-port= 53211