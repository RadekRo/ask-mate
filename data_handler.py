import csv, os

DATA_FILE_PATH_ANSWER = 'data/answer.csv'
DATA_FILE_PATH_QUESTION = 'data/question.csv'

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
        
def get_image(id):
    questions = import_questions(DATA_FILE_PATH_QUESTION)
    for question in questions:
        if question[0] == id:
            image_source = question[6]
            return image_source

