def number_to_word(in_data):
    dictionary = {
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine",
        '0': "zero"
    }
    if in_data.isnumeric():
        output = ""
        for no in in_data:
            output += dictionary.get(no, no) + " "
        return output
    else:
        return "invalid input Please enter numeric value"
