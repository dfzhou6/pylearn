# -*- coding: utf-8 -*-

class FileHandler(object):

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename) as file_object:
            contents = file_object.read()
            print(contents.strip())

    def read_line(self):
        with open(self.filename) as file_object:
            for line in file_object:
                print(line.strip())

    def read_line_new(self):
        with open(self.filename) as file_obj:
            for line in file_obj.readlines():
                print(line.rstrip())

    def write(self, filename, mode = "r+"):
        """
        mode=r read_only
        mode=w new_file
        mode=a append
        mode=r+ read+write
        """
        with open(filename, mode) as file_obj:
            file_obj.write("hello world1\n")
            file_obj.write("hello world2\n")

fh = FileHandler("./test_file.py")
#fh.read_file()
#fh.read_line()
fh.read_line_new()
fh.write("test_zdf.txt", "r+")
