# coding= utf-8
'''
Created on 25 déc. 2016
@author: anis
'''


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
