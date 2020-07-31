import csv
from shutil import copyfile
import random

QuestionArr = []
QuestionObjects = []
index = -1

class QuestionObject:
    def __init__(self, Question, Answer):
        self.Question = Question
        self.CorrectAnswer = Answer.lower()
        QuestionArr.append(self.Question)

    def CheckAnswer(self, InputAns):
        if str(self.CorrectAnswer) == str(InputAns.lower()):
            return True
        else:
            print("\nIncorrect, the correct answer was:\n" + self.CorrectAnswer)
            return False
        

def Main():

    with open("QuestionDump.csv") as QD:
        QD = csv.reader(QD, delimiter=',')
        for row in QD:
            print(row)
            QuestionObjects.append(QuestionObject(row[0], row[1]))

        NoQuestions = int(input("How many questions would you like to go through? "))

        Correct = 0
        Wrong = 0

        for _ in range(0, NoQuestions):
            index = random.randint(0, len(QuestionArr)-1)
            print("\n" + QuestionArr[index])
            InputAns = input()
            if QuestionObjects[index].CheckAnswer(InputAns):
                # Ans correct
                print("Correct!")
                Correct += 1
            else:
                Wrong += 1

        if Correct == 0 :
            print("Out of " + str(NoQuestions) + " questions you got " + str(Correct) + " right and " + str(Wrong) + " wrong\n0 %") # Prevent division by 0 err
        else:
            print("Out of " + str(NoQuestions) + " questions you got " + str(Correct) + " right and " + str(Wrong) + " wrong\n" + (NoQuestions/Correct)*100 + " %")
try:
    Main()
except:
    print("An error occured")
