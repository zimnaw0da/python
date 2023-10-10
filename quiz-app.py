print("Welcome in my quiz game, but in python!")

player = input("Do you want to play Yes/No: ")
if player == "Yes":
    print("Im ready to play and good luck!")
else:
    break()

score = 0

#q1
answer = input("2+2: ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


#q2
answer = input("2+3: ")
if answer == "5":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


#q3
answer = input("2+4: ")
if answer == "6":
    print("Correct!")
    score += 1
else:
    print("Wrong!")



#q4
answer = input("2+5: ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


#q5
answer = input("5+9: ")
if answer == "14":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

#You can change the questions and answers given content was only an example
#add more questions here and answers

#score calculation
#if you add a question increase the number of points by 1
#Example: if you add a question increase the number of points by 1

max_points = 5
percentage = (score/max_points) * 100

#print score and percentage

print("Your score is: " + str(score) + " out of " + str(max_points))
print("Your percentage is: " + str(percentage) + "%")

#Check if the results is above or below 30%
#You can set your own percentage like 34%

if percentage > 30:
    print("Congratulations! You are above 30%! and you passed the quiz!")
else:
    print("Nice try, but you are below 30%! and you failed the quiz!")

#let's check the code using terminal
