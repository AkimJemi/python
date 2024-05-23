import os

target_file = "writeFile.py"
if not os.path.isfile(target_file):
    print("file doesn't exist. New File Created. : ", target_file)
    open(target_file, "w")


def file_read():
    reader = open(target_file, "r")
    file_content = reader.read()
    reader.close()
    return file_content


def file_write(input_text):
    origin_text = file_read()
    writer = open(target_file, "w")
    writer.write(origin_text + "\n" + input_text)
    writer.close()


while True:
    text = input("what you want to type? : ")
    if text == "q":
        break
    else:
        file_write(text)


print(file_read())
