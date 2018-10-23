"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    os.chdir('Lyrics/Christmas')
    rename_files()
    os.chdir('Lyrics/Old')
    rename_files()
    os.chdir('Lyrics/Special')
    rename_files()
    os.chdir('Lyrics/Sunday')
    rename_files()


def rename_files():
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = ""
    for counter, character in enumerate(filename):
        if character.islower() and counter == 0:
            character = character.upper()
        elif character.islower() and (counter += 1, charcter.isupper()):
            pass
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
