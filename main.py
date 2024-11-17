def main():
    path_to_book = "books/frankenstein.txt"
    with open(path_to_book) as f:
        file_contents = f.read()

    # Count words
    number_of_words = count_words(file_contents)
    print(number_of_words)

    # Count characters
    dict_characters_appearance = count_characters(file_contents)
    print(dict_characters_appearance)

    sorted_dict_characters_appearance = get_sorted_dict_desc_by_key(
        dict_characters_appearance
    )

    print_report(path_to_book, number_of_words,
                 sorted_dict_characters_appearance)


def count_words(string: str):
    words = string.split()
    return len(words)


def count_characters(string: str):
    # Lowercase the entire string
    string = string.lower()

    dict_character_to_number_appear = {}
    for character in string:
        # Key not exist in dict, set key to dict with value is 1
        if (character not in dict_character_to_number_appear):
            dict_character_to_number_appear[character] = 1
            continue

        # Key already exist, increase number of appearance by 1
        dict_character_to_number_appear[character] += 1

    return dict_character_to_number_appear


def get_sorted_dict_desc_by_key(dict: dict):
    sorted_dict = {
        k: v for k, v in
        sorted(
            dict.items(),
            key=lambda item: item[1],
            reverse=True
        )
    }
    return sorted_dict


def print_report(
    path_to_book: str,
    number_of_words: int,
    dict_characters_appearance: dict[str, int]
):
    print("--- Begin report of {} ---".format(path_to_book))
    print("{} words found in the document".format(number_of_words))
    print("\n")

    for key in dict_characters_appearance.keys():
        if not key.isalpha():
            continue

        print(
            "The '{}' character was found {} times".format(
                key,
                dict_characters_appearance[key]
            )
        )

    print("--- End report ---")


main()
