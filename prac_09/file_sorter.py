import shutil
import os

FILE_EXTENSIONS = ['doc', 'docx', 'gif', 'jpg', 'png', 'txt', 'xls', 'xlsx']


def main():
    os.chdir('FilesToSort')
    for extension in FILE_EXTENSIONS:
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

    for filename in os.listdir('.'):
        for extension in FILE_EXTENSIONS:
            if filename.endswith(extension):
                shutil.move(filename, extension)


main()
