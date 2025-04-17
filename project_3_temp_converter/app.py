# Temperature converter

# convert between Celsius and Fahrenheit
# C = (F - 32) * 5/9
# F = (C * 9/5) + 32

def temperature_converter(temperature, unit):
    if unit == "F":
        # convert to celcius using the formula
        converted_temp = (temperature - 32) * 5/9
        return f"{temperature} Fahrenheit converted to Celcius is {converted_temp}C."
    elif unit == "C":
        # convert to fahrenheit using the formula
        converted_temp = (temperature * 9/5) + 32
        return f"{temperature} Celcius converted to Fahrenheit is {converted_temp}F."
    else:
        return "Invalid unit pick either F or C for Fahrenheit or Celcius respectively."
    
print("This program converts Fahrenheit to Celcius or vice versa.")
input_temperature = float(input("Enter the temperature: "))
input_unit = input("Enter the unit for the input temperature, F for Fahrenheit and C for Celcius: ")

converted_temperature = temperature_converter(input_temperature, input_unit)
print(converted_temperature)