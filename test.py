"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE.

# Get the user name

# Greet the user

# Show the menu and ask to pick a choice

# If they pick 1
#
# Else, if they pick 2
#
# Else, if they pick 3
#
# Else

# Thank the user for the visit

user_name = input("Welcome to warehouse.com, what is your name?")

print("Hello", user_name)

user_input = input("1. List items by warehouse`, `2. Search an item and place an order` and `3. Quit`")
#11111111111111

from collections import Counter



count1 = Counter(warehouse1)
count2 = Counter(warehouse2)
count_sum = (warehouse1 + warehouse2)
count3 = Counter(count_sum)



if "1" in user_input:
    print("in Warehouse 1 available:",count1)
    print("-----")
    print("in Warehouse 2 available:",count2)
    

elif "2" in user_input:
    find_item = input(str("enter item"))
    print("Total stock is:",count3[find_item],find_item)
    total_stock = count3[find_item]
    print("Warehouse 1 has:",count1[find_item],find_item)
    print("Warehouse 2 has:",count2[find_item],find_item)

    order_query = input("would you like to place an order? y/n")
    if "y" in order_query:
        buy = int(input.lower("how many would you like to buy?")) 
    elif "n" in order_query:
        print("thank you for visiting", user_name)

    if buy <= total_stock:
        print("The order of", buy, find_item, "has been placed")
    elif buy > total_stock:
        total_query = input("Sorry we do not have that much stock, would you like to order the maximum? y/n")
        
    if "y" in total_query:
        print("The order of", total_stock, find_item, "has been placed")
    elif "n" in total_query:
        print("thank you for visiting", user_name)

elif "3" in user_input:
    print("thank you for visiting", user_name)

elif "1,2,3" not in user_input:
    print(user_input, "is not a valid input")
