# nested if
percentage = float(input("Enter the percentage of the student"))
if(percentage>=40):
    if(percentage<=100):
        print('user is pass.')
        if(percentage>=80):
            print('Distinction')
        elif(percentage>=60):
            print('First Division')
        elif(percentage>=50):
            print('Second Division')
        elif(percentage>=30):
            print('Third Division')
    else:
        print("The marks entered is invalid")
else:
    print("The Student has failed")


