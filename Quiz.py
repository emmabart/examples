
'''
Name: Emma
Date: March 26
Title: MC Quiz Assignment - Star Wars
'''
#Set variable score to keep track of the score
score = 0
streak = 0


#Set variable perfect for getting all of the answers correct
perfect = True

#Introduction
print("Welcome to the Star Wars Quiz. Do you think you know all your Star Wars knowledge?")

#Question 1
q = input("Question 1 What is the first ever Star Wars movie called released in 1977:\na) Star Wars: Return of the Jedi\nb) Star Wars: Attack of the Clones\nc) Star Wars A New Hope\nd) Star Wars: The Phantom Menace\n")

#Use conditionals to check the correct answer
#You need to use all if, elif, and else statements to get full marks
if q == "c":
  print("You are correct!")
  streak = streak + 1
  score = score + 1

  if streak == 3:
    print("You have started a streak!")
elif q == "a" or q == "b" or q == "d":
  print("You are incorrect!")
  perfect = False
  if streak >= 3:
    print("You have stopped your streak!")
  streak = 0
else:
  print("Invalid input")
  perfect = False
print("Your score is",score,"!")

#Question 2
q = input("Question 2: What body part does Anakin Skywalker lose in Star Wars: Attack of the Clones?\na) Arm\nb) Leg\nc) Hand\nd) Foot\n")

if q == "a":
  print("You are correct!")
  score = score + 1
  streak = streak + 1
  if streak == 3:
    print("You have started a streak!")
elif q == "c" or q == "b" or q == "d":
  print("You are incorrect!")
  perfect = False
  if streak >= 3:
    print("You have stopped your streak!")
  streak = 0
else:
  print("Invalid input")
  perfect = False
print("Your score is",score,"!")

#Question 3
q = input("Question 3:What is Baby Yoda's real name?\na) Ashoka\nb) Mando\nc) Grogu\nd)Jabba \n")

if q == "c":
  print("You are correct! ")
  score = score + 1
  streak = streak + 1
  if streak == 3:
    print("You have started a streak!")
elif q == "a" or q == "b" or q == "d":
  print("You are incorrect!")
  perfect = False
  if streak >= 3:
    print("You have stopped your streak!")
  streak = 0
else:
  print("Invalid input")
  perfect = False
print("Your score is",score,"!")

#Question 4
q = input("Question 3:What land was Padme the queen of?\na) Tatooine\nb) Naboo\nc) Coruscant\nd) Hoth\n")

if q == "b":
  print("You are correct!")
  score = score + 1
  streak = streak + 1
  if streak == 3:
    print("You have started a streak!")
elif q == "a" or q == "c" or q == "d":
  print("You are incorrect!")
  perfect = False
  if streak >= 3:
    print("You have stopped your streak!")
  streak = 0
else:
  print("Invalid input")
  perfect = False
print("Your score is",score,"!")
  


if perfect == True:
  print(" Congrats! You got all answers right!")
else perfect == False:
print("Have you even watched star wars?")