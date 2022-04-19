def calculate_wind_chill(tempurature_fahrenheit, wind_speed) -> float:
    ''' This function calculates the wind chill for a given tempurature and windspeed. '''
    wind_chill = 35.74 + (0.6215 * tempurature_fahrenheit) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature_fahrenheit * (wind_speed ** 0.16)
    return wind_chill

def convert_celsius_to_fehrenheit(tempurature_celsius) -> float:
    ''' This function converts celsius tempurature to fahrenheit. '''
    tempurature_fahrenheit = (tempurature_celsius * (9 / 5)) + 32
    return tempurature_fahrenheit

# This part gets the user input for tempurate and assigns its fahrenheit value.
tempurature_input = int(input("\nWhat is the temperature? "))
temp_type = input("Fahrenheit or Celsius (F/C)? ")
if temp_type.lower() == "c":
    temperature_fahrenheit = convert_celsius_to_fehrenheit(tempurature_input)
else:
    temperature_fahrenheit = tempurature_input

# This part iterates from 5mph to 60mph windspeed and gets the wind chill calculation for each one.
for i in range(5, 65, 5):
    print(f"At tempurature {temperature_fahrenheit:.1f}F, and wind speed {i} mph,"
    f" the windchill is: {calculate_wind_chill(temperature_fahrenheit, i):.2f}F")

print()