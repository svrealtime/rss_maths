#!usr/bin/python3

__author__ = "Leon Wetzel"
__copyright__ = "Copyright 2018, Leon Wetzel"
__credits__ = "Leon Wetzel"
__license__ = "Beerware License"
__version__ = "1.0"
__maintainer__ = "Leon Wetzel"
__email__ = "leonwetzel@gmail.com"
__status__ = "Development"

import sys
import random

operators = ["+", "-", "/", "*"]


def main():
    report = {}

    print("Welcome to Sommensalsa!")
    print("Please do not use a calculator to answer the following questions :)")
    print("Pen and paper can be used to perform calculations.")

    for _ in range(maximum):

        alpha = random.randrange(1, 101, 2)
        beta = random.randrange(1, 101, 2)
        random.shuffle(operators)

        exercise = Sum(alpha, beta, operators[0])

        answer = input("{}{}{} = ".format(exercise.alpha, exercise.operator, exercise.beta))
        report[(alpha, operators[0], beta)] = (float(answer), float(exercise.answer))

    correct_answers = 0
    for sum, solution in report.items():
        if solution[0] == solution[1]:
            correct_answers += 1
        print(sum, solution)
    print("{} out of {} answers were correct!".format(correct_answers, len(report)))


class Sum:
    def __init__(self, alpha, beta, operator):
        """
        Initiates a Sum.
        :param alpha:
        :param beta:
        :param operator:
        """
        self.alpha = alpha
        self.beta = beta
        self.operator = operator
        self.answer = self.calculate_answer()

    def calculate_answer(self):
        """
        Calculates answer, based on object variables.
        :return:
        """
        if self.operator == "+":
            return self.alpha + self.beta
        elif self.operator == "-":
            return self.alpha - self.beta
        elif self.operator == "/":
            return self.alpha / self.beta
        elif self.operator == "*":
            return self.alpha * self.beta


if __name__ == "__main__":
    try:
        maximum = int(sys.argv[1])
    except IndexError:
        maximum = 15
    main()

