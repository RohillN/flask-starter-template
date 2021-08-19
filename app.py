from flask import Flask

app = Flask(__name__)


# route for index page, status 200 for success
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)


