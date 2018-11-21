from flask import Flask



app = Flask(__name__)

@app.route("/app/tools/create/<string:name>")
def create_table(name):
    print(name)
    return name




if __name__ == "__main__":
    app.run()
