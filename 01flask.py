from flask import Flask
import os

print ( os.path)
print('aaaa222a')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
