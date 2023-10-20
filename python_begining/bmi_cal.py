weight_inkg=56
height_incm=165
height_inmeter=height_incm/100
bmi=weight_inkg/height_inmeter**2
print(bmi)


if(bmi<=19):
    print("The person is under weight")
elif((bmi>=20)and(bmi<=24)):
    print("The persn is normal")
elif((bmi>=25)and(bmi<=29)):
    print("The person is overweight")
elif(bmi>=30):
    print("The person is obesity")