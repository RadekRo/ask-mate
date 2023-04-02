from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def route_list():
    return render_template("list.html")


if __name__ == '__main__':
    app.run(
        host = '127.0.0.1',
        port = 5000,
        debug = True,
    )

# for run the python's flask server
# use python -m flask run