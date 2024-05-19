import random


while True:
    num = input("type a range number : ")
    if num.isdigit():
        random_number = random.randrange(1, int(num))
        break
    else:
        print("please type a number")


while True:
    guess_num = input("guess a number from 1 to " + num + " : ")
    if guess_num.isdigit():
        guess_num = int(guess_num)
        if guess_num > random_number:
            print("you were above than the answer")
        elif guess_num < random_number:
            print("you were lower than the answer")
        else:
            print("correct! answer is ", random_number)
            break
    else:
        print("please type a number")


print("neka hi")

