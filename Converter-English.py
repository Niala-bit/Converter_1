# --- CONVERSION FUNCTIONS ---
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def meters_to_km(meters):
    return meters / 1000

def km_to_meters(km):
    return km * 1000

def meters_to_miles(meters):
    return meters * 0.000621371

def miles_to_meters(miles):
    return miles / 0.000621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def grams_to_ounces(grams):
    return grams * 0.035274

def ounces_to_grams(ounces):
    return ounces / 0.035274

# --- MAIN PROGRAM ---
user_choice = 0

while user_choice != 14:
    print("       ---CONVERTER---")
    print("TEMPERATURE")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("LENGTH")
    print("5. Meters to Kilometers")
    print("6. Kilometers to Meters")
    print("7. Meters to Miles")
    print("8. Miles to Meters")
    print("WEIGHT")
    print("9. Kilograms to Pounds")
    print("10. Pounds to Kilograms")
    print("11. Grams to Ounces")
    print("12. Ounces to Grams")
    print("EXTRAS")
    print("13. EXIT")
    
    user_choice = int(input("Select an option: "))
    
    if user_choice == 1:
        celsius = float(input("Celsius degrees: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Cº is {fahrenheit} Fº")
        input("Press Enter to return to the menu")
    elif user_choice == 2:
        fahrenheit = float(input("Fahrenheit degrees: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fº is {celsius} Cº")
        input("Press Enter to return to the menu")
    elif user_choice == 3:
        celsius = float(input("Celsius degrees: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} Cº is {kelvin} K")
        input("Press Enter to return to the menu")
    elif user_choice == 4:
        kelvin = float(input("Kelvin degrees: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin} K is {celsius} Cº")
        input("Press Enter to return to the menu")
    elif user_choice == 5:
        meters = float(input("Meters: "))
        km = meters_to_km(meters)
        print(f"{meters} meters is {km} kilometers")
        input("Press Enter to return to the menu")
    elif user_choice == 6:
        km = float(input("Kilometers: "))
        meters = km_to_meters(km)
        print(f"{km} kilometers is {meters} meters")
        input("Press Enter to return to the menu")
    elif user_choice == 7:
        meters = float(input("Meters: "))
        miles = meters_to_miles(meters)
        print(f"{meters} meters is {miles} miles")
        input("Press Enter to return to the menu")
    elif user_choice == 8:
        miles = float(input("Miles: "))
        meters = miles_to_meters(miles)
        print(f"{miles} miles is {meters} meters")
        input("Press Enter to return to the menu")
    elif user_choice == 9:
        kg = float(input("Kilograms: "))
        pounds = kg_to_pounds(kg)
        print(f"{kg} kilograms is {pounds} pounds")
        input("Press Enter to return to the menu")
    elif user_choice == 10:
        pounds = float(input("Pounds: "))
        kg = pounds_to_kg(pounds)
        print(f"{pounds} pounds is {kg} kilograms")
        input("Press Enter to return to the menu")
    elif user_choice == 11:
        grams = float(input("Grams: "))
        ounces = grams_to_ounces(grams)
        print(f"{grams} grams is {ounces} ounces")
        input("Press Enter to return to the menu")
    elif user_choice == 12:
        ounces = float(input("Ounces: "))
        grams = ounces_to_grams(ounces)
        print(f"{ounces} ounces is {grams} grams")
        input("Press Enter to return to the menu")
    elif user_choice == 13:
        print("GOODBYE!")
        exit()
    else:
        print("INVALID OPTION. TRY AGAIN")
    print("\n")
