#asking user what and how many times they wanna print something

item = input("What do you want to print? ")
times = int(input("How many times do you want to print? "))

for i in range(times):
    print(item)