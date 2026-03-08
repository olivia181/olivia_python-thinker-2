

# Course Menu
# Course Home
# Collapse
# Announcements
# Class Forum
# Class Videos
# Collapse
# CT07-Mon-5.30pm
# CT07-Wed-3.30pm
# CT07-Thu-5.30pm
# CT07-Sat-2.00pm
# CT07-Sun-11.00am
# CT07-Sun-4.00pm
# Code Books
# Collapse
# PythonThinker 2
# Lesson Guide
# Quizzes
# Collapse
# PY02S1 Mid Sem (Practical)
# PY02S1 Mid Sem (MCQ)
# PY02S1 End Sem (Practical)
# PY02S1 End Sem (MCQ)
# Python Cheatsheet
# Sample Practical Test
# Skip Quiz navigation
# Quiz navigation
# Finish attempt ...
# Hours
# 0
# Minutes
# 54
# Seconds
# 26
# To All Computhinkers, Good Luck and All The Best For Your Exams!


# Python02-2026
# Quizzes
# PY02S1 Mid Sem (Practical)

# PY02S1 Mid Sem (Practical)
# Time left 0:54:27
# Question 1
# Answer saved
# Marked out of 5.000
# Flag question
# Question text
# A hero goes on an adventure, starting at Full Health. He has to fight monsters and clear obstacles in his adventure. Sometimes, he takes damage while fighting these monsters.

# Write a PYTHON program that simulates the battles he fought until his health reaches 0 or below. Print out the number of battles that he fought at the end of the program.

# Hint: You may use a while-loop

# For example:

# Hero starts on his adventure with Health: 100
# After fighting monsters, his Health is now: 98
# After fighting monsters, his Health is now: 89
# ...
# After fighting monsters, his Health is now: 0
# He fought XXX battles, and died.

# Requirements:

# Your hero must start with 100 health
# Print into the console "Hero starts on his adventure with Health: 100"

# Your hero loses between 1 to 15 health (randomly) each round.
# Update the console using "After fighting monsters, his Health is now: xx", where "xx" is your hero's current Health

# Repeat until your hero's Health is less than or equals to 0
# Print "He fought xxx battles, and died", where "xxx" is the number of rounds it took to reach 0 or less Health.
# """
# ============================================================
# Q1. Hero Quest
# ============================================================
# A hero goes on an adventure, starting at Full Health.
# He fights monsters and loses health randomly each round.

# Requirements:
# - Start with 100 health
# - Print starting message
# - Lose between 1 to 15 health each round (random)
# - Use a while-loop
# - Continue until health <= 0
# - Print total number of battles fought

# ============================================================
# """

# # ============================================================
# # Step 1: Import required module
# # ============================================================



# # ============================================================
# # Step 2: Initialize variables
# # ============================================================



# # ============================================================
# # Step 3: Print starting message
# # ============================================================



# # ============================================================
# # Step 4: Create while-loop for battles
# # ============================================================
# # - Randomly reduce health between 1 and 15
# # - Increase battle counter
# # - Print updated health
# # ============================================================



# # ============================================================
# # Step 5: Print final result
# # ============================================================
# # Print in this format:
# # He fought xxx battles, and die

import random
health= 100
battle_counter=0

print("Hero starts on his adventure with Health:", health)

while True:
    num_health_lost=random.randint(1,15)
    health=health-num_health_lost
    battle_counter=battle_counter+1
    print("After fighting monsters, his Health is now:",health)
    if health <= 0:
        break

print("He fought", battle_counter,"battles and died")