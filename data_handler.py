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
        
def get_answers(question_id):
    all_answers = import_data_file(DATA_FILE_PATH_ANSWER)
    selected_answers = list()
    for answer in all_answers:
        if answer[3] == question_id:
            selected_answers.append(answer)
    return selected_answers

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


def save_file(file, current_id, selector):

    if selector == "question":
        upload_folder = UPLOAD_FOLDER_FOR_QUESTIONS
    elif selector == "answer":
        upload_folder = UPLOAD_FOLDER_FOR_ANSWERS

    if file and allowed_file(file.filename) and file.filename != "":
        saved_name = current_id + ".jpg"
        file.save(os.path.join(upload_folder, saved_name))
        return "/" + upload_folder + current_id + ".jpg"
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

def remove_question(id):
    questions = import_data_file(DATA_FILE_PATH_QUESTION)
    answers = import_data_file(DATA_FILE_PATH_ANSWER)
    questions_filtered = list()
    answers_filtered = list()
    for question in questions:
        if question[0] == str(id):
            file_path = "static/images/questions/" + str(id) + ".jpg" 
            os.path.exists(file_path) and os.remove(file_path)
            continue
        else:
            questions_filtered.append(question)
    for answer in answers:
        if answer[3] == str(id):
            file_path = "static/images/answers/" + str(answer[0]) + ".jpg" 
            os.path.exists(file_path) and os.remove(file_path)
            continue
        else:
            answers_filtered.append(answer)
    save_data(DATA_FILE_PATH_QUESTION, questions_filtered)
    save_data(DATA_FILE_PATH_ANSWER, answers_filtered)

def remove_answer(id):
    answers = import_data_file(DATA_FILE_PATH_ANSWER)
    answers_filtered = list()
    question_id = 0
    for answer in answers:
        if answer[0] == str(id):
            file_path = "static/images/answers/" + str(id) + ".jpg" 
            os.path.exists(file_path) and os.remove(file_path)
            question_id = answer[3]
            continue
        else:
            answers_filtered.append(answer)

    save_data(DATA_FILE_PATH_ANSWER, answers_filtered)
    return question_id