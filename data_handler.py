import csv, os

DATA_FILE_PATH_ANSWER = 'data/answer.csv'
DATA_FILE_PATH_QUESTION = 'data/question.csv'
FILES_EXTENSIONS = [".jpg", ".png", ".jpeg"]

EXAMPLE = [["6", "1493068444", "45", "434", "science", "What is the purpose of living?"], ["9", "1495558444", "15", "423", "rock", "What is the purpose of dancin?"]]


def import_questions(filename):
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)


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


import_questions(DATA_FILE_PATH_QUESTION)

