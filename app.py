from flask import Flask
from flask import render_template, request, redirect
import data_handler
from datetime import datetime 

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def route_list():
    all_questions = data_handler.get_all_questions()
    return render_template("list.html", all_questions=all_questions)

@app.route('/question/<id>')
def route_question(id):
    question = data_handler.get_question(id)
    return render_template("question.html", question=question)

@app.route('/ask-question', methods=["POST","GET"])
def ask_question():
    image = ""
    if request.method == 'POST':
        your_question = [data_handler.get_next_id(), str(datetime.now()), "0", "0", request.form.get('title'), request.form.get('message'), image ]
        data_handler.add_question(your_question)
        return redirect("/")
    return render_template("ask-question.html")


if __name__ == '__main__':
    app.run()

# for run the python's flask server
# use> python -m flask run
# for automatic changes and debugger use> "python -m flask --debug run"