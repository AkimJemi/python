from contextlib import contextmanager


# file = open("file.txt", "r")
# try:
#     file.write("hello")
# finally:
#     file.close()
#
# print("mid")
# with open("file.txt", "r") as file:
#     file.write("hello")


class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, exc_type, value, traceback):
        print(f"{exc_type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        if exc_type == Exception:
            return True
        elif exc_type == FileExistsError:
            return False


with File("file.txt", "w") as f:
    print("Middle")
    f.write("hello!")
    raise Exception()


@contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()
    print("exit")


with file("text.txt", "w") as f:
    print("middle")
    f.write("hello2024")
    f.write("hello")

