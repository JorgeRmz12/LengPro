from flask import flask
app = flask(__name__)

@app.router('/')
def helo_world():
    return 'Hola Mundo Flask'

if __name__ == '__main__':
    app.run()