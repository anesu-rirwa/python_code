# BMI Calculator

# input name
# choose units
# input weight in kgs/pounds
# input height in m/inches

# BMI formula = weight in kgs / (height)^2

# use matric or imperial units

def bmi_calculator(weight, height):
    bmi = weight / (height**2)
    return bmi

def bmi_class_function(bmi):
    if bmi < 18.4:
        return "underweight"
    elif bmi < 24.9:
        return "normal"
    elif bmi < 29.9:
        return "overweight"
    else:
        return "obese"

def app():
    name = input("Enter your name: ").capitalize()
    weight = 0
    height = 0
    system = input("Choose system, M for metric or I for imperial: ").upper()

    while system not in ["M", "I"]:
        print("Wrong units! Pick either metric system (M) or imperial system (I).")
        system = input("Choose system, M for metric or I for imperial: ").upper()
    else:
        if system == 'M':
            weight = float(input("Enter your weight (kgs):"))
            height = float(input("Enter your height (metres): "))
        else:
            weight = float(input("Enter your weight (lbs):"))
            height = float(input("Enter your height (inches): "))

    bmi = round(bmi_calculator(weight, height), 2) 
    bmi_class = bmi_class_function(bmi)

    print(f"{name} your BMI is {bmi}, you are {bmi_class}.")

app()