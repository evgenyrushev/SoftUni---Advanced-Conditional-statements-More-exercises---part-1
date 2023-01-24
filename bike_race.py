junior_bikers = int(input())
senior_bikers = int(input())
type_road = input()

total_amount = 0

if type_road == "trail":
    total_amount = junior_bikers * 5.50 + senior_bikers * 7.00

elif type_road == "cross-country":
    total_amount = junior_bikers * 8.00 + senior_bikers * 9.50

elif type_road == "downhill":
    total_amount = junior_bikers * 12.25 + senior_bikers * 13.75

else:
    total_amount = junior_bikers * 20 + senior_bikers * 21.50

if type_road == "cross-country":
    if junior_bikers + senior_bikers >= 50:
        total_amount = (junior_bikers * 8.00 + senior_bikers * 9.50) * 0.75

total_amount *= 0.95

print(f"{total_amount:.2f}")
