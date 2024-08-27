a = float(input('Enter the percentage scored by a student: '))
if(a>100 or a<0):  
    print('You entered invalid input')
elif(100>a>=80):
    print('Distinction')
elif(a>=60 and a<80):
    print('First division')
elif(60>a>=40):
    print('Second division')
elif(40>a>=30):
    print('Third Division')
else:
    print('fail')