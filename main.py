# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# example = open("C:/Users/Finance1/Desktop/jackjack/Mail Merge Project Start/Output/ReadyToSend/example.txt", "r")
#
# with open("C:/Users/Finance1/Desktop/jackjack/Mail Merge Project Start/Input/Names/invited_names.txt", 'r') as letter:
#     for name in letter:
#         x = name.strip("\n")
#         open(f"C:/Users/Finance1/Desktop/jackjack/Mail Merge Project "
#              f"Start/Output/ReadyToSend/letter_for_{x}.txt",
#              "w"
#              )
#         lines = example.readlines()
#         for line in lines:
#             letter.write(line)

with open("C:/Users/Finance1/Desktop/jackjack/Mail Merge Project Start/Input/Letters/starting_letter.txt",
          "r"
          ) as letter:
    lines = letter.readlines()
with open("C:/Users/Finance1/Desktop/jackjack/Mail Merge Project Start/Input/Names/invited_names.txt", 'r'
          ) as names:
    for name in names:
        x = name.strip("\n")
        new_letter = open(f"C:/Users/Finance1/Desktop/jackjack/Mail Merge Project "
                          f"Start/Output/ReadyToSend/letter_for_{x}.txt",
                          "w"
                          )
        for line in lines:
            # a = lines[0]
            # print(a)
            # y = lines[0].replace("[name]", x)
            # print(y)
            new_letter.write(f"{line}")
