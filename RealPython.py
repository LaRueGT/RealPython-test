# import the Flask class
from flask import Flask

# create the application object
app = Flask(__name__)

# enable Flask debug mode/auto reload
app.config["DEBUG"] = True


# decorators to link function to URL
@app.route('/')
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return 'Hello World!?!?!?!?'


# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


# flask converters
@app.route("/int/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"


@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"


@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"


# dynamic route with explicit status codes
@app.route("/name/<name>")
def index(name):
    if name.lower() == "garrett":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

# start dev server using the run() method
if __name__ == '__main__':
    app.run()
