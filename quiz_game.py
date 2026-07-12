#Quiz Game in python

print("Welcome to the Python Quiz game")
print("--------------------------------")

score = 0
#question 1
answer = input("1.what does CPU stand for\n")

if answer.lower() == "central processing unit":
    print("Correct answer!!")
    score += 1
else:
    print("Wrong answer!!")

#question 2
question = input("2.Which language is used in Machine Learning the most?\n")
if question.lower() == "python":
    print("Correct answer!!")
    score += 1
else:
    print("Wrong answer!!")

#question 3
answer = int(input("3.How Much planets does our Solar system has?\n"))
if answer == 8:
    print("Correct answer!!")
    score += 1
else:
    print("Wrong answer!!")

#question 4
answer = input("4.What is the Capital of India? \n")
if answer.lower() == "New Delhi":
    print("Correct answer!!")
    score += 1
else:
    print("Wrong answer!!")

#final Score
print("-------------------------------------")
print("Quiz Finished")
print("Your Score is:",score,"/4")
percentage = (score / 4) * 100
print("Percentage is:",percentage,"%")

