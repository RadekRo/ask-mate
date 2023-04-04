import csv, os

DATA_FILE_PATH_ANSWER = 'data/answer.csv'
DATA_FILE_PATH_QUESTION = 'data/question.csv'
FILES_EXTENSIONS = [".jpg", ".png", ".jpeg"]

def import_questions(filename):
    questions = list()
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            questions.append(row)
    return questions


def get_all_questions():
    questions = import_questions(DATA_FILE_PATH_QUESTION)
    return questions


def get_question(id):
    questions = import_questions(DATA_FILE_PATH_QUESTION)
    for question in questions:
        if question[0] == id:
            return question

def get_href_question(id):
    questions = import_questions(DATA_FILE_PATH_QUESTION)
    for question in questions:
        if question[0] == id:
            return id


import_questions(DATA_FILE_PATH_QUESTION)

