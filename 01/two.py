def is_number(char):
    return 48 < ord(char) < 58


def replace_number_text(line: str):
    buff = ""
    numbers_dict = {
        3: {
            "one": "1",
            "two": "2",
            "six": "6"
            },
        4: {
            "four": "4",
            "five": "5",
            "nine": "9"
        },
        5: {
            "three": "3",
            "seven": "7",
            "eight": "8",
        }
    }
    
    new_line = ""

    for char in line:
        if is_number(char):
            new_line += char
            buff = ""
        else:
            buff += char

            for i in (3, 4, 5):
                if len(buff) < i:
                    continue

                if buff[-i:] in numbers_dict[i]:
                    new_line += numbers_dict[i][buff[-i:]]
                    # buff = ""
                    # break

    return new_line


with open("input.txt", "r") as f:
    lines = f.readlines()

    result = 0

    for line in lines:
        line_replaced = replace_number_text(line)
        result += int(line_replaced[0] + line_replaced[-1])

print(result)
