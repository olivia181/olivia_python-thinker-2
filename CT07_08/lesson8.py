# Lesson 8 - Input Validation

## Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.

# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099,
#  1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020,
#  1084, 1175]

# unique_list=[]
# for num in student_indexes:
#     if num not in unique_list:
#         unique_list.append(num)


# sorted_list = []
# sorted_list = sorted(unique_list)

# extra_list = []

# duplicate= len(student_indexes) - len(sorted_list)


# print(duplicate,len(sorted_list),sorted_list)     

## Task 1: Data Format Check

### Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.

# while True:
#     question1=input("what is your name?")
#     if question1.isalpha():
#         break



# Ask the user to input their age until it is a valid number. 
# Keep asking for a name until a valid number is input.

# while True:
#     question1=input("what is your age?")
#     if question1.isdigit():
#         break
#       print("age is", question1)   
### Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# while True:
#     username = input("what is your username?")
#     if username.isalnum():
#         break
#     print("username set")

## Task 2: Length Check (using a while loop)

### Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!

# while True:
#     phonenumber = input("what is your phone number?")
#     if len(phonenumber) == 8 and phonenumber.isdigit():
#         break

#     else:
#         print("enter valid number")

### Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.
# while True:
#     username=input("enter your username:")
#     if len(username) >= 5 and len(username) <= 18 and username.isalpha():
#         break
# print("username entered")



## Task 3: Range Check (using a while loop)

### Task 3a
# Ask the user to input their birth year and check if it is between 1900 and 
# the current year. Keep asking until a correct value is given.

# while True:
#     birth_year = input("what is your birth year?")
#     if birth_year.isdigit() and int(birth_year) > 1900 and int(birth_year) < 2027:
#         break
# print("age accepted ")

     
### Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 
# 100.
# while True:
#     volume=input("what is your volume setting?")
#     if volume.isdigit() and int(volume) < 0 and int(volume) > 100:
#          break
# print("accepted volume")


## Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” 
# meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY 
# nAmE iS jAmEs”

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.

# is_upper = True
# sentence2 = ""
# sentence=input("enter a sentence:")
# for i in range(len(sentence)):
#     if sentence[i].isalpha():
#         if is_upper:
#             sentence2 += sentence[i].upper()
#         else:
#             sentence2 += sentence[i].lower()
#     else:
#         sentence2 += sentence[i]
#         is_upper = not is_upper
# print(sentence)




## Task 5: Slice String
# word = "SINGAPORE"

# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE



# print(word[:4])
# print(word[3:6])
# print(word[5:9])
# print(word[::2])


## Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, 
# until the input is ‘end’.

# You can try this list of words:
# civic, kayak, level, madam, radar, refer, rotator, tenet, racecar,
 # deified, stats, wow]

# while True:
#     question=input("enter a word:")
#     if question == "end":
#         break
#     if question[::-1] == question:
#         print(question,"is a palindrome")
#     else:
#         print(question,"is not a palindrome")


## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
# - e.g. [“Alice”, “Bob”, Carl”, “Dylan”]

# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)
# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.

# friends_list = ["emeline","charlotte","clarise","yashmita"]
# while True:
#     visitor= input("what is your name? :").strip()
#     if visitor== "":
#         print("please enter something")
#     else:
#         break
#     if visitor in friends_list:
#         print("accepted")
#     else:
#         print("deny")


## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long

# first_letter = ["S", "T", "F", "G", "M"]
# is_first_last_upper = False
# has_seven_digit_between_alphabet = False
# is_nine_char= False
# is_first_letter_in_list = False

# while True:
#     nric = input("NRIC? :")
#     if nric[0].isalpha() and nric[0].isupper() and nric[-1].isalpha() and nric[-1].isupper():
#         is_first_last_upper = True
#     if nric[1:len(nric)-1].isdigit():
#         has_seven_digit_between_alphabet = True
#     if nric[0] in first_letter:
#         is_first_letter_in_list = True
#     if is_first_last_upper and has_seven_digit_between_alphabet and is_first_letter_in_list and is_nine_char:
#         break
#     else:
#         print("please enter correct format")









## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me