weight= float(input("Please enter weight in pounds: "))
height= float(input("Please enter height in inches: "))
weight_in_kg=weight*0.453592
height_in_meters=height*0.0254
BMI= weight_in_kg/ (height_in_meters**2)
print("BMI is:",BMI)