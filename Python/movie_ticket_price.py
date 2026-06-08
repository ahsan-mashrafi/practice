# Ticket price is 50% for people aged 12 and under or 70 and older.
# A flat discount of $2 for everyone on Wednesday.
# Base ticket price is $10.

ticket_price = 10
age = int(input("Enter your age: "))
day = input("What day is today? ").strip().lower()

if age <= 12 or age >= 70:
    ticket_price *= 0.5

if day == "wednesday":
    ticket_price -= 2

print(f"Total price: ${ticket_price}")
