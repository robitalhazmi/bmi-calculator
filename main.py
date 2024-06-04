import pandas as pd

def calculate_bmi(weight, height):
    x = weight / (height/100)**2
    if x < 18.5:
        return 'Underweight'
    if x >= 18.5 and x < 25:
        return "Normal"
    if x >= 25 and x < 30:
        return 'Overweight'
    if x >= 30 and x < 35:
        return 'Obesity (Class 1)'
    if x >= 35 and x < 40:
        return 'Obesity (Class 2)'
    if x >= 40:
        return 'Obesity (Class 3)'

if __name__ == "__main__":
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = calculate_bmi(weight, height)
    bmi_df = pd.DataFrame(data={'weight': [weight], 'height': [height], 'bmi': [bmi]})
    print(bmi_df)