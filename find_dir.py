import os


def find_good(path, dir):
    for d in os.listdir(path):
        dpath = os.path.join(path, d)
        if d == dir:
            print(os.path.abspath(dpath))

        if os.path.isdir(dpath):
            find(dpath, dir)


def find(path, dir):
    oldcwd = os.getcwd()
    try:
        os.chdir(path)

        for d in os.listdir(".."):
            if d == dir:
                print(os.path.join(os.getcwd(), d))

            if os.path.isdir(d):
                find(os.path.join(os.getcwd(), d), dir)
    finally:
        os.chdir(oldcwd)


dir = input("Please enter a directory to look for: ")
path = input("Please enter a starting path for the search: ")

find_good(path, dir)
