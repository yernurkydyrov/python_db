from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask.json import jsonify
import jwt
from flask import abort
import psycopg2


dbName = "myDatabase"
user = "zhangir"
connectionString = "host=localhost dbname={} user={}".format(dbName,user)
conn = psycopg2.connect(connectionString)
cur = conn.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

@app.route('/login')
def login():
    auth = request.authorization
    if auth:
        cur.execute("SELECT * from public.users WHERE login = %s and \"password\" = %s",(auth.username,auth.password))
        if cur.fetchone() is not None:
            token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=1)}, app.config['SECRET_KEY'])
            cur.execute("UPDATE public.users SET \"token\" = %s WHERE login = %s",(token,auth.username))
            h1Token = "<h1>token: {}</h1><br>".format(token)
            href = "/protected?token={}".format(token)
            return h1Token + "<a href=\"{}\">PROTECTED</a>".format(href)
        else:
            return "Could not found a user with login:{}".format(auth.username)
    
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})


def token_required(func):
    def decorator_function():
        token = request.args.get('token')
        response = ""
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            response = "<h1>Hello, token which is provided is correct </h1>"
        except:
            response = "<h1>Hello, Could not verify the token </h1>"
        return func(response)
    return decorator_function

@app.route('/protected')
@token_required
def protected(response):
    return "{}".format(response)

if __name__ == '__main__':
    app.run(debug=True)
