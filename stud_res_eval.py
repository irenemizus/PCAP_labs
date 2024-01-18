import os

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return "Unexpected data were found while parsing the specified input file"


class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return "The specified input file is empty"


file_name = input("Please enter the file name to analize: ")
stud_dict = {}

try:
    fh = open(file_name, "rt")
    lines = fh.readlines()
    fh.close()
    if lines:
        for line in lines:
            row_els = line.split("\t")
            if len(row_els) != 3:
                raise BadLine
            full_name = row_els[0] + " " + row_els[1]
            try:
                pts_numb = float(row_els[2].strip())
            except:
                raise BadLine

            if full_name not in stud_dict.keys():
                stud_dict[full_name] = pts_numb
            else:
                stud_dict[full_name] += pts_numb
    else:
        raise FileEmpty
except IOError as eio:
    print("An I/O problem occured during working with the file \"" + file_name + "\". Error message: " + os.strerror(eio.errno))
    exit(eio.errno)
except FileEmpty as efe:
    print(efe)
    exit(1)
except BadLine as ebl:
    print(ebl)
    exit(2)
except StudentsDataException:
    print("An unrecognizable error occured while working with the specified input file")
    exit(3)

stud_dict_sort = dict(sorted(stud_dict.items(), key = lambda x: x[0]))
for el in stud_dict_sort.keys():
    print(el + "\t" + str(stud_dict_sort[el]))