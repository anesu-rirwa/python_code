# Weight Converter

# Convert between kilograms and pounds

# 1kg = 2.20462 pounds
# 1 pound = 0.453592 kg

def weight_converter(weight, unit):
    if unit == 'kg':
        converted_weight = weight * 2.20462
        converted_unit = 'pounds'
    elif unit == 'pounds':
        converted_weight = weight * 0.453592
        converted_unit = 'kg'
    else:
        raise ValueError("Unit must be either 'kg' or 'pounds'")
    
    return [converted_weight, converted_unit]

input_unit = input("Enter unit (kg or pounds): ").strip().lower()
input_weight = float(input("Enter weight: "))

converted_weight = weight_converter(input_weight, input_unit)

print(f"{input_weight} {input_unit} is equal to {converted_weight[0]:.2f} {converted_weight[1]}")