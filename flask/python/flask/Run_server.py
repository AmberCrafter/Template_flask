from flask import Flask, render_template, request
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/api/")
def index():
    # return "Hello world"
    return render_template('index.html')


if __name__ == "__main__":
    # use 0.0.0.0 to use it in container
    app.run(host='0.0.0.0')