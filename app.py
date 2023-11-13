from flask import Flask
app = Flask(_name_)

@app.route('/')
def Hello_World():
    return "Hello, World!"
