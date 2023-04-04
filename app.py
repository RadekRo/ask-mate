from flask import Flask
from flask import render_template, request
import data_handler

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

@app.route('/ask-question', method=["POST","GET"])
def ask_question():
    if request.method == 'POST':
        your_question = [data_handler.get_last_id()+1,]
            
            'title' : request.form.get('title'),
            'user_story' : request.form.get('user_story'),
            'acceptance_criteria' : request.form.get('acceptance_criteria'),
            'business_value' : request.form.get('business_value'),
            'estimation' : request.form.get('estimation'),
            'status' : request.form.get('status')
        }

        data_handler.add_user_story(user_story)
        return redirect('/')
    return render_template("ask-question.html")


if __name__ == '__main__':
    app.run()

# for run the python's flask server
# use> python -m flask run
# for automatic changes and debugger use> "python -m flask --debug run"