# Exercise 5
# Given some file we would like to read the file and write the
# contents to a new file with all numbers removed. The structure
# of the file should remain identical, i.e. all line breaks and
# punctuation should be written to the new file.


def remove_numbers(file_name: str, output_filename: str) -> None:
    with open(file_name, 'r') as f:
        input_data = f.readlines()
    for idx, line in enumerate(input_data):
        input_data[idx] = ''.join([i for i in line if not i.isdigit()])
    with open(output_filename, 'w') as f:
        for line in input_data:
            f.write(line)


remove_numbers('Exercise_5.txt', 'Exercise_4_no_num.txt')
