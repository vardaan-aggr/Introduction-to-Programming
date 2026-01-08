def dictionary_creator(string):
    mega_list = [[] for _ in range(26)]
    words = string.split(" ")
    for word in words:
        index = ord(word[0].lower()) - ord("a")
        mega_list[index].append(word.lower())
    return mega_list

def multi_to_single(lis):
    single_list = []
    for sublist in lis:
        single_list.extend(sublist)
    return single_list

def check_substring(substring, lis):
    all_words = []
    for word in multi_to_single(lis):
        if substring in word:
            all_words.append(word)
    return all_words

def delete_word(mega_list, word_to_remove):
    index = ord(word_to_remove[0].lower()) - ord("a")
    if word_to_remove in mega_list[index]:
        mega_list[index].remove(word_to_remove)
        return f"'{word_to_remove}' has been removed."
    else:
        return f"'{word_to_remove}' was not found in the dictionary."

def insert(new_word, mega_list):
    index = ord(new_word[0].lower()) - ord("a")
    mega_list[index].append(new_word.lower())
    return f"'{new_word}' has been added to the dictionary."


string = input("Enter words separated by spaces to initialize the dictionary: ")
mega_dictionary = dictionary_creator(string)

while True:
    print(mega_dictionary)
    order = input("\nTell the task you want to perform (insert, delete, check, exit): ")

    if order == "exit":
        print("Exiting the program.")
        break
    elif order == "insert":
        new_word = input("Enter the word you want to insert into the dictionary: ")
        print(insert(new_word, mega_dictionary))
    elif order == "delete":
        word_to_remove = input("Enter the word you want to delete from the dictionary: ")
        print(delete_word(mega_dictionary, word_to_remove))
    elif order == "check":
        substring = input("Enter the substring to search for in the dictionary: ")
        found_words = check_substring(substring, mega_dictionary)
        if found_words:
            print("Words containing the substring:", found_words)
        else:
            print("No words found containing the substring.")
    else:
        print("Invalid command. Please try again.")


def test():
    assert dictionary_creator("a")==[['a'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    assert dictionary_creator("bat")==[[], ['bat'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    assert dictionary_creator("c")==[[], [], ['c'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

test()