# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2

if bmi < 18.5:
  interpretation = "you are underweight."
elif bmi < 25:
  interpretation = "you have a normal weight."
elif bmi < 30:
  interpretation = "you are slightly overweight."
elif bmi < 35:
  interpretation = "you are obese."
else:
  interpretation = "you are clinically obese."

message = f"Your BMI is {round(bmi)}, {interpretation}"

print(message)



