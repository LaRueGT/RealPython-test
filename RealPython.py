#import the Flask class
from flask import Flask

#create the application object
app = Flask(__name__)

#decorators to link function to URL
@app.route('/')
@app.route("/hello")
#define the view using a function, which returns a string
def hello_world():
    return 'Hello World!'


#start dev server using the run() method
if __name__ == '__main__':
    app.run()
