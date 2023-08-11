print("Welcome in my new quiz game!")
print("quiz have X questions and level is easy")
print("If you want to play good luck!")

player = input("Do you want to play Yes/No: ")
if player == "Yes":
    print("Im getting ready to play!")
else:
    quit()

score = 0


#q1
answer = input("(2+2) * 3: ")
if answer == "12":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")


#q2
answer = input("(2-4) * 3: ")
if answer == "-6":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")


#q3
answer = input("7+8/2: ")
if answer == "11":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")


#q4
answer = input("7+4/2: ")
if answer == "9":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")


#add more questions and answers


#score calculation
#if you add a question, increase the number of maximum points!
max_points = 4
percentage = (score / max_points) * 100


#print score and percentage
print("i hope you did quiz very well!")
print("Your score: " + str(score) + "/" + str(max_points))
print(str(percentage) + "%")


# Check if the result is above or below 30%
# You can set any %
if percentage >= 30:
    print("Congratulations! You passed the quiz!")
else:
    print("Sorry, you didn't pass the quiz. Better luck next time!")
