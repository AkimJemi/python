def fetch_lines_before(filename):
    with open(filename, "r") as file:
        lines = []
        for line in file:
            lines.append(line)
        return lines


zen = fetch_lines_before("zonofpython.txt")


# print(zen)


def fetch_lines_after(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line


class File:
    def fetch_lines(self):
        for line in self.file.readlines():
            yield line

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


zen = File("file.txt", "r").fetch_lines()
try:
    print(next(zen))
    print(next(zen))
    print(next(zen))
    print(next(zen))
    print(next(zen))
    print(next(zen))
except StopIteration:
    print("test")


# zen = File.fetch_lines_after("zonofpython.txt")
# fileZ = File.fetch_lines("file.txt")
# print(next(fileZ))

def file_reader(filename, method):
    for i in range(500):
        yield i


file_object = file_reader("", "")
# print(next(file_object))
# print(next(file_object))
# print(next(file_object))
# print(next(file_object))
# print(next(file_object))
