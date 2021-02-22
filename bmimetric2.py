weight= float(input("Please enter weight in kilograms: "))
height= float(input("Please enter height in meters: "))
BMI= weight/ (height**2)
BMI_round=round(BMI,1)
BMI=round(BMI,2)
if (BMI_round<18.5):
    status="Underweight"
elif (18.5<=BMI_round<=24.9):
    status="Normal"
elif (25.0<=BMI_round<=29.9):
    status="Overweight"
elif (BMI_round>=30.0):
    status="Obese"

print("BMI is: ",BMI, ", Status is ",status,sep="")