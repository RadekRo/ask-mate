from flask import Flask
from flask import render_template
import data_handler

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def route_list():
    all_questions = data_handler.get_all_questions()
    return render_template("list.html", all_questions=all_questions)

if __name__ == '__main__':
    app.run()

# for run the python's flask server
# use> python -m flask run
# for automatic changes and debugger use> python -m flask --debug run