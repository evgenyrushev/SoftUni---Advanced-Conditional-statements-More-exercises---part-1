number_chris = int(input())
number_rose = int(input())
number_lale = int(input())
season = input()
holiday = input()

total_amount = 0

s_price_chris = 2
s_price_rose = 4.10
s_price_lale = 2.50

aw_price_chris = 3.75
aw_price_rose = 4.50
aw_price_lale = 4.15

if season == "Spring" or season == "Summer":
    total_amount = number_chris * s_price_chris + number_rose * s_price_rose + number_lale * s_price_lale
elif season == "Autumn" or season == "Winter":
    total_amount = number_chris * aw_price_chris + number_rose * aw_price_rose + number_lale * aw_price_lale

if holiday == "Y":
    total_amount *= 1.15
if number_lale > 7 and season == "Spring":
    total_amount *= 0.95
if number_rose >= 10 and season == "Winter":
    total_amount *= 0.90
if number_lale + number_rose + number_chris > 20:
    total_amount *= 0.80

total_amount += 2

print(f"{total_amount:.2f}")

