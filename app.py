import urllib
import json
import os
#from app import app 
from flask import Flask 
from flask import request 
from flask import make_response  
 
app = Flask (__name__) 
#@app.route('/') 
#@app.route('/index') 
@app.route('/webhook', methods = ['POST']) 
def webhook():
	req = request.get_json(silent=True, force=True)
	print("Request:")
	print(json.dumps(req, indent=4)) 
	res = makeWebhookResult(req) 
	res = json.dumps(res, indent=4)
	print(res)
	r = make_response(res)
	r.headers['Content-Type'] = 'application/json' 
	return r 
 
def makeWebhookResult(req): 
	if req.get("result").get("action") == "index": 
		result = req.get("result") 
 		#parameters = result.get("parameters") 
 		speech=index() 
 		 
 						 
	print("Response:") 
 	print(speech) 
 	return { 
 	"speech": speech, 
 	"displayText": speech, 
     #"data": {}, 
     # "contextOut": [],	 
 	"source": "apiai-Web-Search-1" 
 	} 
 
if __name__ == '__main__': 
	port = int(os.getenv('PORT', 5000))
	print "Starting app on port %d" % port
	app.run(debug=True, port=port, host='0.0.0.0') 

def index(): 
    return "Hello, World!" 
