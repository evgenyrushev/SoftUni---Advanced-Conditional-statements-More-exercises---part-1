budget = float(input())
category = input()
number_of_people = int(input())

total_amount = 0
vip_ticket = 499.99
normal_ticket = 249.99

if number_of_people <= 4:
    budget *= 0.25
elif 5 <= number_of_people <= 9:
    budget *= 0.40
elif 10 <= number_of_people <= 24:
    budget *= 0.50
elif 25 <= number_of_people <= 49:
    budget *= 0.60
else:
    budget *= 0.75

if category == "VIP":
    total_amount = number_of_people * vip_ticket
else:
    total_amount = number_of_people * normal_ticket

if budget > total_amount:
    print(f"Yes! You have {budget - total_amount:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_amount - budget:.2f} leva.")

