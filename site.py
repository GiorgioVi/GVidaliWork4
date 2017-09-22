from flask import Flask
my_app = Flask(__name__)

@my_app.route('/')

def root():
    return "Welcome to Wayne's World"


if __name__ == '__main__':
    my_app.run()
