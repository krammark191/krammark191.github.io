can_ride = False

first_rider_age = int(input("What is the age of the first rider? "))
first_rider_height = int(input("What is the height of the first rider? "))

if first_rider_age >= 12 and first_rider_age < 18:
    first_rider_golden_passport = input("Does this rider have a golden passport (yes/no)? ")

is_second_rider = input("Is there a second rider (yes/no)? ")

if is_second_rider.lower() == "yes":
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = int(input("What is the height of the second rider? "))

    if second_rider_age >= 12 and second_rider_age < 18:
        second_rider_golden_passport = input("Does this rider have a golden passport (yes/no)? ")

    # Rule 1
    if first_rider_height < 36 or second_rider_height < 36:
        can_ride = False
    else:
        # Rule 3
        if first_rider_age >= 18 or second_rider_age >= 18 or first_rider_golden_passport.lower() == "yes" or second_rider_golden_passport.lower() == "yes":
            # At least one is an adult
            can_ride = True
        else:
            # Neither is an adult

            # Rule 4
            if first_rider_age >= 12 and first_rider_height >= 52 and second_rider_age >= 12 and second_rider_height >= 52:
                can_ride = True
            elif (first_rider_age >= 16 and second_rider_age >= 14) or (first_rider_age >= 14 and second_rider_age >= 16):
                # Rule 6
                can_ride = True
            else:
                can_ride = False
else: # There is only one rider
    # Rule 2
    if (first_rider_age >= 18 or first_rider_golden_passport.lower() == "yes") and first_rider_height >= 62:
        can_ride = True
    else:
        can_ride = False


if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")