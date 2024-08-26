a = int(input('Enter the percentage scored by a student: '))
if(a>=80):
    print('Distinction')
elif(a>=60 and a<80):
    print('First division')
elif(60>a>=40):
    print('Second division')
elif(40>a>=30):
    print('Third Division')
else:
    print('fail')