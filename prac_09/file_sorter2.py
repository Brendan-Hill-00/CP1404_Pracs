import shutil
import os

FILE_EXTENSIONS = ['doc', 'docx', 'gif', 'jpg', 'png', 'txt', 'xls', 'xlsx']


def main():
    extension_to_directory = {}
    os.chdir('FilesToSort2')
    for extension in FILE_EXTENSIONS:
        directory = input("What category would you like to sort {} files into: ".format(extension))
        extension
        extension_to_directory[extension] = directory
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

    print(extension_to_directory)
    for filename in os.listdir('.'):
        for extension in FILE_EXTENSIONS:
            if filename.endswith(extension):
                shutil.move(filename, extension_to_directory[extension])


main()
