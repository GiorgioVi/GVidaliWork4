from flask import Flask
my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "<marquee><big>Where Am I?</big></marquee>"
@my_app.route('/goo')
def goo():
    return "this page is gooey"
@my_app.route('/foo')
def foo():
    return "Where is the food"

if __name__ == '__main__':
    #my_app.debug = True
    my_app.run()
