
from data import warehouse1, warehouse2


user_input = input("1. List items by warehouse`, `2. Search an item and place an order` and `3. Quit`")
#11111111111111

print(user_input)
from collections import Counter

count1 = Counter(warehouse1)
count2 = Counter(warehouse2)
count_sum = (warehouse1 + warehouse2)
count3 = Counter(count_sum)

if "1" in user_input:
    print("in Warehouse 1 available:",count1)
    print("-----")
    print("in Warehouse 2 available:",count2)
    
