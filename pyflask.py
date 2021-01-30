#Import Flask Package
from flask import Flask
#Create runner
app = Flask('app')
#Not so sure about this, but is required
@app.route('/')
#Create function on what to do
def hello_world():
  return 'Hello, World!'
  #Text inside the '' can be changed
#Run the server
app.run(host='0.0.0.0', port=8080)
#Change the port to your computer's port
