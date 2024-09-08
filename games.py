import random
'''
a = random.random()
print(int(a*100))
'''

'''
# generate random number and make the user guess
num = random.randrange(1,10)
user_num = int('Guess the number: ')
if(num==user_num):
    print('Correct guess.')
else:
    print('Wrong guess:')
'''

'''
num = random.randrange(1,10)
print(num)
i=0
while (i<3):
    user_num = int(input('Guess the number: '))
    i += 1
    if(num==user_num):
        print(f'Congratulation, you guessed the correct answer in attempt {i}')
        break
    if(i==3):
        print('Guess limit Exceeded')
        break
    print('Incorrect guess, try again.')
'''


# teacher solution
num = random.randrange(1,15)
print(num)
count = 0 

while True:
    user_num = int(input("Guess the number: "))
    count = count+1
    if (num==user_num):
        print(f"Congrulation, you guessed the correct number in attempt {count} ")
        break
    else:
        print("incorect guess,Try again")

    if count  == 3:
        print("Maxmium try reached")
        break

'''
# siva code
num = random.randrange(1, 15)

max_attempts = 3
attempts = 0

while attempts < max_attempts:
  user_num = int(input("Guess your number again:"))
  attempts += 1

  if (num == user_num):
    print("Congratulations, correct guess")
    break
  else:
    print("Wrong Guess. Try again.")
  
  if attempts == max_attempts:
    print("Sorry you have used all your attempts.")
'''