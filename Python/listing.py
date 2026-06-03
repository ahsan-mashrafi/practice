# a program about storing items;

num = int(input("How many do you want to store: "))

items = []

for i in range(num):
    item_1 = input("Enter item name: ")
    items.append(item_1)

print(f"\nYou stored {len(items)} items. \nThey are {items}")
