import random

name=input("Enter your name: ")
print("Good luck " + name + "!")

file=open("namex.txt")
names=file.readlines()
# print(names)
name=random.choice(names)
# print(name)
name=str(name).strip('\n')
name=str(name).strip('\r')

print('Play the game!')

guesses=str()
if ' ' in name:
    guesses += ' '
    # print(guesses)

turns=5
while turns>0:
    flag=0
    for char in name:
        if char in guesses:
            print(char,end=' ')
        else:
            print('_',end=' ')
            flag += 1
    if flag==0:
        print("You won!Congratulations")
        exit()
    guess=input('\n\nGuess the characters: ')
    guesses += guess
    if guess not in name:
        turns -= 1
        print('Wrong guess')
        print('You have ' + str(turns) + ' more guesses left')
    if turns==0:
        print('You loose:(')
        print('It was: '+ name)
        print('Better luck next time!')

