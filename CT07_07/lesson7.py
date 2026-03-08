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


nums = [4,7,2,9,5,8,1,6,3] 
# Using slicing ONLY (no loops), 
# extract all numbers at EVEN positions.
print(nums[2:])
print(nums[:9:])
