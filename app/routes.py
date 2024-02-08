from app import app


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/homepage", methods=["GET"])
def index():
    return "Hello World! This is Me!"
