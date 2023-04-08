import csv, os

DATA_FILE_PATH_ANSWER = 'data/answer.csv'
DATA_FILE_PATH_QUESTION = 'data/question.csv'
UPLOAD_FOLDER_FOR_QUESTIONS = 'static/images/questions/'
UPLOAD_FOLDER_FOR_ANSWERS = 'static/images/answers/'
ALLOWED_EXTENSIONS = {'jpg'}


def import_data_file(filename):
    questions = list()
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            questions.append(row)
    return questions


def get_all_questions():
    return import_data_file(DATA_FILE_PATH_QUESTION)


def get_question(id):
    questions = import_data_file(DATA_FILE_PATH_QUESTION)
    for question in questions:
        if question[0] == id:
            return question
        
    
def get_next_id(selector):
    if selector == "answer":
        data_file = import_data_file(DATA_FILE_PATH_ANSWER )
    elif selector == "question":
        data_file = import_data_file(DATA_FILE_PATH_QUESTION)
    try:
        id = int(data_file[-1][0]) + 1
    except:
        id = 1
    return str(id)


def add_question(question):
    questions = import_data_file(DATA_FILE_PATH_QUESTION)
    questions.append(question)
    save_data(DATA_FILE_PATH_QUESTION, questions)
    

def save_data(filename, questions, separator = ","):
   with open(filename, "w") as file:
        for record in questions:
            row = separator.join(record)
            file.write(row + "\n")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file, question_id, selector):

    if selector == "question":
        upload_folder = UPLOAD_FOLDER_FOR_QUESTIONS
    elif selector == "answer":
        upload_folder = UPLOAD_FOLDER_FOR_ANSWERS

    if file and allowed_file(file.filename) and file.filename != "":
        saved_name = question_id + ".jpg"
        file.save(os.path.join(upload_folder, saved_name))
        return "/" + upload_folder + question_id + ".jpg"
    else:
        return ""
    
def add_answer(answer):
    answers = import_data_file(DATA_FILE_PATH_ANSWER)
    answers.append(answer)
    save_data(DATA_FILE_PATH_ANSWER, answers)

def count_votes(id):
    questions = import_data_file(DATA_FILE_PATH_QUESTION)
    for question in questions:
        if question[0] == id:
            votes = question[3]
            votes = int(votes)
            votes += 1
            question[3] = str(votes)
            save_data(DATA_FILE_PATH_QUESTION, questions)

