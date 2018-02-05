# -*- coding:utf-8 -*-

import random


def ask_question():
    a = input("What is your question?")
    if a == 'quit':
        quit()
    while a[-1] is not '?':
        a = input("I’m sorry, I can only answer questions. To quit, enter 'quit'.\nPlease input your question again:")

    twenty_possible_answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely",
                               "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
                               "Signs point to yes", "Reply hazy try again", "Ask again later",
                               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
                               "Very Doubtful"]
    answer = random.choice(twenty_possible_answers)
    print(answer)


def main():
    while True:
        ask_question()


if __name__ == '__main__':
    main()
