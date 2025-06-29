from functools import reduce

with open(r"C:\Networks\Sigit\Next\names.txt", "r") as file:
    file_data = file.read().split('\n')

# Print the longest name in the file
print(max([name for name in file_data], key=len))

# Print the sum of name length
print(reduce(lambda sum, name: sum + len(name), file_data, 0))

# Print the shortest name in the file
min_len = len(min([name for name in file_data], key=len))
list(map(lambda name: print(name), list(filter(lambda name: len(name) == min_len, [name for name in file_data]))))


# Open file, and write the length of each word in the same order
with open(r"C:\Networks\Sigit\Next\len_file.txt", "w") as len_file:
    [len_file.write(str(len(name)) + '\n') for name in file_data]


# Input number and print all the names in the same length
input_len = int(input("Enter name length: "))
list(map(lambda name: print(name), list(filter(lambda name: len(name) == input_len, [name for name in file_data]))))
