def print_f(value):
    print(value)
    print(f"{value = }")


def input_check():
    while True:
        my_name = input("type any word : ")
        if my_name:
            print(f"{my_name = }")
            return my_name
        else:
            print("not typed")
            continue


input_value = input_check()


print(input_value)

