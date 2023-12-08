def get_digits(line):
    """
    Converts a letter

    :param line: (str) Line from text file
    :return: (int) The first and last digits in the line added to one number

    """

    digits = [char for char in line if char.isdigit()]

    if len(digits) == 0:
        return 0

    if len(digits) == 1:
        return int(digits[0] * 2)

    else:
        return int(digits[0] + digits[-1])


def get_calibration_values(file):
    """
    :param file: (str) The file to draw the calibration values from
    :return: (int) The total calibration value from the file
    """

    calibration_values = 0

    with open(file, encoding="utf-8") as f:
        for line in f:
            calibration_values += get_digits(line)
    f.close()

    return calibration_values


if __name__ == "__main__":
    print(get_calibration_values("data/day_1_input.txt"))
