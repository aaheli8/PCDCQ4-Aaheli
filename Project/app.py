from flask import Flask, render_template, session, redirect, url_for
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

# Loading the environment variables
load_dotenv() # In the .env all the client id and secrets have been kept
template_folder="templates" #Loading the templates from this folder

app = Flask(__name__) #Using the Flask class
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-key")

# OAuth setup for Google 
oauth = OAuth(app)
oauth.register(
    name="google",
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"}
)

@app.route("/") #Base Route for homepage
def index():
    user = session.get("user")
    return render_template("index.html", user=user) #Rendering the index.html page

@app.route("/login") # Login page that redirects to the oauth.authorize
def login():
    redirect_uri = url_for("authorize", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route("/authorize") # This extracts tthe basic details of the google user and redirects to profile page
def authorize():
    token = oauth.google.authorize_access_token()
    user_info = oauth.google.userinfo()

    session["user"] = {
        "name": user_info.get("name"),
        "email": user_info.get("email"),
        "picture": user_info.get("picture")
    }
    return redirect(url_for("profile"))

@app.route("/profile") # shows the user details and the profile template shows the 
def profile():
    user = session.get("user")
    if not user:
        return redirect(url_for("index"))
    return render_template("profile.html", user=user)

@app.route("/logout") #This is for the signout hyperlink it will redirect to index page
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
