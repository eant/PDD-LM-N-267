from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hola desde Flask :D'

app.run( port = 3030 )