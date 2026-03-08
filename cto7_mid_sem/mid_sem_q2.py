# """
# ============================================================
# Q2. Food Order System
# ============================================================
# Write a PYTHON program that simulates a restaurant order
# system using list and while loop.

# Requirements:
# - Use a while loop
# - Ask: "What would you like to order?"
# - Store each order into a list
# - Stop when user enters "end"
# - After ending, print all orders in numbered format

# ============================================================
# """

# # ============================================================
# # Step 1: Initialize variables
# # ============================================================



# # ============================================================
# # Step 2: Create a loop
# # ============================================================

food_list=[]
while True:
    food_item=input("What would you like to order?")
    if food_item == "end":
        break
    food_list.append(food_item)


print("You have ordered the following:")    
for i in range (len(food_list)):
    print(i+1 ,food_list[i])
