COLOUR_TO_CODE = {'AliceBlue': '#f0f8ff', 'AntiqueWhite': '#faebd7', 'BlueViolet': '#8a2be2', 'cyan1': '#00ffff',
                  'DarkGreen': '#006400', 'DarkKhaki': '#bdb76b', 'chocolate': '#d2691e', 'CadetBlue': '#5f9ea0',
                  'black': '#000000', 'blue1': '#0000ff', 'blue4': '#00008b', 'BlanchedAlmond': '#ffebcd'}


def print_colours():
    max_key_length = max([len(key) for key in COLOUR_TO_CODE.keys()])
    for colour, code in COLOUR_TO_CODE.items():
        print("{:{col_width}} - {}".format(colour, code, col_width=max_key_length))


def main():
    #ask user for input for colour
    colour_to_code = {colour.lower() : code for colour, code in COLOUR_TO_CODE.items()}
    colour_name = input("Enter a colour: ").strip().lower()
    while colour_name != "":
        print("Colour code is {} for {}".format(colour_to_code.get(colour_name), colour_name))
        colour_name = input("Enter a colour: ").strip().lower()
    #print the output - hexadecimal example #00ffff if the user keys in cyan1 or Cyan1

if __name__ == '__main__':
    main()