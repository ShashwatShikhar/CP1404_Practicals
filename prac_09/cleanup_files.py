import os


def main():
    os.chdir('Lyrics')
    for directory_name, sub_directories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    count_whitespace = 0
    for name in filename:
        if (name.isspace()) == True:
            count_whitespace = count_whitespace + 1
    new_name = ""
    if count_whitespace > 0:
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    else:
        for current_index, letter in enumerate(filename):
            new_name = new_name + letter
            if current_index < len(filename) - 1:
                if letter.isalnum and filename[current_index + 1].isupper():
                    new_name += "_"

    return new_name


main()