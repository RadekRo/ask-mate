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
    next_id = data_handler.get_next_id("question")
    current_date = str(datetime.now())[0:19]
    
    if 'file' not in request.files:
        image = ""
    else:
        file = request.files['file']
        image = data_handler.save_file(file, next_id)

    if request.method == 'POST':
        your_question = [next_id, current_date, "0", "0", request.form.get('title'), request.form.get('message'), image ]
        data_handler.add_question(your_question)
        return redirect("/")
    return render_template("ask-question.html")

@app.route('/question/<id>/new-answer')
def route_answer(id):
    return render_template("new-answer.html", id=id)

@app.route('/new-answer', methods=["POST","GET"])
def new_answer():
    next_id = data_handler.get_next_id("answer")
    current_date = str(datetime.now())[0:19]
    image = ""
    if request.method == 'POST':
        your_answer = [next_id, current_date, "0", str(request.form.get('id')), request.form.get('new-answer'), image ]
        new_str = "/question/" + str(request.form.get('id'))
        data_handler.add_answer(your_answer)
        return redirect(new_str)
    return render_template("new-answer.html")


if __name__ == '__main__':
    app.run()

# for run the python's flask server
# use> python -m flask run
# for automatic changes and debugger use> "python -m flask --debug run"