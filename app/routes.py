from app import app

@app.route("/")
def index():
    return "Let's see if it work"