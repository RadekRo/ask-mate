import csv, os

DATA_FILE_PATH_ANSWER = 'data/answer.csv'
DATA_FILE_PATH_QUESTION = 'data/question.csv'

EXAMPLE = [["6", "1493068444", "45", "434", "science", "What is the purpose of living?"], ["9", "1495558444", "15", "423", "rock", "What is the purpose of dancin?"]]

def import_questions():
    with open() as f:
        file = f.readlines()
        questions = list()
        for i in file:
            question = i.rstrip("\n").split(",")
            questions.append(question)
        for question in questions:
            print(question)

def get_all_questions():
    return EXAMPLE

def get_question(id):
    for question in EXAMPLE:
        if question[0] == id:
            return question

def get_href_question(id):
    for question in EXAMPLE:
        if question[0] == id:
            return id




