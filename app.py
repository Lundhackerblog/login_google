from flask import Flask, url_for, session, redirect
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY', 'app-secret-key')

oauth = OAuth(app)

google = oauth.register(
    "myApp",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def homepage():
    user = session.get('user')
    if user:
        return (
            f'<h2>Hello {user.get("given_name")}</h2>'
            f'<p><strong>Your email:</strong> {user.get("email")}</p>'
            '<br><a href="/logout">Logout</a>'
        )
    return '<a href="/login">Log in with Google</a>'

@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    session['user'] = token.get('userinfo')
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)