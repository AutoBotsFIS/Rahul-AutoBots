from app import app



#@app.route('/')
#@app.route('/index')
@app.route('/webhook', methods = ['GET'])
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
