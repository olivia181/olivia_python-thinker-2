## Recap 1: Pseudocode (Recycling logic)
#Task: Write down the steps on how to solve the problem below
#Design pseudocode for a recycling robot that sorts items
#into bins for glass, plastic, and paper. The robot should
#check each item's material and place it in the correct bin.

# 1.ask the user for the material of the item
# 2.create variables called "glass" , "plastic" , "paper"
# 3.if the user inputs "glass" sort it into the variable called glass
# 4.if the user inputs "plastic" sort it into the variable called plastic
# 5.if the user inputs "paper" sort it into the variable called paper


## Recap 2: Variables & Mind map
#Use mindmap to think about the number of variables you need for
#the following. Then, create a program that does the following:
#You just had lunch at a sushi restaurant and have to calculate
#the total amount you have spent. Different coloured plates
#costs different as shown below:



# You have ordered a total of 3 red plates, 5 blue plates,
# and 4 green plates. Calculate and print the total amount you
# have spent:
# ask the user for the number of plate for red, blue and green


#red_amt=int(input("how many red plates are there?"))
#blue_amt=int(input("how many blue plates are there"))
#green_amt=int(input("how many green plates are there?"))

#red= red_amt*1
#blue= blue_amt*2
#green= green_amt*3
#total_amt_spent= red + blue + green
#print("total =", "$" + str(total_amt_spent))


## Recap 3: Debugging Average Score Program
# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:

#
# score_one = 80
#score_two = 90
#score_three = 75

#total = score_one + score_two + score_three


#average_score = total / 3

#student_name = "Alex"

#print("Average score for " + student_name + " is: " + str(average_score))


## Recap 4: If..elif..else & Flowchart
# Write a program that asks the user to input a score
# (as an integer) and then assigns a grade based on that score.
# Use the following grading scheme:

# If the score is 75 or higher, the grade is 'A'.
# If the score is between 60 and 74 (inclusive), the grade is 'B'.
# If the score is between 50 and 59 (inclusive), the grade is 'C'.
# Any score below 50 will be graded as 'Fail'.

# Use flowchart to draw out all decisions that are to be made
# before starting on your code.
# If..elif..else
score=int(input("input a score:"))
grade="0"
if score >= 75:
    grade= "A"
elif score >= 60:
    grade= "B"
elif score >= 50:
    grade = "C"
else:
    grade ="fail"

print(grade)
