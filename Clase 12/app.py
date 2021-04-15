from flask import Flask, json

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hola desde Flask :D'

@app.route('/users')
def usersTwitter():
    users = [
        { 'name' : 'smessina_' },
        { 'name' : 'eanttech' },
        { 'name' : 'TinchoLutter' },
        { 'name' : 'bitcoinArg' }
    ]

    response = app.response_class( response = json.dumps(users), status = 200, mimetype = 'application/json' )

    return response


if __name__ == '__main__':
    app.run( port = 3030 )