budget = float(input())
season = input()

class_type = ""
type_car = ""
car_price = 0

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.35
    else:
        type_car = "Jeep"
        car_price = budget * 0.65

elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.45
    else:
        type_car = "Jeep"
        car_price = budget * 0.80

else:
    class_type = "Luxury class"
    type_car = "Jeep"
    car_price = budget * 0.90

print(f"{class_type}")
print(f"{type_car} - {car_price:.2f}")


