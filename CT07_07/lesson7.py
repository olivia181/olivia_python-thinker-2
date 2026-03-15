## Recap 1: Student Contact Database
# Task: Create a contact database for students
# 1. Create a list variable called students
# 2. Create 3 lists called student1, student2, student3
#     each student should have the following info:
#         1. name
#         2. phone number
#         3. CCA
# 3. Add student1, student2, student3 into the students list.
# 4. Unpack the list and use loop and string concatenation to
#    print the details for each student in the following format:

#    Name: James
#    Phone number: 85726845
#    CCA: Hockey


# students= []
# student1= ["olivia", 1234567 , "modern dance"]
# student2= ["emeline", 1432567, "npcc"]
# student3= ["clarise", 1456727, "volleyball"]

# students.append(student1)
# students.append(student2)
# students.append(student3)

# for student in students:
#     name,phonenumber,cca = student
#     print("name:", name)
#     print("phone number:",phonenumber)
#     print("cca:", cca)

## Task 1: Introduction to List Merging
# You are given 2 lists of fruits. Merge them into 1 list and
# print the result:

# list1 = ["Apple", "Banana", "Cherry"]
# list2 = ["Durian", "Elderberry", "Figs"]

# 1. Use the + operator to combine the lists.
# 2. Print the combined list.




## Task 2: Ordered List Merging
# You are given 2 lists that contain the price of fruits. Now,
# merge 2 given lists and ensure the resulting list is sorted.

# list1 = [3.20, 2.65, 1.75]
# list2 = [6.15, 5.45, 4.20]

# 1. Merge the lists using the + operator.
# 2. Use the sorted() function to sort the combined list.
# 3. Print the sorted list.

# list3 = list1 + list2
# sorted_list3=sorted(list3)
# print(sorted_list3)


## Task 3: Splitting Lists at a Point
# You are required to divide a basket of fruits.
# Split the given list at the specified index:

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# index = 3

# 1. Use slicing to split the list at the provided index.
# 2. Print the resulting sublists.

# print(fruits[:index])
# print(fruits[index:])


#nums = [4,7,2,9,5,8,1,6,3] 
# # Using slicing ONLY (no loops), 
# # extract all numbers at EVEN positions.




# ## Task 4: Splitting a List in Half
# You have been tasked to divide the basket of fruits into
# 2 equal halves. Given a list of even length, split it
# into 2 equal halves.

# fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]

# 1. Find the midpoint of the list.
# 2. Split the list into 2 halves using slicing.
# 3. Print both halves.

# middle = len(fruits)//2

# print(fruits[:middle])
# print(fruits[middle:])

# ---------------------------------------------------------------

# ## Task 5: Identifying Common Elements in Lists
# You have been given 2 lists of fruits. However, there might be
# duplicates. Your job is to identify and print the common fruits
# between them.

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# 1. Create an empty list named 'common'
# 2. Using 'for' loops, append common elements into 'common'
# 3. Print the common elements

# common_list = []
# for fruit in list1:
#     for fruit2 in list2:
#         if fruit == fruit2:
#             common_list.append(fruit)
# print(common_list)
# ---------------------------------------------------------------

# ## Task 6: Merging Lists Unique Items
# You have been given 2 lists of fruits that contains duplicates.
# Your task is to merge the 2 lists into a new list that contain
# no duplicates.

# list1 = ["Apple", "Banana", "Cherry", "Cherry"]
# list2 = ["Cherry", "Durian", "Durian", "Figs"]

# 1. Create an empty list named 'unique'
# 2. Using 'for' loops, append unique elements into 'unique'
# 3. Print the unique elementscommon_list = []

# unique_list = []
# for fruit in list1 + for fruit in list2:
#     if fruit not in unique_list:
#         unique_list.append(fruit)
# print(unique_list)


# ---------------------------------------------------------------

# ## Task 7: Merging Lists with Conditions
# You have been given the index number of 2 groups of students.
# However, only students with even index number is allowed
# to come into the room. Create a Python script that will
# merge the 2 lists, including only the elements that are
# even from both.

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# # 1. Merge the lists.
# # 2. Print the new list.

# list3 = []
# for number in list1 + list2:
#     if number %2 ==0:
#         list3.append(number)
# print(list3)

# ---------------------------------------------------------------

# ## Task 8: Nested List Splitting
# You are given a nested list of 3 groups of students that
# are each seated in a pair. However, you want to unpack
# the nested lists in order to have a list of all students.

# nested_list = [[1, 2], [3, 4], [5, 6]]

# 1. Use a loop or list comprehension to flatten the list.
# 2. Print the flattened list.

# list_flat = []
# for list1 in nested_list:
#     for num in list1:
#         list_flat.append(num)
# print(list_flat)
# ---------------------------------------------------------------

# ## Task 9: Partitioning a List into Smaller Lists
# You have been tasked to divide a class of 9 students
# into groups of 3.

# Given a list and a size, split the list into multiple
# sub-lists where each sub-list is of the given size.

# students = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12]
# size = 2
# nested_student_list = []
# 1. Use a loop to create sub-lists of the specified size.
# 2. Print the sub-lists.
# in range(0, len(students), size)
# for i in range(0, len(students), size):
#     nested_student_list.append(students[i:i+size])
# print(nested_student_list)
