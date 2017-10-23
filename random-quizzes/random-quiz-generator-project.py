#! /usr/bin/python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random

# Quiz data: Keys are states and values are their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 5 quiz filenames --> originally 35
for quizNum in range(5):
   # Create the quiz and answer key files.
   quizFile = open('quizzes/capitals-quiz-{}.txt'.format(quizNum + 1), 'w')
   answerKeyFile = open('answers/capitals-quiz-answers-{}.txt'.format(quizNum + 1), 'w')

   # Write out the header for the quiz.
   quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
   quizFile.write((' ' * 20) + 'State Capitals Quiz (Form {})'.format(quizNum + 1))
   quizFile.write('\n\n')

   # Shuffle the order of the states.
   states = list(capitals.keys())
   random.shuffle(states)

   # Loop through all 50 states, making a question for each.
   for questionNum in range(50):

       # Get right answer
       correctAnswer = capitals[states[questionNum]] # loop through the states in the shuffled states list, find each state in capitals, and store that state's corresponding capital in correctAnswer

       # Get wrong answer
       wrongAnswers = list(capitals.values()) # create list of all answers
       del wrongAnswers[wrongAnswers.index(correctAnswer)] # delete the correct answer
       wrongAnswers = random.sample(wrongAnswers, 3) # choose 3 random wrong answers

       # Create answer options list and shuffle them
       answerOptions = wrongAnswers + [correctAnswer] # create a list of answer options with 3 wrong and 1 correct option
       random.shuffle(answerOptions) # shuffle the answer options so that the correct answer isn't always D

       # Write the question and answer options to the quiz file.
       quizFile.write('{}. What is the capital of {}?\n'.format(questionNum + 1, states[questionNum]))

       for i in range(4): # writes the answer options in the answerOptions list
           quizFile.write(' {}. {}\n'.format('ABCD'[i], answerOptions[i])) # treats 'ABCD' as an array and will go through each on each respective iteration through the loop
       quizFile.write('\n')

       # Write the answers key to a file
       answerKeyFile.write(' {}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)])) # finds the integer index of the correct answer in the randomly ordered answer options, and 'ABCD will evaluate to the correct answer's letter to be written to the file

   quizFile.close()
   answerKeyFile.close()
