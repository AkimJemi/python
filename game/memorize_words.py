import random
from game.vocabularys import en_vocabulary as en
from game.vocabularys import ja_vocabulary as ja

count = 0
total_length = len(en.words)
test_list = random.sample(range(total_length), total_length)
while True:
    if count == total_length:
        print("you got all test")
        break

    random_len_num = test_list[count]
    if_continue = input("Do you want to continue? :")
    if if_continue.lower() in ["yes", "y"]:
        count += 1
        while True:
            answer = input(f"{ja.words[random_len_num]}, How do you say it in English? : ")
            if answer.lower() == "quit":
                print("The right answer is ", en.words[random_len_num])
                break

            if answer.lower() == en.words[random_len_num].lower():
                print("you got it")
                break
            else:
                print("Wrong answer!")

    else:
        print("Game end! ByeBye! See you nex time!")
        break

