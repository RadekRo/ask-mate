import csv, os
from werkzeug.utils import secure_filename

DATA_FILE_PATH_ANSWER = 'data/answer.csv'
DATA_FILE_PATH_QUESTION = 'data/question.csv'
UPLOAD_FOLDER = 'static/images/users/'
ALLOWED_EXTENSIONS = {'jpg'}

def import_questions(filename):
    questions = list()
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            questions.append(row)
    return questions


def get_all_questions():
    return import_questions(DATA_FILE_PATH_QUESTION)


def get_question(id):
    questions = import_questions(DATA_FILE_PATH_QUESTION)
    for question in questions:
        if question[0] == id:
            return question
        
    
def get_next_id():
    questions = import_questions(DATA_FILE_PATH_QUESTION)
    try:
        id = int(questions[-1][0]) + 1
    except:
        id = 1
    return str(id)


def add_question(question):
    questions = import_questions(DATA_FILE_PATH_QUESTION)
    questions.append(question)
    save_data(DATA_FILE_PATH_QUESTION, questions)
    

def save_data(filename, questions, separator = ","):
   with open(filename, "w") as file:
        for record in questions:
            row = separator.join(record)
            file.write(row + "\n")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file, question_id):
    if file and allowed_file(file.filename) and file.filename != "":
        saved_name = question_id + ".jpg"
        file.save(os.path.join(UPLOAD_FOLDER, saved_name))
        return "/" + UPLOAD_FOLDER + question_id + ".jpg"
    else:
        return ""