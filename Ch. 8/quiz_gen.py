#! /usr/bin/env python3
'''
Project from Ch. 8 of Automate the Boring Stuff with Python

quiz_gen.py - creates random quiz questions and their respective answer keys.

This program will take the number of students in a class (or the desired number
of individual tests) and make a unique multiple-choice quiz for each. The current
implementation is for testing state capitals, but can be generalized for any "zero sum" quiz, 
such as vocabulary for a unit or any other test where the answer choices besides the correct
one for a given question don't matter (e.g. this would be a poor way to generate random
math quizzes, unless one simply wanted to switch up the /order/ of questions and their answers 
and not randomize the selection of wrong answer choices as well.)

My additions:   1. a way to check if you have more quizzes than possible
                    permutations (i.e., (# of states)!),
                2. a way to make sure that the "random" quizzes are actually unique,
                    which is important for quizzes with fewer possibilities, and
                3. I replaced the string formatting % with .format()
                
This could be written as a class, but it's easier to run from the command line as-is. 
'''

import math, random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
           'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
           'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
           'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 
           'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 
           'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 
           'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 
           'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 
           'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 
           'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
           'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
           'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
           'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
           'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
           'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
           'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
           'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

max_quizzes = math.factorial(len(capitals)) - 1

num_students = 35

list_state = []

for quizzes in range(num_students):
    
    if quizzes > max_quizzes - 1:
        print('The maximum number of unique quiz permutations has been reached.')
        break
    
    # Structure the quiz and answer key files as "quiz1", "quiz2", etc.:
    
    quizFile = open('capitalsquiz{}.txt'.format(quizzes + 1), 'w')
    answerKeyFile = open('capitals_quiz_answers{}'.format(quizzes + 1), 'w')
    
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' '*20 + 'State Capitals Quiz (Form {})'.format(quizzes + 1))
    quizFile.write('\n\n')
    
    states = list(capitals.keys())
    random.shuffle(states)
    
    # Ensures that the quizzes are each unique, and not just "random":
    
    while True:
        
        if states in list_state:
            random.shuffle(states)
        else:
            break
    
    for questionNum in range(len(states)):
        
        # All 50 states will get a question, starting at states[0]:
        correctanswer = capitals[states[questionNum]]
        # Generate every answer (every capital):
        wronganswers = list(capitals.values())
        # Delete correct answer from list of wrong answers:
        del wronganswers[wronganswers.index(correctanswer)]
        # Choose three random wrong answers:
        wronganswers = random.sample(wronganswers, 3)
        # Re-assemble:
        answeroptions = wronganswers + [correctanswer]
        # Randomize:
        random.shuffle(answeroptions)
        
    # Write the question and answer options to the quiz file:
    
        quizFile.write('{}. What is the capital of {}?\n'.format(questionNum + 1, states[questionNum]))
        
        for i in range(4):
            quizFile.write('    {}. {}\n'.format('ABCD'[i], answeroptions[i]))
        quizFile.write('\n')
        
    # Write the answer key to a file:
        
        answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answeroptions.index(correctanswer)]))
        
    quizFile.close()
    answerKeyFile.close()
