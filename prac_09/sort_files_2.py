import os


def main():
    extension_folder = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_folder:
            category = input("What folder would you like to arrange {} files to? ".format(extension))
            extension_folder[extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(extension_folder[extension], filename))


main()