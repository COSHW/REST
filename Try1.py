from flask import Flask



app = Flask(__name__)

@app.route("/<string:name>")
def create_table(name):
    return name




if __name__ == "__main__":
    app.run()
