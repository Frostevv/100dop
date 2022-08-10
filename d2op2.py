height = input("Enter your height in meters:")
weight = input("Enter your weight in kg:")

height = float(height)
weight = float(weight)

bmi = (weight / (height ** 2))
bmi = int(bmi)
print(bmi)