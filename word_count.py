def main():
    file_path_input = "input.txt"
    file_path_output = "output.txt"
    with open(file_path_input, "r") as file:
        content = file.read()
        lines = content.count("\n")
        character_count = len(content) - lines
        character_count_no_spaces = character_count - content.count(" ")
        the_dict = common_words(content)
        words = str(content.count(" ") + 1)
        with open(file_path_output, "w") as file:
            file.write("The total amount of words is " + words + '\n')
            file.write(f"The total amount of characters is {character_count}\n")
            file.write(f"The total amount of characters not including spaces is {character_count_no_spaces}\n")
            for word in the_dict:
                value = str(the_dict.get(word))
                file.write(word + ": " + value  + '\n')

def common_words(input):
    words_dict = {}
    parts = input.split(" ")
    for part in parts:
        if part in words_dict:
            update = words_dict.get(part) + 1
            words_dict.update({part: update})
        else:
            words_dict[part] = 1
    return words_dict
def sort_words(dict):
    new_dict = {}
    pass

def common_characters(input):
    pass


if __name__ == "__main__":
    main()